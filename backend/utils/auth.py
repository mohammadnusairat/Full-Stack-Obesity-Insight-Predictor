import bcrypt
import jwt
import os
from datetime import datetime, timedelta

def hash_password(password):
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

def verify_password(password, hashed):
    return bcrypt.checkpw(password.encode('utf-8'), hashed)

def create_token(user_id):
    payload = {
        'user_id': user_id,
        'exp': datetime.utcnow() + timedelta(hours=2)
    }
    token = jwt.encode(payload, os.getenv('JWT_SECRET_KEY'), algorithm='HS256')
    return token

def verify_token(token):
    try:
        decoded = jwt.decode(token, os.getenv('JWT_SECRET_KEY'), algorithms=['HS256'])
        return decoded
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
