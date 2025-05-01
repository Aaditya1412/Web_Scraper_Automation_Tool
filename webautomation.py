import os
import time
import pyautogui
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import glob

# Read DNA sequences from Excel
excel_file_path = r"C:\Users\f2021\OneDrive\Desktop\New folder (2)\sequence_list.xlsx"
sequences_df = pd.read_excel(excel_file_path)

# Set up Chrome options to customize the download behavior
chrome_options = webdriver.ChromeOptions()

# Set the download directory
download_directory = r"C:\Users\f2021\OneDrive\Desktop\bdna"

prefs = {
    "download.default_directory": download_directory,  # Replace with your desired download path
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True,
    "safebrowsing.disable_download_protection": True,  # Disable download protection to avoid "insecure download" warnings
}
chrome_options.add_experimental_option("prefs", prefs)

# Initialize the WebDriver with Chrome options
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)

# Function to get the latest downloaded file
def get_latest_file(path):
    files = glob.glob(os.path.join(path, '*'))
    return max(files, key=os.path.getctime)  # Corrected the argument passed to os.path.getctime

# Loop through each DNA sequence in the Excel file
for index, row in sequences_df.iterrows():
    sequence_no = row['S.no']  # Assuming 'S.no' is the column name in the Excel file
    sequence = row['Sequence']  # Assuming 'Sequence' is the column name in the Excel file

    # Open the webpage
    driver.get('http://www.scfbio-iitd.res.in/software/drugdesign/bdna.jsp')
    time.sleep(3)

    # Fill in the form with the input data
    inbox_box = driver.find_element(By.XPATH, '//*[@id="main"]/tbody/tr[2]/td/table[2]/tbody/tr/td/table/tbody/tr[1]/th/table/tbody/tr[2]/th/span/fieldset/div/form/p[1]/input[1]')
    time.sleep(1)
    inbox_box.send_keys(sequence)

    # Select the B-DNA option
    B_DNA_check = driver.find_element(By.XPATH, '//*[@id="main"]/tbody/tr[2]/td/table[2]/tbody/tr/td/table/tbody/tr[1]/th/table/tbody/tr[2]/th/span/fieldset/div/form/p[2]/span/input[2]')
    time.sleep(3)
    B_DNA_check.click()

    # Submit the form
    submit_element = driver.find_element(By.XPATH, '//*[@id="main"]/tbody/tr[2]/td/table[2]/tbody/tr/td/table/tbody/tr[1]/th/table/tbody/tr[2]/th/span/fieldset/div/form/p[3]/input[1]')
    time.sleep(5)
    submit_element.click()

    # Click on the output file link
    output_file = driver.find_element(By.PARTIAL_LINK_TEXT, "outputfile")
    output_file.click()

    # Wait for the download to start and the "Keep" button to appear
    time.sleep(5)

    # Simulate pressing 'Tab' and 'Enter' to interact with the "Keep" button
    pyautogui.press('tab')  # Move focus to the "Keep" button
    time.sleep(1)
    pyautogui.press('enter')  # Press "Enter" to confirm

    # Wait for the download to finish
    time.sleep(10)

    # Get the latest downloaded file
    latest_file = get_latest_file(download_directory)

    # Define the new file name based on the sequence number
    new_file_name = os.path.join(download_directory, f"{sequence_no}.pdb")  # Adjust extension as necessary
    os.rename(latest_file, new_file_name)

# Close the browser after all sequences have been processed
driver.quit()


