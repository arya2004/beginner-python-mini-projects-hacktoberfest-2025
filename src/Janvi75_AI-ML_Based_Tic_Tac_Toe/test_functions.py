# level1-utils/janvi75/test_functions.py

from functions import sigmoid, relu, tanh, dot_product, cosine_similarity
from functions import l1_normalization, l2_normalization, min_max_normalization
from functions import greedy_move

def run_tests():
    print("Sigmoid(0.5):", sigmoid(0.5))
    print("ReLU(-2):", relu(-2))
    print("Tanh(1):", tanh(1))

    v1 = [1, 2, 3]
    v2 = [4, 5, 6]
    print("Dot product:", dot_product(v1, v2))
    print("Cosine similarity:", cosine_similarity(v1, v2))

    print("L1 Normalization:", l1_normalization(v1))
    print("L2 Normalization:", l2_normalization(v1))
    print("Min-Max Normalization:", min_max_normalization(v1))

    board = ["X", "O", "X", " ", "O", " ", " ", " ", " "]
    move = greedy_move(board, "X")
    print("Greedy move for X:", move)

if __name__ == "__main__":
    run_tests()
