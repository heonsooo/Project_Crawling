from selenium import webdriver
import time

# 크롬 열기
driver = webdriver.Chrome('./chromedriver.exe')
url = 'https://www.naver.com/'

driver.get(url)

# 최대화
driver.maximize_window()
a = '#NM_FAVORITE > div.group_nav > ul.list_nav.type_fix > li:nth-child(4) > a'.replace(' ', '')
driver.find_element_by_css_selector(a).click()

time.sleep(5)