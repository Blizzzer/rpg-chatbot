from typing import List

import spacy

from model import Corpus
from model import NeuralNetworkTrainingDTO


class Preprocessor:

    def __init__(self,
                 corpuses : List[Corpus]) -> None:
        super().__init__()
        self.corpuses = corpuses
        self.skipped_characters = [',', '?', '.', '\'', ':', ';']

    def prepare_nn_entries(self):
        neural_network_dtos = []
        for corpus in self.corpuses:
            if corpus.tag == 'UNKNOWN' or corpus.tag == 'ROOT_TAG':
                continue
            neural_network_dtos.append(
                NeuralNetworkTrainingDTO(corpus.tag, [self.lemmatize_expression(pat) for pat in corpus.patterns]))
        return neural_network_dtos

    def lemmatize_all_patterns(self):
        patterns = [c.patterns for c in self.corpuses]
        lemmas = []
        for sentences in patterns:
            for s in sentences:
                lemmas.append(self.lemmatize_expression(s))
        flat_lemmas = [item for sublist in lemmas for item in sublist]
        return list(set(flat_lemmas))

    def lemmatize_expression(self, line: str):
        nlp = spacy.load('en')
        doc = nlp(line)
        lemmas = []
        for token in doc:
            lemma = token.lemma_
            if lemma not in lemmas:
                lemmas.append(lemma)
        return list(set(lemmas) - set(self.skipped_characters))
