from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Scraper:
    def __init__(self, url):
        self.url = url
        self.driver = None

    def start_browser(self):
        """Start the Chrome browser and open the specified URL."""
        self.driver = webdriver.Chrome()  # Ensure ChromeDriver is installed
        self.driver.get(self.url)

    def search_product(self, search_query):
        """Search for a product on the page."""
        if not self.driver:
            raise Exception("Browser not started.")
        
        # Ensure search_query is a string
        if not isinstance(search_query, str):
            raise ValueError("Search query must be a string.")
        
        try:
            search_box = self.driver.find_element(By.CSS_SELECTOR, 'input[name="field-keywords"]')  # Amazon search box selector
            search_box.send_keys(search_query)  # Directly use the query, it should already be a string
            search_box.send_keys(Keys.RETURN)  # Simulate pressing the 'Enter' key to initiate the search
        except Exception as e:
            print(f"Error in search: {e}")

    def extract_reviews(self):
        """Extract reviews from the product page."""
        reviews = []
        while True:  # Loop through all pages of reviews
            elements = self.driver.find_elements(By.CSS_SELECTOR, ".celwidget")  # Review containers
            for element in elements:
                try:
                    # Extracting Review Title
                    title = element.find_element(By.CSS_SELECTOR, ".review-title-content").text

                    # Extracting Review Body
                    body = element.find_element(By.CSS_SELECTOR, ".review-text-content span").text

                    # Extracting Rating
                    rating = element.find_element(By.CSS_SELECTOR, ".a-icon-alt").text

                    # Extracting Reviewer
                    reviewer = element.find_element(By.CSS_SELECTOR, ".a-profile-name").text

                    reviews.append({
                        "title": title,
                        "body": body,
                        "rating": rating,
                        "reviewer": reviewer
                    })
                except Exception as e:
                    print(f"Error extracting review: {e}")
            
            # Check if there's a "Next" page button and click it
            try:
                next_button = self.driver.find_element(By.CSS_SELECTOR, ".a-last a")
                next_button.click()
                WebDriverWait(self.driver, 10).until(
                    EC.staleness_of(elements[0])  # Wait for the page to refresh
                )
            except Exception as e:
                print(f"Error navigating to next page: {e}")
                break  # Exit the loop if there's no "Next" button
        return reviews

    def close_browser(self):
        """Close the browser."""
        if self.driver:
            self.driver.quit()
