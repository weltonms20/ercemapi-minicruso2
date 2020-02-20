from flask import Flask
from flask_restful import Resource, Api
import json

app = Flask(__name__)
api = Api(app)


with open('Tema1.json', 'r') as f:
    json_data = json.load(f)
    print(json_data)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n")

class HelloWorld(Resource):
    def get(self):
        return json_data

api.add_resource(HelloWorld, '/Tema1')

if __name__ == '__main__':
    app.run(debug=True)