# from selenium import webdriver
# from bs4 import BeautifulSoup
#
# # 设置浏览器选项
# options = webdriver.ChromeOptions()
# options.add_argument('--headless')  # 无头模式
# options.add_argument('--disable-gpu')  # 禁用GPU加速
#
# # 创建浏览器对象
# browser = webdriver.Edge(options=options)
#
# # 访问京东主页
# browser.get('https://www.jd.com/')
#
# # 获取页面源代码
# html = browser.page_source
#
# # 解析页面
# soup = BeautifulSoup(html, 'html.parser')
# pv = soup.find('span', {'class': 'curr-shopcart-num'}).text
# if pv is not None:
#     pv = pv.text
# else:
#     pv = 'N/A'
#
# # 关闭浏览器
# browser.quit()
#
# print('京东主页的日均PV为：', pv)
import requests
from bs4 import BeautifulSoup

url = 'https://www.jd.com/'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
pv = soup.find('h2', {'class': 'logo_subtit'})
if pv is not None:
    pv = pv.text
else:
    pv = 'N/A'
print(pv)
