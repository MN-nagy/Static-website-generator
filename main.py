def verify_tsp(paths, final_dist, actual_path):
    for city in actual_path:
        sum_distances = 0
        for dist in paths[city]:
            sum_distances += dist
        if sum_distances < final_dist:
            return True
    return False
