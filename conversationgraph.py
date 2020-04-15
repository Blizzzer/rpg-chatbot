from model import Corpus
from reader import InputStreamReader


class ConversationGraph(InputStreamReader):

    def __init__(self):
        super().__init__("conversations-test.json")
        self.parse_json()

    def get_by_tag(self, tag: str) -> Corpus:
        for x in self.corpuses:
            if x.tag == tag:
                break
        else:
            x = None
        return x

    def check_if_is_achieved(self, tag: str) -> bool:
        for requirement in self.get_by_tag(tag).tagsToAchieveBefore:
            if not self.get_by_tag(requirement).isAchieved:
                return False
        return True

    def get_corpus_to_respond(self, tag: str) -> Corpus:
        corpus: Corpus = self.get_by_tag(tag)

        if self.check_if_is_achieved(tag) and not corpus.isClosed:
            return corpus
        else:
            return self.get_corpus_to_respond(corpus.redirectTo)

    def close_corresponding_tags(self, corpus: Corpus):
        for tag in corpus.tagsToCloseWhenDone:
            self.get_by_tag(tag).isClosed = True
