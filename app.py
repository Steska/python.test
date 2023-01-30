from flask import Flask, jsonify, request
import connect
from models.Dictionary import Dictionary
from application import app


@app.route("/")
def index():
    db = connect.connectDb()
    return "success"


@app.route("/dictionaries", methods=['GET'])
def getDictionaries():

    dictionaries = Dictionary().getAll()
    result = []
    for dictionary in dictionaries:
        dd = dict()
        dd['id'] = dictionary.id
        dd['title'] = dictionary.title
        result.append(dd)
    return result


@app.route("/dictionaries/<id>", methods=['GET'])
def getDictioneryById(id):
    dictionary = Dictionary().getOneById(id)
    dd = dict()
    dd['id'] = dictionary.id
    dd['title'] = dictionary.title
    return dd


@app.route("/dictionaries", methods=['POST'])
def addDictionary():
    if request.method == 'POST':
        data = request.get_json()
        Dictionary().AddDictionary(data)
    return ''


if __name__ == 'main':
    app.run(debug=True)