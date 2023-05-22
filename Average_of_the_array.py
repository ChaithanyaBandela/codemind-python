def find_average(arr):
    total_sum = sum(arr)
    avg = total_sum / len(arr)
    return f"{avg:.2f}"

n = int(input())
a = list(map(int,input().split()))

average = find_average(a)
print(average)
