from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver')

chrome_browser.maximize_window()

chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

assert 'Selenium Easy Demo' in chrome_browser.title

button = chrome_browser.find_element_by_class_name('btn-default')
assert 'Show Message' in button.get_attribute('innerHTML')
assert 'Show Message' in chrome_browser.page_source
user_message = chrome_browser.find_element_by_id('user-message')
user_message.clear()
user_message.send_keys('typing a message')
button.click()
out_message = chrome_browser.find_element_by_id('display')
assert 'typing a message' in out_message.text

chrome_browser.close()