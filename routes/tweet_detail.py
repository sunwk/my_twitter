from routes import *

main = Blueprint('tweet', __name__)


@main.route('/<int:tweet_id>')
def tweet_view(tweet_id):
    u = current_user()
    tweet=Tweet.query.filter_by(id=tweet_id).first()
    comments = tweet.comments
    return render_template('tweet_detail.html', tweet=tweet, user=u, comments=comments)