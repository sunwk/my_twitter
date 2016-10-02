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
            r['next'] = request.args.get(url_for('.show_view'))
        else:
            r['success'] = False
            r['message'] = '账号名或密码错误，需重新登录'
            log('账号名或密码错误，需重新登录', user)
    else:
        r['success'] = False
        r['message'] = '账号名或密码错误，需重新登录'
        log('用户尚未注册，须先注册再登录', user)
    return jsonify(r)



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
