#Given a string. Split it into two equal parts. Swap these parts and return the result.
#If the string has odd characters, the first part should be one character greater than the second part
#Example: string = 'bbbbbcaaaaa'. Result = ‘aaaaabbbbbc’
def split_in_half(s):
    first_half = ""
    second_half = ""
    string_length = len(s)
    if string_length % 2 == 0:
        first_half = s[0:(string_length/2-1)]
        second_half = s[string_length/2:]
        return (second_half + first_half)
    else:
        first_half = s[0:(string_length // 2 + 1)]
        second_half = s[string_length // 2 + 1:]
        return (second_half + first_half)
print(split_in_half("bbbbbcaaaaa"))

#Given a string, determine if it consists of all unique characters.
#For example, the string 'abcde' has all unique characters and should return True.
#The string 'aabcde' contains duplicate characters and should return False.
def unique_char(s):
    chars = set()
    for char in s:
       if char in chars:
           return False
       else:
           chars.add(char)
    return True
print(unique_char('abcde'))
print(unique_char('aabcde'))

