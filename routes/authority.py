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
    else:
        log('用户登录失败')
        flash('账户名或密码错误，请重新登录')
        return redirect(url_for('auth.login_view'))


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
    is_unique_user = len(User.query.filter_by(username=u.username).all()) == 0
    if is_unique_user:
        if u.valid():
            log('注册成功，已跳转到timeline页面，并直接保持登录状态')
            u.save()
            session.permanent = True
            session['user_id'] = u.id
            return redirect(url_for('timeline.timeline_view'))
        else:
            log('用户名或密码不合规范，需重新输入')
            flash('用户名或密码不合规范，需重新输入')
            return redirect(url_for('auth.register_view'))
    else:
        flash('用户名已存在，再重新想一个把')
        return redirect(url_for('auth.register_view'))


@main.route('/register', methods=['GET'])
def register_view():
    u = current_user()
    if u is not None:
        return redirect(url_for('timeline.timeline_view'))
    else:
        return render_template('register_step1.html')


@main.route('/logout', methods=['GET'])
def logout():
    u = current_user()
    if u is not None:
        session.pop('user_id')
    return redirect(url_for('timeline.timeline_view'))
