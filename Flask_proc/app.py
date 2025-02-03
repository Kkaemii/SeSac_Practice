from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
  return render_template('index.html')

#method는 리스트 형태로 제공해야 flask가 해석하는 방식이기 때문이다.
@app.route('/user', methods=['POST'])
def user():
  username = request.form.get('username', '') .strip()

  return render_template('user.html', username = username)

#method는 리스트 형태로 제공해야 flask가 해석하는 방식이기 때문이다.
@app.route('/multiple', methods=['POST','GET']) 
def multiple():
  if request.method == 'POST':
    num = request.form.get('num', '')
  else:
    num = request.args.get('num', '')

  return render_template('multiple.html', num = int(num))


if __name__ == '__main__':
  app.run(port= 3000 ,debug=True)