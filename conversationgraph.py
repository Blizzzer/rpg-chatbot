import random

from model import Corpus
from reader import ConversationGraphJsonReader


class ConversationGraph(ConversationGraphJsonReader):

    def __init__(self, path: str):
        super().__init__(path)
        self.parse_json()

    def get_by_tag(self, tag: str) -> Corpus:
        for x in self.corpuses:
            if x.tag == tag:
                break
        else:
            x = None
        return x

    def is_available_to_respond(self, tag: str) -> bool:
        return self.check_if_is_achieved(tag) and not self.get_by_tag(tag).isClosed

    def check_if_is_achieved(self, tag: str) -> bool:
        for requirement in self.get_by_tag(tag).tagsToAchieveBefore:
            if not self.get_by_tag(requirement).isAchieved:
                return False
        return True

    def get_corpus_to_respond(self, tag: str) -> Corpus:
        corpus: Corpus = self.get_by_tag(tag)

        if self.is_available_to_respond(tag):
            return corpus
        else:
            if len(corpus.redirectTo) == 1:
                return self.get_corpus_to_respond(corpus.redirectTo[0])
            else:
                for corpus_to_go in corpus.redirectTo:
                    if self.is_available_to_respond(corpus_to_go):
                        self.get_by_tag(corpus_to_go)
                return self.get_corpus_to_respond(random.choice(corpus.redirectTo))

    def close_corresponding_tags(self, corpus: Corpus):
        for tag in corpus.tagsToCloseWhenDone:
            self.get_by_tag(tag).isClosed = True

    def get_tag_by_response(self, response: str):
        for corpus in self.corpuses:
            if response in corpus.responses:
                return corpus.tag
