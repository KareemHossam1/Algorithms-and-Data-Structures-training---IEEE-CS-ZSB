buildings = int(input())
heights = list(map(int, input().split()))
areas = []
for index in range(len(heights)):
    area = heights[index]
    right = index + 1
    left = index - 1
    while right != len(heights) and heights[right] >= heights[index]:
        area += heights[index]
        right += 1
    while left != -1 and heights[left] >= heights[index]:
        area += heights[index]
        left -= 1
    areas.append(area)
print(max(areas))
