import csv
import requests
from bs4 import BeautifulSoup

# Step 1: Fetch the HTML content
url = 'http://example.com'
response = requests.get(url)
html_content = response.text

# Step 2: Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Step 3: Find all paragraph tags
additional_data = soup.find_all('p')

# Step 4: Open a CSV file and create a csv.writer object
with open('output.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)

    # Step 5: Write the text of each paragraph to the CSV file
    for data in additional_data:
        writer.writerow([data.text])

print("Data written to output.csv")
