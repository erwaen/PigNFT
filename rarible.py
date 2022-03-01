# Selenium module imports: pip install selenium
from ast import Pass
from selenium import webdriver
from selenium.common.exceptions import TimeoutException as TE
from selenium.common.exceptions import ElementClickInterceptedException as ECIE
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Python default import.
from time import sleep
from glob import glob
import os

def login_metamask():
    print('Login to MetaMask extension.', end=' ')
    driver.switch_to.window(driver.window_handles[0])
    while True:
        # If page is fully loaded.
        if 'initialize' in driver.current_url:
            break
        driver.refresh()  # Reload page.
        sleep(1)  # Wait 1 second.

    try:
        start_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app-content"]/div/div[3]/div/div/div/button')))
        start_btn.click()
       
        import_wallet_btn = start_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app-content"]/div/div[3]/div/div/div[2]/div/div[2]/div[1]/button')))
        import_wallet_btn.click()

        i_agree_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app-content"]/div/div[3]/div/div/div/div[5]/div[1]/footer/button[2]')))
        i_agree_btn.click()

        sleep(2)

        recovery_phrase_input = driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[3]/div/div/form/div[4]/div[1]/div/input')
        new_password_input = driver.find_element(By.ID, 'password')
        confirm_password_input = driver.find_element(By.ID, 'confirm-password')
        agree_terms_checkbox = driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[3]/div/div/form/div[7]/div')
        submit_btn = driver.find_element(By.XPATH, '//*[@id="app-content"]/div/div[3]/div/div/form/button')

        recovery_phrase, password = get_metamask_credentials()
        
        recovery_phrase_input.send_keys(recovery_phrase)
        new_password_input.send_keys(password)
        confirm_password_input.send_keys(password)
        agree_terms_checkbox.click()
        submit_btn.click()

        # next page

        all_done_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app-content"]/div/div[3]/div/div/button')))
        all_done_btn.click()

        sleep(2)
    except Exception as e:
        print(e)

def sign_in_rarible():
    driver.get("https://rarible.com/")
    try:
        sign_in_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'sign-in')))
        sign_in_btn.click()
        
        sign_in_with_metamask_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="root"]/div[2]/div[2]/div/div[2]/div/div/div[2]/div[2]/div[1]/button/span')))
        sign_in_with_metamask_btn.click()

        # Now this open a  little new window of metamask extensiond
      
        sleep(3) ##wait to open the new window
        
        driver.switch_to.window(driver.window_handles[2]) # change the driver to the new window (metamask extension)
        # Click on "Next" button.
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app-content"]/div/div[3]/div/div[2]/div[4]/div[2]/button[2]'))).click()
        # Click on "Connect" button.
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app-content"]/div/div[3]/div/div[2]/div[2]/div[2]/footer/button[2]'))).click()

        print("\n$$$$$ LOGGED TO RARIBLE $$$$$\n")
        driver.switch_to.window(driver.window_handles[0]) # Back to our main window
    
        
    except Exception as e:
        print(e)

def get_metamask_credentials():
    f = open('assets/password.txt', 'r')
    password = f.read()
    f.close()
    f = open('assets/recovery_phrase.txt', 'r')
    recovery_phrase = f.read()
    f.close()
    return recovery_phrase, password

def upload_image_rarible():
    # Go to the page to upload the nft on etherum
    driver.get("https://rarible.com/create/erc-721")
    try:
        choose_file_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[1]/div[2]/div/input')))
        image_path = get_image_path()
        print(os.getcwd())
        choose_file_btn.send_keys(image_path)
    except Exception as e:
        print(e)
  
   

def get_image_path():
    return 'G:/My Drive/Developer/nft/PigNFT/result/0.png'
    


if __name__ == '__main__':
    options = webdriver.ChromeOptions()  # Configure options for Chrome.
    options.add_extension("assets/MetaMask.crx")  # Add extension.
    # options.add_argument("headless")  # Headless ChromeDriver.
    options.add_argument("log-level=3")  # No logs is printed.
    options.add_argument("--mute-audio")  # Audio is muted.
    driver = webdriver.Chrome("assets/chromedriver.exe",  options=options)
    driver.maximize_window()  # Maximize window to reach all elements.

    login_metamask()
    sign_in_rarible()
    upload_image_rarible()
    


    input("type and enter to close")
    driver.close()