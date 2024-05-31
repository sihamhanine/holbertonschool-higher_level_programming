#!/usr/bin/env python3
"""Module task_02_requests"""
import requests
import csv


def fetch_and_print_posts():
    """
    Method that that fetches all post from JSONPlaceholder.
    """
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    print("Status Code: {}".format(response.status_code))
    if response.status_code == 200:
        data = response.json()
        for post in data:
            print(post['title'])


def fetch_and_save_posts():
    """
    Method that fetches all post from JSONPlaceholder.
    """
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        keys = ['id', 'title', 'body']
        with open('posts.csv', 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=keys)
            writer.writeheader()
            for post in data:
                filtered_post = {key: post[key] for key in keys}
                writer.writerow(filtered_post)
