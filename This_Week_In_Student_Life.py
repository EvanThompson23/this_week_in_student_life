from selenium import webdriver
import Date_Selector
import Selenium_Request
import Event
import Write_To_Docx

dates = Date_Selector.Date_Selector(None, None)
dates.cal_selector()
driver =  webdriver.Chrome()
raw_events = Selenium_Request.Selenium_Request.load_page(driver, dates)
events_list = Event.Events()
events_list.pull_elements(raw_events)
driver.quit()
events_list.fix_events()
Write_To_Docx.print_to_file(dates, events_list.get_event_list()) # Edit to work with new file

