from selenium import webdriver
import subprocess
import time

# 设置浏览器
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)

# 打开网站
driver.get("https://wegic.ai/")

# 开始录制
subprocess.Popen(['ffmpeg', '-f', 'x11grab', '-r', '30', '-s', '1920x1080', '-i', ':0.0', 'output.mp4'])

# 浏览操作
time.sleep(10)  # 模拟操作时间

# 停止录制
driver.quit()
subprocess.call(['pkill', 'ffmpeg'])
