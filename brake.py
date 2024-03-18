import os
import requests
import json  # for parsing JSON response

os.environ['HTTPS_PROXY'] = 'http://127.0.0.1:3128'
os.environ['HTTP_PROXY'] = 'http://127.0.0.1:3128'

API_KEY = "AIzaSyBguyKaWZar3My8QH8yJgH6fcn0OVeRDNU"  # Replace with your actual key
Search_ID = "912f8f8e2fbb54bf5"  # Replace with your actual ID

search_query = "connected braking"
url = "https://www.googleapis.com/customsearch/v1"
params = {
  "q": search_query,
  'key': API_KEY,
  'cx': Search_ID
}

response = requests.get(url, params=params)
results = response.json()

if 'items' in results:
  print(results['items'][0]['link'])

# Check for successful response
if response.status_code == 200:
  # Parse JSON data
  data = response.json()
  
  # Extract search results (assuming structure)
  results = data.get('items', [])  # Handle potential missing items key
  for item in results:
    title = item.get('title')
    snippet = item.get('snippet')
    link = item.get('link')
    # Process or store these results (title, snippet, link)
    print(f"Title: {title}\nSnippet: {snippet}\nLink: {link}\n")
else:
  print(f"Error: {response.status_code}")

# url = "https://www.datacenterdynamics.com/en/news/"



# response = requests.get(url)
# print(response.content)
# soup = BeautifulSoup(response.content, 'html.parser')

# # Replace with the actual class/tag that holds news reports
# news_items = soup.find_all('div', class_='news-item')  # Modify this selector based on website structure

# reports = []
# for item in news_items:
#   # Extract title, date, summary using appropriate tags/attributes within the news_item element
#   title = item.find('h3').text.strip()
#   date = item.find('span', class_='date').text.strip()
#   summary = item.find('p', class_='summary').text.strip()
#   reports.append({'title': title, 'date': date, 'summary': summary})


# df = pd.DataFrame(reports)
# df.to_excel('brake_report_news.xlsx', index=False)
