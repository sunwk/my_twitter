from routes import *

main = Blueprint('follow', __name__)


@main.route('/followee')
def followee_view():
    u = current_user()
    follows = Follow.query.filter_by(follower_id=u.id).all()
    follows.sort(key=lambda t: t.time, reverse=True)
    user_list = []
    if u is not None:
        for follow in follows:
            user = User.query.filter_by(id=follow.followee_id).first()
            user_list.append(user)
        # 继承的父模板里要用到user参数，不传进去就会出现bug，这里只是为了避免bug，没什么用
        return render_template('follow_view.html', users=user_list, user=u)
    else:
        return redirect(url_for('timeline.timeline_view'))


@main.route('/follower')
def follower_view():
    u = current_user()
    follows = Follow.query.filter_by(followee_id=u.id).all()
    follows.sort(key=lambda t: t.time, reverse=True)
    user_list = []
    if u is not None:
        for follow in follows:
            user = User.query.filter_by(id=follow.follower_id).first()
            user_list.append(user)
        # 继承的父模板里要用到user参数，不传进去就会出现bug，这里只是为了避免bug，没什么用
        return render_template('follow_view.html', users=user_list, user=u)
    else:
        return redirect(url_for('timeline.timeline_view'))