import os
from flask import Flask, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import  cross_origin

app = Flask(__name__)
# dir_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__))).replace ("\\" , '/').split(':')[1]
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///home/qhazale/my_flask_app/DataBase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow (app)

@cross_origin(supports_credentials=True)
def show_posts():
    posts = PostModel.query.all()
    out = {'posts':PostModel.serialize_many(posts), 'status':'OK'}
    print (out['posts'])
    return jsonify(out)

app.add_url_rule('/api/posts' , view_func = show_posts )


@cross_origin(supports_credentials=True)
def add_posts():
    req = request.get_json(force = True)
    title = req['title']
    description = req['description']
    print (title, description)

    new_post = PostModel (title, description)
    new_post.save()

    out = {'status':'OK'}
    return jsonify (out)

app.add_url_rule('/api/addPost' , view_func = add_posts, methods = ['GET','POST'])


@cross_origin(supports_credentials=True)
def delete_post (post_id):
    post = PostModel.query.get(int(post_id))
    post.delete()

    out = {'status':'OK'}
    return jsonify(out)

app.add_url_rule('/api/deletePost/<int:post_id>' , view_func = delete_post)


@cross_origin(supports_credentials=True)
def edit_post (post_id):
    post = PostModel.query.get (int(post_id))
    req = request.get_json(force = True)
    title = req['title']
    description = req['description']
    post.edit (title, description)

    out = {'status':'OK'}
    return jsonify(out)

app.add_url_rule('/api/editPost/<int:post_id>' , view_func = edit_post, methods = ['GET','POST'])


class PostModel (db.Model):

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column (db.String(40), nullable = False)
    description = db.Column (db.Text , nullable = False)

    def __init__ (self , title , description):
        self.title = title
        self.description = description

    def edit (self, title, description):
        self.title = title
        self.description = description
        db.session.commit()

    def save (self):
        db.session.add (self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def serialize_many (arg):
        return PostModelSchema(many = True).dump (arg).data

class PostModelSchema (ma.ModelSchema):
    class Meta:
        model = PostModel
