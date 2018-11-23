def brute_force(string, pattern):
    i = len(string)-1
    res = []
    moved = 0
    comparisons = 0
    while i > len(pattern):
        moved += 1
        j = len(pattern)
        count = 0
        index = i
        while j >= 0:

            if count == (len(pattern)):
                res.append(i)
                count = 0
                i -= 1
                break
            comparisons += 1
            if string[index] == pattern[j-1]:
                j -= 1
                index -= 1
                count += 1
            else:
                i -= 1
                j -= 1
                break
    print("Moved : ", moved, " times")
    print("Comparisons made : ", comparisons)
    return res


# strings = ["brave abrasive abracadabra candelabra","aaabraaabq","abcdeabxa","abcabcabca","a string searching example consisting of sample text","asdaf fafs nomono  mon sal las nomolas"]
# patterns = ["abracadabra","aab","xab","abcd","sting","nomolas"]
# i = 0
# for string in strings:
#     print("Pattern found at indexes = ",brute_force(string, patterns[i])," with Brute Force")
#     i += 1
