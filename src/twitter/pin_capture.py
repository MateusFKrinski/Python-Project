from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def pin_capture(initial_url, email, password):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)

    try:
        driver.get(initial_url)

        email_field = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.ID, 'username_or_email'))
        )
        email_field.send_keys(email)

        password_field = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.ID, 'password'))
        )
        password_field.send_keys(password)

        authorize_button = WebDriverWait(driver, 30).until(
            EC.element_to_be_clickable((By.ID, 'allow'))
        )
        authorize_button.click()

        pin_element = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'kbd[aria-labelledby="code-desc"] > code'))
        )

        pin_code = pin_element.text

        return pin_code

    finally:
        driver.quit()
