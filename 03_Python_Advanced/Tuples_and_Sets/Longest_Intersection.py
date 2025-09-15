def gen_seq(range_info):
    start, end = [int (x) for x in range_info.split(',')]
    return set(range(start, end + 1))
n = int(input())
best_int = set()
for _ in range(n):
    line_parts = input().split('-')
    first_set = gen_seq(line_parts[0])
    second_set = gen_seq(line_parts[1])
    current_int = first_set.intersection(second_set)
    if len(current_int) > len(best_int):
        best_int = current_int
print(f"Longest intersection is [{", ".join(str(x) for x in best_int)}] with length {len(best_int)}")