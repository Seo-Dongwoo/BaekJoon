N = int(input())
count = 0
stack = []
result = []
message = True

for i in range(N):
    x = int(input())

    while count < x:
        count += 1
        stack.append(count)
        result.append("+")

    if stack[-1] == x:
        stack.pop()
        result.append("-")
    else:
        message = False
        break

if message == False:
        print("NO")
else:
    for i in result:
        print(i)