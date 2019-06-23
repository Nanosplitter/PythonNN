import random
#from UTTTNN import Neural_Network as NN

class Player:
    num_inputs = 163
    num_outputs = 81
    hidden_layer_sizes = [8, 8, 16, 16, 8]
    def __init__(self, randomPlayer):
        #if not randomPlayer:
         #   self.nn = NN(num_inputs, num_outputs, hidden_layer_sizes)
        self.randomPlayer = randomPlayer
    def makeMove(self, board, validMoves):
#         print("Valid Moves:", validMoves)
        if self.randomPlayer:
            return random.choice(validMoves)

    #def finishGame(GameRes, playerNum):
        #self.nn.backpropogate(reward, 0.1)
