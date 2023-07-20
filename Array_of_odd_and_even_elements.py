n=int(input())
lst=list(map(int,input().split()))
odd_elements = [num for num in lst if num % 2 != 0]
even_elements = [num for num in lst if num % 2 == 0]
print(*odd_elements,*even_elements)