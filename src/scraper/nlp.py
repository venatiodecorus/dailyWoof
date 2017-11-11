from nltk import FreqDist, ne_chunk, pos_tag, word_tokenize, sent_tokenize
from textblob import TextBlob, Word
from textblob.taggers import NLTKTagger

import numpy

## Convert all the nouns into their singular form and return a list
def commonNouns(tagText):
    words = []
    for (word, tag) in tagText:
        if tag not in ['NN', 'NNS']:
            continue
        elif tag == 'NNS':
            word = Word(word).singularize()
        words.append(word.lower())

    return list(map(fmtNouns, FreqDist(words).most_common()))

## Formats tuples of nouns like (dog, 2) => (dog, dogs, 2)
def fmtNouns(tpl):
    return (
        tpl[0],
        Word(tpl[0]).pluralize(),
        tpl[1]
    )

def commonAdj(tagTxt):
    adjectives = [word.lower() for (word, pos) in tagTxt if pos == 'JJ']
    return FreqDist(adjectives).most_common()

def getNames(text):
    pNouns = []
    for sent in sent_tokenize(text):
        for chunk in ne_chunk(pos_tag(word_tokenize(sent))):
            if hasattr(chunk, 'label') and chunk.label() == 'PERSON':
                pNouns += chunk.leaves()

    return list(set([x[0] for x in pNouns]))

# Wrapped this to help with testing
def makeTextBlob(txt):
    return TextBlob(txt, pos_tagger = NLTKTagger())

# Main function, returns common nouns, adjectives and names
def processTxt(inputText):
    txt = makeTextBlob(inputText)
    tagTxt = txt.tags

    return {
        'commonNouns': commonNouns(tagTxt),
        'commonAdj': commonAdj(tagTxt),
        'names': getNames(inputText)
    }
