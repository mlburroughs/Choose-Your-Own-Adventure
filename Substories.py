"""
SubStories.py
Description: This file includes all the sub story modules for use in Main_Story.py

path: dictionary containing the logic between sub modules
text: tuple that contains all text sub files
endings: tuple that contains all text endings
options: tuple containing a sub tuple for path values that contain 2 options
mp: tuple containing moral points corresponding to options
storyitems: dictionary containing key:value pairs of items found in the text.

Author: Michelle Burroughs
Date: 4/25/2021
"""

# Text and Option (if applicable) of each module
text1 = "Chapter 1" + "\n" + """On a dark swampy night at the end of a long weekend filled with the usual tourist 
adventures of Bourbon St., alligator show and tells, and delicious creole cuisine, you decide to venture into the most 
famous cemetery of the south: Saint Louis #1. Out of child-like mischief and the thrill of possibly having a real 
supernatural encounter you enter the cemetery thirty minutes before closing and camp between two narrow vaults heavily 
decorated with overgrown foliage. Your heart can't stop beating but as you remain still a guard passes over you without 
an inkling of suspicion. Fifteen minutes later you venture back onto the path just as the sun set transitions into a 
hazy darkness. To your right, you see an illuminated bronze panel that seems to grow brighter the closer you step. 
But to your left, you hear faint whisperings of what seems to be a little girl speaking french to a worn out doll in
18th century clothing. 

Choose your first step wisely."""

options1 = ["venturing towards the illuminated bronze panel", "approaching the little girl"]

text2 = """As you draw closer to bronze plaque, you see an older gentlemen arguing to himself. Unsure if it's your 
already vulnerable imagination stemming from a mixture of sugary hurricanes and possible dehydration, you see the
plague of Homer Adolph Plessy, a creole man who dared to sit on a whites-only railroad car. He ultimately lost his
US supreme court case due to segregation laws. You overhear the man rambling about railroad cars and when will we see
change. You try to tell him that this is now 2021 and he is free to go where he wishes, but he simply replies in a 
somber,yet serious tone: 'The past is never dead, it isn't even past.' He points toward where the bronze panel stood,
which has now openned into a stairwell descending into the earth. Unsure about diving into a possible water table,
you hear an upbeat jazz trumpet which seems much more light than where the gentleman points."""

options2 = ["entering into the mysterious portal of Homer Plessy", "following the jazz trumpet"]

text3 = """'Dors mon petit ange' or 'sleep my little angel' is what you overhear the fair-haired little girl say as she 
gently rocks her dilapitated but clearly 18th century doll. 'Oh please help mon pauvre bebe, she has the fever and I 
fear I might lose her too,' she says urgently to you. Startled, you reply 'She's just a doll, she can't..' You stop as 
you notice her yellow-tinged skin and an obvious discomfort. 'Did you die from yellow fever?, Where are your parents?' 
you demand as she starts to whimper and cry. 'I can't find maman and papa, I searched for so long, mon bebe is all I 
have left,' she replies. 'Can you help me?,' she inquires and you must make a choice: help her find her parents or 
continue to find something less-disease ridden to look at."""

options3 = ["helping the yellow-fever stricken girl", "continuing on your way"]

text4 = """As you enter the portal and descend the cobble-stone stairwell, you are instantly placed in the middle of 
Jackson Square in stark day-light. Wincing as your eyes slowly adjust to the bright surroundings, you see yourself
walking from just 10 hours prior on your way to brunch. Unsure of what you are supposed to do, you follow yourself
through _ St. Not noticing the scene across the street before, you see a group of drunken male college students pouring
cheap drinks on a sun-weathered elderly homeless man. Do you confront the arrogant group of unsympathetic party-goers, 
or do you continue to follow yourself?"""

options4 = ["confronting the harassing party-goers", "ignoring the scene just witness and continue to follow yourself"]

text5 = """Ignoring the apparition and continuing on your way toward the trumpet, you feel an ominous warning.
Shaking off any discomfort, you tell yourself: 'The past isn't dead, of course it is,' you say to yourself as you bask
in the hypnotizing rhythms. As soon as you take down your guard, a stocky middle-aged man swiftly puts down his 
trumpet and picks up an axe. It is flight or fight time! Do you run between the opening you see between two vaults to 
right or confront the axeman and possibly lose your own life?"""

options5 = ["sprinting away from the murderous apparition", "confronting the threatening axeman and fight"]

