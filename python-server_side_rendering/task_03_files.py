from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

# Function to load products from JSON
def load_products_from_json(filename):
    with open(filename, 'r') as f:
        products = json.load(f)
    return products

# Function to load products from CSV
def load_products_from_csv(filename):
    products = []
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            products.append(row)
    return products

# Function to determine source and load products
def load_products(source):
    if source == 'json':
        return load_products_from_json('products.json')
    elif source == 'csv':
        return load_products_from_csv('products.csv')
    else:
        return None  # Return None for invalid source

# Route to handle product display with filtering
@app.route('/products')
def display_products():
    source = request.args.get('source')
    id = request.args.get('id')

    # Load products based on source
    products = load_products(source)

    if products is None:
        return render_template('product_display.html', error="Wrong source")

    if id:
        filtered_products = [p for p in products if str(p.get('id')) == id]
        if not filtered_products:
            return render_template('product_display.html', error="Product not found")
    else:
        filtered_products = products

    return render_template('product_display.html', products=filtered_products)

if __name__ == '__main__':
    app.run(debug=True)