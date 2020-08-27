import requests
from pathlib import Path


Path(r"e:\Python\DVMN2\photo_inst\venv\Include\inst_photo\images").mkdir(parents=True, exist_ok=True)

filename = 'satellite.jpeg'
url = "https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg"

response = requests.get(url)
response.raise_for_status()

with open(filename, 'wb') as file:
    file.write(response.content)
