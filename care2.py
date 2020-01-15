
from time import sleep
import os
import datetime 
from PIL import Image
import pytesseract
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


user=''            ##Please input your jaccount user 
password=''         ##Please input your jaccount password



def login(model):
    input_user = driver.find_element_by_id('user').send_keys(user)
    input_pass = driver.find_element_by_id('pass').send_keys(password)
    uuid = driver.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div[2]/div[2]/form/div[3]/div/img')
    driver.save_screenshot('E:\\vscode work\\PYTHON\\aixinwu\\my.png')  ##the address to store Screenshots
    if model==1:
        rangle=(1450,494,1740,553)     
    else:
        rangle=(1450,540,1740,600)
    i = Image.open('E:\\vscode work\\PYTHON\\aixinwu\\my.png')  
    #i.show()
    i = i.resize((1920,850))
    i = i.crop(rangle)  
    i.save('E:\\vscode work\\PYTHON\\aixinwu\\jacc.png')   ## the address to store captcha pictures
    image = Image.open('E:\\vscode work\\PYTHON\\aixinwu\\jacc.png')
    image=image.convert('L')
    threshold=230
    table=[]
    for i in range(256):
        if i <threshold:
            table.append(0)
        else:
            table.append(1)
    image=image.point(table,'1')
    #image.show()
    result = pytesseract.image_to_string(image,lang='eng')
    input_code = driver.find_element_by_id('captcha')
    result=result.replace(' ','')
    input_code.send_keys(result)
    input_code.send_keys(Keys.ENTER)
    driver.refresh()
    
chrome_options=Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver=webdriver.Chrome(r'E:\vscode work\PYTHON\chromedriver.exe',chrome_options=chrome_options)  ##chromedriver
driver.implicitly_wait(15)
driver.maximize_window()  
driver.get('https://aixinwu.sjtu.edu.cn/index.php/customer/home')
login(model=1)
while driver.current_url!='https://aixinwu.sjtu.edu.cn/index.php/home':
    login(model=2)
driver.get('https://aixinwu.sjtu.edu.cn/index.php/customer/home')
data=driver.find_element_by_xpath('/html/body/div[5]/div[3]/div[1]').text
print("Register Successfully,the current time is",end=" ")
print(datetime.datetime.now())
print(data)