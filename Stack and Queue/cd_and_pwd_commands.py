n = int(input())
commands = []
for i in range(0,n):
    cmd = input()
    commands.append(cmd)
stack = []
for command in commands:
    if command == 'pwd':
        if len(stack) != 0:
            ans = ''
            for item in stack:
                ans = ans + item + '/'
            print('/' + ans)
        else:
            print('/')
        continue
    if command[3] == '/':
        stack = []
    individual_cmds = command[3:].split('/')
    for cmd in individual_cmds:
        if cmd == '':
            continue
        elif cmd == '..' and len(stack) != 0:
            stack.pop()
        else:
            stack.append(cmd)