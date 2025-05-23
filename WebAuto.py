from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time, random
from selenium import webdriver
from bs4 import BeautifulSoup
import capsolver
import os, string
import base64
from path import Path
from selenium.webdriver.common.by import By
import requests
import socket
from selenium.webdriver.firefox.options import Options



import threading

def type_field(field, text):
    for letter in text:
        time.sleep(random.uniform(0.1,0.1))
        field.send_keys(letter)


def generate_account():



    # Init Driver

    ffOptions = Options()
    ffOptions.add_argument("-profile")
    ffOptions.add_argument(r'C:\Users\Yordan\AppData\Local\Mozilla\Firefox\Profiles\7')

    # Uncomment the following lines if you want to use Chrome instead of Firefox
    # exectubale_path = "path_to_chromedriver"
    # os.environ["webdriver.chrome.driver"] = exectubale_path
    # driver = webdriver.Chrome(executable_path=exectubale_path, options=ffOptions)

    driver = webdriver.Firefox(options=ffOptions)
    driver.get("https://www.kickz.com/de")
    time.sleep(4)




    # Fill out fields
    mail_field = driver.find_element(By.XPATH,'/html/body/onereg-app/div/onereg-form/div/div/form/section/section[1]/onereg-alias/fieldset/onereg-progress-meter/div[2]/div[2]/div/pos-input[1]/input')


    all_names = open('names.txt',encoding='utf-8').read().splitlines()
    name = random.choice(all_names)
    first_name = name.split()[0]
    last_name = name.split()[1]

    mail = first_name.lower().replace('ä', 'ae').replace('ü', 'ue').replace('ö', 'oe') + '.' + last_name.lower().replace('ä', 'ae').replace('ü', 'ue').replace('ö', 'oe') + ''.join(random.choice(string.digits) for _ in range(5))
    type_field(mail_field, mail)
    print('Mail: ' + mail)


    first_name_field = driver.find_element(By.XPATH,'/html/body/onereg-app/div/onereg-form/div/div/form/section/section[3]/onereg-progress-meter/onereg-personal-info/fieldset/onereg-form-row[1]/div/div[2]/pos-input/input')
    type_field(first_name_field, first_name)

    # string ist immer in source

    if 'technischer Fehler ist' in driver.page_source:
        return False

    last_name_field = driver.find_element(By.XPATH,'/html/body/onereg-app/div/onereg-form/div/div/form/section/section[3]/onereg-progress-meter/onereg-personal-info/fieldset/onereg-form-row[2]/div/div[2]/pos-input/input')
    type_field(last_name_field, last_name)

    postcode_field = driver.find_element(By.XPATH,'/html/body/onereg-app/div/onereg-form/div/div/form/section/section[3]/onereg-progress-meter/onereg-personal-info/fieldset/fieldset/div/div/div[1]/onereg-form-row/div/div/pos-input/input')
    postcode = open('postcode.txt').read().splitlines()
    postcode = random.choice(postcode)
    type_field(postcode_field, postcode)

    location_field = driver.find_element(By.XPATH,'/html/body/onereg-app/div/onereg-form/div/div/form/section/section[3]/onereg-progress-meter/onereg-personal-info/fieldset/fieldset/div/div/div[2]/onereg-form-row/div/div[2]/pos-input/input')
    location = open('locations.txt',encoding='utf-8').read().splitlines()
    location = random.choice(location)
    type_field(location_field, location)

    time.sleep(0.5)

    genders_field = driver.find_element(By.XPATH,'/html/body/onereg-app/div/onereg-form/div/div/form/section/section[3]/onereg-progress-meter/onereg-personal-info/fieldset/div/div/onereg-radio-wrapper[2]/pos-input-radio/label/i/span')
    genders_field.click()

    address_field = driver.find_element(By.XPATH,'/html/body/onereg-app/div/onereg-form/div/div/form/section/section[3]/onereg-progress-meter/onereg-personal-info/fieldset/fieldset/div/onereg-form-row/div/div[2]/pos-input/input')
    street = open('streets.txt',encoding='utf-8').read().splitlines()
    number = open('numbers.txt').read().splitlines()
    street = random.choice(street)
    number = random.choice(number)
    type_field(address_field, street + ' ')
    type_field(address_field, number)

    birthday_field = driver.find_element(By.XPATH,'/html/body/onereg-app/div/onereg-form/div/div/form/section/section[3]/onereg-progress-meter/onereg-personal-info/fieldset/onereg-form-row[3]/div/div/div/onereg-dob-wrapper/pos-input-dob/pos-input[1]/input')
    birthmonth_field = driver.find_element(By.XPATH,'/html/body/onereg-app/div/onereg-form/div/div/form/section/section[3]/onereg-progress-meter/onereg-personal-info/fieldset/onereg-form-row[3]/div/div/div/onereg-dob-wrapper/pos-input-dob/pos-input[2]/input')
    birthyear_field = driver.find_element(By.XPATH,'/html/body/onereg-app/div/onereg-form/div/div/form/section/section[3]/onereg-progress-meter/onereg-personal-info/fieldset/onereg-form-row[3]/div/div/div/onereg-dob-wrapper/pos-input-dob/pos-input[3]/input')

    type_field(birthday_field, str(random.randint(1,28)))
    type_field(birthmonth_field, str(random.randint(1,12)))
    type_field(birthyear_field, str(random.randint(1990, 2004)))

    password_field = driver.find_element(By.XPATH,'/html/body/onereg-app/div/onereg-form/div/div/form/section/section[4]/onereg-password/fieldset/onereg-progress-meter/onereg-form-row[1]/div/div/pos-input/input')
    password_2_field = driver.find_element(By.XPATH,'/html/body/onereg-app/div/onereg-form/div/div/form/section/section[4]/onereg-password/fieldset/onereg-progress-meter/onereg-form-row[2]/div/div/pos-input/input')
    pw = ''.join(random.choice(string.ascii_letters) for _ in range(10))
    type_field(password_field, pw)
    type_field(password_2_field, pw)
    print('Password: ' + pw)

    phonenumber_field = driver.find_element(By.XPATH,'/html/body/onereg-app/div/onereg-form/div/div/form/section/section[5]/onereg-password-recovery/fieldset/onereg-progress-meter/onereg-form-row[1]/div/div/div/pos-input[2]/input')
    all_numbers = open('phonenumber.txt').read().splitlines()
    phonenumber = random.choice(all_numbers)
    type_field(phonenumber_field, phonenumber)





    # Solve CAPTCHA
    img = driver.find_element(By.XPATH, '//*[@id="captchaImage"]')
    full = img.get_attribute('src')
    captcha_base64 = full.split(',')[1].replace(' ', '')
    capsolver.api_key = 'CAP-E9C1E990C372131C4C99FE7719B89960'
    solution = capsolver.solve(
        {
            "type":"ImageToTextTask",
            "module":"web-de-register",
            "body" : captcha_base64
        }
    )
    captcha_text = solution['text']
    type_field(driver.find_element(By.XPATH, '//*[@id="captcha"]'), captcha_text)


    time.sleep(7)

    # Click Confirm
    driver.find_element(By.XPATH,'/html/body/onereg-app/div/onereg-form/div/div/form/section/section[6]/onereg-terms-and-conditions/onereg-progress-meter/fieldset/div[3]/div/button').click()
    time.sleep(1)
    driver.find_element(By.XPATH,'/html/body/onereg-app/div/onereg-form/div/div/form/section/section[6]/onereg-terms-and-conditions/onereg-progress-meter/fieldset/div[3]/div/button').click()

    with open('working_accounts.csv', 'a') as f:
        f.write(mail+'@web.de,'+pw + '\n')
        
    time.sleep(2)
    #Welcome/Site


    time.sleep(3)

    driver.find_element(By.XPATH, '//*[@id="continueButton"]').click()

    time.sleep(3)

    driver.refresh()

    time.sleep(5)


    try:

        driver.switch_to.frame('thirdPartyFrame_permission_dialog')
        driver.switch_to.frame('permission-iframe')
        driver.find_element(By.XPATH, '//*[@id="save-all-pur"]').click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, '//*[@id="close-layer"]').click()

    except:
        print('Gab kein Popup')

    # Go To Settings
    time.sleep(2)
    driver.switch_to.default_content()
    time.sleep(2)
    driver.switch_to.frame('thirdPartyFrame_home')
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div[1]/ul/li[31]/a').click()
    driver.switch_to.default_content()
    time.sleep(2)
    driver.switch_to.frame('thirdPartyFrame_mail')
    time.sleep(2)
    driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div[2]/div/div/div[1]/div/div/div/ul/li[1]/div[2]/ul/li[3]/a').click()
    time.sleep(2)

    # Setup Forward
    driver.switch_to.default_content()
    driver.switch_to.frame('thirdPartyFrame_mail')
    driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div[2]/div/div/div[2]/form/div[2]/div/div/div/fieldset/ul[1]/li[1]/div/span/span/label').click()
    time.sleep(1)
    mail_field = driver.find_element(By.XPATH, '/html/body/div[3]/div[3]/div[2]/div/div/div[2]/form/div[2]/div/div/div/fieldset/ul[2]/li[2]/div/span/input')

    type_field(mail_field, 'cronicshoes@gmail.com')
    driver.find_element(By.XPATH,'/html/body/div[3]/div[3]/div[2]/div/div/div[2]/form/div[2]/div/div/div/div[3]/div/button').click()



    print('Account successfully generated.')

    driver.quit()













