import os
import time
from posting import exception_message, new_post
from download import get_last_post
from config import artists

def check_for_new_posts(artists):
    for a in artists:
        get_last_post(a)
        print('search...')
        if [file for file in os.listdir('media/') if os.path.isfile(os.path.join('media/', file))]:
            new_post(a)
            
def main():
    try:
        while True:
            check_for_new_posts(artists)
            time.sleep(180)
    except Exception as e:
        print(e)
        exception_message(e)


if __name__ == '__main__':
    main()