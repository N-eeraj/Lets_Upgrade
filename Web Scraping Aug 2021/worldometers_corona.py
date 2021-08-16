from bs4 import BeautifulSoup
import requests
import pandas as pd
from collections import defaultdict

def getCovidData():
    response = requests.get("https://www.worldometers.info/coronavirus/")

    data = BeautifulSoup(response.text, "html.parser")
    details = defaultdict(list)

    table = data.find("table", {"id": "main_table_countries_today"}).find("tbody").find_all("tr")

    for country in table[8:]:
        details["Country"].append(country.find_all("td")[1].text)
        details["Total Cases"].append(country.find_all("td")[2].text)
        details["New Cases"].append(country.find_all("td")[3].text)
        details["Total Deaths"].append(country.find_all("td")[4].text)
        details["Total Recovered"].append(country.find_all("td")[6].text)
        details["Active Cases"].append(country.find_all("td")[8].text)

    df = pd.DataFrame(details)
    return df

df = getCovidData()
print(df.head())