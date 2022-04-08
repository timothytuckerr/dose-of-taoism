import redis
import os
from dotenv import load_dotenv

load_dotenv()
URL = os.getenv('URL')

r = redis.Redis.from_url(URL)

directory = './chapters'
for filename in os.listdir(directory):
    chapter_num = str(filename.split('.')[0])
    f = open(os.path.join(directory, filename), 'r')
    text = f.read()
    set_redis = r.set(chapter_num, text)
    print(chapter_num, set_redis)
