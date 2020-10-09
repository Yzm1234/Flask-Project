# Flask-Project
## A practice project with Flask
This project is using Flask to create http server and api

### Installation
Clone the repo on your local machine and install dependency.

$ pip install -r requirements.txt

### 1. HTTP server 
This section is a small practice to help bigainner get familiar with Flask. A web application is created in Hello.py file and some functions can be triggered 
by certain url paths.
The templates folder contain HTML templates that will be parsed by client web browser as responds for client requests.

### 2. API in Flask
In this section, an API to a samll video database is created in video.py folder. It allows clients to interact with the data, to create, update, delete and 
get rescources by using HTTP methods(POST/PUT/DELETE/GET).

The test.py is a test file for api in video.py. It has some requests to test different http methods.

### 3. PokeAPI

This api mirror was built using [PokeAPI](https://pokeapi.co/).

In PokemonAPI folder, the Pokeapi.py builds the API and the test.py file has http requests to test the api in Pokeapi.py.
Because [PokeAPI](https://pokeapi.co/) only supports http GET method, the API in Pokeapi.py only has endpoints to read info from [PokeAPI](https://pokeapi.co/).
