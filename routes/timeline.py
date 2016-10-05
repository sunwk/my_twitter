from routes import *

main = Blueprint('timeline', __name__)


@main.route('/')
def timeline_view():
    u = current_user()
    tweets = Tweet.query.all()
    tweets.sort(key=lambda t: t.created_time, reverse=True)
    if u is None:
        return render_template('all_timeline_beforesign.html', tweets=tweets)
    else:
        return render_template('all_timeline_aftersign.html', tweets=tweets)


@main.route('/<int:user_id>')
def self_timeline_view(user_id):
    user = User.query.filter_by(id=user_id).first()
    u = current_user()
    log('debug current_user is:', u.id, u.username)
    if user is not None:
        if u is not None:
            user.visitors_add()
            tweets = user.tweets
            tweets.sort(key=lambda t: t.created_time, reverse=True)
            log('debug user id  u id', user_id, u.id, type(u.id), type(user_id), u.id == user_id)
            if u.id == user_id:
                log('走这里')
                return render_template('self_timeline_aftersign.html', tweets=tweets, user=user)
            else:
                return render_template('other_timeline.html', tweets=tweets, user=user)
    else:
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
    return render_template('self_timeline_aftersign.html')
