import copy

# s1 = {'a', 'b', 'c', 'a'}
# print(s1)
# print(max(s1))
# s2 = {'a', 'b', 'd'}
# print(s1 - s2)  # 集合s1中包含s2中不包含的元素
# print(s1 | s2)
# print(s1 & s2)
# print(s1 ^ s2)  # 不同时包含于s1和s2的元素
#
# s1 = {"a", "b"}
# s2 = {"a", "c"}
# s3 = set()
# print(s1.union(s2).union(s3))
# print(s1)


def merge_two_unique_groups(group1, group2):
    """
    合并group1和group2，举例：
    group1 = {
        "2021-10-11": {"uv": ["a", "b"]}, "2021-10-12": {"uv": ["a", "c"]}
    }
    group2 = {
        "2021-10-11": {"uv": ["a", "c"]}, "2021-10-12": {"uv": ["c", "d"]}
    }
    合并后：
    merge_group = {
        "2021-10-11": {"uv": ["a", "b", "c"]}, "2021-10-12": {"uv": ["a", "c", "d"]}
    }
    """
    group1_key_set = set()
    for outer_key, outer_value in group1.items():
        for inner_key, inner_value in outer_value.items():
            group1_key_set.add(outer_key + "_" + inner_key)
    group2_key_set = set()
    for outer_key, outer_value in group2.items():
        for inner_key, inner_value in outer_value.items():
            group2_key_set.add(outer_key + "_" + inner_key)
    key_set = group1_key_set.union(group2_key_set)
    merge_dict = dict()
    for key in key_set:
        outer_key = key.split("_")[0]
        inner_key = key.split("_")[1]
        merge_dict[key] = group1.get(outer_key, dict()).get(inner_key, set()).union(
            group2.get(outer_key, dict()).get(inner_key, set())
        )

    return split_groups(merge_dict)


def split_groups(merge_dict):
    """
        {
            '2021-10-11_pv': {'a'},
            '2021-10-11_uv': {'d', 'c', 'b', 'a'}},
            '2021-10-12_uv': {'a'},
            '2021-10-12_pv': {'a'}
    拆成：
        {
            "2021-10-11": {"pv": {'a'}, "uv": {"a", "b", "c", "d"}},
            "2021-10-12": {"uv": {"a"}, "pv": {"a"}}
        }
    """
    outer_dict = dict()
    for key, value in merge_dict.items():
        outer_key = key.split("_")[0]
        inner_key = key.split("_")[1]
        if not outer_dict.get(outer_key):
            outer_dict[outer_key] = dict()
        outer_dict[outer_key][inner_key] = value
    return outer_dict


g1 = {
    "2021-10-11": {"uv": {"a", "b"}}, "2021-10-12": {"pv": {"a"}}
}
g2 = {
    "2021-10-11": {"uv": {"c", "d"}, "pv": {"a"}}, "2021-10-12": {"uv": {"a"}}
}

print(merge_two_unique_groups(g1, g2))
