string = "abcabcbb"


def return_maxlength_unrepetitives(string):
    length = len(string)

    l = []
    for j in range(length):
        if string[j] not in l:
            l.append(string[j])
    return len(l)

if __name__ == '__main__':

    result = return_maxlength_unrepetitives("abcabcbb")
    print(result)