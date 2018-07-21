from selenium import webdriver
from time import sleep
k=2
driver = webdriver.Firefox()
for j in range(1,55):
    url = 'http://dailycrossstitch.com/product-category/animals-creatures/page/' + str(j) + '/'
    driver.get(url)
    sleep(4)
    for i in range(1,17):
        elem = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div/div[2]/main/ul/li['+str(i)+']/a[2]')
        inner = elem.get_attribute('innerHTML')
        if inner == "Add to cart":
            elem.click()
            sleep(k)
        if inner == "FREE":
            sleep(k)
            pass
        if inner == "Read more":
            sleep(k)
            pass

##_____________________________________________________________________________
##elements
##/html/body/div[1]/div[3]/div/div[2]/main/ul/li[1]/a[2]
##/html/body/div[1]/div[3]/div/div[2]/main/ul/li[2]/a[2]
##/html/body/div[1]/div[3]/div/div[2]/main/ul/li[3]/a[2]
##/html/body/div[1]/div[3]/div/div[2]/main/ul/li[4]/a[2]
##/html/body/div[1]/div[3]/div/div[2]/main/ul/li[5]/a[2]
##/html/body/div[1]/div[3]/div/div[2]/main/ul/li[13]/a[2]
