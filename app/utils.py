from app.models import BlogPost


def get_user_blogs(user_id):
    return BlogPost.query.filter_by(author_id=user_id).all()
