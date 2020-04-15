from conversationgraph import ConversationGraph
from model import NeuralNetworkTrainingDTO
import spacy


class Lemmatizer:

    def __init__(self) -> None:
        super().__init__()
        self.skipped_characters = [',', '?', '.', '\'', ':', ';']
        self.corpuses = ConversationGraph().corpuses

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


res = Lemmatizer().prepare_nn_entries()
