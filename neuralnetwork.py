from typing import List
from model import NeuralNetworkTrainingDTO
import numpy as np
import tflearn


class NeuralNetwork:

    def __init__(self,
                 numberOfNeurons) -> None:
        super().__init__()
        self.model: tflearn.DNN
        self.numberOfNeurons = numberOfNeurons

    def predict(self,
                line: str):
        print("Hello World")

    def train(self,
              trainSet: List[NeuralNetworkTrainingDTO],
              inputLemmas: List[str]):
        training = []
        outputs = []
        for ts in trainSet:
            for tsl in ts.lemmas:
                entry = []
                for lemma in inputLemmas:
                    if lemma in tsl:
                        entry.append(1)
                    else:
                        entry.append(0)
                training.append(entry)
                outputs.append(ts.tag)

        classes = []
        for out in outputs:
            output = [0 for _ in range(len(set(outputs)))]
            for i, tag in enumerate(set(outputs)):
                if out == tag:
                    output[i] = 1
                    classes.append(output)
                    continue

        training = np.array(training)
        classes = np.array(classes)

        net = tflearn.input_data(shape=[None, len(training[0])])
        net = tflearn.fully_connected(net, self.numberOfNeurons)
        net = tflearn.fully_connected(net, self.numberOfNeurons)
        net = tflearn.fully_connected(net, len(classes[0]), activation="softmax")
        net = tflearn.regression(net)

        model = tflearn.DNN(net)

        model.fit(training, classes, n_epoch=1000, batch_size=8, show_metric=True)
