def brute_force(string, pattern):
    i = 0
    res = []
    comparisons = 0
    while i < (len(string) - len(pattern)):

        j = 0
        count = 0
        while j <= len(pattern):

            if count == (len(pattern)):
                res.append(i)
                count = 0
                i += 1
                break
            comparisons += 1
            if string[j + i] == pattern[j]:
                j += 1
                count += 1
            else:
                i += 1
                j += 1
                break
    print("Moved : ", i, " times")
    print("Comparisons made : ", comparisons)
    return res


class KMP:
    def partial(self, pattern):
        """ Calculate partial match table: String -> [Int]"""
        ret = [0]

        for i in range(1, len(pattern)):
            j = ret[i - 1]
            while j > 0 and pattern[j] != pattern[i]:
                j = ret[j - 1]
            ret.append(j + 1 if pattern[j] == pattern[i] else j)
        return ret

    def search(self, T, P):
        """
        KMP search main algorithm: String -> String -> [Int]
        Return all the matching position of pattern string P in S
        """
        partial, ret, j = self.partial(P), [], 0
        count = 0
        while_count = 0
        for i in range(len(T)):
            while j > 0 and T[i] != P[j]:
                j = partial[j - 1]
                while_count += 1
                print("Moved: ", while_count)
            if T[i] == P[j]: j += 1
            if j == len(P):
                ret.append(i - (j - 1))
                j = partial[j - 1]
            count += 1
        print("Comparisons made : ", count)

        return ret


# strings = ["brave abrasive abracadabra candelabra","aaabraaabq","abcdeabxa","abcabcabca","a string searching example consisting of sample text"]
# patterns = ["abracadabra","aab","xab","abcd","sting"]
# i = 0
# for string in strings:
#     temp = KMP()
#     print("-------------Brute Force--------------")
#     print("Pattern found at indexes = ",brute_force(string, patterns[i])," with Brute Force")
#     print("--------------------------------------")
#
#     print("-----------------KMP------------------")
#     print("Pattern found at indexes = ", temp.search(string,patterns[i]), " with KMP")
#     print("--------------------------------------")
#     i += 1

