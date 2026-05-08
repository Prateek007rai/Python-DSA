# Sum to target
# i/p: [2,7,11,15], k = 9
# o/p: [0,1]

# Time: O(n), Space: O(n)

def two_sum(nums, target):
    mp={}

    for i in range(len(nums)):
        diff = target - nums[i]

        if diff in mp:
            return [mp[diff], i]                  #bcz mp has { 2: 0, 7: 1, 11: 2, 15: 3}
        mp[nums[i]] = i

print(two_sum([2,7,11,15], 9))
print(two_sum([2,7,11,15], 9))
