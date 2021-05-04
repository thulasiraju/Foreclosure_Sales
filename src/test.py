from selenium import  webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome('../drivers/chromedriver.exe')
driver.get('https://google.com')
driver.execute_script("window.open('')")
driver.find_element_by_xpath("//input[@title='Search']").send_keys(Keys.CONTROL+'t')
#driver.switch_to.window(driver.window_handles[1])
