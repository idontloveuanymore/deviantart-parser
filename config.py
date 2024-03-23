import os 
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

BOT_TOKEN = os.getenv('BOT_TOKEN')
ADMIN_ID = os.getenv('ADMIN_ID')
CHANNEL_ID = os.getenv('CHANNEL_ID')


artists = [
    'idontioveuanymore', # https://www.deviantart.com/idontioveuanymore/gallery
    'test',
    'test1',
    'test2',
    'test3',
]

MEDIA_FOLDER = "media/"