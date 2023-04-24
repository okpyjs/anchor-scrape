import codecs

import requests
from bs4 import BeautifulSoup

from scrape.BaseDriver import BaseDriver

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
    " (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
}


def file_save(content: str, file_name_with_extension: str = "default"):
    f = codecs.open(f"resource/{file_name_with_extension}", mode="wb")
    f.write(content)
    f.close()


def get_soup(url: str):
    resp = requests.get(url, headers=headers)
    if resp.status_code < 400:
        soup = BeautifulSoup(resp.content, features="html.parser")
    else:
        driver = BaseDriver(url).get_driver()
        soup = driver.get_soup()
        driver.close()
    return soup
