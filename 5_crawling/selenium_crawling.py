from selenium import webdriver
from PIL import Image # pip install pillow : 이미지 처리를 위한 모듈

url = "https://www.coupang.com/np/campaigns/11338"

options = webdriver.ChromeOptions()
options.add_argument("window-size=1920,1080") # 창 크기
options.add_argument("lang=ko_KR") # 언어 설정

driver = webdriver.Chrome(options=options)
driver.get(url)
driver.implicitly_wait(3)
driver.get_screenshot_as_file("web.png")

# 이미지 처리
Image.open("web.png").convert("RGB").save("web.jpg", quality=100)
im = Image.open("web.jpg")
# 시작 좌표 (280, 300)에서 끝 좌표 (1100, 780)까지를 잘라 저장
cropped_image = im.crop((280,300, 1100, 780))
cropped_image.save("web_cropped.jpg", quality=100)

driver.close()