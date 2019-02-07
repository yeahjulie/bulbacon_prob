from numpy import random

def run_test(initial_pos, n_iter=1000):

    successes = 0

    for iter in range(n_iter):
        pos_x = initial_pos[0]
        pos_y = initial_pos[1]
        for step in range(5):
            u1 = random.random()
            u2 = random.random()
            if u1 < 0.2:
                pos_y -= 1
            elif (u1 >= 0.2) & (u1 < 0.5):
                pos_y += 1
            if u2 < 0.2:
                pos_x -= 1
            elif (u2 >= 0.2) & (u2 < 0.6):
                pos_x += 1
        if (pos_x, pos_y) == initial_pos:
            successes += 1
    print('Probability of staying in the same cell = %.2f' % (successes / n_iter))

run_test((0, 0), n_iter=1000000)
