from scraper import nlp

txt = nlp.makeTextBlob('cat cat cat dog dog monkey')
txt = txt.tags

txt2 = nlp.makeTextBlob('The quick brown fox jumped over the lazy dog')
txt2 = txt2.tags

def test_fmtNouns():
    assert nlp.fmtNouns(('cat', 1)) == ('cat', 'cats', 1)

def test_commonNouns_one():
    cmnNouns = nlp.commonNouns(txt)

    assert len(cmnNouns) == 3
    assert ('cat', 'cats', 3) in cmnNouns
    assert nlp.fmtNouns(('cat', 3)) in cmnNouns
    assert cmnNouns == [nlp.fmtNouns(('cat', 3)), ('dog', 'dogs', 2), ('monkey', 'monkeys', 1)]

def test_commonNouns_two():
    cmnNouns = nlp.commonNouns(txt2)

    # known bug that "brown" comes in as a noun
    assert ('fox', 'foxes', 1) in cmnNouns
    assert nlp.fmtNouns(('fox', 1)) in cmnNouns
    assert nlp.fmtNouns(('dog', 1)) in cmnNouns

def test_getNames_one():
    assert len(nlp.getNames('The quick brown fox jumped over the lazy dog')) == 0
    assert len(nlp.getNames('cat cat dog dog')) == 0

def test_commonAdj_one():
    assert len(nlp.commonAdj(txt)) == 0

# Really bums me out brown is not getting registered as an adjective
# Luckily this error will translate into the stories reading a bit more nonsensical
# It's out of the scope of this to improve the ease of using natural language
# processing libraries
def test_commonAdj_two():
    adj = nlp.commonAdj(txt2)
    assert ('quick', 1) in adj
    assert ('lazy', 1) in adj
