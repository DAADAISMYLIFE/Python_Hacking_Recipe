from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

login_url = "http://sugang.deu.ac.kr:8080/DEUSugang_LogIn.aspx"

user_id = "20203161"
user_pw = "tnseoaos123!"

def load_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("window-size=1920,1080")
    options.add_argument("lang=ko_KR")
    options.add_experimental_option("detach", True) # 브라우저 바로 꺼지는 
    return webdriver.Chrome(options=options)

def try_login():
    driver.get(login_url)
    driver.implicitly_wait(3)
    
    for id in user_id:
        driver.find_element(By.NAME, "txtID").send_keys(id)
    
    for pw in user_pw: 
        driver.find_element(By.NAME, "txtPW").send_keys(pw)
    
    driver.find_element(By.NAME, "ibtnLogin").click()
    
    elements = driver.find_elements(By.XPATH, "/html/body/ul/li[1]/a")
    for element in elements:
        print(element.text)
        
if __name__ == "__main__":
    driver = load_driver()
    try_login()