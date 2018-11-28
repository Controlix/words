letters = ["a", "b", "c", "d"]

def print_combinations(choices, prefix=""):
    length = len(choices)
    if length == 0:
        print(prefix)
    else:
        for i in range(length):
            new_choices = choices.copy()
            choice = prefix + str(new_choices.pop(i))
            print_combinations(new_choices, choice)

print_combinations(letters)
