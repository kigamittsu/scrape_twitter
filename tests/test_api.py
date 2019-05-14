import unittest
import requests

TEST_URL_HASHTAG = 'http://127.0.0.1:5000/hashtags/twitter'
TEST_URL_USER = 'http://127.0.0.1:5000/users/twitter'
RESPONSE_KEYS = {'account', 'date', 'hashtags',
                 'text', 'likes', 'replies', 'retweets'}


class TestTweetsByHashtag(unittest.TestCase):

    def test_api_with_illegal_parameter(self):
        params = {'limit': 'aaa'}
        response = requests.get(TEST_URL_HASHTAG, params=params)
        self.assertEqual(400, response.status_code)

    def test_api_with_no_parameter(self):
        response = requests.get(TEST_URL_HASHTAG)
        self.assertEqual(200, response.status_code)
        self.assertEqual(30, len(response.json()))

    def test_api_with_parameter(self):
        params = {'limit': 40}
        response = requests.get(TEST_URL_HASHTAG, params=params)
        self.assertEqual(200, response.status_code)
        self.assertEqual(40, len(response.json()))

    def test_api_response(self):
        params = {'limit': 1}
        response = requests.get(TEST_URL_HASHTAG, params=params)
        self.assertEqual(200, response.status_code)
        json = response.json()
        self.assertEqual(1, len(json))
        self.assertEqual(True, set(json[0]) >= RESPONSE_KEYS)


class TestTweetsByUser(unittest.TestCase):

    def test_api_with_illegal_parameter(self):
        params = {'limit': 'aaa'}
        response = requests.get(TEST_URL_USER, params=params)
        self.assertEqual(400, response.status_code)

    def test_api_with_no_parameter(self):
        response = requests.get(TEST_URL_USER)
        self.assertEqual(200, response.status_code)
        self.assertEqual(30, len(response.json()))

    def test_api_with_parameter(self):
        params = {'limit': 40}
        response = requests.get(TEST_URL_USER, params=params)
        self.assertEqual(200, response.status_code)
        self.assertEqual(40, len(response.json()))

    def test_api_response(self):
        params = {'limit': 1}
        response = requests.get(TEST_URL_USER, params=params)
        self.assertEqual(200, response.status_code)
        json = response.json()
        self.assertEqual(1, len(json))
        self.assertEqual(True, set(json[0]) >= RESPONSE_KEYS)


if __name__ == '__main__':
    unittest.main()
