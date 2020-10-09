from flask import Flask, jsonify, Response
from flask_restful import Resource, Api, fields, marshal_with
import requests, json

app = Flask(__name__)
api = Api(app)

# Get all Pokemon info
@app.route('/pokemon/all', methods=['GET'])
def poke_names():
    data = []
    name_url = "https://pokeapi.co/api/v2/pokemon?limit=50"
    while True:
        resp = requests.get(name_url)
        json = resp.json()
        data.extend(json.get('results', []))
        name_url = json.get('next')
        if not name_url: break
    return json


# Get pokemon description by id
@app.route('/pokemon/<int:pokemon_id>', methods=['GET'])
def get_description(pokemon_id):
    descrip_url = f"https://pokeapi.co/api/v2/pokemon-species/{pokemon_id}"
    r = requests.get(descrip_url)
    json_blob = r.json()
    flav_text = extract_descriptive_text(json_blob)
    return jsonify({'description': flav_text})


def extract_descriptive_text(json_blob, language='en'):
    text = []
    for f in json_blob['flavor_text_entries']:
        if f['language']['name'] == language:
            text.append(f['flavor_text'])
    return text

# Get pokemon by name
@app.route('/pokemon/<string:name>')
def get_poke_(name):
    descrip_url = f"https://pokeapi.co/api/v2/pokemon-species/{name}"
    r = requests.get(descrip_url)
    json_blob = r.json()
    flav_text = extract_descriptive_text(json_blob)
    return jsonify({'name': name},{'description': flav_text})



if __name__ == "__main__":
    app.run(debug=True)
