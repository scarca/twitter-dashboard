import pika
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import time

class StreamProducer(StreamListener):

    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
        self.channel = self.connection.channel()
        self.channel.exchange_declare(exchange='tweets', type='fanout')
        return

    def on_data(self, data):
        print data
        self.channel.basic_publish(exchange='tweets', routing_key='', body=data)
        return True

    def on_error(self, status):
        print status


if __name__ == '__main__':
    producer = StreamProducer()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, producer)
    stream.sample()
    # while True:
    #     producer.on_data('its a message')
    #     time.sleep(3)
