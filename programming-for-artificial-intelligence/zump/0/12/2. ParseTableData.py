#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 01:26:10 2026

@author: awais
"""

import requests
from bs4 import BeautifulSoup

def scrape_product_list():
    # Using an explicit sandbox URL designed for practice scraping
    url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Error accessing the page.")
        return []

    soup = BeautifulSoup(response.text, 'html.parser')
    products = []
    
    # Find all product item card divs
    cards = soup.find_all('div', class_='thumbnail')
    
    for card in cards:
        # Extract item details safely
        title = card.find('a', class_='title').text.strip()
        price = card.find('h4', class_='price').text.strip()
        description = card.find('p', class_='description').text.strip()
        
        products.append({
            "item_name": title,
            "price": price,
            "details": description
        })
        
    return products

# --- Execution ---
laptop_data = scrape_product_list()
for item in laptop_data[:3]:  # Print first 3 results
    print(item["item_name"], item["price"])
    
    
# //div[@class='card thumbnail']
# //div[contains(@class,'thumbnail')]
