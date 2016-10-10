from routes import *

main = Blueprint('edit', __name__)


@main.route('/<int:user_id>')
def edit_view(user_id):
    user = User.query.filter_by(id=user_id).first()
    u = current_user()
    # if user is not None:
    #     if u is not None:
    #         if u.id == user_id:
    if user is not None and u is not None and u.id == user_id:
        log('debug current_user is:', u.id, u.username)
        return render_template('personal_info_edit.html', user=user)
    else:
        return redirect(url_for('timeline.timeline_view'))