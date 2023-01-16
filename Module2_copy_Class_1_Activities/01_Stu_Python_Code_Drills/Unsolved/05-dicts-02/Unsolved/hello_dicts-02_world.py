# Use the `from` keyword to import the `shows` dictionary from the `show_data.py` file
from show_data import shows


# QUESTION 1: Is the Walking Dead still running?
show = shows["genre"]["drama"]["the_walking_dead"]["still_running"]
print(f"It is {show} that the show The Walking Dead still running.")

# QUESTION 2: Who hosts the Daily Show (talk)?
show_host = shows["genre"]["talk"]["the_daily_show"]["host"] 
print(f"The host of the Daily Show is {show_host}")

# QUESTION 3: Who does Will Arnett play in Arrested Development (comedy)
character_comic = shows["genre"]["comedy"]["arrested_development"]["cast"][2]["character"]
print(f"Actor Will Arnett play the character of {character_comic} in the comedy Arrested Development.")

# QUESTION 4: Who does Peter Dinklage play in Game of Thrones (drama)?
character_drama = shows["genre"]["drama"]["game_of_thrones"]["cast"][1]["character"]
print(f"Actor Peter Dinklage play the character of {character_drama} in the drama Game of Thrones.")

# QUESTION 5: Who plays Dexter in Dexter (drama) and who plays Dexter in Dexter's Lab (kids)?
# HINT: You can print multiple items at once by using a comma like this: print(thing1, thing2)
drama = shows["genre"]["drama"]["dexter"]["cast"][0]["actor"]
kids = shows["genre"]["kids"]["dexters_lab"]["cast"][0]["actor"]
print(f"In the TV drama Dexter, actor {drama} plays the main character name Dexter; while in kids TV Dexter's Lab, actress {kids} plays the main character also name Dexter.")

# QUESTION 6: Who are the main characters of the Office (comedy) (not the actors, but the actual character names)?
character_office = shows["genre"]["comedy"]["the_office"]["cast"]
#print(f"The main chracters in the comedy The office are {character_office}.")
"""keep working on this one"""
counter = 0
for p in character_office:
    #chtr = p["actor"]
    d = p["character"]
    counter = counter + 1
    #print(f"Actor {chtr} plays {d}")
    print(f"{counter}. The main character in the TV comedy The Office is {d}")

# QUESTION 7: List the main cast of Dexter (drama) (the actors, not the characters)
drama = shows["genre"]["drama"]["dexter"]["cast"]
for p in drama:
    d = p["actor"]
    counter = counter + 1 #"this counter needs work"
    print(f"{counter}. The main cast in TV drama Dexter is {d}")


# QUESTION : List the American Idol Judges
reality = shows["genre"]["reality"]["american_idol"]["judges"]
for p in reality:
    print(f"{p} is a judge in the TV reality The American Idol.")



# QUESTION 9: What are the show names of the Impractical Jokers (comedy)
# Hint: You will need to use a loop for this one. You may not simply log the entire list, but must log each name individually
p = shows["genre"]["comedy"]["impractical_jokers"]["cast"]
for d in p:
    shw = d["showName"]
    actor = d["actor"]
    print(f"Actor {actor} show name in TV comedy Impractical Jokers is: {shw}.")

