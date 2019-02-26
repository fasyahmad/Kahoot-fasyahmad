from flask import request
from functools import wraps

from .crypt import encrypt
from .token import encode

def generateToken(data):
    data = encrypt(data)
    token = encode(data)

    return token

def verifyLogin(f):
#     @wraps(f)
#     def decoratedFunction(*args, **kwargs):
        
#         token = request.headers["Authorization"]
#         data = decode(token)
#         username = decrypt(data["data"])

#         g.username = username

#         print("lewat decorator")
#         return f(*args, **kwargs)
    return decoratedFunction
