def verify_tsp(paths, final_dist, actual_path):
    total = 0
    for i in range(len(actual_path) - 1):
        total += paths[actual_path[i]][actual_path[i + 1]]
    return total < final_dist
