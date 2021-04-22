"""
Main_Story.py
Choose Your Own Adventure
Description: This file creates instances of a Choose Your Own Adventure story
using a story created by the author


Author: Michelle Burroughs
"""

class MainStory:
    moral_points = 0
    items = {}

    def __init__(self, name, text):
        self.name = name
        self.text = text

    def __repr__(self):
        print("Into St. Louis Cemetery #1: A Choose Your Own Adventure Story")

    # Navigates modules
    def choices(self):
        choice = input("Please choose which option you would like:")
        next_path = path[text]
        return next_path

    # Returns ending
    def endings(self):
        total_ending = moral_points + item_total
        if total_ending >= 5:
            result = endings[0]
        elif total_ending < 5 and total_ending > -5:
            result = endings[1]
        else:
            result = endings[2]
        return result

    # Adds items collected, each item has a value used for calculating ending
    def collect(self, item):
        items[item]
        return items

    # Adds moral_points for use in calculating ending
    def moralpoints(self, moral_points, mp):
        return moral_points += mp


