def does_name_exist(first_names, last_names, full_name):
    for f_name in first_names:
        for l_name in last_names:
            if full_name.startswith(f_name):
                if full_name.endswith(l_name):
                    return True
                continue
            continue
    return False
