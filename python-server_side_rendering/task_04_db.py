import sqlite3
import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__)

def load_products_from_json(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data['items']

def load_products_from_csv(filename):
    products = []
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            products.append(row)
    return products

def load_products_from_sql():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Products')
    rows = cursor.fetchall()
    products = [{'id': row[0], 'name': row[1], 'category': row[2], 'price': row[3]} for row in rows]
    conn.close()
    return products

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source == 'json':
        products = load_products_from_json('products.json')
    elif source == 'csv':
        products = load_products_from_csv('products.csv')
    elif source == 'sql':
        try:
            products = load_products_from_sql()
        except sqlite3.Error as e:
            return render_template('product_display.html', error=f"Database error: {e}")
    else:
        return render_template('product_display.html', error="Wrong source")

    if product_id:
        product_id = int(product_id)
        products = [product for product in products if int(product['id']) == product_id]
        if not products:
            return render_template('product_display.html', error="Product not found")

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
