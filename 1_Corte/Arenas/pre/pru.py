
results = []
def find_sums(t, nums):
    #results = []
    nums.sort(reverse=True)  # ordenamos la lista de mayor a menor para evitar sumas repetidas

    def backtrack(sum_so_far, i):
        if sum_so_far == t:
            results.append(list(curr))
        elif sum_so_far < t and i < len(nums):
            curr.append(nums[i])
            backtrack(sum_so_far + nums[i], i)
            curr.pop()
            backtrack(sum_so_far, i+1)

    curr = []
    backtrack(0, 0)

    if not results:
        print("NONE")
    else:
        for r in results:
            print("Sums of {}: {}".format(t, " + ".join(map(str, r))))

find_sums(4, [4, 3, 2, 2, 1, 1])
normal = []
repe = []
for i in results:
    if i not in normal:
        normal.append(i)
    else:
        repe.append(i)
print(normal)