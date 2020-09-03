#!/usr/bin/env python3

import json
from flask import Flask, request, abort
from flask_cors import CORS, cross_origin
from lib.model.service.MagnetRepository import MagnetRepository
from lib.model.service.search_handler import search_magnet_links

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['CORS_HEADERS'] = 'Content-Type'
cors = CORS(app)

@app.route('/', methods=['GET'])
@cross_origin()
def home():
    return 'home'

@app.route('/magnets', methods=['GET'])
def list():
    repository = MagnetRepository()
    magnets = repository.list()

    return app.response_class(
        response=json.dumps(magnets),
        status=200,
        mimetype='application/json'
    )

@app.route('/search', methods=['GET'])
@cross_origin()
def search():
    query = request.args.get('query')

    magnet = search_magnet_links(query)

    if not magnet:
        return app.response_class(
            response=json.dumps({'message': 'not found'}),
            status=404,
            mimetype='application/json'
        )
# Not working
    return app.response_class(
        response=json.dumps([magnet.to_dict()]),
        status=200,
        mimetype='application/json'
    )

app.run()
