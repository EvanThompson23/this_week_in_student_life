import re
import Event
from dateutil import parser
from selenium.webdriver.common.by import By

class Event:
  def __init__(self, Name, Dstart, Location, Xhosts, Url):
   self.Name = Name
   self.Dstart = Dstart
   self.Location = Location
   self.Xhosts = Xhosts
   self.Url = Url

class Events:
   def __init__(self):
      self.event_list = []

   def get_event_list(self):
      return self.event_list

   def append_event(self, value):
      self.event_list.append(value)

   def pull_elements(self, raw_events):
      for event in raw_events:
         el = event.text.split('\n')
         link = event.find_element(By.CSS_SELECTOR, 'a')
         url = link.get_attribute('href')
         el.append(url)
         if "Student Success and Support Center" not in el[3]:
            self.append_event(Event(el[0],el[1],el[2],el[3],el[4])) # Edit to work with new file

   def fix_events(events_list):
      #Parses weird time standard for ICS files
      for event in events_list.get_event_list():
         Events.__remove_characters__(event)
         Events.__parse_time__ (event)

   def __parse_time__ (event):
      event.Dstart = parser.parse(event.Dstart)

   def __remove_characters__(node):
      node.Name = re.sub(r"[^\x00-\x7F]+", "", node.Name)
      node.Dstart = node.Dstart.replace(" EST", '')
      node.Dstart = node.Dstart.replace(" EDT", '')
