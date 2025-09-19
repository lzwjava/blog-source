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
profile_path = "/home/lzw/.mozilla/firefox/stp0k50c.default-release"  # Adjust based on profiles.ini
firefox_profile = FirefoxProfile(profile_path)
firefox_options.profile = firefox_profile
# Set up geckodriver service
service = Service(
    executable_path="/home/lzw/bin/geckodriver"
)  # Adjust if geckodriver is elsewhere
driver = webdriver.Firefox(service=service, options=firefox_options)

driver.get("https://chat.qwen.ai")

try:
    # Wait for the chat input element to be present
    chat_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "chat-input"))
    )

    # Type "hi" into the chat input
    chat_input.send_keys("hi")

except Exception as e:
    print(f"Error: {e}")

    # Locate the submit button using XPath and click it
submit_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(
        (By.CSS_SELECTOR, 'button#send-message-button[type="submit"]')
    )
)
submit_button.click()

# Open a new tab
driver.execute_script("window.open('https://chat.mistral.ai/chat', '_blank');")

# Switch to the new tab
driver.switch_to.window(driver.window_handles[1])

# Wait for the chat input element to be present
chat_input = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, "//div[@data-placeholder='Ask le Chat']"))
)

# Type "hi" into the chat input
chat_input.send_keys("hi")

# Locate the submit button using XPath and click it
submit_button = WebDriverWait(driver, 20).until(
    EC.element_to_be_clickable((By.XPATH, "//button[contains(.,'Send')]"))
)
submit_button.click()


time.sleep(60)

# Close the driver
driver.quit()
