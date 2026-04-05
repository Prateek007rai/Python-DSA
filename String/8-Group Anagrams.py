# Group Anagrams
# i/p - ["ate", "eat", "tea", "tan", "ant"]
# o/p - [["ate","tea","eat"],["ant", "tan"]]

def group_anagrams(arr):
    res = {}

    for word in arr:
        key = "".join(sorted(word))

        if key not in res:
            res[key] = []
        res[key].append(word)
    
    return list(res.values())
    
print(group_anagrams(["ate", "eat", "tea", "tan", "ant"]))