from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import pickle

def save_cookies(driver, location):
    with open(location, 'wb') as filehandler:
        pickle.dump(driver.get_cookies(), filehandler)

def load_cookies(driver, location, url=None):
    cookies = pickle.load(open(location, 'rb'))
    driver.delete_all_cookies()
    for cookie in cookies:
        driver.add_cookie(cookie)
    if url:
        driver.get(url)

def check_chromedriver():
    try:
        chrome_options = Options()
        chrome_options.add_argument("--incognito")  # 启用无痕模式
        chrome_options.add_argument("--headless")  # 无头模式
        chrome_options.add_argument("--disable-blink-features=AutomationControlled")
        chrome_options.add_experimental_option('useAutomationExtension', False)
        chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])

        service = Service('/Users/Meraki/Downloads/chromedriver-mac-arm64/chromedriver')  
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.get("https://www.google.com")
        time.sleep(3)

        # 尝试加载保存的cookies
        try:
            load_cookies(driver, "cookies.pkl", "https://www.google.com")
            driver.get("https://www.google.com")
            time.sleep(3)
        except Exception as e:
            print("Failed to load cookies:", e)

        # 如果没有成功加载cookies，进行手动登录
        if "klklhong48967@gmail.com" not in driver.page_source:
            driver.get("https://accounts.google.com/ServiceLogin")
            email_input = driver.find_element(By.ID, "identifierId")
            email_input.send_keys("klklhong48967@gmail.com")  # 替换为你的Google邮箱
            driver.find_element(By.ID, "identifierNext").click()
            time.sleep(10)  # 增加等待时间

            password_input = driver.find_element(By.NAME, "password")
            password_input.send_keys("19198028246")  # 替换为你的Google密码
            driver.find_element(By.ID, "passwordNext").click()
            time.sleep(20)  # 增加等待时间

            save_cookies(driver, "cookies.pkl")

        # 检查页面是否加载成功
        driver.get("https://woy.ai/manage/p/diffsynth-studio/en/faq")
        body = driver.find_element(By.TAG_NAME, "body")
        if body:
            print("Page loaded successfully!")
        else:
            print("Failed to load the page.")

        input("Press Enter to close the browser...")
        driver.quit()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    check_chromedriver()
