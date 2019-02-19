from ecommerce import db, login_manager, mongo
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from flask_login import UserMixin
from bson.objectid import ObjectId
from flask_admin.contrib.pymongo import ModelView, filters

#from flask_admin.contrib.mongoengine import ModelView


class User(UserMixin, db.Document):
    #meta = {'collection': 'users'}
    #meta = {'DB': 'myDatabase'}
    username = db.StringField(max_length=30)
    email = db.EmailField(max_length=30)
    password = db.StringField()
    role = db.StringField()
    approved = db.BooleanField()
    isactive = db.BooleanField()
    item = db.StringField()
    wishlist = db.StringField()
    list_address = db.StringField()

    def __rep__(self):
        return 'User({},{})'.format(self.username, self.email)

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'])
        print('Serializer working',type(self.id))

        return s.dumps({'user_id': self.email}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SERET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

# with switch_db(User, 'archive') as User:
# User(name='Ross').save()  # Saves the 'archive-user-db'
'''
hashpass = generate_password_hash("mohitarora123", method='sha256')
role = 'admin'
User("Mohit Arora","arora3mohit@gmail.com",hashpass,role).save()
'''
@login_manager.user_loader
def load_user(user_id):
    return User.objects(pk=user_id).first()

class UserView(ModelView):
    column_list = ('name', 'email', 'password')
    column_sortable_list = ('name', 'email', 'password')

    form = User

'''
class UserView(ModelView):
    column_list = ('name', 'email', 'password')
    column_sortable_list = ('name', 'email', 'password')
    form = User


aadmin.add_view(ModelView(User))

'''
#admin.add_view(ModelView(Post, db.session))
# Admin.add_view(UserView(User))


'''class User(Document):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True, nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)
    #items= db.relationship('Item', backref='user', lazy =True)

    def __rep__(self):
        return 'User({},{})'.format(self.username, self.email)

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SERET_KEY'])
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SERET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)
'''