text6 = """'Please stop crying, I can try to help you,' you say reassuringly. Instantly, her demeanor transforms from
nearly inconsolable and listless to carefree and energetic. She says 'Oh thank you! All the other ghosts around here
just tell me its hopeless, except Madame L. But, she won't help me unless I have someone tethered more strongly to 
this world - which you are! Will you please take me to the voodoo priestess's grave? It is only around the corner
past the bench? Unsure if a voodoo priestess might do, you ponder if this is the path that would help the sickly ghost
find her parents"""

options6 = ["following the girl to Madame L's grave", "asking the girl for a different, less black magic option"]

text7 = """'I'm sorry,' you say. 'I'm not sure there is anything I can do help', you say sheepishly as you plan
your exit away from this helpless ghost. Taking two steps backwards, you regret your inaction but feel immediately
lightened. Ducking past a few gothic vaults you notice an interesting plaque that captures your attention: 'Here lies
Delphine LaLaurie.' You are taken back to two nights ago on your haunted New Orleans tour with your over-the-top yet,
undoubtedly entertaining tour guide who took your group by the LaLaurie house of horrors. Mrs. LaLaurie, a wealthy 
slave owner apparently used to torture her slaves and even use the blood of dead slave babies as part of her beauty
regime. As soon as you turn around, a portly middle-aged woman stands right in front of you and asks in a sweet
southern drawl, 'Mon Cheri, will you ever be so kind and set me free?'"""

options7 = ["setting Madame LaLaurie free", "telling her off and trying to lock her further into her grave"]

text8 = """'Hey!, stop that!,' you say to the drunken idiots. They ignore you as expected as they head toward the
next bar but you pick up a beer car and chuck it in their direction. 'What is your problem bro?,' one of the guys asks,
turning around and confronting you. 'Where is your common decency? This man has done nothing to you,' you reply 
ready to start a brawl. 'Whatever,' the guy replies as he pushes you to the ground. Defeated and uncertain if this was
the right course of action, the homeless man places a __ in your hands. You look at it carefully while your surroundings
return to the gloomy darkness of the graveyard and hear the barely audible whisperings of a young girl."""

text9 = """Ignoring the idiotcracy you see, you continue to follow yourself. You think of that mouth-watering butter
pecan bread pudding a la mode you are about the enjoy at the brunch and your thoughts are carefree as a bird. 
Intoxicated by your daydream, you don't initially notice that instead of entering the restaurant at the end of your
stroll, you are entering a familiar cobblestone stairway."""

text10 = """Running clumsly at lightning pace toward the main gate, you trip on a distorted cobblestone only 8 feet 
from the axeman. Accepting that coming to this cemetery was an instant mistake, you resign to your seemingly, 
sealed fate. As the axeman's shadow from the moonlight looms over your head, a surge of adreneline takes over as you
get up and head towards your hiding spot between two tight vaults. 'I think I've had enough adventure for a lifetime,'
you say to yourself as you remain on-guard for any other threatening phantoms. Curled up in the fetal position, you
subconsciously rock yourself back and forth. You stay in this position for the remainder of the night until you see
the first hint of daybreak."""

text11 = """Your fight instinct takes over and as the Axeman swings towards your neck, you reach out and grab the axe
arm with two handles, causing the axeman to lose his balance for a moment. You use this opportunity to pull the axe
away from his hands and immediately you feel a sense of accomplishment over this evil. As you lift the axe for a blow
to this evil spirit, he mysteriously disolves into the fog that permeates the graveyard. 'What good is an axeman
without an axe,' you say to yourself as you continue your promenade with a new found feeling of empowerment."""

text12 = """As the spirit leads you by the hand to Madame L's resting place, you scold yourself for ignorance of who she
is beyond the few episodes of American Horror Story: Coven you watched a few years prior. As you reach your
destination the girl enthusiasticcally shouts out 'Madame, I finally found someone willing to participate in the ritual!
'Ritual?' Uhh I'm not sure if I can...' you try to articulate before Marie cuts you off. 'You want to help oui ou non?'
'Oui, yes!' you reply as you continue to work up the courage to overcome your own fears of the unknown. 'Ok, what do 
you have to offer me?,' she says. Opening the contents of your backpack you list the items found. 'I have an apple 
swiped from the hotel breakfast buffet, a french quarter map, a free T-shirt promoting a gentleman's club, oh and some 
pound cake i bought today,' You say unsure if any of the items would work, Marie snatches the pound cake and simply
states 'This will do.' The next moment Marie turns her back and speaks as if she is having a conversation to someone, 
but no one is there. A minute later, she emerges from what seems to be a trance-like state and proclaims that the
parents of the girl spirit were placed in Saint Louis Cemetery #2 and that the girl was not placed with her parents
when her time came due to a name error. 'Seraphine, ma fille, you will be able to leave this cemetery if and only if
this living creature has passed through this night with honor,' Marie says to the girl. 'Take this,' she says to you
as a statue of Saint Expedite is placed in your hand. As you examine the object both apparitions disappear and you are
again alone wondering along the graveyard."""

