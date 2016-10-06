from routes import *


main = Blueprint('auth', __name__)


@main.route('/login', methods=['POST'])
def login():
    u = User(request.form)
    user = User.query.filter_by(username=u.username).first()
    if user is not None and user.validate(u):
        log('用户登录成功', user, user.username, user.password)
        session.permanent = True
        session['user_id'] = user.id
    return redirect(url_for('timeline.timeline_view'))


@main.route('/login', methods=['GET'])
def login_view():
    u = current_user()
    if u is not None:
        return redirect(url_for('timeline.timeline_view'))
    else:
        return render_template('login.html')


@main.route('/register', methods=['POST'])
def register():
    u = User(request.form)
    if u.valid():
        log('注册成功，已跳转到内容页面')
        u.save()
        return redirect(url_for('login_view'))
    else:
        log('用户名或密码不合规范，需重新输入')
        return redirect(url_for('register_view'))


@main.route('/logout', methods=['GET'])
def logout():
    u = current_user()
    if u is not None:
        session.pop('user_id')
    return redirect(url_for('timeline.timeline_view'))
