from flask import Blueprint, render_template, request
from ..services.shopify_service import search_products

bp = Blueprint('shop', __name__)

@bp.route('/', methods=['GET', 'POST'])
def search():
    products = []
    query = ''
    if request.method == 'POST':
        query = request.form.get('query')
        products = search_products(query)
    return render_template('search.html', products=products, query=query)
