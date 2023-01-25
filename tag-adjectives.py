"""
Tags adjectives and adverbs in a text file and saves the result as an html file.
code adapted from https://towardsdatascience.com/visualizing-part-of-speech-tags-with-nltk-and-spacy-42056fcd777e
"""

import spacy
from spacy import displacy

# read article
with open('article.txt') as f:
    text = f.read()

# load spacy model
nlp = spacy.load("en_core_web_sm")
doc = nlp(text)

# entities to be tagged
ents = []

# parts of speech we care about
pos_tags = ["ADJ", "ADV"]

# loop through toekns
for token in doc:
    # if the token is an adjective or adverb, add it to the list of entities
    if token.pos_ in pos_tags:
        ents.append({"start" : token.idx, 
                    "end" : token.idx + len(token), 
                    "label" : token.pos_})

# create doc object
doc = {"text" : text, "ents" : ents}

# create options for displacy
colors = {
            "ADJ" : "lime",
            "ADV" : "orange"
            }
options = {"ents" : pos_tags, "colors" : colors}
html = displacy.render(doc, 
                style = "ent", 
                options = options, 
                manual = True,
                )

# save html file
with open(f"tagged-article.html", "w") as f:
    f.write(html)