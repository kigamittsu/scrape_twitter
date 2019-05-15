from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import chromedriver_binary
import time


class Scraper():
    def scrape_from_twitter(self, url, limit):
        try:
            driver = self.get_page(url)
            body = driver.find_element_by_tag_name('body')
            response = self.get_tweets(driver, body, limit)
            return response
        except Exception as e:
            print('catch exception!', e)
        finally:
            driver.quit()

    def get_page(self, url):
        options = Options()
        #options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
        options.add_argument('--headless')
        driver = webdriver.Chrome(chrome_options=options)
        driver.get(url)
        return driver

    def get_tweets(self, driver, body, limit):
        tweets = []
        responses = []

        while (len(tweets) < limit):
            body.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.2)
            tweets = driver.find_elements_by_class_name('tweet')
            if len(tweets) == 0:
                print('Not Found! Please change your search word!')
                return responses
        if len(tweets) > limit:
            tweets = tweets[:limit]

        for tweet in tweets:
            response = {}
            hashtags_array = []
            account_group = tweet.find_element_by_class_name('account-group')
            response['account'] = {
                "fullname": tweet.find_element_by_class_name('fullname').text,
                "href": account_group.get_attribute('href'),
                "user_id": account_group.get_attribute('data-user-id')
            }
            response['date'] = tweet.find_element_by_class_name(
                'tweet-timestamp').get_attribute('title')

            hashtags = tweet.find_elements_by_class_name(
                'twitter-hashtag')
            if len(hashtags) != 0:
                for hashtag in hashtags:
                    hashtags_array.append(hashtag.text)
            response['hashtags'] = hashtags_array

            response['text'] = tweet.find_element_by_class_name(
                'tweet-text').text

            likes = tweet.find_element_by_class_name(
                'js-actionFavorite').find_element_by_class_name('ProfileTweet-actionCountForPresentation').text
            if not likes:
                likes = '0'
            response['likes'] = int(likes.replace(',', ''))

            replies = tweet.find_element_by_class_name(
                'js-actionReply').find_element_by_class_name('ProfileTweet-actionCountForPresentation').text
            if not replies:
                replies = '0'
            response['replies'] = int(replies.replace(',', ''))

            retweets = tweet.find_element_by_class_name(
                'js-actionRetweet').find_element_by_class_name('ProfileTweet-actionCountForPresentation').text
            if not retweets:
                retweets = '0'
            response['retweets'] = int(retweets.replace(',', ''))

            responses.append(response)
        return responses
