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

    def getByTag(self, tag: str) -> Corpus:
        for x in self.corpuses:
            if x.tag == tag:
                break
        else:
            x = None
        return x
