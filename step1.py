import requests

from pathlib import Path
from pprint import pprint


def download_picture(url, path, filename):
    response = requests.get(url, verify=False)
    response.raise_for_status()
    with open(path + filename, 'wb') as file:
        file.write(response.content)


def get_links_spacex(url):
    response = requests.get(url)
    response.raise_for_status()
    links = response.json()["links"]["flickr"]["original"]
    return links


def fetch_spacex_last_launch(links, path):
    for link_number, link in enumerate(links):
        link_number += 1
        download_picture(link, path, filename="spacex{}.jpeg".format(link_number))


def get_links_hubble(url):
    links = []
    response = requests.get(url)
    response.raise_for_status()
    list_info = response.json()['image_files']
    for info in list_info:
        link = "https:{}".format(info['file_url'])
        links.append(link)
    return links


def display_expansion(url):
    link = url.split('.')
    print("File format: {}.".format(link[-1]))


def get_pictures_hubble(links, path):
    for link_number, link in enumerate(links):
        link_number += 1
        download_picture(link, path, filename="hubble{}.jpeg".format(link_number))


path_images = r"e:\Python\DVMN2\photo_inst\venv\Include\inst_photo\images\\"
Path(path_images).mkdir(parents=True, exist_ok=True)

url_spacex = "https://api.spacexdata.com/v4/launches/latest"
url_hubblesite = "http://hubblesite.org/api/v3/image/1"

# fetch_spacex_last_launch(get_links_spacex(url_spacex), path_images)
# pprint(get_links_hubble(url_hubblesite))

url_picture = "https://imgsrc.hubblesite.org/hvi/uploads/image_file/image_attachment/2/full_tif.tif"
# display_expansion(url_picture)
get_pictures_hubble(get_links_hubble(url_hubblesite), path_images)
