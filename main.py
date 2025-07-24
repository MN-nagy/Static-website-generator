def get_avg_brand_followers(all_handles: list, brand_name: str) -> int:
    b_count = 0
    for handle in all_handles:
        for b_name in handle:
            if brand_name in b_name:
                b_count += 1
    return b_count / len(all_handles)
