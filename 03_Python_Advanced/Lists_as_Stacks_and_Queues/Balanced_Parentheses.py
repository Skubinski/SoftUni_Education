
expression = input()

opening = []
is_closed = True
for char in expression:
    if char in '({[':
        opening.append(char)
    elif not opening:
        is_closed = False
        break
    else:
        last_opening_bracket = opening.pop()
        if f"{last_opening_bracket}{char}" not in '()[]{}':
            is_closed = False
            break

if is_closed:
    print('YES')
else:
    print('NO')