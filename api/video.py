from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

videos = {}
video_args = reqparse.RequestParser()
video_args.add_argument("name", type = str, help = "Name of the video")
video_args.add_argument("views", type = int, help = "views of the video")
video_args.add_argument("likes", type = int, help = "Likes on the video")

def abort_if_video_does_not_exist(video_id):
	if video_id not in videos:
		abort(404, message = 'Not Found.')

def abort_if_video_exists(video_id):
	if video_id in videos:
		abort(409, message = 'Video already exists.')

def get_new_video_id():
	cnt = len(videos.keys())
	return cnt

class Video(Resource):
	def get(self, video_id):
		abort_if_video_does_not_exist(video_id)
		return videos[video_id]

	def put(self, video_id):
		args = video_args.parse_args()
		videos[video_id] = args
		return {video_id: args}, 201

	def post(self, video_id):
		abort_if_video_exists(video_id)
		args = video_args.parse_args()
		videos[video_id] = args
		return {video_id: args}, 201


	def delete(self, video_id):
		abort_if_video_does_not_exist(video_id)
		del videos[video_id]
		return '', 204

api.add_resource(Video, '/video/<video_id>')


if __name__ == '__main__':
   app.run(debug = True)