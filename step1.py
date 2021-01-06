import requests


def download_picture(url, path, filename):
    response = requests.get(url)
    response.raise_for_status()
    with open(path + filename, 'wb') as file:
        file.write(response.content)


url = "https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg"
path = r"e:\Python\DVMN2\photo_inst\venv\Include\inst_photo\Test\\"
download_picture(url, path,filename="hubble.jpeg")
