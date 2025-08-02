# web_path_scanner.py
# html 문서 내의 태그를 분석하여 경로를 탐색

import requests
from bs4 import BeautifulSoup, SoupStrainer

target_domain = "https://shop.hakhub.net/"

content = requests.get(url=target_domain).content
links = set()

# SoupStrainer : BeautifulSoup에 추출할 부분을 알려주고 구문 분석 시 조건에 맞는 요소만 구성 가능함
for link in BeautifulSoup(content, features="html.parser", parse_only=SoupStrainer("a")): # "a" 태그만 가져오도록함
    # href 속성이 있다면 이 요소로 가져와 경로로 변환한다.
    if hasattr(link, "href"):
        path = link["href"]
        if target_domain not in path and path[:4] != "http":
            links.add(target_domain + path)
        else:
            links.add(path)
            
for link in links:
    print(link)