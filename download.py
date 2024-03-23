from bs4 import BeautifulSoup as bs
from posting import exception_message
import requests
import os

def download_img(url, save_path='media/'):
    try:
        print(f'downloading...')
        response = requests.get(url)
        if response.status_code == 200:
            filename = os.path.join(save_path, url.split('/')[-1][-10:] + '.jpg')
            with open(filename, 'wb') as f:
                f.write(response.content)
        else:
            exception_message(response.status_code)
    except Exception as e:
        exception_message(e)

def get_good_rosolution(url):
    try:
        print(f'get_good_rosolution...')
        response = requests.get(url)

        if response.status_code == 200:
            soup = bs(response.text, 'html.parser')
            image_url = soup.find('meta', property='og:image')['content']
            download_img(image_url)
        else:
            print(f"Failed to load {url}. Status code: {response.status_code}")
    except Exception as e:
        exception_message(e)


def skin_test(link):
    try:
        print(f'skin_test...')
        with open('verification/downloaded.txt', 'r') as file:
            existing_links = file.readlines()

        if link + '\n' not in existing_links:
            with open('verification/downloaded.txt', 'a') as file:
              get_good_rosolution(link)
              file.write(link + '\n')
    except Exception as e:
        exception_message(e)

def get_last_post(artist):
    try:
        print(f'check {artist}')
        url = f'https://www.deviantart.com/{artist}/gallery/'

        response = requests.get(url)
        html_content = response.text
        soup = bs(html_content, 'html.parser')
        element = soup.find(class_="_1xcj5 _1QdgI")

        if element:
            link = element.find('a')['href']
            skin_test(link)
        else:
            exception_message(f'No image found on page {url}!')
    except Exception as e:
        exception_message(e)