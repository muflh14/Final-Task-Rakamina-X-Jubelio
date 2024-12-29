from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=options)
driver.get("https://app2.jubelio.com/login")

element = driver.find_element(By.NAME, "email")
element.clear()
element.send_keys("bartholomewmr1@gmail.com")

element = driver.find_element(By.NAME, "password")
element.clear()
element.send_keys("Jubelio123$")


driver.find_element(By.CSS_SELECTOR, "span.ladda-label").click()

driver.implicity_wait(10)

try:
	driver.find_element(By.XPATH, "//span[contains(text(), 'Dashboard')]")
	print("login successful")
	driver.quit()

except Exception as e:
	print("Error during login", str(e))
	driver.quit()