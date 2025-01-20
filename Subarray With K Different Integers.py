def subarrays_with_exactly_k(nums, k):
    def at_most_k(nums, k):
        l = 0
        count = 0
        currSeen = {}
        
        for r in range(len(nums)):
            if nums[r] not in currSeen:
                currSeen[nums[r]] = 1
            else:
                currSeen[nums[r]] += 1
            
            while len(currSeen) > k:
                currSeen[nums[l]] -= 1
                if currSeen[nums[l]] == 0:
                    del currSeen[nums[l]]
                l += 1

            count += r - l + 1
        
        return count

    return at_most_k(nums, k) - at_most_k(nums, k - 1)