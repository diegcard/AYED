def find_sums(total, nums):
    nums.sort(reverse=True)  # ordenamos los números en orden descendente
    results = []
    
    def backtrack(target, partial_sum, start):
        if partial_sum == target:
            results.append(list(temp))  # encontramos una suma que coincide con el total
        elif partial_sum < target:
            for i in range(start, len(nums)):
                temp.append(nums[i])
                backtrack(target, partial_sum + nums[i], i)
                temp.pop()
                
    temp = []
    backtrack(total, 0, 0)
    
    if results:
        print(f"Sums of {total}:")
        #for r in results:
            #print("+".join(map(str, r)))
    else:
        print(f"Sums of {total}: NONE")
        

while True:
    total, n, *nums = map(int, input().split())
    if total == 0:
        break
    find_sums(total, nums)
