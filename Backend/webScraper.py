import csv
import requests 
from bs4 import BeautifulSoup as bs
import selenium.webdriver as webdriver




# url = 'http://instagram.com/umnpics/'
# driver = webdriver.Chrome()
# driver.get(url)

# soup = bs(driver.page_source, 'html.parser')

# # x = soup.find('div', {'id':'mount_0_0_4R'})
# # print(x)
def scrapeFull(url):
    page = requests.get(url) 
    urlinput= input("Name html file:\n")
    html_file = open(urlinput, "w", encoding = "utf-8")
    # driver = webdriver.Chrome()
    # driver.get(url)

    html_file.write(page.text) # write html_text from website to file 
    html_file.close()
    return urlinput
def urlExtract():
    u= input("Give me instagram url:\n")
    fullData = scrapeFull(u)
    with open(fullData, encoding="utf8") as htmltext:
        
        soup = bs(htmltext, 'html.parser')

# #         img_div = soup.findAll("div", {"class": "_aagu"})
# #         print(img_div)
#     # for i in img_div:
#     #     img_url = i.find("img", attrs="src")

#     # with open('petrs.csv', 'w') as csvfile:
#     #     writer = csv.writer(csvfile)
#     #     writer.writerow(ilist)
    
urlExtract()
