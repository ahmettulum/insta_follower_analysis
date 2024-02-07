from selenium import webdriver
import time
from selenium.webdriver.common.by import By

browser=webdriver.Chrome()

url = "https://www.instagram.com/"

browser.get(url)

time.sleep(2)

user=browser.find_element(By.XPATH,"""//*[@id="loginForm"]/div/div[1]/div/label/input""")
user.send_keys("ahmet.tlm")
time.sleep(1)
psw=browser.find_element(By.XPATH,"""//*[@id="loginForm"]/div/div[2]/div/label""")
psw.send_keys("25453802582ahmet")
time.sleep(1)
login=browser.find_element(By.XPATH,"""//*[@id="loginForm"]/div/div[3]""").click()
time.sleep(10)
not_now=browser.find_element(By.CLASS_NAME,"_ac8f").click()
time.sleep(5)

not_now1=browser.find_element(By.XPATH,"/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]").click()
time.sleep(3)
search_button=browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[2]/span/div/a/div/div[1]/div/div").click()
time.sleep(3)

find_user=browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div/input")
find_user.send_keys("habibeelma")
time.sleep(7)
found_user=browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[3]/div/a[1]/div[1]/div/div").click()
time.sleep(5)
followers=browser.find_element(By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[3]/a").click()
time.sleep(3)
jscommand="""
followers=document.querySelector("._aano");
followers.scrollTo(0,followers.scrollHeight);
var lenOfPage=followers.scrollHeight;
return lenOfPage;
"""
lenOfPage = browser.execute_script(jscommand)
match=False
while (match==False):
    lastCount = lenOfPage
    time.sleep(3)
    lenOfPage = browser.execute_script(jscommand)
    if lastCount == lenOfPage:
        match=True

elements = browser.find_elements(By.CSS_SELECTOR,"._aad7")
followings=[]
for element in elements:
    followings.append(element.text)

print(len(followings))
with open("followings.txt", "w", encoding="utf-8") as file1:
    for i in followings:
        file1.write(i+"\n")

browser.close()