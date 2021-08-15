from bs4 import BeautifulSoup
import requests
import shutil

URL = "https://xkcd.com/"

for i in range(1, 11):
    res = requests.get(f"{URL}/{i}")

    data = BeautifulSoup(res.text, "html.parser")

    image = data.find("div", {"id": "comic"}).find("img")
    img_url = URL + image.attrs["src"]
    img_req = requests.get(img_url, stream=True)
    if img_req.status_code == 200:
        print(f"Downloading{img_url}")
        with open(f"images/{i}.png", "wb") as f:
            img_req.raw.decode_content = True
            shutil.copyfileobj(img_req.raw, f)