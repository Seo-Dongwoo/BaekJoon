import sys
N = int(sys.stdin.readline().rstrip())

queue = []

for i in range(N):
    cmd = sys.stdin.readline().split()

    if cmd[0] == 'push':
        queue.append(cmd[1])

    elif cmd[0] == 'pop':
        if len(queue) != 0:
            print(queue[0])
            del queue[0]
        else:
            print(-1)

    elif cmd[0] == 'size':
        print(len(queue))

    elif cmd[0] == 'empty':
        if len(queue) != 0:
            print(0)
        else:
            print(1)

    elif cmd[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)

    elif cmd[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)