from api import *


@main.route('/login', methods=['POST'])
def login():
    form = request.get_json()
    u = User(form)
    user = User.query.filter_by(username=u.username).first()
    r = {
        'success': True,
    }
    if user is not None:
        if user.validate(u):
            log('用户登录成功', user,user.username, user.password)
            session.permanent = True
            session['user_id'] = user.id
            r['next'] = request.args.get(url_for('routes.show_view'))
        else:
            r['success'] = False
            r['message'] = '账号名或密码错误，需重新登录'
            log('账号名或密码错误，需重新登录', user)
    else:
        r['success'] = False
        r['message'] = '账号名或密码错误，需重新登录'
        log('用户尚未注册，须先注册再登录', user)
    return jsonify(r)


# 处理注册的请求  POST
@main.route('/register', methods=['POST'])
def register():
    form = request.get_json()
    u = User(form)
    r = {
        'success': True
    }
    if u.valid():
        log('注册成功，已跳转到内容页面')
        u.save()
        r['next'] = request.args.get(url_for('routes.show_view'))
        session.permanent = True
        session['user_id'] = u.id
    else:
        log('用户名或密码不合规范，需重新输入')
        r['success'] = False
        r['message'] = '用户名或密码不合规范，需重新输入'
    return jsonify(r)

