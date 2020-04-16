from conversationgraph import ConversationGraph
from neuralnetwork import NeuralNetwork
from preprocessing import Preprocessor

conversation_graph = ConversationGraph()
lemmatizer = Preprocessor(conversation_graph.corpuses)
neural_network = NeuralNetwork(8, conversation_graph)

neural_network.train(
    lemmatizer.prepare_nn_entries(),
    lemmatizer.lemmatize_all_patterns())

print("Welcome in our rpg chat bot npc !!!")

while True:
    expression = input("Player: ")
    input_lemmatize = lemmatizer.lemmatize_expression(expression)
    neural_network.predict(input_lemmatize)
