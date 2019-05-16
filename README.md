# scrape_twitter

This API can search the tweet information from twitter by hashtag or username. 

_No need authentication_



## Prerequisites

If you want to use this API in local, please install the packages using pip or other package manager.

this application depends on the following libraries.

| Library             | version        |
| ------------------- | -------------- |
| flask               | 1.0.2          |
| flask_restful       | 0.3.7          |
| requests            | 2.21.0         |
| selenium            | 3.141.0        |
| chromedriver-binary | 73.0.3683.68.0 |

_Note: You have to download the chromedriver-binary which has same major version of your chrome browser. If you want to check the chrome browser version, you can check it in your browser_

The following examples is using pip to install the dependencies.

1. Install the Flask.

```
pip install flask
```

2. Install the flask_restful

```
pip install flask_restful
```

3. Install the requests

```
pip install requests
```

4. Install the selenium

```
sudo pip install selenium
```

5. Install the chromedriver-binary

```
sudo pip install chromedriver-binary=="{Your Chrome version}"
```

## Usage for API

1. Create the clone of project from github.

```
git clone https://github.com/kigamittsu/scrape_twitter.git
```

2. Run the server

```
cd ~/scrape_twitter
python server.js
```

3. Now you can call this API.

## Testing API (Local)

1. Run the server

```
python server.js
```

2. Run the test

```
python -m unittest tests.test_api
```

## API Design

### /hashtags/{hashtagname}?{limit}

Get the tweets information which has target hashtag name

#### Resource

| Resource    | Description         |
| ----------- | ------------------- |
| hashtagname | Target hashtag name |

#### Request parameter

| Request Parameter | Type    | Description                                                   |
| ----------------- | ------- | ------------------------------------------------------------- |
| limit (Optional)  | Integer | Specifies the number of tweets to retrieve, the default is 30 |

### /users/{user}?{limit}

Get the tweets information which has target user name

#### Resource

| Resource | Description      |
| -------- | ---------------- |
| username | Target user name |

#### Request parameter

| Request Parameter | Type    | Description                                                   |
| ----------------- | ------- | ------------------------------------------------------------- |
| limit (Optional)  | Integer | Specifies the number of tweets to retrieve, the default is 30 |

### Sample Requests

If you want to test this API, we highly recommend to use the [Postman](https://www.getpostman.com/) or [Insomnia](https://insomnia.rest/)

Sample requests of _/hashtags/{hashtagname}_

```
http://127.0.0.1:5000/hashtags/twitter?limit=20
```

Sample requests of _/users/{username}_

```
http://127.0.0.1:5000/users/twitter?limit=20
```

### Sample Response

```
[
  {
    "account": {
      "fullname": "foo bar",
      "href": "https://twitter.com/foobar",
      "user_id": "342384"
    },
    "date": "16:23 - 2019年5月15日",
    "hashtags": [
      "#Twitter"
    ],
    "text": "Sample text",
    "likes": 10,
    "replies": 4,
    "retweets": 5
  },
  ...
]
```

## Feature Plan

1. Improve response speed (more quick)
2. Add other endpoints
3. Write more test

## License

This project is licensed under the MIT License
