from functools import wraps
from flask import request, jsonify
from flask import current_app as app
import jwt

def token_required(f):
   @wraps(f)
   def decorator(*args, **kwargs):

       token = None
       print(request.headers)
       if 'Authorization' in request.headers:
           token = request.headers['Authorization']
           print(token)

       if not token:
           return jsonify({'message': 'a valid token is missing'})
       try:
           print(token)
           data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
           print(data)
       except Exception as e:
           print(e)
           return jsonify({'message': 'token is invalid'})

       return f(*args, **kwargs)
   return decorator
