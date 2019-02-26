from flask import Flask, request, json, jsonify
import jwt
from random import randint
import requests
import os
from src.routes import router
# from ..utils.authorization import generateToken

app = Flask(__name__)
app.register_blueprint(router)

@app.route('/encode')
def jwtEncode():
    encode = jwt.encode({"data": "makers"}, "kucing-merah", algorithm="HS256")
    return encode

@app.route('/decode')
def jwtDecode():
    decode = jwt.decode(request.json["token"], "kucing-merah", algorithms=["HS256"])
    return str(decode)


# if name == "__main__":
#     app.run(debug=True, port=14045)