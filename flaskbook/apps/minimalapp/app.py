# from flask import Flask, render_template
# app = Flask(__name__)

# # @app.route('/')
# # def home():
# #     return render_template('home.html')

# # @app.route('/user/<username>')
# # def user_profile(username):
# #     return render_template('user.html',username=username)

# # @app.route('/post/<int:post_id>')
# # def show_post(post_id):
# #     return f'포스트 번호 : {post_id}'

# @app.route('/')
# def home():
#     return '<h1>Hello, FlaskBook </h1>'

# @app.route('/hello', methods=['GET'],endpoint='hello-endpoint')
# def hello():
#     return '<h1> hello World!!'

# @app.route('/hello/<name>', methods=['GET'], endpoint='hello-user')
# def hello(name):
#     return f'<h1> 유저 "{name}"의 페이지 입니다'

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=8000, debug=True)