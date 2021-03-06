from api import *


@main.route('/login', methods=['POST'])
def login():
    r = {
        'success': True,
    }
    form = request.get_json()
    if form is not None:
        u = User(form)
        user = User.query.filter_by(username=u.username).first()
        if user is not None:
            if user.validate(u):
                log('用户登录成功', user, user.username, user.password)
                session.permanent = True
                session['user_id'] = user.id
                r['next'] = url_for('timeline.timeline_view', user_id = user.id)
            else:
                r['success'] = False
                r['message'] = '账号名或密码错误，需重新登录'
                log('账号名或密码错误，需重新登录', user)
        else:
            r['success'] = False
            r['message'] = '账号名或密码错误，需重新登录'
            log('用户尚未注册，须先注册再登录', user)
    else:
        r['success'] = False
        r['message'] = '账号名或密码错误，需重新登录'
        log('账号名或密码错误，需重新登录')
    return jsonify(r)


# 处理注册的请求  POST
@main.route('/register', methods=['POST'])
def register():
    r = {
        'success': True
    }
    form = request.get_json()
    ip_addr = request.remote_addr
    log('测试注册form', form)
    if form is not None:
        u = User(form)
        is_unique_user = len(User.query.filter_by(username=u.username).all()) == 0
        if is_unique_user:
            if u.valid():
                log('注册成功，已跳转到内容页面')
                u.ip = ip_addr
                u.save()
                r['next'] = url_for('timeline.timeline_view')
                session.permanent = True
                session['user_id'] = u.id
            else:
                log('用户名或密码不合规范，需重新输入')
                r['success'] = False
                r['message'] = '用户名或密码不合规范，需重新输入'
        else:
            log('用户名已存在')
            r['success'] = False
            r['message'] = '用户名已存在'
    else:
        log('用户名或密码不合规范，需重新输入')
        r['success'] = False
        r['message'] = '用户名或密码不合规范，需重新输入'
    return jsonify(r)


@main.route('/comment', methods=['POST'])
def comment_add():
    form = request.get_json()
    comment = Comment(form)
    u = current_user()
    log('debug current user:', u)
    if u is not None:
        comment.user_id = u.id
        comment.save()
        current_username = u.username
        response = {
            'success': True,
            'content': comment.content,
            'created_time': comment.created_time,
            'current_username': current_username,
        }
    else:
        response = {
            'success': False,
        }
    return jsonify(response)


@main.route('/tweet', methods=['POST'])
def tweet_add():
    form = request.get_json()
    tweet = Tweet(form)
    u = current_user()

    log('debug current user:', u, len(tweet.comments))
    if u is not None:
        tweet.user_id = u.id
        tweet.save()
        current_username = u.username
        response = {
            'success': True,
            'content': tweet.content,
            'created_time': tweet.created_time,
            'current_username': current_username,
            'user_id': tweet.user_id,
            'id': tweet.id,
            'comments_num': len(tweet.comments)
        }
    else:
        response = {
            'success': False,
        }
    return jsonify(response)


@main.route('/edit', methods=['POST'])
def info_edit():
    form = request.get_json()
    u = User(form)
    log('!!!!!!!!!!!!!', u.json(),url_for('timeline.timeline_view'))
    user = current_user()
    response = user.json()
    is_unique_user = len(User.query.filter_by(username=u.username).all()) == 0
    if u is not None:
        if is_unique_user:
            user.username = u.username
            user.email = u.email
            user.signature = u.signature
            user.sex = u.sex
            user.save()
            current_username = user.username
            response['success'] = True
            response['next'] = url_for('timeline.timeline_view')
            # response = {
            #     'success': True,
            #     'content': tweet.content,
            #     'created_time': tweet.created_time,
            #     'current_username': current_username,
            #     'user_id': tweet.user_id,
            #     'id': tweet.id,
            #     'comments_num': len(tweet.comments)
            # }
        else:
            response['success'] = False
            response['message'] = '该用户名已经被其他人征用啦~~换一个吧'
    else:
        response['success'] = False,
        response['message'] = '未登录提交无效'
    log(response)
    return jsonify(response)


@main.route('/follow', methods=['POST'])
def follow():
    form = request.get_json()
    u = current_user()
    r = {
        'success': True,
    }
    if u is not None:
        follow = Follow()
        follow.followee_id = form.get('followee_id')
        follow.follower_id = u.id
        follow.save()
    else:
        r['success'] = False
        r['message'] = '想关注，先登录！'
    return jsonify(r)


@main.route('/unfollow', methods=['POST'])
def unfollow():
    form = request.get_json()
    followee_id = form.get('followee_id')
    user = User.query.filter_by(id=followee_id).first()
    u = current_user()
    r = {
        'success': True,
    }
    if u is not None:
        follows = Follow.query.filter_by(followee_id=followee_id).all()
        for follow in follows:
            if follow.follower_id == u.id:
                follow.delete()
        return jsonify(r)
    else:
        r['success'] = False
    return jsonify(r)

