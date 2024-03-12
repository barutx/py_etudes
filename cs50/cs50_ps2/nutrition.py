#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 22:52:56 2024

@author: barut
"""
def main():
    dic=[
        {'fruit': "Apple", "calories":"130"},
        {'fruit': "Avocado", "calories": "50"},
        {'fruit': "Banana", "calories": "110"},
        {'fruit': "Cantaloupe", "calories": "50"},
        {'fruit': "Grapefruit", "calories": "60"},
        {'fruit': "Grape", "calories": "90"},
        {'fruit': "Honeydew Melon", "calories": "50"},
        {'fruit': "Kiwifruit", "calories": "90"},
        {'fruit': "Lemon", "calories": "15"},
        {'fruit': "Lime", "calories": "20"},
        {'fruit': "Nectarine", "calories": "60"},
        {'fruit': "Orange", "calories": "80"},
        {'fruit': "Peach", "calories": "60"},
        {'fruit': "Pear", "calories": "100"},
        {'fruit': "Plums", "calories": "50"},
        {'fruit': "Strawberry", "calories": "50"},
        {'fruit': "Sweet Cherry", "calories": "100"},
        {'fruit': "Tangerine", "calories": "50"},
        {'fruit': "Watermelon", "calories": "80"}
        ]

    x = str(input("What's the fruit you're looking for? ")).title().strip()
    for fruits in dic:
            if x in fruits["fruit"]:
                print(fruits["calories"])
main()

