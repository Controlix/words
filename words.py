letters = ["a", "b", "c", "d"]
combination = [-1, -1, -1, -1]
ordinal = 1
word = list()

for a in range(4):
    combination[0] = a
    # print("a={}, combination={}".format(a, combination))
    for b in range(4):
        if not b in combination:
            combination[1] = b
            # print("b={}, combination={}".format(b, combination))
            for c in range(4):
                if not c in combination:
                    combination[2] = c
                    # print("c={}, combination={}".format(c, combination))
                    for d in range(4):
                        if not d in combination:
                            combination[3] = d
                            # print("d={}, combination={}".format(d, combination))
                            for l in range(4):
                                word.append(letters[combination[l]])
                            print(ordinal, combination, word, sep=':')
                            word.clear()
                            ordinal = ordinal + 1
                    combination[3] = -1
            combination[2] = -1
    combination[1] = -1
