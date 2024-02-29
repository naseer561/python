import requests
from bs4 import BeautifulSoup

def scrape_amazon(search_query):
    # Amazon search URL
    url = f'https://www.flipkart.com/search?q=iphone'

    # Send HTTP request and get the content
    response = requests.get(url)
    if response.status_code != 200:
        print('Failed to fetch the page')
        return

    soup = BeautifulSoup(response.content, 'html.parser')
    # print(soup.prettify())
    # Extract product information
    products = soup.find_all('div', {'class': '_30jeq3 UMT9wN'})
    print(products.string)
    # strong=products.find("div")
    # print(strong)
    # print(.string)


if __name__ == '__main__':
    search_query = input('Enter the product you want to search for on Amazon: ')
    scrape_amazon(search_query)