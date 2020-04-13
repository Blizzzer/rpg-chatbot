import json
from typing import List


class Corpus:
    def __init__(self,
                 tag: str,
                 keywords: List[str],
                 tagsToAchieveBefore: List[str],
                 nextTags: List[str],
                 tagsToCloseWhenDone: List[str],
                 isClosed: bool,
                 isAchieved: bool,
                 redirectTo: str,
                 patterns: List[str],
                 responses: List[str]):
        self.tag = tag
        self.keywords = keywords
        self.tagsToAchieveBefore = tagsToAchieveBefore
        self.nextTags = nextTags
        self.tagsToCloseWhenDone = tagsToCloseWhenDone
        self.isClosed = isClosed
        self.isAchieved = isAchieved
        self.redirectTo = redirectTo
        self.patterns = patterns
        self.responses = responses


class ConversationGraph:
    def __init__(self, path: str):
        with open(path) as json_file:
            data = json.load(json_file)
            self.corpuses: List[Corpus] = []
            for tag in data:
                self.corpuses.append(
                    Corpus(
                        tag["tag"],
                        tag["keywords"],
                        tag["tagsToAchieveBefore"],
                        tag["nextTags"],
                        tag["tagsToCloseWhenDone"],
                        tag["isClosed"],
                        tag["isAchieved"],
                        tag["redirectTo"],
                        tag["patterns"],
                        tag["responses"]
                    )
                )

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
