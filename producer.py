import pika
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

access_token = "3344745593-v2hyQ5BXJd67iDyBEwFBlCMRJ8uPuYAeMmOkSxt"
access_token_secret = "j7S0Pi5Xusl1Tftna5cCb0EtgLTBanuE5UnMwGFC3DqI2"
consumer_key = "rzVhEV6XGLGOUrrvq6hxpS38m"
consumer_secret = "3CXsrtozZE0a7AFKva7FDqT6exBt42bR7gvZdBuH0pp2rXr9B7"


class StreamProducer(StreamListener):

    def __init__(self):
        return

    def on_data(self, data):
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':
    producer = StreamProducer()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, producer)
    stream.sample()
