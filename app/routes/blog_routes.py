from flask import Blueprint, request, jsonify
from app.models import BlogPost, db
from flask_jwt_extended import jwt_required, get_jwt_identity

blog_bp = Blueprint('blog', __name__)


@blog_bp.route('/', methods=['GET'])
def get_posts():
    page = request.args.get('page', 1, type=int)
    per_page = 5
    posts = BlogPost.query.paginate(
        page=page, per_page=per_page, error_out=False)
    return jsonify([{"id": post.id, "title": post.title, "content": post.content} for post in posts.items])


@blog_bp.route('/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = BlogPost.query.get_or_404(post_id)
    return jsonify({"id": post.id, "title": post.title, "content": post.content})


@blog_bp.route('/', methods=['POST'])
@jwt_required()
def create_post():
    data = request.get_json()
    user_id = get_jwt_identity()
    post = BlogPost(title=data['title'],
                    content=data['content'], author_id=str(user_id))
    db.session.add(post)
    db.session.commit()
    return jsonify({"message": "Post created"}), 201


@blog_bp.route('/<int:post_id>', methods=['PUT'])
@jwt_required()
def update_post(post_id):
    post = BlogPost.query.get_or_404(post_id)
    data = request.get_json()
    post.title = data['title']
    post.content = data['content']
    db.session.commit()
    return jsonify({"message": "Post updated"}), 200


@blog_bp.route('/<int:post_id>', methods=['DELETE'])
@jwt_required()
def delete_post(post_id):
    post = BlogPost.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    return jsonify({"message": "Post deleted"}), 200
