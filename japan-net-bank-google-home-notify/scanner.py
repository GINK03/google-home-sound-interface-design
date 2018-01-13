from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import datetime 
import requests
JNB_SECRET = os.environ['JNB_SECRET']
driver = webdriver.Chrome()
driver.get("https://login.japannetbank.co.jp")

import bs4
html = driver.page_source
soup = bs4.BeautifulSoup(html)
print(soup.title)
'''
elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
'''
#driver.find_element_by_class_name('login').click()
driver.find_element_by_class_name('btn02').click()
html = driver.page_source
soup = bs4.BeautifulSoup(html)
print(soup.title)

elem = driver.find_element_by_name("TenNo")
elem.send_keys("001")
elem = driver.find_element_by_name("KozaNo")
elem.send_keys("4661230")
elem = driver.find_element_by_name("LoginId")
elem.send_keys("gink03")
elem = driver.find_element_by_name("Pw")
elem.send_keys(JNB_SECRET)

driver.find_element_by_name('login').click()
now = datetime.datetime.now()
now = now.strftime('%Y-%m-%d %H:%M:%S')
driver.save_screenshot('screenshot/screenshot_{}.png'.format(now))
#driver.find_element_by_name('logout').click()
try:
  html = driver.page_source
  now = datetime.datetime.now()
  now = now.strftime('%Y-%m-%d %H:%M:%S')
  open('html/{}.html'.format(now), 'w').write( html )
  soup = bs4.BeautifulSoup(html)
  amount_money =  soup.find('td', {'class':'yenBalance'}).text.strip()
  text = '今のJNBの残りの残高は、' + amount_money + 'です'
  requests.post("http://192.168.14.31:8091/google-home-notifier", data={'text': text})
  # ログアウト処理
  driver.execute_script('javascript:commonSubmit("ln0002")')
except Exception as ex:
  print(ex)
  ...
driver.close()
os.system('pkill chrome')
