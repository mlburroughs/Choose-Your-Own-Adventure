"""
Tree_Node.py

Project Title: Choose Your Own Adventure
Description: This file defines the node and tree data structure relationships between story modules
using user input

class TreeNode - provides the tree structure that allows each story module to be encapsulated
into a node structure, defines the relationship between nodes, and executes the traversal of
the choose your adventure story

class Functions:
__init__() - creates a story node and defines the tree relationship between nodes
add_child - adds a child node to a node
traverse - executes the tree traversal
print_story_node - prints the text of a story module
add_moral_points - adds moral points from a node
add_story_items - adds story item points from a node

Author: Michelle Burroughs
Date 12/19/21
"""

from Substories import *

class TreeNode:
    def __init__(self, story_piece, option_text=None, moral_points=None, story_items=None):
        self.story_piece = story_piece
        self.choices = []
        self.option_text = option_text
        self.moral_points = moral_points
        self.story_items = story_items

    def add_child(self, child_text):
        self.choices.append(child_text)

    def traverse(self):

        story_node = self

        chapter = 1  # chapter local variable initialized
        tmp = 0  # total moral points local variable initialized
        tip = 0  # total item points local variable initialized

        print(story_node.print_story_node(chapter))  # print story root

        # while node has at least one child, additional chapters are executed
        while story_node.choices:

            if len(story_node.choices) == 1:  # if node only has one child, story is executed w/o user choice
                choice = 1
                chosen_index = int(choice) - 1
                chosen_child = story_node.choices[chosen_index]
                chapter += 1
                story_node = chosen_child
                print(story_node.print_story_node(chapter))
            else:  # user chooses child from node
                optiona = story_node.option_text[0]
                optionb = story_node.option_text[1]
                print("Choose '{}' by entering 1 or '{}' by entering 2".format(optiona, optionb))
                choice = input("Enter 1 or 2 to continue the story: ")
                if choice not in ["1", "2"]:  # if user enters outside of "1" or "2"
                    print("Not a valid choice, choose again")
                else:
                    chosen_index = int(choice) - 1
                    chosen_child = story_node.choices[chosen_index]
                    chapter += 1
                    story_node = chosen_child
                    print(story_node.print_story_node(chapter))
                    tmp = story_node.add_moral_points(tmp, chosen_index)
                    tip = story_node.add_story_items(tip)

        return tmp, tip

    def print_story_node(self, chapter):
        print()
        print("Chapter: {}".format(chapter))
        print(self.story_piece)
        print()

    def add_moral_points(self, tmp, chosen_index):
        if self.moral_points is not None:
            tmp += self.moral_points[chosen_index]
        return tmp

    def add_story_items(self, tip):
        if self.story_items is not None:
            tip += story_items[self.story_items]
        return tip




