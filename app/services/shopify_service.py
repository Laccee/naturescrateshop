import requests
from flask import current_app

def search_products(query):
    url = f"https://{current_app.config['SHOPIFY_API_KEY']}:" \
          f"{current_app.config['SHOPIFY_API_PASSWORD']}@" \
          f"{current_app.config['SHOPIFY_STORE_NAME']}.myshopify.com/admin/api/2023-01/products.json"
    
    params = {
        "title": query,
    }
    
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json().get('products', [])
    return []
