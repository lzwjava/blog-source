from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up Firefox options
firefox_options = Options()
# firefox_options.add_argument("--headless")  # Optional: Remove for visible browser

# Specify the default profile path
profile_path = (
    "/home/lzw/.mozilla/firefox/wzfodx6v.default"  # Adjust based on profiles.ini
)
firefox_profile = FirefoxProfile(profile_path)
firefox_options.profile = firefox_profile

# Set up geckodriver service
service = Service(
    executable_path="/home/lzw/bin/geckodriver"
)  # Adjust if geckodriver is elsewhere
driver = webdriver.Firefox(service=service, options=firefox_options)

driver.get("https://grok.com")

# Add the cookies you extracted
cookies = [{"name": "cf_clearance", "value": "value", "domain": ".grok.com"}]
for cookie in cookies:
    driver.add_cookie(cookie)

# Open the URL
driver.get("https://grok.com")

# Print the title of the page
print("Title of the page:", driver.title)

try:
    # Wait for the textarea to be present
    wait = WebDriverWait(driver, 20)
    textarea = wait.until(
        EC.presence_of_element_located(
            (By.XPATH, "//textarea[@aria-label='Ask Grok anything']")
        )
    )
    print("Textarea found:", textarea.is_displayed())

except Exception as e:
    print("Textarea not found:", e)

time.sleep(60)

# Close the driver
driver.quit()
