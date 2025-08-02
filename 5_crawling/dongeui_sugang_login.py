import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


login_url = "http://sugang.deu.ac.kr:8080/DEUSugang_LogIn.aspx"
userID = "20203161"
userPW = "tnseoaos123!"

def load_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("window-size=1920,1080")
    options.add_argument("lang=ko_KR")
    return webdriver.Chrome(options=options)

def login_site(driver):
    driver.get(login_url)
    driver.implicitly_wait(3)
    
    driver.find_element(By.NAME, "txtID").send_keys(userID)
    driver.find_element(By.NAME, "txtPW").send_keys(userPW)
            
    driver.find_element(By.NAME, "ibtnLogin").click()
        
        
def check_my_lecture(driver):
    driver.find_element(By.XPATH, "//*[@id='pnl_stu']/ul/li[4]/a").click()
    
    try:
        driver.switch_to.frame("contentFrame")
        print("iframe 전환 성공")
    except Exception as e:
        print("iframe 전환 실패 : ", e)
        return
    
    wait = WebDriverWait(driver, 10)  # 최대 10초 대기
    apply_table = wait.until(EC.presence_of_element_located((By.ID, "CP1_dt_apply")))
    
    wait = WebDriverWait(driver, 10)  # 최대 10초 대기
    daegi_table = wait.until(EC.presence_of_element_located((By.ID, "CP1_dt_daegi")))
    
    if apply_table or daegi_table:
        print("========== 수강확정 ==========")
        print(apply_table.text)
        
        print("========== 수강대기 ==========")
        print(daegi_table.text)
        
    else:
        print("❌ 테이블 요소 찾기 실패!")
    

if __name__ == "__main__":
    # 0. 드라이버 준비
    # 1. 사이트 로그인 -> 성공시 리다이렉트
    # 2. "수강확정/대기내역" 버튼 클릭
    # 3. 수강확정 내역 및 수강 대기내역 확인
    #   3-1. 세부 내용이 iframe 이므로 변경
    #   3-2. iframe 변경 후 table로된 수강 내역
    #   3-5. 수강확정, 대기내역 구분하여 print
    
    driver = load_driver()
    login_site(driver)
    check_my_lecture(driver)
    driver.quit()