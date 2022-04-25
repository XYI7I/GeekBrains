from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--window-size=765,1200')

driver = webdriver.Chrome(executable_path='./chromedriver.exe', options=chrome_options)

driver.get('https://gb.ru/login')

login = driver.find_element_by_id('user_email')
login.send_keys('study.ai_172@mail.ru')

passw = driver.find_element_by_id('user_password')
passw.send_keys('Password172')

passw.send_keys(Keys.ENTER)

menu = driver.find_element_by_xpath("//span[contains(text(),'меню')]")
menu.click()

button = driver.find_element_by_xpath("//button[@data-test-id='user_dropdown_menu']")
button.click()

link = driver.find_element_by_xpath("//li/a[contains(@href,'/users/')]")
url = link.get_attribute('href')
driver.get(url)







