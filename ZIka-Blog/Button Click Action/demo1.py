from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import time

# 设置Chrome驱动的路径
chrome_driver_path = '/Users/Meraki/Downloads/chromedriver-mac-arm64/chromedriver'  # 替换为你的chromedriver路径
service = Service(chrome_driver_path)

# 初始化Chrome浏览器
driver = webdriver.Chrome(service=service)

# 打开网页
driver.get("https://woy.ai/manage/p/diffsynth-studio/en/faq")

# 等待页面加载
time.sleep(3)  # 可以根据实际情况调整等待时间

# 定位并点击“生成”按钮
generate_button = driver.find_element(By.CSS_SELECTOR, 'button.mx-auto.flex.justify-center.items-center.rounded-md.bg-amber-500.px-3.py-2.text-lg.font-semibold.text-white.shadow-sm')
generate_button.click()

# 关闭浏览器
time.sleep(3)  # 可以根据实际情况调整等待时间
driver.quit()
