
while True:
    try:
        line = input()
        if not line:
            break
        print(line)
    except EOFError:
        break