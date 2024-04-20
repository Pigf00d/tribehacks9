from selenium import webdriver
from selenium.webdriver.common.by import By



DRIVER_PATH = "C:\\Users\\theso\\chromedriver-win64"
driver = webdriver.Chrome()
driver.get('https://www.ratemyprofessors.com/search/professors/269?q=*')
h1 = driver.find_elements(By.CLASS_NAME, 'TeacherCard__StyledTeacherCard-syjs0d-0 dLJIlx')
h2 = driver.find_elements(By.TAG_NAME, 'a')
print(h2[0].text)


