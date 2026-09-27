#write  a program to input any alphabetand check whether it is vowel or constant

ch = input("Enter an alphabet: ")

if ch in "aeiouAEIOU":
    print("Vowel")
else:
    print("Consonant")