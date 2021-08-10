# CAUTION!!!!
# Whenever you web scrape a website do not just put the url into Python. Instead take the url for example www.reddit.com and add a /robots.txt to the end.
# By doing this www.reddit.com/robots.txt. You may now see if you can web scrape the website.
# In some cases you may have to check the actual website if you can web scrape it or not.
# To use one of the extractions uncomment that extraction but make sure everything else is commented. comment and uncomment hotkey (CTRL - /)

from bs4 import BeautifulSoup
import requests

url = "https://weather.com/weather/today/l/8bad02a12c27aa6b1dd86458beda72ec0b10a07d4ce18fee858fcc5c7d8be8a6"
page = requests.get(url)  # stores the contents from the url from above.

soup = BeautifulSoup(page.content, "html.parser")

# EXTRACTING ALL INFO FROM A CLASS!
# results = soup.find_all('div', class_='DaybreakLargeScreen--gridWrapper--3-iLh')
# for results in results:
#     print(results)  # by default the results is set to nothing, if you just want the text then type .text at the end. EXAMPLE: results.txt

# EXTRACTING INFO USING AN ID!
# results = soup.find(id='WxuTodayWeatherCard-main-486ce56c-74e0-4152-bd76-7aea8e98520a')
# print(results)

# EXTRACTING INFO USING STRING!
# results = soup.find_all('h1',string=lambda text:"ny weather" in text.lower()) # When typing the word your finding, please type it in lowercase.
# for result in results:
#     print(result)

# FINDING HYPERLINKS
results = soup.find_all('div', id='WxuHurricaneTrackerCard-sidebar-eaf3a578-6862-468e-9c75-5973515b2d3f')
for result in results:
    hyperlink = result.find('a')['href']
    print(f"Found the following links: {hyperlink} \n")

