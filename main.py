#importing modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.common.exceptions import ElementClickInterceptedException

#Constants
DRIVER_PATH ="C:\Development\chromedriver.exe"
DRIVER_SERVICE = Service(executable_path=DRIVER_PATH)
USER_NAME ="HIRUKA_MUN"
PASSWORD ="Hiruka123@@"
SIMILAR_ACCOUNT ="chefsteps"

#Creating a class
class InstaFollower:
    def __init__(self,driver_service,driver_path):
        self.driver_service = Service(executable_path=driver_path)
        self.driver = webdriver.Chrome(service=driver_service)

#Login
    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)
        user_name = self.driver.find_element(By.NAME,'username')
        user_name.send_keys(USER_NAME)
        user_name.send_keys(Keys.ENTER)
        time.sleep(2)

        password = self.driver.find_element(By.NAME,'password')
        password.send_keys(PASSWORD)
        time.sleep(2)
        password.send_keys(Keys.ENTER)

#find followers
    def find_followers(self):
        time.sleep(3)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")
        follower = self.driver.find_element(By.CSS_SELECTOR,'.wW3k- button')
        follower.click()
        user_name = self.driver.find_element(By.NAME,'username')
        user_name.send_keys(USER_NAME)
        user_name.send_keys(Keys.ENTER)
        time.sleep(2)
        password = self.driver.find_element(By.NAME,'password')
        password.send_keys(PASSWORD)
        time.sleep(2)
        password.send_keys(Keys.ENTER)
        time.sleep(2)

        modal = self.driver.find_element(By.XPATH,'/html/body/div[4]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)

#follow
    def follow(self):
        all_buttons = self.driver.find_element(By.CSS_SELECTOR,'li button')
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH,'/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()


bot = InstaFollower(DRIVER_SERVICE,DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()

