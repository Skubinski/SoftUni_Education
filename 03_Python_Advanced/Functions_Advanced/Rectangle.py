def rectangle(a, b):
    if type(a) != int or type(b) != int:
        return "Enter valid values!"

    def area(a, b):
        return a * b

    def rect_perim(a, b):
        return 2*a + 2*b

    area = area(a,b)
    perim = rect_perim(a,b)

    return f"Rectangle area: {area} \nRectangle perimeter: {perim}"


print(rectangle(2, 10))