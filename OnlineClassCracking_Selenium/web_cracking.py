from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

chromedriver = r'D:\Users\User\Downloads'
url = r'https://hoc22.ebssw.kr/sso/loginView.do?loginType=onlineClass&hmpgId=cham2020212'
options = webdriver.ChromeOptions()

options.add_argument(r"user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36")
driver = webdriver.Chrome(chromedriver, chrome_options=options)
driver.get(url)

    
idBtn = driver.find_element_by_xpath(r'//input[@id="j_username"]')
idBtn.click()
idBtn.send_keys(r'siajin1')

psBtn = driver.find_element_by_xpath(r'//input[@id="j_password"]')
psBtn.click()
psBtn.send_keys(r'shi1528624')

btn = driver.find_element_by_xpath(r'//button[@onclick="doGroupMberCheck();"]')
btn.click()


try:
    WebDriverWait(driver, 3).until(EC.alert_is_present(),'Timed out waiting for PA creation ' +'confirmation popup to appear.')
    alert = driver.switch_to.alert
    alert.accept()



subject = input()


driver.find_element_by_partial_link_text(subject).click()
