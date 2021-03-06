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
import json

# Python default import.
from time import sleep
from glob import glob
import os

METADATA = []

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

def upload_image_rarible(image_data):
    # Go to the page to upload the nft on etherum
    driver.get("https://rarible.com/create/erc-721")
    try:
        # get the input tag for upload a image file
        choose_file_btn = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[1]/div[2]/div/input')))
        image_path = get_image_path(image_data)
    
       
        choose_file_btn.send_keys(image_path) # Send the image file to rarible

        timed_auction_option_btn = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[3]/div/div/button[3]')
        timed_auction_option_btn.click()

        price = get_price(image_data)
        minimun_bid_input = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#root > div:nth-child(2) > div.sc-bdvvtL.sc-crHmcD.sc-egiyK.sc-cCcXHH.ebRXgR.clWcnz.dbbKCr > div.sc-bdvvtL.sc-crHmcD.sc-egiyK.sc-eXlEPa.ebRXgR.clWcnz.iXKoRS > div.sc-bdvvtL.sc-crHmcD.sc-egiyK.sc-fbyfCU.sc-GEbAx.sc-fmciRz.ebRXgR.clWcnz.fNQPTr.cmoGy.kbMOKW > div > div > div > div.sc-bdvvtL.sc-crHmcD.sc-egiyK.fSHCvX.clWcnz > div:nth-child(4) > div > div.sc-bdvvtL.sc-crHmcD.sc-egiyK.sc-gIBqdA.eWvLRx.clWcnz.YWhZx > div.sc-bdvvtL.sc-crHmcD.sc-egiyK.iuoVZP.clWcnz > input')))
        minimun_bid_input.send_keys(price)
        seven_days_opt = None
        
        try:
            expiration_date_btn_selector = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[5]/div/div/div[2]/div/div[2]/div[1]/input')))
            expiration_date_btn_selector.click()
            # expiration_date_btn_selector.send_keys('7 days')
            # expiration_date_btn_selector.send_keys(Keys.RETURN)
            
            days_list_options = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="tippy-11"]/div/div/div/div/div[1]/div/div')))
            if days_list_options:
                print("Encontro la lista")
            days_options_btns = days_list_options.find_elements(By.TAG_NAME, 'button')

            for day_opt in days_options_btns:
                divs = day_opt.find_elements(By.TAG_NAME, 'div')
                for div in divs:
                    
                    print("the text is: ", div.text)
                    if div.text == "7 days":
                        seven_days_opt = day_opt
                        seven_days_opt.click() 
                    
        except Exception as e:
            print("Error to find the days list element:\nTrying again...\n ", e)
                # upload_image_rarible()


        

        image_name, image_description = get_name_and_description_image(image_data)
        name_inp = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[9]/div/div[2]/div/input')
        description_inp = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[10]/div/div[2]/div/textarea')
        name_inp.send_keys(image_name)
        description_inp.send_keys(image_description)

        # Click on 'show advance options'
        show_adv_opt_btn = driver.find_element(By.XPATH, '//*[@id="root"]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[12]/button')
        show_adv_opt_btn.click()

        image_properties = get_image_properties(image_data)

        # Fill properties options (property and value)
        for index, key in enumerate(image_properties):
            new_index = index * 2
            prop_inp = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, f'//*[@id="root"]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[12]/div/div[1]/div[2]/div[{new_index+1}]/div/input')))
            value_inp = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, f'//*[@id="root"]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[12]/div/div[1]/div[2]/div[{new_index+2}]/div/input')))
            prop_inp.send_keys(key)
            value_inp.send_keys(image_properties[key])
        
        # Click to finish btn
        create_item_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'//*[@id="root"]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[13]/div/div/button')))
        create_item_btn.click()
        
        # Change to metamask extension pop up window
        sign_in_btn = '//*[@id="app-content"]/div/div[3]/div/div[4]/button[2]'
        sign_btn = '//*[@id="app-content"]/div/div[3]/div/div[3]/button[2]'
        sleep(20) ##wait to open the new window
        
        driver.switch_to.window(driver.window_handles[2]) # change the driver to the new window (metamask extension)
        # Click on "Next" button.
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, sign_in_btn))).click()
        
        sleep(15)
        driver.switch_to.window(driver.window_handles[2])
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, sign_btn))).click()

        print("\n$$$$$ Imagen subida $$$$$\n")
        driver.switch_to.window(driver.window_handles[0]) # Back to our main window
    except Exception as e:
        print(e)

    
    # //*[@id="root"]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[12]/div/div[1]/div[2]/div[1]/div/input
    # //*[@id="root"]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[12]/div/div[1]/div[2]/div[2]/div/input
    # //*[@id="root"]/div[2]/div[2]/div[2]/div[1]/div/div/div/div[1]/div[12]/div/div[1]/div[2]/div[3]/div/input
   

def get_image_path(image_data):
    return image_data["file_path"]

def get_price(image_data):
    return image_data["price"]
    
def get_name_and_description_image(image_obj):
    name = image_obj["nft_name"]
    description = image_obj["description"]
    return name, description

def get_image_properties(image_obj):
    properties = image_obj["properties"]
    properties_to_return = {}
    for property in properties:
        properties_to_return[property["type"]] = property["value"]
    
    return properties_to_return

def get_metadata():

    with open('./metadata/_metadata.json') as json_file:
        data = json.load(json_file)
    
        return data

if __name__ == '__main__':
    options = webdriver.ChromeOptions()  # Configure options for Chrome.
    options.add_extension("assets/MetaMask.crx")  # Add extension.
    # options.add_argument("headless")  # Headless ChromeDriver.
    options.add_argument("log-level=3")  # No logs is printed.
    options.add_argument("--mute-audio")  # Audio is muted.
    driver = webdriver.Chrome("assets/chromedriver.exe",  options=options)
    driver.maximize_window()  # Maximize window to reach all elements.
    
    metadata = get_metadata()
  

    login_metamask()
    sign_in_rarible()

    for image_metadata in metadata["nft"]:
        upload_image_rarible(image_metadata)
        
        sleep(10)
    


    input("type and enter to close")
    driver.close()