def main():
    sequence = input().split()
    moves = 0

    while True:
        command = input()
        if command == "end":
            break

        moves += 1
        idx1, idx2 = map(int, command.split())

        if (
            idx1 == idx2
            or idx1 < 0
            or idx2 < 0
            or idx1 >= len(sequence)
            or idx2 >= len(sequence)
        ):
            print("Invalid input! Adding additional elements to the board")
            middle_idx = len(sequence) // 2
            sequence.insert(
                middle_idx,
                f"-{moves}a",
            )
            sequence.insert(
                middle_idx,
                f"-{moves}a",
            )
        else:
            if sequence[idx1] == sequence[idx2]:
                matching_element = sequence[idx1]
                del sequence[max(idx1, idx2)]
                del sequence[min(idx1, idx2)]
                print(f"Congrats! You have found matching elements - {matching_element}!")
            else:
                print("Try again!")

        if not sequence:
            print(f"You have won in {moves} turns!")
            break

    if sequence:
        print("Sorry you lose :(")
        print(" ".join(sequence))


if __name__ == "__main__":
    main()
