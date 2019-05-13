from flask import Flask
from flask_restful import Resource, Api, reqparse
from scraper import Scraper

URL_HASHTAG = 'https://twitter.com/hashtag/'
URL_USER = 'https://twitter.com/'

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('limit', type=int, default=30)
scraper = Scraper()


class TweetsByHashtag(Resource):
    def get(self, tagname):
        args = parser.parse_args()
        limit = args['limit']
        url = URL_HASHTAG + tagname
        response = scraper.scrape_from_twitter(url, limit)
        return response


class TweetsByUser(Resource):
    def get(self, username):
        args = parser.parse_args()
        limit = args['limit']
        url = URL_USER + username
        response = scraper.scrape_from_twitter(url, limit)
        return response


api.add_resource(TweetsByHashtag, '/hashtags/<string:tagname>')
api.add_resource(TweetsByUser, '/users/<string:username>')

if __name__ == '__main__':
    app.run(debug=True)
