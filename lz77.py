triples = [[0, 0, "a"], [0, 0, "b"], [2, 1, "a"], [3, 2, "b"], [5, 3, "b"], [1, 5, "a"]]


def decode(triple, output):
    if len(output) == 0 or triple[0] == 0 or triple[2] == 0:
        output += triple[2]
    else:
        startIndex = int((len(output) - triple[0]))
        endIndex = int(startIndex + triple[1])
        copyString = output[startIndex: endIndex]

        # deal with recursion
        neededLength = triple[1] + len(output)
        possibleLength = len(output[startIndex:]) + len(output)
        if neededLength > possibleLength:
            while len(output) < neededLength:
                output += copyString
        else:
            output += copyString
        output += triple[2]
        print(output)
    return output


def main():
    output = ""
    for triple in triples:
        output = decode(triple, output)
    return output


print(main())
