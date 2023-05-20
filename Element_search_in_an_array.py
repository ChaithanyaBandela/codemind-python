def is_element_present(arr, element):
    return element in arr
N = int(input())
arr = list(map(int, input().split()))
search_element = int(input())
present = is_element_present(arr, search_element)
if present:
    print("True")
else:
    print("False")
