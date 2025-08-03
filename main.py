def get_num_guesses(length):
    N = 26
    total_gusses = 0
    for i in range(1, length + 1):
        total_gusses += N**i
    return total_gusses
