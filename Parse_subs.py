
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()

try:
    # Open the webpage
    driver.get("https://www.youtube.com/watch?v=MbTaFACzX0o")
    time.sleep(3)
    expand_button = driver.find_element(By.XPATH, '//*[@id="expand"]')
    expand_button.click()

    # Find the element by ID
    show_transcript_button = driver.find_element(By.XPATH, '//*[@id="primary-button"]/ytd-button-renderer/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]')


    # Click the element
    show_transcript_button.click()
    time.sleep(3)
    transcript_data = driver.find_element(By.XPATH, '//*[@id="segments-container"]')
    innerHTML = transcript_data.get_attribute('innerHTML')
    soup = BeautifulSoup(innerHTML, "html.parser")
    transcription = []
    for string in soup.findAll("yt-formatted-string", class_="segment-text"):
        transcription.append(string.text)
    print(".".join(transcription))
except Exception as e:
    print(e)
finally:
    # Close the browser
    driver.quit()