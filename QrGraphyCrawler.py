from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import json

def read_string_from_json(file_path, index):
    """
    Reads a string from a JSON file at a specific index.

    :param file_path: Path to the JSON file.
    :param index: Index of the string to read.
    :return: The string at the specified index, or None if the index is out of range.
    """
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)  # Load the JSON data

        # Check if the index is within the range of the list
        if 0 <= index < len(data):
            return data[index]
        else:
            print("Index out of range.")
            return None

    except FileNotFoundError:
        print("The specified file was not found.")
        return None
    except json.JSONDecodeError:
        print("Error decoding JSON.")
        return None
    
url = 'https://userpanel.qrgraphy.com/ords/r/shadris/qrgraphy/login'
links_file = 'E:/PROJECTS/crwaler/instagram_links.json'
username = '09939244826'
password = 'Ka1311535884'


driver = webdriver.Chrome()

driver.get(url)

time.sleep(2)
login_with_user_pass_button = driver.find_element(By.ID, 'B171028706455266114')  # Replace with the actual button ID
login_with_user_pass_button.click()

username_field = driver.find_element(By.ID, 'P9999_FIX_USER_NAME')  
password_field = driver.find_element(By.NAME, 'P9999_FIX_PASSWORD')  

username_field.send_keys(username)
password_field.send_keys(password)
user_answer = input("Please enter your answer: ")
answer_field = driver.find_element(By.ID, 'P9999_CAPTCHA')  
answer_field.send_keys(user_answer)

login_button = driver.find_element(By.ID, 'B171027881550266105')  
login_button.click()
time.sleep(5) ### login process
i = 6
while(i < 10):
    make_qr_button = driver.find_element(By.ID, 't_TreeNav_2')  
    make_qr_button.click()
    time.sleep(5)
    link_qr_button = driver.find_element(By.ID, 'linkqr_region')  
    link_qr_button.click()
    time.sleep(5)
    link_field = driver.find_element(By.NAME, 'P6_URL')  
    link = read_string_from_json(links_file, i)
    link_field.send_keys(link)
    send_link_button = driver.find_element(By.ID, 'B236349844614043037')  
    send_link_button.click()
    time.sleep(2)
    qr_name_field = driver.find_element(By.ID, 'P7_NAME')  
    name = f"Qallery {i}"
    qr_name_field.send_keys(name)
    create_qr_button = driver.find_element(By.ID, 'B187817548252270229')  
    time.sleep(3)

    create_qr_button.click()
    time.sleep(30)
    # print(driver.page_source)
    # with open('page_source.html', 'w', encoding='utf-8') as f:
    #     f.write(driver.page_source)
    edit_button = driver.find_element(By.ID, 'B236576145074645864')  
    edit_button.click()
    time.sleep(2)
    choose_type_button = driver.find_element(By.ID, 'R239647476780061583')  
    choose_type_button.click()
    time.sleep(10)
    choose_design_button = driver.find_element(By.ID, 'design_4763')  
    choose_design_button.click()
   
    time.sleep(10)
    save_edition_button = driver.find_element(By.ID, 'B190263639662011628')  
    choose_design_button.click()
    time.sleep(20)
    download_png_button = driver.find_element(By.ID, 'pngimage')  
    download_png_button.click()
    # download_png_button = WebDriverWait(driver, 10).until(
    # EC.presence_of_element_located((By.ID, 'pngimage'))
    # )
    time.sleep(5)
    i += 1




 