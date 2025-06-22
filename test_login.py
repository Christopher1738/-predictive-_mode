from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 1. Launch browser (auto-downloads driver)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    # 2. Load login page
    driver.get("https://the-internet.herokuapp.com/login")
    print("Page loaded successfully!")
    
    # 3. Find elements and login (with waiting)
    username = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    )
    username.send_keys("tomsmith")
    
    password = driver.find_element(By.ID, "password")
    password.send_keys("SuperSecretPassword!")
    
    # 4. Click login
    driver.find_element(By.CSS_SELECTOR, "button.radius").click()
    
    # 5. Verify login success
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.ID, "flash"), "You logged into")
    )
    print("TEST PASSED! Login successful.")
    
    # 6. Take screenshot (save to your computer)
    driver.save_screenshot("login_success.png")
    print("Screenshot saved as 'login_success.png'")

finally:
    # 7. Close browser
    driver.quit()