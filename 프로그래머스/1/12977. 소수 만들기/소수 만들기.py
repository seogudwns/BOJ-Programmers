def solution(nums):
    nums.sort()
    n = sum(nums[-3:])
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
                
    return sum(1 for i in range(2,len(nums)) for j in range(1,i) for k in range(j) if is_prime[nums[i]+nums[j]+nums[k]])