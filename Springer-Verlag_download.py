import json
import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

Edge_options = webdriver.EdgeOptions()
save_directory=r'D:\PycharmProjects\Extract_table\Literature_Download_1'

appState = {
    "recentDestinations": [
        {
            "id": "Save as PDF",
            "origin": "local"
        }
    ],
    "selectedDestinationId": "Save as PDF",
    "version": 2
}
profile = {
    'savefile.default_directory': save_directory,
    'printing.print_preview_sticky_settings.appState': json.dumps(appState),
    'download.default_directory': save_directory
}

Edge_options.add_experimental_option('prefs', profile)
Edge_options.add_argument(r'--user-data-dir=C:\Users\Administrator\AppData\Local\Microsoft\Edge\User Data')
Edge_options.add_experimental_option("excludeSwitches", ["enable-automation"])
Edge_options.add_experimental_option('useAutomationExtension', False)
Edge_options.add_argument("--disable-blink-features=AutomationControlled")
Edge_options.add_argument('--kiosk-printing')


driver = webdriver.Edge(options=Edge_options)
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": """
    Object.defineProperty(navigator, 'webdriver', {
    get: () => undefined
    })
    """
})

def every_downloads_chrome(save_directory):
    datanames = os.listdir(save_directory)
    for dataname in datanames:
        if os.path.splitext(dataname)[1] == '.crdownload':  # 目录下包含.crdownload的文件
            return False
    return True


url = 'https://www.webofscience.com/api/gateway?GWVersion=2&SrcAuth=DOISource&SrcApp=WOS&KeyAID=10.1007%2Fs00604-022-05489-x&DestApp=DOI&SrcAppSID=USW2EC0AFABxF4JQW3R4yUT4EnU3M&SrcJTitle=MICROCHIMICA+ACTA&DestDOIRegistrantName=Springer-Verlag'
driver.get(url)
sleep(5)
driver.find_element(By.XPATH,'//*[@id="sidebar"]/aside/div[1]/div/div').click()
sleep(2)
while(1):
    sleep(1)
    if every_downloads_chrome(save_directory):
        break


url = 'https://www.webofscience.com/api/gateway?GWVersion=2&SrcAuth=DynamicDOIArticle&SrcApp=WOS&KeyAID=10.1007%2Fs11426-021-9988-6&DestApp=DOI&SrcAppSID=USW2EC0AFABxF4JQW3R4yUT4EnU3M&SrcJTitle=SCIENCE+CHINA-CHEMISTRY&DestDOIRegistrantName=Springer-Verlag'
driver.get(url)
sleep(5)
driver.find_element(By.XPATH,'//*[@id="sidebar"]/aside/div[1]/div/div').click()
sleep(2)
while(1):
    sleep(1)
    if every_downloads_chrome(save_directory):
        break
