from routes import *


main = Blueprint('timeline', __name__)


@main.route('/<user_id>')
def tweet_view(user_id):
    user = User.query.filter_by(id=user_id).first()
    u = current_user()
    log('debug current_user is:',u)
    if user is not None:
        user.visitors_add()
        if u is not None:
            if user.is_admin():
                tweets = Tweet.query.all()
                return render_template('mytimeline.html', user=user, tweets=tweets)
            else:
                tweets = user.tweets
                tweets.sort(key=lambda t: t.created_time, reverse=True)
                users = User.query.all()
                user_others = []
                for user in users:
                    if user.id == u.id:
                        user_self = user
                    else:
                        user_others.append(user)
                return render_template('mytimeline.html', user=user_self, users=user_others, tweets=tweets)
        else:
            return redirect(url_for('showpage.show_view'))
    else:
        return redirect(url_for('showpage.show_view'))


@main.route('/test')
def test_view():
    return render_template('personal_info_edit.html')