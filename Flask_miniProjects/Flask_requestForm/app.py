from flask import Flask, render_template, url_for, redirect,request, session
app = Flask(__name__)
app.secret_key = '움하하하하하하!'


#시작페이지를 /conatct로 보이기 위해 리다이렉트
@app.route('/')
def home():
  return redirect('contact')


@app.route('/contact')
def contact():
  return render_template('index.html')

@app.route('/contact_save', methods=['POST'])
def contact_save():
  description = request.form.get('description','')
  session['description'] = description #세션에 description 저장
  return redirect(url_for('complete' ))


@app.route('/complete', methods=['POST','GET'])
def complete():
  if not session.get('description'):
    return redirect('contact')
  description = session.get('description', '') #세션에 저장한 값 가지고 오기

  if not description:
    return redirect(url_for('contact'))
  session.pop('description', None)
  return render_template('contact_complete.html', description = description)


if __name__ == '__main__':
  app.run( port= 4000 ,debug=True)