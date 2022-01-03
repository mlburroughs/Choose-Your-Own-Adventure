"""
main_story.py

Project Title: Choose Your Own Adventure
Description: This file executes the Choose Your Own Adventure story using an
original story created by the author. The text content is found in substories.py
and the tree structure is found in tree_node.py.

Author: Michelle Burroughs
Date: 4/25/2021
"""

from substories import texts, options, endings, mp
from tree_node import TreeNode


class MainStory:
    """Defines the tree structure and executes interactive story."""

    def endings(total_moral_points, total_items):
        """Computes and prints ending based on items total (self.items_total)
        and moral points (self.moral_points).
        """

        total_ending = total_moral_points + total_items
        if total_ending >= 5:
            result = endings[0]
        elif total_ending <= 5 and total_ending > -5:
            result = endings[1]
        else:
            result = endings[2]
        print("Conclusion:" + "\n" + result + "\n" + "Moral Points: "
              + str(total_ending))

    story_root = TreeNode(texts[0], options[0])
    text2 = TreeNode(texts[1], options[1], mp[0])
    text3 = TreeNode(texts[2], options[2], mp[1])
    text4 = TreeNode(texts[3], options[3], mp[2])
    text5 = TreeNode(texts[4], options[4], mp[3])
    text6 = TreeNode(texts[5], options[5], mp[4])
    text7 = TreeNode(texts[6], options[6], mp[5])
    text8 = TreeNode(texts[7], story_items='judge hammer')
    text9 = TreeNode(texts[8], story_items='beads')
    text10 = TreeNode(texts[9])
    text11 = TreeNode(texts[10], story_items='axe trophy')
    text12 = TreeNode(texts[11], story_items='statue')
    text13 = TreeNode(texts[12])
    text14 = TreeNode(texts[13], story_items='silver spoon')
    text15 = TreeNode(texts[14])

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

