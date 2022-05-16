N = int(input())

for i in range(N):
    input_data = input()
    arr = []

    for j in input_data:
        if j == "(":
            arr.append(j)
        elif j == ")":
            if len(arr) != 0 and arr[-1] == "(":
                arr.pop()
            else:
                arr.append(")")
                break

    if len(arr) == 0:
        print("YES")
    else:
        print("NO")



