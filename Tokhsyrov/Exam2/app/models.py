# import os
# from flask import url_for
# import sqlalchemy as sa
# from flask_login import UserMixin
# from werkzeug.security import generate_password_hash, check_password_hash
# import markdown
# from app import db



# class Image(db.Model):
#     __tablename__ = 'images'

#     id = db.Column(db.String(36), primary_key=True)
#     file_name = db.Column(db.String(100), nullable=False)
#     mime_type = db.Column(db.String(100), nullable=False)
#     md5_hash = db.Column(db.String(100), nullable=False, unique=True)
#     created_at = db.Column(db.DateTime, nullable=False, server_default=sa.sql.func.now())
#     object_type = db.Column(db.String(100))
#     object_id = db.Column(db.Integer)
#     active = db.Column(db.Boolean(False), nullable=False, default=False)

#     def __repr__(self):
#         return '<Image %r>' % self.file_name

#     @property
#     def url(self):
#         return url_for('image', image_id=self.id)

#     @property
#     def storage_filename(self):
#         _, ext = os.path.splitext(self.file_name)
#         return self.id + ext


