def shopping (list):
    while True:
        command = input().split()
        if command[0] == "Go" and command[1] == "Shopping!":
            break
        elif command[0] == "Urgent" and not command[1] in list:
            added_product = command[1]
            list.insert(0, added_product)

        elif command[0] == "Unnecessary" and command[1] in list:
            removed_product = command[1]
            list.remove(removed_product)

        elif command[0] == "Correct" and command[1] in list:
            word_to_replace = command[1]
            new_word = command[2]
            index_to_replace = list.index(word_to_replace)
            list[index_to_replace] = new_word

        elif command[0] == "Rearrange" and command[1] in list:
            removed_item = command[1]
            list.remove(removed_item)
            list.append(removed_item)
    return ', '.join(list)


shopping_list = input().split('!')
print(shopping(shopping_list))
