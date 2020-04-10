from conversationgraph import ConversationGraph, Corpus
import random

print("Hello World")

graph = ConversationGraph("conversations-test.json")
print(graph.corpuses[0].tag)

input_string: str = ""

# TODO: obtain input string
# input_string = inputStringObtainer()

mostFittingTag: str = ""

# TODO: obtain mostFittingTag based on input string
# mostFittingTag = neuralNetworkAnalysis(input_string)

tag: Corpus

# TODO: obtain corpus based on tags probabilities map and searcher result
# tag = graph.searchTagToReturn(mostFittingTag)

textToPrint: str = random.choice(tag.responses)

print(textToPrint)




