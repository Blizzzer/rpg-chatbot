from conversationgraph import ConversationGraph
import spacy

QUIT_CONDITION = "exit"


def lemmatize_patterns():
    patterns = [c.patterns for c in ConversationGraph("conversations-test.json").corpuses]
    lemmas = []
    for sentences in patterns:
        for s in sentences:
            lemmas.append(lemmatize_expression(s))
    flat_lemmas = [item for sublist in lemmas for item in sublist]
    unique_lemmas = []
    for lemma in flat_lemmas:
        if lemma not in unique_lemmas:
            unique_lemmas.append(lemma)
    return unique_lemmas


def lemmatize_expression(line: str):
    nlp = spacy.load('en')
    doc = nlp(line)
    lemmas = []
    for token in doc:
        lemma = token.lemma_
        if lemma not in lemmas:
            lemmas.append(lemma)
    return lemmas


def process_input(line: str):
    if line != QUIT_CONDITION:
        lemmatize_expression(line)
    else:
        exit()


for i in (lemmatize_patterns()):
    print(i)