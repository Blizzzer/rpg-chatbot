from conversationgraph import ConversationGraph, Corpus
import random

graph = ConversationGraph("conversations-test.json")
print(graph.corpuses[0].tag)

input_string: str = ""

# TODO: obtain input string
# input_string = inputStringObtainer()

mostFittingTag: str = ""

# TODO: obtain mostFittingTag based on input string
# mostFittingTag = neuralNetworkAnalysis(input_string)

tag: Corpus

tag = graph.get_corpus_to_respond(mostFittingTag)

# need to check if it is working - "reference problem"
graph.close_corresponding_tags(tag)

tag.isAchieved = True

textToPrint: str = random.choice(tag.responses)

print(textToPrint)




