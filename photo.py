from pathlib import Path
from pprint import pprint

import requests


def download_picture(url, path, filename):
    response = requests.get(url)
    response.raise_for_status()
    with open(path + filename, 'wb') as file:
        file.write(response.content)


def get_link(url):
    response = requests.get(url)
    response.raise_for_status()
    links = response.json()[12]['links']['flickr']['original']
    return links


def fetch_spacex_last_launch(links, path):
    for link_number, link in enumerate(links):
        link_number += 1
        download_picture(link, path, filename="spacex{}.jpeg".format(link_number))


def display_links(url):
    link_list = []
    response = requests.get(url)
    response.raise_for_status()
    list_info = response.json()['image_files']
    for info in list_info:
        link = info['file_url']
        print("https:{}".format(link))


Path(r"e:\Python\DVMN2\photo_inst\venv\Include\inst_photo\images").mkdir(parents=True, exist_ok=True)
url = "https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg"
url_spacex = "https://api.spacexdata.com/v4/launches"
url_hubblesite = "http://hubblesite.org/api/v3/image/1"
path = r"e:\Python\DVMN2\photo_inst\venv\Include\inst_photo\images\\"
links = get_link(url_spacex)
fetch_spacex_last_launch(links, path)
display_links(url_hubblesite)
