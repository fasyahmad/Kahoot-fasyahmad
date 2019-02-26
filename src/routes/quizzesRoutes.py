from flask import Flask, request, json, jsonify
import os

from . import router, quizzesFileLocation, questionsFileLocation
from ..utils.file import readFile, writeFile
from ..utils.authorization import verifyLogin

# bikin kuis baru
@router.route('/quizzes', methods=['POST'])
def createQuiz():
    body = request.json

    quizData = {
        "total-quiz-available": 0,
        "quizzes": []
    }

    if os.path.exists(quizzesFileLocation):
        quizzesFile = open(quizzesFileLocation, 'r')
        quizData = json.load(quizzesFile)
    else:
        quizzesFile = open(quizzesFileLocation, 'x')

    quizData["total-quiz-available"] += 1
    quizData["quizzes"].append(body)

    quizzesFile = open(quizzesFileLocation, 'w')
    quizzesFile.write(str(json.dumps(quizData)))

    return jsonify(quizData)

# meminta data kuis dan soalnya
@router.route('/quizzes/<quizId>') #kalau gaada methodnya itu defaulnya ["GET"]
def getQuiz(quizId):
    # nyari quiznya
    quizzesFile = open(quizzesFileLocation)
    quizzesData = json.load(quizzesFile) #kalo load itu dari file

    for quiz in quizzesData["quizzes"]:
        if quiz["quiz-id"] == int(quizId):
            quizData = quiz
            break

    # nyari soalnya
    questionsFile = open(questionsFileLocation)
    questionsData = json.load(questionsFile)

    for question in questionsData["questions"]:
        # question = json.loads(question)
        if question["quiz-id"] == int(quizId):
            quizData["question-list"].append(question)

    return jsonify(quizData)

#update dan delete quiz
@router.route('/quizzes/<quizId>', methods=["PUT", "DELETE"])
def updateDeleteQuiz(quizId):
    if request.method == "DELETE":
        return deleteQuiz(quizId)
    elif request.method == "PUT":
        return updateQuiz(quizId)

def deleteQuiz(quizId):
    
    # nyari quiznya
    quizzesFile = open(quizzesFileLocation)
    quizzesData = json.load(quizzesFile) 

    for i in range(len(quizzesData["quizzes"])):
        if quizzesData["quizzes"][i]["quiz-id"] == int(quizId):
            quizzesData["quizzes"].pop(i)
            quizzesData["total-quiz-available"] -= 1
            break


    with open(quizzesFileLocation, 'w') as quizzesFile:
        quizzesFile.write(str(json.dumps(quizzesData)))

    return jsonify(quizzesData)

def updateQuiz(quizId):
    body = request.json
    
    quizzesFile = open(quizzesFileLocation)
    quizzesData = json.load(quizzesFile) 

    for i in range(len(quizzesData["quizzes"])):
        if quizzesData["quizzes"][i]["quiz-id"] == int(quizId):
            quizzesData["quizzes"][i]["quiz-category"] = body["quiz-category"]
            quizzesData["quizzes"][i]["quiz-name"] = body["quiz-name"]
            break

    with open(quizzesFileLocation, 'w') as quizzesFile:
        quizzesFile.write(str(json.dumps(quizzesData)))

    return jsonify(quizzesData)
