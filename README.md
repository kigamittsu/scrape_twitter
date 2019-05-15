# scrape_twitter

This API can search the tweet information from twitter by hashtag or username.

You can test this API at Heroku!

## Prerequisites

If you want to use this API in local, please install the dependencies using pip or other dependencies manager.

this application depends on the following libraries.

| Library             | version        |
| ------------------- | -------------- |
| flask               | bbb            |
| flask_restful       | bbb            |
| requests            | bbb            |
| selenium            | bbb            |
| chromedriver-binary | 73.0.3683.68.0 |

_Note: You have to download the chromedriver-binary which has same major version of your chrome browser. If you want to check the chrome browser version, you can use the following command._

```
google-chrome --version
```

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

### API Definition

| Library             | version        |
| ------------------- | -------------- |
| flask               | bbb            |
| flask_restful       | bbb            |
| requests            | bbb            |
| selenium            | bbb            |
| chromedriver-binary | 73.0.3683.68.0 |

### Sample Requests

If you want to test this API, we highly recommend to use the [Postman]() or [Insomnia]()

Sample requests of _/hashtags/{hashtagname}_

```
http://127.0.0.1:5000/hashtags/twitter
```

Sample requests of _/users/{username}_

```
http://127.0.0.1:5000/users/twitter
```

### Sample Response

## Feature Plan

1. Response speed (more quick)
2. Add other endpoints
3. Write more test

## License

This project is licensed under the MIT License
