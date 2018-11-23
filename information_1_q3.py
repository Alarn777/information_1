# Retain the first letter of the name and drop all other occurrences of .A, E, I, O, U, H, W, and Y.
# Replace consonants with digits as follows (after the first letter):
from curses.ascii import islower


class SoundEx:

    coding_set = {'b': 1, 'f': 1, 'p': 1, 'v': 1,
                  'c': 2,'g': 2,'j': 2,'k': 2,'q': 2,'s': 2,'x': 2,'z': 2,
                  'd': 3,'t': 3,
                  'l': 4,
                  'm': 5,'n': 5,
                  'r': 6 }
    def code(self,string):
        if len(string) == 0:
            print("Nothing to code!")
            return
        string = string.lower()
        # self.coded_word.__add__(string[0])
        coded_word = ""
        coded_word += string[0].upper()
        # coded_word += "-"
        string = string[1:]
        string = string.replace("a", "")
        string = string.replace("e", "")
        string = string.replace("i", "")
        string = string.replace("o", "")
        string = string.replace("u", "")
        string = string.replace("y", "")
        string = string.replace("h", "")
        string = string.replace("w", "")

        for char in string:
            coded_word += str(self.coding_set[char])

        for char in coded_word:
            count = 0
            for char2 in coded_word:
                if(char2 == char):
                    count += 1
            if count > 1:
                delete_string = ""
                while count:
                    delete_string += char
                    count -= 1
                coded_word = coded_word.replace(delete_string,char)

        while len(coded_word) < 4:
            coded_word += "0"


        return coded_word



#
# temp = SoundEx()
# arr = ["levi", "levy", "levine", "loweb", "lovi", "john", "jhon", "jhonee", "johne",
# "cohen", "choen", "kohen", "kahana", "khan", "cownn", "aa", "aaaaa", "rr", "rrrrr", "et", "eeet"]
# for var in arr:
#     print("Input: ", var, " Output: ", temp.code(var))
#



