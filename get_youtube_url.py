from selenium import webdriver

# 크롬드라이버 열기
driver = webdriver.Chrome('./chromedriver.exe')

# 웹사이트 들어가기
keyword = '손흥민'
url = 'https://www.youtube.com/results?search_query='+keyword
driver.get(url)

# 최대화 (링크만 얻을때는 주석처리 )
driver.maximize_window()

# 맨 위의 youtube 영상 클릭 
driver.find_element_by_css_selector('#video-title > yt-formatted-string').click()

# 맨 위의 youtube 영상의 링크 획득
you_url = driver.current_url

print(you_url)