import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Edge(executable_path="C:/Users/nejag/OneDrive/Desktop/Year Up"
                                        "/Module 3/CIS 403/Week 18/Project/edgedriver_win64/msedgedriver.exe")
driver.get("https://oxylabs.io/blog")
results = []
other_results = []
content = driver.page_source
soup = BeautifulSoup(content)
driver.quit()

for a in soup.findAll(attrs="blog-card__content-wrapper"):
    name = a.find('h2')
    if name not in results:
        results.append(name.text)

for b in soup.findAll(attrs="blog-card__date-wrapper"):
    date = b.find('p')
    if date not in results:
        other_results.append(date.text)

df = pd.DataFrame({"Names": results, "Dates": other_results})
df.to_csv('names.csv', index=False, encoding='utf-8')

