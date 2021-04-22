"""
SubStories.py
Description: This file includes all the sub story modules for Main_Story.py

Author: Michelle Burroughs
"""
# Text of each module
text1 = "On a dark swampy night at the end of a long weekend filled with the usual tourist adventures of Bourbon St.,\""\
        "alligator show and tells, and delicious creole cuisine, you decide to venture into the most famous cemetary \""\
        "of the south: Saint Louis #1. Out of child-like mischief and the thrill of possibly having a real supernatural \""\
        "encounter you enter the cemetery thirty minutes before closing and camp between two narrow vaults heavily \""\
        "decorated with overgrown foliage. Your heart can't stop beating but as you remain still a guard passes over \"" \
        "you without an inkling of suspicion. Fifteen minutes later you venture back onto the path just as the sun \""\
        "set transitions into a hazy darkness. To your right, you see an illuminated bronze panel that seems to grow \"" \
        "brighter the closer you step. But to your left, you hear faint whisperings of what seems to be a \""\"
        "little girl speaking french. Choose your first step wisely."\

text2 = "As you draw closer to bronze plaque, you see an older gentlemen arguing. Unsure if it's your already \"" \
         "vulneraable imagination stemming from possible dehydration

text3 =

text4 =
text5 =
text6 =
text7 =
text8 =
text9 =
text10 =
text11 =
text12 =
text13 =
text14 =
text15 =

# Best Ending
ending1 = "As you start to feel that exhaustion might overpower you imminently, you suddenly feel a rush of energy \""\
    "as the sun begins its ascent. 'It's over,' you say to yourself repeatedly as you eye the front gate. As you \""\
    "towards freedom, you see many others you encountered join you in escaping the cemetery. You hear the faint \""\
    "sounds of a jazz quartet, the unshackling of iron chains, and the gigglings of young children. This final \""\
    "walk has become a parade of sort, with you leading the spirits to wherever they desire to reside. For youself, \""\
    "a much needed batch of warm, filling beignets and black coffee is your sort of heaven this morning."

# Neutral Ending
ending2 = "As daybreak approaches, you see the main gate 15 yards away and sprint right away. At the corner \""\
    "of your eye you see various figures such as (insert goodies) despondantly wave goodbye as if you have failed \""\
    " to help them conquer the malicious forces that bind them eternally to this one block prison. In your heart, \""\
    " you know you could have done more to help these trapped souls, but you are grateful that your journey through \""\
    "through the cemetery is over. You quickly exit the main gate, spooking the morning-shift guard on your \""\
    "way out. In freedom, your mind already starts to forget about your encounters, as if the cemetery is \""\
    ".format()


# Worst Ending
ending3 = "Oh no, as you frantically head towards the main gate at daybreak, an omnious figure pulls you toward an open \""\
    "an open vault. Scratching your fingernails to the stump as it drags you 20 ft along the cobble stone \""\
    "path, you realize that this cemetery will next let you leave. Crammed into the tiny above ground vault, \""\
    "the apparition quickly but meticulously bricks and mortors the opening at your feet. As the burning sun \""\
    "transforms your burial chamber into an oven, all you can think of is 'I hope I don't get the shaft'

# Each Module corresponds to a text to print, a choice on the next path, and moral points
modules = {1: (text1, choice, mp), 2: (text2, choice, mp), 3: (text3, choice, mp), 4: (text4, choice mp),
           5: (text5, choice, mp), 6: (text6, choice, mp), 7: (text7, choice, mp)}

# Endings will be based on combination of moral points and items collected
endings = [ending1, ending2, ending3]

# Path from each choice
path = {1: (2,3), 2: (4,5), 3: (6,7), 4: (8,9), 5: (10, 11), 6: (12, 13), 7: (14, 15)}

# Items that user can collect which have an assigned value to success
items = {'voodoo doll': 1, 'sugar bowl': -4, 'judge hammer': -4, 'key': 4, 'beads': 1, 'mask': 3, 'ax': 3}