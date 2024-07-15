from flask import Flask, render_template
import json

app = Flask(__name__)

# Function to load items from items.json
def load_items():
    with open('items.json', 'r') as f:
        items_data = json.load(f)
    return items_data.get('items', [])

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    items_list = load_items()
    return render_template('items.html', items=items_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
