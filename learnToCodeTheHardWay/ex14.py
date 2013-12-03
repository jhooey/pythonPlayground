from sys import argv

script, user_name = argv
prompt = '>'

print ("Hi {}, I'm the {} script.".format(user_name, script))
print ("I'd like to ask you a few questions.")
print ("{}, what kind of sword are you carrying?".format(user_name))
sword = raw_input(prompt)

print ("Where do you live {}?".format(user_name))
lives = raw_input(prompt)

print ("What kind of quest are you on?")
quest = raw_input(prompt)

print ("""
Alright, so you said you are carrying a {}.
You live in {}. Pretty sure that's not a real place.
and you are on a {} quest. Good luck!
""".format(sword, lives, quest))
