def merge_two_groups(group1, group2):
    """
    合并group1和group2，举例：
    group1 = {
        ("2021-10-11", "APP"): {"uv": {"a", "c"}},
        ("2021-10-12", "APP"): {"uv": {"c", "d"}}
    }
    group2 = {
        ("2021-10-12", "APP"): {"uv": {"a", "c"}},
        ("2021-10-12", "FOOD"): {"uv": {"c", "d"}}
    }
    合并后：
    merge_group = {
        ('2021-10-11', 'APP'): {'uv': {'a', 'c'}},
        ('2021-10-12', 'APP'): {'uv': {'a', 'd', 'c'}},
        ('2021-10-12', 'FOOD'): {'uv': {'d', 'c'}}
    }
    """

    merge_dict = dict()
    for outer_key, outer_value in group1.items():
        for inner_key, inner_value in outer_value.items():
            if not merge_dict.get(outer_key):
                merge_dict[outer_key] = dict()
            merge_dict[outer_key][inner_key] = inner_value.union(group2.get(outer_key, dict()).get(inner_key, set()))
    for outer_key, outer_value in group2.items():
        for inner_key, inner_value in outer_value.items():
            if not merge_dict.get(outer_key):
                merge_dict[outer_key] = dict()
            merge_dict[outer_key][inner_key] = inner_value.union(group1.get(outer_key, dict()).get(inner_key, set()))
    return merge_dict


if __name__ == "__main__":
    groupa = {
        ("2021-10-11", "APP"): {"uv": {"a", "c"}}, ("2021-10-12", "APP"): {"uv": {"c", "d"}}
    }
    groupb = {
        ("2021-10-12", "APP"): {"uv": {"a", "c"}}, ("2021-10-12", "FOOD"): {"uv": {"c", "d"}}
    }
    print(merge_two_groups(groupa, groupb))
