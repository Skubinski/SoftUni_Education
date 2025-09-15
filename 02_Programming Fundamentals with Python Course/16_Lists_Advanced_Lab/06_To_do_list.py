def to_do_list():
    to_do_list = []
    while True:
        command = input()
        if command == 'End':
            break
        to_do_list.append(command)
    sorted_notes = sorted(to_do_list, key=lambda x: int(x.split('-')[0]))
    return [note.split('-')[1] for note in sorted_notes]
print(to_do_list())
