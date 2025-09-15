from collections import deque

def find_colors():
    main_colors = {"red", "yellow", "blue"}
    secondary_colors = {"orange", "purple", "green"}
    color_requirements = {
        "orange": {"red", "yellow"},
        "purple": {"red", "blue"},
        "green": {"yellow", "blue"}
    }

    # Read input from the console
    substrings = deque(input().split())
    found_colors = []

    while substrings:
        if len(substrings) == 1:
            current = substrings.popleft()
        else:
            first = substrings.popleft()
            last = substrings.pop()

            combined1 = first + last
            combined2 = last + first

            if combined1 in main_colors or combined1 in secondary_colors:
                current = combined1
            elif combined2 in main_colors or combined2 in secondary_colors:
                current = combined2
            else:
                first = first[:-1]
                last = last[:-1]
                middle_index = len(substrings) // 2
                if first:
                    substrings.insert(middle_index, first)
                if last:
                    substrings.insert(middle_index, last)
                continue

        if current in main_colors or current in secondary_colors:
            found_colors.append(current)

    final_colors = []
    for color in found_colors:
        if color in main_colors:
            final_colors.append(color)
        elif color in secondary_colors:
            required = color_requirements[color]
            if required.issubset(set(found_colors)):  # Ensure main colors exist
                final_colors.append(color)

    print(final_colors)

find_colors()
