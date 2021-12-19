"""
Main_Story.py

Project Title: Choose Your Own Adventure
Description: This file executes the Choose Your Own Adventure story using an original story created
by the author. The text content is found in Substories.py and the tree structure is found in Tree_Node.py.

class functions:
endings() - computes and prints ending based on items total (self.items_total and moral points (self.moral_points)


Author: Michelle Burroughs
Date: 4/25/2021
12/19/2021 - Complete restructure of program used Tree Data Structure for simplification
"""

from Substories import *
from Tree_Node import *


class MainStory:

    def endings(total_moral_points, total_items):
        total_ending = total_moral_points + total_items
        if total_ending >= 5:
            result = endings[0]
        elif total_ending <= 5 and total_ending > -5:
            result = endings[1]
        else:
            result = endings[2]
        print("Conclusion:" + "\n" + result + "\n" + "Moral Points: " + str(total_ending))

    story_root = TreeNode(text1, options1)
    text2 = TreeNode(text2, options2, mp[0])
    text3 = TreeNode(text3, options3, mp[1])
    text4 = TreeNode(text4, options4, mp[2])
    text5 = TreeNode(text5, options5, mp[3])
    text6 = TreeNode(text6, options6, mp[4])
    text7 = TreeNode(text7, options7, mp[5])
    text8 = TreeNode(text8, story_items='judge hammer')
    text9 = TreeNode(text9, story_items='beads')
    text10 = TreeNode(text10)
    text11 = TreeNode(text11, story_items='axe trophy')
    text12 = TreeNode(text12, story_items='statue')
    text13 = TreeNode(text13)
    text14 = TreeNode(text14, story_items='silver spoon')
    text15 = TreeNode(text15)

    story_root.add_child(text2)
    story_root.add_child(text3)
    text2.add_child(text4)
    text2.add_child(text5)
    text3.add_child(text6)
    text3.add_child(text7)
    text4.add_child(text8)
    text4.add_child(text9)
    text5.add_child(text10)
    text5.add_child(text11)
    text6.add_child(text12)
    text6.add_child(text13)
    text7.add_child(text14)
    text7.add_child(text15)
    text8.add_child(text3)
    text9.add_child(text4)
    text11.add_child(text3)
    text13.add_child(text7)
    total_moral_points, total_items = story_root.traverse()

    endings(total_moral_points, total_items)

