
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the Chrome driver (make sure ChromeDriver is in PATH)
driver = webdriver.Chrome()

# Open the target website
driver.get("https://automationexercise.com")

# Maximize the window
driver.maximize_window()

# Click on 'Signup / Login' link
login_link = driver.find_element(By.LINK_TEXT, "Signup / Login")
login_link.click()
time.sleep(2)

# Input email address and password
email_input = driver.find_element(By.NAME, "email")
password_input = driver.find_element(By.NAME, "password")
email_input.send_keys("test@example.com")
password_input.send_keys("password123")

# Click the Login button
login_button = driver.find_element(By.XPATH, "//button[text()='Login']")
login_button.click()
time.sleep(3)

# Optional: Validate login success (check for logout button or username)
try:
    logout_link = driver.find_element(By.LINK_TEXT, "Logout")
    print("Login test passed: Logout link found.")
except:
    print("Login test failed: Logout link not found.")

# Close the browser
driver.quit()
