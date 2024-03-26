from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the WebDriver
driver = webdriver.Chrome()

# Set implicit wait
driver.implicitly_wait(10)

# Navigate to a URL
driver.get('http://example.com')

# Perform actions on the page...

# Use explicit wait to wait for an element to be present before interacting
element = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.ID, 'myElement'))
)

# Interact with the element
element.click()

# Close the current window
driver.close()

# Quit the driver and close all windows
driver.quit()
