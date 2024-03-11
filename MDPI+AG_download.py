from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

Edge_options = webdriver.EdgeOptions()
# Edge_options.add_experimental_option("debuggerAddress","127.0.0.1:9527")
# prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': r'D:\EdgeDownload'}
prefs = {'profile.default_content_settings.popups': 0, 'download.default_directory': r'D:\PycharmProjects\Extract_table\Literature_Download'}  # 设置下载文件存放路径，这里要写绝对路径
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

url = 'https://www.webofscience.com/api/gateway?GWVersion=2&SrcAuth=DynamicDOIArticle&SrcApp=WOS&KeyAID=10.3390%2Fcryst12020168&DestApp=DOI&SrcAppSID=USW2EC0AFABxF4JQW3R4yUT4EnU3M&SrcJTitle=CRYSTALS&DestDOIRegistrantName=MDPI+AG'
driver.get(url)
sleep(3)
driver.find_element(By.LINK_TEXT,"Download").click()
sleep(1)
driver.find_element(By.LINK_TEXT,"Download PDF").click()
sleep(3)
url = 'https://www.webofscience.com/api/gateway?GWVersion=2&SrcAuth=DynamicDOIArticle&SrcApp=WOS&KeyAID=10.3390%2Fpolym13152398&DestApp=DOI&SrcAppSID=USW2EC0AFABxF4JQW3R4yUT4EnU3M&SrcJTitle=POLYMERS&DestDOIRegistrantName=MDPI+AG'
driver.get(url)
sleep(3)
driver.find_element(By.LINK_TEXT,"Download").click()
sleep(1)
driver.find_element(By.LINK_TEXT,"Download PDF").click()
# driver.find_element(By.ID,'mat-input-0').clear()
# //*[@id="drop-download-732487"]/a[1]
# # 查找元素
sleep(30)

content = driver.page_source

print(driver.title)
print(content)
