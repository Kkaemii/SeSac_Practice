from flask import Flask,  request, render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/post/<file_name>')
def post_file():
  return



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8000, debug=True)