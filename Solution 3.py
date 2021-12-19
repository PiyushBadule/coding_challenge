# Question:-  Let's say you are given a string. You can get many strings (combination)
# out of the given original string if you rearrange characters of original string.
# String is Palindromable if any one combination is palindrome.
# Example 1:
# Original String: NINIT
# Combinations: NINIT, NNIIT,IINNT,ININT,IITNN,NITIN,INTIN,INTNI,NTNII,NNTII and so on
# Original string is  Palindromable because two palindrome can be made out of it.
# Example 2:
# Original String: NINNIT
# Combinations: NINITN, NNINIT,IINNNT,INNINT,INITNN,NNITIN,INTNIN,INTNIN,NTNINI,NNTINI and so on
# Original string is NOT Palindromable because NO palindrome can be made out of it.
# Write a program to check it given string is Palindromable or not. (please note this is not a
# question to check if string is palindrome or not).
# (Hint: Do not write a program to find the permutation and combination of original string and then
# check combination. Program is much simpler than finding permutation and combination. )
a = input()
flag = 0
c = 0
L = list(a)
for x in L:
    if (L.count(x) == 1 or L.count(x) % 2 == 0):
        if (L.count(x) == 1):
            c = c + 1
            if (c < 2):
                pass
            else:
                print("NOT Palindromable")
                flag = 0
                break
        flag = 1
    else:
        print("NOT Palindromable")
        flag = 0
        break
if (flag == 1):
    print("Palindromable")