# nums = input().split(", ")
# final = []
# counter = 0
# for num in nums:
#     counter += 1
#     if int(num) % 2 == 0:
#         final.append(counter - 1)
# print(final)

nums = list(map(int, input().split(", ")))
print([index for index in range(len(nums)) if nums[index] % 2 == 0])