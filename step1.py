import requests

from pathlib import Path
from pprint import pprint


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


Path(r"e:\Python\DVMN2\photo_inst\venv\Include\inst_photo\\Test").mkdir(parents=True, exist_ok=True)

url = "https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg"
url_spacex = "https://api.spacexdata.com/v4/launches/latest"
path = r"e:\Python\DVMN2\photo_inst\venv\Include\inst_photo\Test\\"

# download_picture(url, path, filename="hubble.jpeg")
show = get_link(url_spacex)
pprint(show)
