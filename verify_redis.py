import redis
import os
from dotenv import load_dotenv

load_dotenv()
URL = os.getenv('URL')

r = redis.Redis.from_url(URL)

directory = './chapters'
for filename in os.listdir(directory):
    chapter_num = str(filename.split('.')[0])
    text = r.get(chapter_num)
    print(chapter_num)
    print(text)
    print('\n\n')
