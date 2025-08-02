import requests
from bs4 import BeautifulSoup

url = "https://shop.hakhub.net"

r = requests.get(url)
soup = BeautifulSoup(r.text, "html.parser")
print(r.text)

elem_li = soup.find_all("li", {"class": "product"}) # 태그가 li이면서 class가 product로 시작하는 모든 태그를 가져옴

for index, li in enumerate(elem_li):
    print(f"\n========{index + 1}========")
    print(li.find("h2", {"class" : "woocommerce-loop-product__title"}).text)
    print(li.find("span", {"class" : "price"}).text)
    try:
        print(li.find("strong", {"class" : "rating"}).text)
    except Exception as e:
        print("가격 정보 없음")