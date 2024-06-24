from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def check_chromedriver():
    try:
        chrome_options = Options()
        service = Service('/Users/Meraki/Downloads/chromedriver-mac-arm64/chromedriver')  

        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.get("https://woy.ai/manage/p/diffsynth-studio/en/faq")

        # 检查页面标题是否包含 "Google"
        if "Google" in driver.title:
            print("ChromeDriver is working!")
        else:
            print("ChromeDriver is not working correctly.")

        driver.quit()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    check_chromedriver()
