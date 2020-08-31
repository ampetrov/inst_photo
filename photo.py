from pathlib import Path

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


Path(r"e:\Python\DVMN2\photo_inst\venv\Include\inst_photo\images").mkdir(parents=True, exist_ok=True)

url = "https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg"
url_spacex = "https://api.spacexdata.com/v4/launches"
path = r"e:\Python\DVMN2\photo_inst\venv\Include\inst_photo\images\\"
# filename = "spacex.jpeg"
# download_picture(url, path, filename)
links = get_link(url_spacex)
# ['https://farm9.staticflickr.com/8617/16789019815_f99a165dc5_o.jpg',
#  'https://farm8.staticflickr.com/7619/16763151866_35a0a4d8e1_o.jpg',
#  'https://farm9.staticflickr.com/8569/16169086873_4d8829832e_o.png']

for link_number, link in enumerate(links):
    link_number +=1
    download_picture(link, path, filename="spacex{}.jpeg".format(link_number))