text13 = """'Uh, I'm not sure I want to get mixed up in any black magic,' looking away from the spirit as you 
cowardly reply to her suggestion. 'I understand I guess, all the others through the last 243 years have said that,'
she says. 'I just thought you were special...if you change your mind, please call me by my name -Seraphine LeBlanc,'
she says before disappearing into the mist. She begins to cry with shrieks similar to a kitten, you feel terrible.
Disappointed in yourself, you try to calm her down."""

text14 = """Oh no! By removing the loose stone on the north side of Madame LaLaurie's vault, """

text15 = """"'Aren't you that racist bitch who tortured slaves? Burn in hell,' you exclaim as she reveals her true 
nature. 'You don't know anything, they deserved everything they got. After being driven out New Orleans by those 
hypocrites, I came back and was welcomed with open arms. And I know I'm still welcomed in today's soceity,' she 
proudly states. 'That might be so, but the world is definitely better off without you,' as you walk away resisting 
the urge to continue on your tirade. As the night transitions into day, you slump down to review your night and if
you have done enough to make right in this city of the dead."""

#Endings
# Best Ending
ending1 = """As you start to feel that exhaustion might overpower you imminently, you suddenly feel a rush of energy
as the sun begins its ascent. 'It's over,' you say to yourself repeatedly as you eye the front gate. As you
towards freedom, you see many others you encountered join you in escaping the cemetery. You hear the faint
sounds of a jazz quartet, the unshackling of iron chains, and the gigglings of young children. This final
walk has become a parade of sort, with you leading the spirits to wherever they desire to reside. For yourself, 
a much needed batch of warm, filling beignets and black coffee is your sort of heaven this morning."""

# Neutral Ending
ending2 = """As daybreak approaches, you see the main gate 15 yards away and sprint right away. At the corner 
of your eye you see various figures such as {} despondently wave goodbye as if you have failed 
to help them conquer the malicious forces that bind them eternally to this one block prison. In your heart, 
you know you could have done more to help these trapped souls, but you are grateful that your journey through 
through the cemetery is over. You quickly exit the main gate, spooking the morning-shift guard on your 
way out. In freedom, your mind already starts to forget about your encounters, as if the cemetery is preventing 
you from maintaining any memories of your frightful excursion. By the time you make it to your hotel on Bourbon
Street, you forget everything and all you think about is getting a few hours of sleep before check-out."""

# Worst Ending
ending3 = """Oh no, as you frantically head towards the main gate at daybreak, an omnious figure pulls you toward
an open vault. Scratching your fingernails to the stump as it drags you 20 ft along the cobble stone 
path, you realize that this cemetery will next let you leave. Crammed into the tiny above ground vault, 
the apparition quickly but meticulously bricks and mortors the opening at your feet. As the burning sun 
transforms your burial chamber into an oven and you see your appendages dissolve into ash, all you can think of is 
'I hope I don't get the shaft...'"""


# Path logic
path = {1: (2, 3), 2: (4, 5), 3: (6, 7), 4: (8, 9), 5: (10, 11), 6: (12, 13), 7: (14, 15), 8: 3, 9: 4, 11: 3, 13: 7}

# Text
text = (text1, text2, text3, text4, text5, text6, text7, text8, text9, text10, text11, text12, text13, text14, text15)

# Options
options = (options1, options2, options3, options4, options5, options6, options7)

# Endings
endings = (ending1, ending2, ending3)

# Moral points
mp = ((0, 0), (2, 0), (4, -2), (5, -2), (-6, 7), (7, -1), (-7, 4))

# Items
storyitems = {'statue': 4, 'judge hammer': 3, 'key': 4, 'beads': -3,  ' axe ': 3}
