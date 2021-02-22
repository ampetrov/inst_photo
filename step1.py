import requests

from pathlib import Path


def download_picture(url, path, filename):
    response = requests.get(url)
    response.raise_for_status()
    with open(path + filename, 'wb') as file:
        file.write(response.content)


def get_link(url):
    response = requests.get(url)
    response.raise_for_status()
    links = response.json()["links"]["flickr"]["original"]
    return links


def fetch_spacex_last_launch(links, path):
    for link_number, link in enumerate(links):
        link_number += 1
        download_picture(link, path, filename="spacex{}.jpeg".format(link_number))


def display_links(url):
    response = requests.get(url)
    response.raise_for_status()
    list_info = response.json()['image_files']
    for info in list_info:
        link = info['file_url']
        print("https:{}".format(link))


path_images = r"e:\Python\DVMN2\photo_inst\venv\Include\inst_photo\images\\"
Path(path_images).mkdir(parents=True, exist_ok=True)

url_spacex = "https://api.spacexdata.com/v4/launches/latest"
url_hubblesite = "http://hubblesite.org/api/v3/image/1"

fetch_spacex_last_launch(get_link(url_spacex), path_images)
display_links(url_hubblesite)
