from routes import *

main = Blueprint('timeline', __name__)


@main.route('/')
def timeline_view():
    u = current_user()
    tweets = Tweet.query.all()
    tweets.sort(key=lambda t: t.created_time, reverse=True)
    # log('debug current user', u.id, u.username)
    if u is None:
        return render_template('all_timeline_beforesign.html', tweets=tweets, user=u)
    else:
        return render_template('all_timeline_aftersign.html', tweets=tweets, user=u)


@main.route('/<int:user_id>')
def self_timeline_view(user_id):
    user = User.query.filter_by(id=user_id).first()
    u = current_user()
    follows = Follow.query.filter_by(followee_id=user_id).all()
    if user is not None:
        log('de bug user', user, user.username, user.id)
        if u is not None:
            log('debug current_user is:', u.id, u.username)
            user.visitors_add()
            user.save()
            tweets = user.tweets
            tweets.sort(key=lambda t: t.created_time, reverse=True)
            log('debug user id  u id', user_id, u.id, type(u.id), type(user_id), u.id == user_id, session.items())
            is_followed = ''
            for follow in follows:
                if follow.follower_id == u.id:
                    is_followed = True
                else:
                    is_followed = False
            if u.id == user_id:
                log('走这里')
                arg = dict(
                    tweets=tweets,
                    user=u
                )
                return render_template('self_timeline_aftersign.html', **arg)
            else:
                arg = dict(
                    tweets=tweets,
                    user=user,
                    is_followed=is_followed
                )
                return render_template('other_timeline.html', **arg)
    return redirect(url_for('timeline.timeline_view'))


# @main.route('/<user_id>')
# def tweet_view(user_id):
#     user = User.query.filter_by(id=user_id).first()
#     u = current_user()
#     log('debug current_user is:', u)
#     if user is not None:
#         user.visitors_add()
#         if u is not None:
#             if user.is_admin():
#                 tweets = Tweet.query.all()
#                 return render_template('mytimeline.html', user=user, tweets=tweets)
#             else:
#                 tweets = user.tweets
#                 tweets.sort(key=lambda t: t.created_time, reverse=True)
#                 users = User.query.all()
#                 user_others = []
#                 for user in users:
#                     if user.id == u.id:
#                         user_self = user
#                     else:
#                         user_others.append(user)
#                 return render_template('mytimeline.html', user=user_self, users=user_others, tweets=tweets)
#         else:
#             return redirect(url_for('showpage.show_view'))
#     else:
#         return redirect(url_for('showpage.show_view'))


@main.route('/test')
def test_view():
    return render_template('login.html')
