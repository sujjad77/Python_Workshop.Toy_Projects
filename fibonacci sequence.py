def fibonacci(num, limit):
    _list = []
    _sum = 0
    _list.append(num)
    _list.append(num+1)
    for each in range(0, limit):
        _sum = _list[each] + _list[each+1]
        _list.append(_sum)

    return _list


n = int(input("Enter a number to begin to find the fibonacci sequence : "))
_limit = int(input("Enter the limit of the sequence:"))

print(f"The fibonacci sequence is {fibonacci(n,_limit)}")

