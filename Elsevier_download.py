from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import json

Edge_options = webdriver.EdgeOptions()
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
    'printing.print_preview_sticky_settings.appState': json.dumps(appState),
    'savefile.default_directory': r'D:\PycharmProjects\Extract_table\Elsevier'
}
# prefs = {'profile.default_content_settings.popups': 0, 'savefile.default_directory': r'D:\PycharmProjects\Extract_table\Literature_Download'}  # 设置下载文件存放路径，这里要写绝对路径
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

url_lists = open(r'D:\PycharmProjects\Extract_table\Url_lists\94-Elsevier.txt', 'r')
Failure_num = 0
Failure_url = []
for i in url_lists:
    try:
        url = i.replace("'", '')
        driver.get(url)
        sleep(3)
        driver.find_element(By.XPATH, '//*[@id="mathjax-container"]/div[1]/div/div[2]/ul/li[1]/a').click()
        # # 查找元素
        sleep(10)
        driver.execute_script('window.print();')
        sleep(5)
    except Exception as e:
        print('\033[1;31m*****************************\033[0m')
        print(e)
        print('\033[1;31m*****************************\033[0m')
        Failure_num+=1
        Failure_url.append(url)
        continue

print('\033[1;31m##################################\033[0m')
print("下载完成，失败"+str(Failure_num)+"次")
if(Failure_num != 0):
    for i in Failure_url:
        print(i)




'''
url = 'https://pdf.sciencedirectassets.com/271607/1-s2.0-S0032386122X00189/1-s2.0-S0032386122007558/main.pdf?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAAaCXVzLWVhc3QtMSJGMEQCIAcEG56%2F%2F%2FhXT23in%2BKi95GPGgepChGnwA5yExCFvlfeAiBBX4Ypd1nuSGyM%2FvX20s6jOq8Dk%2FexBfIhiiTt4VwM3SrMBAgpEAUaDDA1OTAwMzU0Njg2NSIMnUHr3EIIvlPLaQpnKqkEc2Lo6WTDL9drWxVbmBaijBul4QypDThup%2BlSAqyhYMlPVSDVq3tcOGFa%2FYZFKanb1LVA8CfUuXpQid7EpsVGpv9RZ7sr0eNgI31C71jJmDNoRNyEAq3Qwvls4lDVxbBTr1%2BAbRtlh6W%2BG%2BHsuVVVrSdMJQnWfxRzoY%2FDalBctvP5FsAc2AjHQ3W1W4X%2FCIrLOQ9n3TMBv%2FGNuB%2FdQFQuzkcpMBQUXxFtpuoK2Sgos9NJ6kQtZ5lB9x8nyiHuUlTmXNGKknXyTJhJcOcdikeVnPWDMAsUXvJi2y2i8xtnv9rXsL4c81IlRiVv%2FPRkRPwo%2BGpbMlFMfSbrJ4wW9lok8srpg9kvoUswvUPVIGQOPUmMEpOt3vygKqvIxb43rpd7hl3X3cNRf9XgFpZv6F%2Bnja5iPGpyB%2FEWkKcCHW2iC5%2FNPO7xmjJr9k%2FMq5rQ3WrhEdH1iVtOlOPmkzzjhosCstX%2B46lPcAfODtGvfObWCpykHX1hRoBt9UJhhDXKR1Gix5BqPqrSg9wc4C9z2aQTG8CZPPWp0SrXfYeWsSs3PxsBj8Ch6cxCg3j2l0sJX0EMK8g6AOZZ117BZIflDisx8PdkiXl1CI2vA6%2BIYsnmYk4gn8c3PeVwQ%2Bu6ddAIxd3zdYVJce1gZKbSZ7YiCsun6DGWLV2%2FTfpCk7cXllnW1FG89N3owZvfIX7jubwCAKWHiPgWhhOu8y0zdpDJPmuANQxkQWQy6QbTRjChhcGcBjqqAU%2FrdHgUc0tFqVZEswmOuvn3L7UR7GXM9d62A4X%2BURZIqirEPwVnKEL0NuFZxZxRczrStdmdRQK6gL2IjNbrhlDf53Pb%2BS%2FqCF4L5EI7nCydwCAe4BQmwGtlCa6n882H0l7CX%2B4tjW6dpe2orrBNksqxPlHI2ZlQEGx85FK8FDlKw0xCIFNsbhiO%2B1CCBWUP9yDZuC%2BKwyxQEGIqNgWDK4NxpLoEHrGNsxoj&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20221207T082658Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIAQ3PHCVTYR6OKBE4C%2F20221207%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=7b67776a2298931caa81616d392e5927253db34dd8807c4f13476260566ee84c&hash=d35655eb7d6ff1055bf0d12176c4d485fd48e6505c76dc06ba5e5e823087d3db&host=68042c943591013ac2b2430a89b270f6af2c76d8dfd086a07176afe7c76c2c61&pii=S0032386122007558&tid=spdf-89c97f48-fe4a-40f3-b5e2-dc623c62f69f&sid=7d03104a282986486558fdf89d2771f4504egxrqa&type=client&ua=4d51540d04565d5501010c&rr=775be122babbcf87'
# url = 'https://www.baidu.com'
driver.get(url)
sleep(3)
driver.find_element(By.XPATH,'//*[@id="mathjax-container"]/div[1]/div/div[2]/ul/li[1]/a').click()
# # 查找元素
sleep(5)
driver.execute_script('window.print();')
sleep(10)


url = 'https://www.webofscience.com/api/gateway?GWVersion=2&SrcAuth=DynamicDOIArticle&SrcApp=WOS&KeyAID=10.1016%2Fj.solener.2021.09.017&DestApp=DOI&SrcAppSID=USW2EC0AFABxF4JQW3R4yUT4EnU3M&SrcJTitle=SOLAR+ENERGY&DestDOIRegistrantName=Elsevier'
driver.get(url)

sleep(3)
driver.find_element(By.XPATH,'//*[@id="mathjax-container"]/div[1]/div/div[2]/ul/li[1]/a').click()
sleep(5)
driver.execute_script('window.print();')
sleep(10)

content = driver.page_source
# f = open('Download.pdf', 'wb')
# f.write(content)
# f.close()
# content.encode("utf8")
print(driver.title)
'''