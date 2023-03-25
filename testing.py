import os
from bs4 import BeautifulSoup

# Read the saved HTML file
with open("mobilelegends_rank.html", "r", encoding="utf-8") as file:
    html_content = file.read()

# Initialize a Beautiful Soup object with the HTML content
soup = BeautifulSoup(html_content, "html.parser")

# Find the table with data
table = soup.find('table', {'class': 'table table-striped'})

# Extract table headers
headers = [th.text.strip() for th in table.find_all('th')]

# Extract table rows
rows = table.find_all('tr')[1:]  # Skip the first row (headers)

# Extract data from table rows
data = []
for row in rows:
    cells = row.find_all('td')
    row_data = [cell.text.strip() for cell in cells]
    data.append(row_data)

# Print headers and data
print(headers)
for row_data in data:
    print(row_data)