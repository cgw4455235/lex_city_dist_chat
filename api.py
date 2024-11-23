from flask import Flask, Response
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)
parser = reqparse.RequestParser()
saved_val = {"num": 0}

class AllResources(Resource):
  def get(self):
    return Response(str(saved_val["num"]), 200)
  def post(self):
    parser.add_argument("num")
    args = parser.parse_args()
    saved_val["num"] = args["num"]
    return Response(str(saved_val["num"]), 200)
api.add_resource(AllResources, '/')

if __name__ == "__main__":
  app.run(debug=True)
