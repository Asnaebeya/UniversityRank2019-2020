import pandas as pd
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

url = 'https://www.timeshighereducation.com/student/best-universities/best-universities-world'

req= Request(url , headers={'User-Agent': 'Mozilla/5.0'})
webpage = urlopen(req).read()
soup = BeautifulSoup(webpage,"html.parser")
table = soup.find('table')
rows = table.find_all('tr')
data = []
for row in rows[1:]:
    cols = row.find_all('td')
    cols = [ele.text.strip() for ele in cols]
    data.append([ele for ele in cols if ele])

result = pd.DataFrame(data, columns=['rank_2020', 'rank_2019','University','Country'])

result.to_csv('file1.csv')