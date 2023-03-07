import pandas as pd

# create example texts
text = ["Yes. I can't believe he would do this knowing what I'm going through with the divorce!", 
        "Yeah, well, my big brother once hit me in the head with the claw end of a hammer.",
        "What a jerk! If I was there I could've helped you, since I'm in my second year of medical school.",
        "Ha-ha.  Yeah, no doubt.  I was just a kid and kind of indestructible.  We fought a lot.",
        "That's very unfortunate. I hope my two kids never fight that way. Are you on good terms with your brother now?", 
        "We are great friends now.  I don't get to see him so much since I'm on tour with my band.", 
        "I'm happy to hear that, I hope you get to seem him soon. Maybe he can come to see one of your shows.", 
        "Yeah, he's been to a few.  I was hoping we could do X-mas with the whole family.  Maybe next year.",
        "I don't know how Christmas is gonna go with my family this year either... it's hard to be divorced when there's two kids mixed in.", 
        "Divorce is the WORST.  I, too, am divorced.  Worst experience of my life.  I don't speak to my ex.", 
        "I'm sorry to hear that. It's very hard. I'm just ready to be done with the process.", 
        "It will get better over time.  Focus on your kids if you can.  It's gotta be rough.  Oh and get another partner!"]

# convert to DataFrame of pandas
df = pd.DataFrame(text, columns=['text'])

# save to csv
df.to_csv('example.csv', index=False)