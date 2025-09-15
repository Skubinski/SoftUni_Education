def fill_the_box(height, length, width, *args):
    dimension = height * length * width

    for arg in args:
        if arg == "Finish":
            break
        dimension -= arg

    if dimension >= 0:
        return f'There is free space in the box. You could put {dimension} more cubes.'

    return f'No more free space! You have {abs(dimension)} cubes left.'

print(fill_the_box(5,5,2,40,11,7,3,1,5,"Finish"))