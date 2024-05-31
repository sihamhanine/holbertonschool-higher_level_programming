#!/usr/bin/env python3
import requests
import csv


def fetch_and_print_posts():
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    print("Status code:", response.status_code)
    if response.status_code == 200:
        data = response.json()
        for post in data:
            print(post.get('title', 'Title not found'))

def fetch_and_save_posts():
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        keys = ['userId', 'id', 'title', 'body']  # Ajouter 'id' aux noms de colonnes
        with open('posts.csv', 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=keys)
            writer.writeheader()
            for post in data:
                writer.writerow(post)
    else:
        print("Failed to fetch posts from the server.")
