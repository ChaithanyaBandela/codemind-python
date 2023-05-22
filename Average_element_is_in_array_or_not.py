def check_average_presence(arr):
    average = sum(arr) // len(arr)
    return average in arr
n = int(input())
a = list(map(int,input().split()))

average_present = check_average_presence(a)
print(average_present)
