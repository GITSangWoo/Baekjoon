import sys
input = sys.stdin.readline

N = int(input())
stack = []

for _ in range(N):
    todo = input().rstrip().split()
    cmd = int(todo[0])
    
    if cmd == 1:
        # push
        stack.append(int(todo[1]))
    elif cmd == 2:
        # pop
        print(stack.pop() if stack else -1)
    elif cmd == 3:
        # size
        print(len(stack))
    elif cmd == 4:
        # empty
        print(0 if stack else 1)
    elif cmd == 5:
        # top
        print(stack[-1] if stack else -1)