import information_1_q1
import information_1_q2
import information_1_q3



strings = ["brave abrasive abracadabra candelabra", "aaabraaabq", "abcdeabxa", "abcabcabca",
           "a string searching example consisting of sample text"]
patterns = ["abracadabra", "aab", "xab", "abcd", "sting"]
i = 0
print("---------------------------------------------------------Q1-------------------------------------------------------")
for string in strings:
    temp = information_1_q1.KMP()
    print("-------------Brute Force--------------")
    print("Pattern found at indexes = ", information_1_q1.brute_force(string, patterns[i]), " with Brute Force")
    print("--------------------------------------")

    print("-----------------KMP------------------")
    print("Pattern found at indexes = ", temp.search(string, patterns[i]), " with KMP")
    print("--------------------------------------")
    i += 1

print("---------------------------------------------------------Q2-------------------------------------------------------")

strings = ["brave abrasive abracadabra candelabra", "aaabraaabq", "abcdeabxa", "abcabcabca",
           "a string searching example consisting of sample text", "asdaf fafs nomono  mon sal las nomolas"]
patterns = ["abracadabra", "aab", "xab", "abcd", "sting", "nomolas"]
i = 0
for string in strings:
    print("Pattern found at indexes = ", information_1_q2.brute_force(string, patterns[i]), " with Brute Force")
    i += 1


print("---------------------------------------------------------Q3-------------------------------------------------------")

temp = information_1_q3.SoundEx()
arr = ["levi", "levy", "levine", "loweb", "lovi", "john", "jhon", "jhonee", "johne",
       "cohen", "choen", "kohen", "kahana", "khan", "cownn", "aa", "aaaaa", "rr", "rrrrr", "et", "eeet"]
for var in arr:
    print("Input: ", var, " Output: ", temp.code(var))

