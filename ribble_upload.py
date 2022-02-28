from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

s=Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=s)
options.add_extension('assets/MetaMask.crx')


driver.get("https://chrome.google.com/webstore/detail/phantom/bfnaelmomeimhlpmgjnjophhpkkoljpa")
sleep(2)
driver.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/div/div[2]/div[2]/div").click()
input("type and enter to close")

driver.get("https://solanart.io/")


input("type and enter to close")
driver.close()