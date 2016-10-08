from routes import *

main = Blueprint('tweet', __name__)


@main.route('/<int:tweet_id>')
def tweet_view(tweet_id):
    u = current_user()
    tweet = Tweet.query.filter_by(id=tweet_id).first()
    if u is not None:
        comments = tweet.comments
        comments.sort(key=lambda t: t.created_time, reverse=True)
        arg = dict(
            tweet=tweet,
            user=u,
            comments=comments
        )
        return render_template('tweet_detail.html', **arg)
    else:
        return redirect(url_for('timeline.timeline_view'))