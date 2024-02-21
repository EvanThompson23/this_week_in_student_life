import time
from dateutil import parser
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

class Selenium_Request:
   
   def load_page(driver, dates):
      driver.get("https://floridatech.campuslabs.com/engage/account/login?returnUrl=/engage/events")
      WebDriverWait(driver,1000).until(EC.title_is("Upcoming Events - Florida Tech Engage")) 
      button = driver.find_element(By.CSS_SELECTOR, "#react-app > div > div > div > div:nth-child(4) > div > div > div:nth-child(2) > div:nth-child(2) > div.outlinedButton > button")
      wait = WebDriverWait(driver, 10)
      while Selenium_Request.__check_element__(button) and Selenium_Request.__check_date__(driver, dates):
         wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#react-app > div > div > div > div:nth-child(4) > div > div > div:nth-child(2) > div:nth-child(2) > div.outlinedButton > button")))
         button.click() 

      return driver.find_elements(By.CSS_SELECTOR, "#event-discovery-list > div > div")

   def __check_date__(driver, dates):
      events = driver.find_elements(By.CSS_SELECTOR, "#event-discovery-list > div > div")
      event = events[len(events)-1]
      time = event.text.split('\n')[1]
      time = time.replace(" EST", '')
      time = time.replace(" EDT", '')
      time_parsed  = parser.parse(time).date()
      if(time_parsed > dates.get_date_end()):
         return False
      return True

   def __check_element__(element):
      try:
         element.get_attribute("span")
      except StaleElementReferenceException:
         return False
      return True
