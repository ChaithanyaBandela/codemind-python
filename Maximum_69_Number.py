def maximum69Number(num):
    num_str = str(num)
    found = False

    for i in range(len(num_str)):
        if num_str[i] == '6':
            num_str = num_str[:i] + '9' + num_str[i+1:]
            found = True
            break

    if found:
        return int(num_str)
    else:
        return num
num=input()
print(maximum69Number(num))