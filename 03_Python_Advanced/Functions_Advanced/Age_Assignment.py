def age_assignment(*args, **kwargs):
    people = {}
    for name in args:
        first_letter = name[0]
        people[name] = kwargs[first_letter]
    return people

print(age_assignment("Peter", "George", G=26, P=19))