from flask import Flask, jsonify, request
import connect
from repositories.DictionaryRepository import DictionaryRepository
from Entity.Dictionary import Dictionary
from application import app
import json


@app.route("/")
def index():
    db = connect.connectDb()
    return "success"


@app.route("/dictionaries", methods=['GET'])
def getDictionaries():
    repository = DictionaryRepository(Dictionary, )
    dictionaries = repository.getAll()
    result = []
    for dictionary in dictionaries:
        dd = dict()
        dd['id'] = dictionary.id
        dd['title'] = dictionary.title
        result.append(dd)
    return result


@app.route("/dictionaries/<id>", methods=['GET'])
def getDictioneryById(id):
    repository = DictionaryRepository(Dictionary)
    dictionary = repository.getOneById(id)
    dd = dict()
    dd['id'] = dictionary.id
    dd['title'] = dictionary.title
    return dd


@app.route("/dictionaries", methods=['POST'])
def addDictionary():
    if request.method == 'POST':
        data = request.get_json()
        repository = DictionaryRepository(Dictionary)
        repository.AddDictionary(data)
    return 1


if __name__ == 'main':
    app.run(debug=True)