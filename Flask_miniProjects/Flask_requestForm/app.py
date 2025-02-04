from email_validator import validate_email, EmailNotValidError
from flask import Flask, render_template, url_for, redirect,request, session, flash

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
  username = request.form.get('username', '')
  email = request.form.get('email','')
  session['description'] = description #세션에 description 저장
  session['username'] = username
  session['email'] = email

  #사용자의 입력 체크
  is_valid = True
  if not username:
    flash('사용자 명은 필수입니다.')
    is_valid = False
  
  if not email:
    flash('메일 주소는 필수입니다.')
    is_valid = False
    try:
      validate_email(email)
    except EmailNotValidError:
      flash('메일 주소 형식으로 입력해주세요.')
    is_valid = False

  if not description:
    flash('문의 내용은 필수입니다.')
    is_valid=False

  if not is_valid:
    return redirect(url_for('contact'))
  
  flash('문의내용이 정상적으로 전달되었습니다. 문의해주셔서 감사합니다.')
  return redirect(url_for('complete' ))


@app.route('/complete', methods=['POST', 'GET'])
def complete():
  if not session.get('description') or not session.get('username') or not session.get('email'):
    return redirect('contact')
  description = session.get('description', '') #세션에 저장한 값 가지고 오기

  if not description:
    return redirect(url_for('contact'))
  session.pop('description', None)
  return render_template('contact_complete.html', description = description)


if __name__ == '__main__':
  app.run( port= 4000 ,debug=True)