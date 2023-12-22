import re

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from openpyxl import Workbook
import logging

# Set up logging
logging.basicConfig(filename='whatsapp_scraper.log', level=logging.INFO)


def display_welcome_message():
    print("Welcome to the WhatsApp Phone Number Scraper!")
    print("Please scan the QR code and log in to WhatsApp on the opened browser.")
    input('Press Enter when you are ready to proceed.')


def initialize_driver():
    try:
        driver = webdriver.Chrome()
        driver.get('https://web.whatsapp.com/')
        return driver
    except Exception as e:
        logging.error(f'Error initializing the driver: {e}')
        print("An error occurred while initializing the driver. Please check logs for details.")
        return None


def login(driver):
    try:
        display_welcome_message()
        # Wait for the user to scan the QR code and log in to WhatsApp
        input('Press Enter after scanning QR code and logging in to WhatsApp')
    except Exception as e:
        logging.error(f'Error during login: {e}')
        print("An error occurred during login. Please check logs for details.")


def scrape_all_content(driver):
    try:
        # Wait for the page to load completely
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'body'))
        )

        # Get all page content
        page_content = driver.find_element(By.CSS_SELECTOR, 'body').text

        return page_content
    except Exception as e:
        logging.error(f'Error during scraping: {e}')
        print("An error occurred during scraping. Please check logs for details.")
        return None


def extract_phone_numbers(page_content):
    try:
        # Use regex to extract phone numbers
        phone_numbers = re.findall(
            r'\+\d{1,3}\s\d{1,4}\s\d{1,4}\s\d{1,}', page_content)

        return phone_numbers
    except Exception as e:
        logging.error(f'Error during phone number extraction: {e}')
        print("An error occurred during phone number extraction. Please check logs for details.")
        return None


def export(phone_numbers):
    try:
        # Create a new Excel workbook and worksheet
        workbook = Workbook()
        worksheet = workbook.active

        # Write the phone numbers to the worksheet
        for i, phone_number in enumerate(phone_numbers, start=1):
            worksheet.cell(row=i, column=1, value=phone_number)

        # Save the workbook
        workbook.save('member_info.xlsx')

        print("Phone numbers have been successfully exported to 'member_info.xlsx'")
    except Exception as e:
        logging.error(f'Error during export: {e}')
        print("An error occurred during export. Please check logs for details.")


def main():
    try:
        driver = initialize_driver()
        if driver:
            login(driver)
            page_content = scrape_all_content(driver)
            if page_content:
                phone_numbers = extract_phone_numbers(page_content)
                if phone_numbers:
                    export(phone_numbers)
    except Exception as e:
        logging.error(f'Unexpected error: {e}')
        print("An unexpected error occurred. Please check logs for details.")


if __name__ == "__main__":
    main()
