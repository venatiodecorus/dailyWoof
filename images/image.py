from redis import Redis
from imgurpython import ImgurClient
from time import sleep
import json

with open('client.json') as clientFile:
    secrets = json.load(clientFile)

redis = Redis(host='redis', port=6379)
client = ImgurClient(secrets['client_id'], secrets['client_secret'])


while True:
    res = client.gallery_search('fluffy dog', sort='score', window='all', page=0)
    res = ",".join([x.link for x in res])
    redis.set('img:default', res)
    sleep(100000)
