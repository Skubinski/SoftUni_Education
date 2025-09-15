def fill_shells(electrons):
    shell_list = []
    n = 1
    while electrons > 0:
        max_electrons = 2 * n ** 2
        if electrons >= max_electrons:
            shell_list.append(max_electrons)
            electrons -= max_electrons
        else:
            shell_list.append(electrons)
            electrons = 0
        n += 1

    return shell_list


electrons = int(input())
filled_shells = fill_shells(electrons)
print(filled_shells)
