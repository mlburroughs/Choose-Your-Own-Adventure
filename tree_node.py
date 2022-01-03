"""
tree_node.py

Project Title: Choose Your Own Adventure
Description: This file defines the node and tree data structure relationships
between story modules using user input

Author: Michelle Burroughs
Date 12/19/21
"""

from substories import story_items
import typing


class TreeNode:
    """Provides the tree structure that allows each story module to be
    encapsulated into a node structure, defines the relationship between nodes,
    and executes the traversal of the choose your adventure story."""

    def __init__(self, story_piece, option_text=None,
                 moral_points: typing.Tuple[int, int] = None, story_items=None):
        """creates a story node and defines the tree relationship between nodes

        Args:
        story_piece (string): story text attached to self
        moral_points (2-tuple): value attached to respective story modules
        children, used to calculate ending
        story_items (dict): each item corresponds to a value used to calculate
        ending
        """
        self.story_piece = story_piece
        self.choices = []
        self.option_text = option_text
        self.moral_points = moral_points
        self.story_items = story_items

    def add_child(self, child_text):
        """adds a child node to a node

        Args:
        child_text (TreeNode): story module to be added as a child of self
        """
        self.choices.append(child_text)

    def traverse(self):
        """Executes the tree traversal."""

        story_node = self
        chapter = 1  # chapter local variable initialized
        tmp = 0  # total moral points local variable initialized
        tip = 0  # total item points local variable initialized

        story_node.print_story_node(chapter)  # print story root

        # while node has at least one child, additional chapters are executed
        while story_node.choices:
            # if node only has one child, story is executed w/o user choice
            if len(story_node.choices) == 1:
                choice = 1
                chosen_index = int(choice) - 1
                chosen_child = story_node.choices[chosen_index]
                chapter += 1
                story_node = chosen_child
                story_node.print_story_node(chapter)
            else:  # user chooses child from node
                option_a = story_node.option_text[0]
                option_b = story_node.option_text[1]
                print("Choose '{}' by entering 1 or '{}' by entering 2".format(
                        option_a, option_b))
                choice = input("Enter 1 or 2 to continue the story: ")
                # if user enters outside of "1" or "2"
                if choice not in ["1", "2"]:
                    print("Not a valid choice, choose again")
                else:
                    chosen_index = int(choice) - 1
                    chosen_child = story_node.choices[chosen_index]
                    chapter += 1
                    story_node = chosen_child
                    story_node.print_story_node(chapter)
                    tmp = story_node.add_moral_points(tmp, chosen_index)
                    tip = story_node.add_story_items(tip)

        return tmp, tip

    def print_story_node(self, chapter):
        """prints the text of a story module

        Args:
        chapter (int): chapter number that corresponds with story module
        """
        print()
        print("Chapter: {}".format(chapter))
        print(self.story_piece)
        print()

    def add_moral_points(self, tmp, chosen_index):
        """adds moral points from a node

        Args:
        tmp (int): total moral points computed at each story module if
        applicable chosen_index (int): index, 0 or 1, based on user input
        """
        if self.moral_points is not None:
            tmp += self.moral_points[chosen_index]
        return tmp

    def add_story_items(self, tip):
        """adds story item points from a node

        Args:
        tip (int): total item points computed at each story module if applicable
        """
        if self.story_items is not None:
            tip += story_items[self.story_items]
        return tip
