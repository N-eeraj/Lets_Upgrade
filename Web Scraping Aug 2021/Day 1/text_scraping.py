from bs4 import BeautifulSoup
import requests
import pandas as pd
from collections import defaultdict

URL = "https://www.python.org/events"
res = requests.get(URL)

soup = BeautifulSoup(res.text, "html.parser")
details = defaultdict(list)

events = soup.find("ul", {"class": "list-recent-events"}).find_all("li")
    
for event in events:
    details["title"].append(event.h3.text)
    details["location"].append(event.find("span", {"class": "event-location"}).text)
    details["time"].append(event.find("time").text)
    
df = pd.DataFrame(details)
df.to_csv("Python Events.csv", index = False)