# code adapted from https://towardsdatascience.com/visualizing-part-of-speech-tags-with-nltk-and-spacy-42056fcd777e
import spacy
from spacy import displacy
import nltk
from nltk.tokenize import TreebankWordTokenizer as twt


# Load English tokenizer, tagger, parser and NER
nlp = spacy.load("en_core_web_sm")

# read article
with open('hindutva-pop.txt') as f:
    text = f.read()

def visualize_pos(text):
    pos_tags = ["ADJ", "ADV"]
    
    # Tokenize text and pos tag each token
    tokens = twt().tokenize(text)
    tags = nltk.pos_tag(tokens, tagset = "universal")

    # Get start and end index (span) for each token
    span_generator = twt().span_tokenize(text)
    spans = [span for span in span_generator]

    # Create dictionary with start index, end index, 
    # pos_tag for each token
    ents = []
    for tag, span in zip(tags, spans):
        if tag[1] in pos_tags:
            ents.append({"start" : span[0], 
                         "end" : span[1], 
                         "label" : tag[1] })

    doc = {"text" : text, "ents" : ents}

    colors = {
              "ADJ" : "lime",
              "ADV" : "orange"
              }
    
    options = {"ents" : pos_tags, "colors" : colors}
    
    return displacy.render(doc, 
                    style = "ent", 
                    options = options, 
                    manual = True,
                   )


html = visualize_pos(text)
with open(f"tagged.html", "w") as f:
    f.write(html)