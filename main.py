import random
import urllib.request


def download_web_image(url):
    name = random.randrange(1, 1000)
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url, full_name)


download_web_image("https://pm1.narvii.com/6830/486b9d45ebc083034464e6cd9afe39f27daedd25v2_hq.jpg")
