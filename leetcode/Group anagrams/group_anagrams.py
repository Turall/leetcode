# Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
# Output:
# [
#   ["ate","eat","tea"],
#   ["nat","tan"],
#   ["bat"]
# ]

import collections


def func(mylist):
    m = collections.defaultdict(list)
    for s in mylist:
        m["".join(sorted(s))].append(s)
    return list(m.values())


arr = [["ate", "eat", "tea"], ["nat", "tan"], ["bat"]]

print(func(arr))
