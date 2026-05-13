nums=list(range(500))
for i in range(0, 496, 4):
    a,b,c,d = nums[i], nums[i+1], nums[i+2], nums[i+3]
    nums[i], nums[i+1], nums[i+2], nums[i+3] = d, a, b, c
mistakes = 0
total = 0
for i in range(500):
    for j in range(i+1, 500):
        total += 1
        if nums[i] > nums[j]:
            mistakes += 1
print(f"Disorder: {mistakes/total:.4f}")
print(" ".join(map(str, nums)))
