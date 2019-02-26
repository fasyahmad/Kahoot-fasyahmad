from flask import Flask, request, json, jsonify
import os

from . import router, usersFileLocation

from ..utils.crypt import encrypt, decrypt
from ..utils.file import readFile, writeFile
from ..utils.authorization import generateToken


@router.route('/alaala')
def alaala():
    return "sampe"


# Register user
@router.route('/register', methods=['POST'])
def register():
    print(os.getenv("API_KEY"))
    body = request.json

    if body["todo"] == "encrypt":
        body["password"] = encrypt(body["password"])
    elif body["todo"] == "decrypt":
        body["password"] == decrypt(body["password"])

    userData = {
        "userList": []
    }

    if os.path.exists(usersFileLocation):
        userFile = open(usersFileLocation, 'r')
        userData = json.load(userFile)
    else:
        userFile = open(usersFileLocation, 'x')

    userData["userList"].append(body)

    userFile = open(usersFileLocation, 'w')
    userFile.write(str(json.dumps(userData)))

    return jsonify(userData)


# Login user
@router.route('/login', methods=["POST"])
def login():
    body = request.json

    if body["todo"] == "encrypt":
        body["password"] = encrypt(body["password"])
    elif body["todo"] == "decrypt":
        body["password"] == decrypt(body["password"])

    # buka file yang udah register
    userFile = open(usersFileLocation)
    userData = json.load(userFile)

    result = ""
    # cari user yang udah register 
    for i in range(len(userData["userList"])):
        registeredUser = userData["userList"][i]
        if registeredUser["username"] == body["username"]:
            if registeredUser["password"] == body["password"]:
                result = "Selamat anda berhasil login"
                body["token"] = generateToken(body["username"])
                break
            else:
                result = "Password anda salah"

    return result