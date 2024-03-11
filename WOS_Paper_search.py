import os
import re
import math

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

# CMD命令
# msedge.exe --remote-debugging-port=9527 --user-data="D:\UserBrowerData"

Edge_options = webdriver.EdgeOptions()
# Edge_options.add_experimental_option("debuggerAddress","127.0.0.1:9527")
# prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': r'D:\EdgeDownload'}
prefs = {'profile.default_content_settings.popups': 0,
         'download.default_directory': r'D:\PycharmProjects\Extract_table\Literature_Download'}  # 设置下载文件存放路径，这里要写绝对路径
Edge_options.add_experimental_option('prefs', prefs)
Edge_options.add_argument(r'--user-data-dir=C:\Users\Administrator\AppData\Local\Microsoft\Edge\User Data')
Edge_options.add_experimental_option("excludeSwitches", ["enable-automation"])
Edge_options.add_experimental_option('useAutomationExtension', False)
Edge_options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Edge(options=Edge_options)

url = 'https://www.webofscience.com/wos/woscc/basic-search'
# url = 'https://www.baidu.com'
driver.get(url)

# 查找元素
sleep(1)
driver.find_element(By.ID, 'mat-input-0').clear()
driver.find_element(By.ID, 'mat-input-0').send_keys('Y6 donors')
sleep(3)
driver.find_element(By.XPATH, '//*[@id="snSearchType"]/div[3]/button[2]/span[1]').click()
sleep(1)
content = driver.page_source
regex = r"<span class=\"brand-blue\">(.*?)</span>"
Resul_num = re.findall(regex, content)
# 定义一个期刊列表存储期刊种类
Periodical_list = {}
Periodical_url_list = {}
# 设置爬取几页
# 爬取前设置每页显示25条记录
for i in range(1, math.ceil(int(Resul_num[0])/25)+1):
    if(i!=1):
        current_url = str(driver.current_url)
        next_url = current_url.split('relevance/')[0] + 'relevance/' + str(i)
        driver.get(next_url)
        sleep(10)
    # 定义一个初始值
    temp_height = 0
    while True:
        # 循环将滚动条下拉
        driver.execute_script("window.scrollBy(0,600)")
        # sleep一下让滚动条反应一下
        sleep(0.5)
        # 获取当前滚动条距离顶部的距离
        check_height = driver.execute_script(
            "return document.documentElement.scrollTop || window.pageYOffset || document.body.scrollTop;")
        # 如果两者相等说明到底了
        if check_height == temp_height:
            break
        temp_height = check_height
    sleep(1)
    content = driver.page_source
    regex = r"<!----><a cdxanalyticsevent=.*? href=\"(.*?)\".*?<!"
    url = re.findall(regex, content)
    for j in url:
        s = j.replace('amp;', '').replace('href="', '').replace('"', '')
        Journal_title = s.split('=')[-1].replace('\n', '')
        if(len(Journal_title) == len(s)):
            continue
        if (Journal_title in Periodical_list.keys()):
            Periodical_list[Journal_title] += 1
            Periodical_url_list[Journal_title].append(str(s))
        else:
            Periodical_list[Journal_title] = 1
            Periodical_url_list[Journal_title] = [str(s)]


# 网页路径存放地址
Url_path = r"D:\PycharmProjects\Extract_table\Url_lists"
for i in Periodical_url_list.keys():
    full_path = os.path.join(Url_path,str(len(Periodical_url_list[i]))+"-"+str(i)+".txt")
    file = open(full_path, 'w')
    for j in Periodical_url_list[i]:
        file.write(str(j)+'\n')
    file.close()




a = sorted(Periodical_list.items(), key=lambda x: x[1], reverse=True)
print(a)

# 退出模拟浏览器
driver.quit()
