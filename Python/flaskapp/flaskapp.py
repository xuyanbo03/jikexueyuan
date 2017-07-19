from flask import Flask, request, url_for, render_template, flash,abort
from models import User

app = Flask(__name__)
app.secret_key = '123'


@app.route('/')
def hello_world():
    flash("Hello World")
    return render_template("index.html")


@app.route('/login', methods=['POST'])
def login():
    form = request.form
    username = form.get('username')
    password = form.get('password')

    if not username:
        flash("Please input username")
        return render_template("index.html")
    if not password:
        flash("Please input password")
        return render_template("index.html")

    if username == 'Awe' and password == '123456':
        flash("login success")
        return render_template("index.html")
    else:
        flash("username or password is wrong")
        return render_template("index.html")


@app.errorhandler(404)
def not_found():
    return render_template("404.html")


@app.route('/users/<user_id>')
def users(user_id):
    if int(user_id)==1:
        return render_template("user.html")
    else:
        abort(404)

@app.route('/user')
def user_index():
    user = User(1, 'Awe')
    return render_template("user_index.html", user=user)


@app.route('/query_user/<user_id>')
def query_user(user_id):
    user = None
    if int(user_id) == 1:
        user = User(1, 'Awe')
    return render_template("user_id.html", user=user)


@app.route('/users')
def user_list():
    users = []
    for i in range(1, 11):
        user = User(i, 'Awe' + str(i))
        users.append(user)
    return render_template("user_list.html", users=users)


@app.route('one')
def one_base():
    return render_template("one_base.html")


@app.route('two')
def two_base():
    return render_template("two_base.html")


@app.route('/user/<id>')
def user_id(id):
    id = request.args.get('id')
    return 'query_user' + id


@app.route('/query_url')
def query_url():
    return 'query url:' + url_for('query_user')


if __name__ == '__main__':
    app.run()
