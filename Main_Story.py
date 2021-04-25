"""
Main_Story.py

Project Title: Choose Your Own Adventure
Description: This file creates instances of a Choose Your Own Adventure story using an original story created
by the author. The content and path logic are found in Substories.py.

class functions:
__init__(): initializes story

__repr__(): gives string representation of class

showtime(): runs the storyline until completion

nav(): updates the path (self.path based choice (if applicable) to update text (self.text),
moral points (self.moral_points), options (self.options), collected items (self.items), itemstotal (self.itemstotal),
and chapter (self.chapter)

currentState(): prints out current text

endings(): computes and prints ending based on items total (self.items_total and moral points (self.moral_points)

moralpoints(): updates the moral points (self.moral_points)

collect(): updates the items collected based on keyword in subtext.


Author: Michelle Burroughs
4/25/2021
"""

from Substories import *

class MainStory:

    def __init__(self, name):
        self.name = name
        self.path = 1
        self.choice = 0
        self.options = options[0]
        self.text = text[0]
        self.chapter = 1
        self.moral_points = 0
        self.items = []
        self.itemstotal = 0

        print("Welcome {} to Into St. Louis Cemetery #1: A Choose Your Own Adventure Story".format(self.name) + "\n" +
              "\n" + self.text + "\n")

    def __repr__(self):
        return "Into St. Louis Cemetery #1: A Choose Your Own Adventure Story, story defined by {}".format(self.name)

    # Plays out story to completion
    def showtime(self):
        while self.path != 10 and self.path != 12 and self.path != 14 and self.path != 15:
            self.nav()
            self.currentState()
        self.endings()
        return

    # Navigates modules
    def nav(self):
        if len(path[self.path]) > 1: # If value of path features options
            try: # User updates choice
                self.choice = input("Please choose either {} by typing 1 or {} by typing 2: ".format(self.options[0],
                                                                                             self.options[1]))
            except IndexError:
                print("Choice is out of range")

            self.path = path[self.path][int(self.choice) - 1] #Updates path
            if self.path != 10 and self.path != 12 and self.path != 14 and self.path != 15: # If new options in new path
                self.options = options[self.path - 1]
                self.moral_points = self.moralpoints(mp)

        else: # If options do not exist in current path
            self.path = path[self.path] #Updates path

        self.text = text[self.path - 1] # Updates Text
        self.collect(storyitems) # collects items
        self.chapter += 1 # Updates Chapter
        return self.path, self.options, self.text, self.choice, self.chapter, self.moral_points, self.items, \
               self.itemstotal

    # Prints current text
    def currentState(self):
        print('\n')
        print('Chapter: ' + str(self.chapter))
        print(self.text)
        print('\n')
        return

    # Calculates and prints ending
    def endings(self):
        total_ending = self.moral_points + self.itemstotal
        if total_ending >= 5:
            result = endings[0]
        elif total_ending < 5 and total_ending > -5:
            result = endings[1]
        else:
            result = endings[2]
        print("Final Chapter:" + "\n" + result + "\n" + "Moral Points: " + str(total_ending))

        return

    # Adds moral_points for use in calculating ending
    def moralpoints(self, mp):
        self.moral_points += mp[self.path - 1][int(self.choice)-1]
        return self.moral_points

    # Adds items collected, each item has a value used for calculating ending
    def collect(self, storyitems):
        for item in storyitems:
            if item in self.text:
                self.items.append(item)
                self.itemstotal += storyitems[item]
        return self.items, self.itemstotal


newStory = MainStory('Logan') #create new instance of story
newStory.showtime() #runs the story to completion
