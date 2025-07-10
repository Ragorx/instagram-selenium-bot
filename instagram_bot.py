import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv

class InstagramBot:
    def __init__(self, username, password):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("prefs", {"intl.accept_languages": "en,en_US"})
        self.browser = webdriver.Chrome(options=options)
        self.username = username
        self.password = password

    def sign_in(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)
        username_input = self.browser.find_element(By.NAME, "username")
        password_input = self.browser.find_element(By.NAME, "password")
        username_input.send_keys(self.username)
        password_input.send_keys(self.password)
        password_input.send_keys(Keys.ENTER)
        time.sleep(5)

    def get_followers(self, target_username, max_followers=15):
        self.browser.get(f"https://www.instagram.com/{target_username}/followers/")
        time.sleep(3)
        dialog = self.browser.find_element(By.CSS_SELECTOR, "div[role='dialog'] ul")
        followers_loaded = len(dialog.find_elements(By.CSS_SELECTOR, "li"))
        print(f"Initial followers loaded: {followers_loaded}")
        action = webdriver.ActionChains(self.browser)

        while followers_loaded < max_followers:
            dialog.click()
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(2)
            new_count = len(dialog.find_elements(By.CSS_SELECTOR, "li"))
            if new_count == followers_loaded:
                break
            followers_loaded = new_count

        followers = dialog.find_elements(By.CSS_SELECTOR, "li")[:max_followers]
        follower_links = [
            user.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
            for user in followers
        ]

        with open("followers.txt", "w", encoding="utf-8") as file:
            for link in follower_links:
                file.write(link + "\n")

        print(f"{len(follower_links)} followers successfully saved.")

    def close(self):
        self.browser.quit()

if __name__ == "__main__":
    load_dotenv()
    username = os.getenv("INSTAGRAM_USERNAME")
    password = os.getenv("INSTAGRAM_PASSWORD")
    bot = InstagramBot(username, password)
    bot.sign_in()
    bot.get_followers("target_username_here", max_followers=15)
    input("Press Enter to exit...")
    bot.close()
