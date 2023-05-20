def count_occurrences(arr, element):
    count = 0
    for num in arr:
        if num == element:
            count += 1
    return count
N = int(input())
arr = list(map(int, input().split()))
search_element = int(input())
occurrences = count_occurrences(arr, search_element)
print(occurrences)
