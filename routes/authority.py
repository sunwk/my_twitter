from routes import *


main = Blueprint('auth', __name__)


@main.route('/login', methods=['POST'])
def login():
    u = User(request.form)
    user = User.query.filter_by(username=u.username).first()
    if user is not None:
        if user.validate(u):
            log('用户登录成功', user,user.username,user.password)
            # cookie_id = str(uuid.uuid4())
            # cookie_dict[cookie_id] = user
            session['user_id'] = user.id
            r = redirect(url_for('tweet_view', user_id=user.id))
            # r.set_cookie('cookie_id', cookie_id)
            return r
        else:
            log('账号名或密码错误，需重新登录', user)
            return redirect(url_for('login_view'))
    else:
        log('用户尚未注册，须先注册再登录', user)
        return redirect(url_for('register_view'))


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