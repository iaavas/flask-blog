from flask import Blueprint, request, jsonify, render_template
from app.models import BlogPost, db, User
from flask_jwt_extended import jwt_required, get_jwt_identity

blog_bp = Blueprint('blog', __name__)


@blog_bp.route('/', methods=['GET'])
def get_posts():
    page = request.args.get('page', 1, type=int)
    per_page = 5
    posts = BlogPost.query.paginate(
        page=page, per_page=per_page, error_out=False)

    return jsonify({
        "blogs": [{"id": post.id, "title": post.title, "content": post.content, "created_at": post.created_at, "author_id": post.author_id} for post in posts.items],
        "current_page": posts.page,
        "total_pages": posts.pages,
        "per_page": posts.per_page,
        "total_items": posts.total
    })


@blog_bp.route('/<int:post_id>', methods=['GET'])
def get_post(post_id):
    post = BlogPost.query.get_or_404(post_id)
    author_name = User.query.get(post.author_id).username
    return jsonify({"id": post.id, "title": post.title, "content": post.content, "created_at": post.created_at, "author_name": author_name})


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
