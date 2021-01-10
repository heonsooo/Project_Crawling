from selenium import webdriver
import time

### 개인정보
id = ''
pw = ''
### 



# 크롬 열기
driver = webdriver.Chrome('./chromedriver.exe')

# 웹사이트 들어가기

# url = 'https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com'

driver.get(url)

# 최대화
driver.maximize_window()

# 아이디, 비밀번호
driver.find_element_by_css_selector('#id').send_keys(id)
driver.find_element_by_css_selector('#pw').send_keys(pw)

# 로그인 버튼 클릭
driver.find_element_by_css_selector('#log\.login').click()

time.sleep(5)

driver.get_screenshot_as_file('capture.png')
