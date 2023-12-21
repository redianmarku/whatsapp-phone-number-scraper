from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from openpyxl import Workbook

# Set up the Selenium driver
driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')

# Wait for the user to scan the QR code and log in to WhatsApp
input('Press Enter after scanning QR code and logging in to WhatsApp')

# Wait for the group chat to load and find the member elements
member_elements = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located(
        (By.CSS_SELECTOR, '._2h0YP'))
)

# Extract the phone numbers from the member elements
phone_numbers = [element.text for element in member_elements]

# Close the Selenium driver
driver.quit()

# Create a new Excel workbook and worksheet
workbook = Workbook()
worksheet = workbook.active

# Write the phone numbers to the worksheet
for i, phone_number in enumerate(phone_numbers, start=1):
    worksheet.cell(row=i, column=1, value=phone_number)

# Save the workbook
workbook.save(
    'I:\\original\\Coding\\whatsapp-phone-number-scraper\\member_info.xlsx')
