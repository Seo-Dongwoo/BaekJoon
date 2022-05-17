import sys
l_stack = list(input())
r_stack = []
T = int(input())

for i in range(T):
    cmd = sys.stdin.readline().split()

    if cmd[0] == 'L' and l_stack:
        r_stack.append(l_stack.pop())
    elif cmd[0] == 'D' and r_stack:
        l_stack.append(r_stack.pop())
    elif cmd[0] == 'B' and l_stack:
        l_stack.pop()
    elif cmd[0] == 'P':
        l_stack.append(cmd[1])

print("".join(l_stack + list(reversed(r_stack))))