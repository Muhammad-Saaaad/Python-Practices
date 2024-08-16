# import requests
# from bs4 import BeautifulSoup
# from time import sleep
# from urllib.parse import urljoin, urlparse

# url = r'https://www.flipkart.com/'

# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
# }


# while True:
#     response = requests.get(url, headers=headers)
#     if response.status_code == 429:
#         print("429 error: Too many requests. Waiting...")
#         sleep(5)  # Wait 5 seconds before retrying
#         continue
#     break

# soap = BeautifulSoup(response.text , 'lxml')
# # print(soap)


# links = soap.findAll('a')

# # for link in url:
# #     print(link , '\n\n')
# internal_links = []
# for url in links:

#     href = url.get('href')
#     if href and isinstance(href, str):
#         full_link = urljoin(url , href)
#         if urlparse(full_link).netloc == urlparse(url).netloc:  
#             internal_links.append(full_link)

# internal_links = list(set(internal_links)) # for removing the duplicate links

# for links in internal_links:
#     print(links)



# with open('Web_scraping/Urls.txt' , 'a') as f:
#     for url in urls:
#         f.write(str(url) +'\n')



import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
import time

url = 'https://www.cityofsacramento.gov/police'  # Replace with the website you want to scrape
response = requests.get(url)

# Handle 429 error by checking response status code
while response.status_code == 429:
    print("429 error: Too many requests. Waiting...")
    time.sleep(5)  # Wait for 5 seconds before trying again
    response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
links = soup.find_all('a')

internal_links = []
for link in links:
    href = link.get('href')
    if href and isinstance(href, str):  # Check if href is not None and is a string
        full_url = urljoin(url, href)
        if urlparse(full_url).netloc == urlparse(url).netloc:
            internal_links.append(full_url)

internal_links = list(set(internal_links))

with open(r'Web_scraping/police_urls.txt' , 'a') as f:
    for link in internal_links:
        f.write(str(link) + '\n')
print('done')

