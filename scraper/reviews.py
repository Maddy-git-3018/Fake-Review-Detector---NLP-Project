from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from webdriver_manager.chrome import ChromeDriverManager

def get_reviews(url):
    # Set up headless Chrome
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    service = Service(ChromeDriverManager().install())  # ✅ Setup Service properly
    driver = webdriver.Chrome(service=service, options=chrome_options)  # ✅ Use named arguments

    driver.get(url)

    reviews = []

    try:
        # Scroll to load reviews (adjust sleep/scroll depth if needed)
        for _ in range(2):  # was missing range limit!
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)

        # Find reviews
        review_elements = driver.find_elements(By.CSS_SELECTOR, "span[data-hook='review-body']")
        for elem in review_elements:
            reviews.append(elem.text.strip())

    except Exception as e:
        print("Scraping error:", e)

    finally:
        driver.quit()

    return reviews