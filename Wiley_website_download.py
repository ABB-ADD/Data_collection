# def Wiley_download():
import random
from time import sleep
from selenium import webdriver
import os

from selenium.webdriver.common.by import By

Edge_options = webdriver.EdgeOptions()
save_directory = r'D:\PycharmProjects\Extract_table\Wiley_website'

prefs = {'profile.default_content_settings.popups': 0,
         'download.default_directory': save_directory}  # 设置下载文件存放路径，这里要写绝对路径
Edge_options.add_experimental_option('prefs', prefs)
Edge_options.add_argument(r'--user-data-dir=C:\Users\Administrator\AppData\Local\Microsoft\Edge\User Data')
Edge_options.add_experimental_option("excludeSwitches", ["enable-automation"])
Edge_options.add_experimental_option('useAutomationExtension', False)
Edge_options.add_argument("--disable-blink-features=AutomationControlled")

driver = webdriver.Edge(options=Edge_options)
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
    Object.defineProperty(navigator, 'webdriver', {
    get: () => undefined
    })
    """
})

url_lists = open(r'Wiley_Url_lists.txt', 'r')
url_lists = url_lists.readlines()
Failure_num = 0
Failure_url = []


def every_downloads_chrome(save_directory):
    datanames = os.listdir(save_directory)
    for dataname in datanames:
        if os.path.splitext(dataname)[1] == '.crdownload':  # 目录下包含.crdownload的文件
            return False
    return True


# 记录爬取文献数量，设置爬取多少篇后暂停然后重新爬取
j = 0
# for i in url_lists[0:]:

for i in url_lists[len(os.listdir(save_directory)):]:
    try:
        if (j % 30 == 0) and j != 0:
            driver.quit()
            sleep(3)
            driver = webdriver.Edge(options=Edge_options)
            driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
                "source": """
                Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
                })
                """
            })
        url = i.replace("'", '').replace("/n",'')
#         driver.get(url)
        sleep(3)
#         print(url)
#         url_before = driver.current_url
        url_download = url.split('doi/')[0] + 'doi/' + 'pdfdirect/' + url.split('doi/')[1] + '?download=true'
        print(url_download)
        driver.get(url_download)
        while (1):
            sleep(1)
            if every_downloads_chrome(save_directory):
                break

        # Text =driver.find_element(By.XPATH, '// *[ @ id = "challenge-running"]').text
        print(len(os.listdir(save_directory)))
        print('%' * 30)

        # // *[ @ id = "challenge-running"]
        j += 1
        sleep(random.randint(3, 15))
    except Exception as e:
        print('\033[1;31m*****************************\033[0m')
        print(e)
        print('\033[1;31m*****************************\033[0m')
        Failure_num += 1
        Failure_url.append(url)
        continue

print('\033[1;31m##################################\033[0m')
print("下载完成，失败" + str(Failure_num) + "次")
if (Failure_num != 0):
    for i in Failure_url:
        print(i)
