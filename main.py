TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

lines = "----------------------------------------"

punctuations = "\\\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

login = input("username:")
password = input("password:")

for reg_user in users:
    if login == reg_user:
        if password == users[reg_user]:
            print(lines)
            print(f"Welcome to the app, {login}")
            print(f"We have {len(TEXTS)} texts to be analyzed. \n{lines}")
            sel_text = input(f"Enter a number btw. 1 and {len(TEXTS)} to select:")
            break
        else:
            print("unregistered user, terminating the program.")
            break
else:
    print("unregistered user, terminating the program.")


if sel_text.isdigit():
    if (int(sel_text) - 1) >= len(TEXTS):
        print("text doesn't exist, terminating the program.")
    else:
        analyzed_text = TEXTS[int(sel_text) - 1]
else:
    print("input is not a number, terminating the program.")

bareanalyzed_text = analyzed_text

for punctuation in punctuations:
    bareanalyzed_text = (analyzed_text.replace(punctuation, ""))

bareanalyzed_text = bareanalyzed_text.split()

word_count = len(bareanalyzed_text)

titlecase_count = 0
for titlecases in bareanalyzed_text:
    if titlecases.istitle():
        titlecase_count = titlecase_count + 1

uppercase_count = 0
for uppercases in bareanalyzed_text:
    if uppercases.isupper():
        uppercase_count = uppercase_count + 1

lowercase_count = 0
for lowercases in bareanalyzed_text:
    if lowercases.islower():
        lowercase_count = lowercase_count + 1

numericstrings_count = 0
for numericstrings in bareanalyzed_text:
    if numericstrings.isdigit():
        numericstrings_count = numericstrings_count + 1

sumof_numericstr = 0
for sumofnumstr in bareanalyzed_text:
    if sumofnumstr.isdigit():
        sumof_numericstr = sumof_numericstr + int(sumofnumstr)

print(lines)
print(f"There are {word_count} words in the selected text.")
print(f"There are {titlecase_count} titlecase words.")
print(f"There are {uppercase_count} uppercase words.")
print(f"There are {lowercase_count} lowercase words.")
print(f"There are {numericstrings_count} numeric strings.")
print(f"The sum of all the numbers {sumof_numericstr}.")
print(lines)
print("LEN|  OCCURRENCES  |NR.")

lenghts_count = {}
for lenght in bareanalyzed_text:
    l = len(lenght)
    lenghts_count[l] = lenghts_count.get(l, 0) + 1

for lenght, count in sorted(lenghts_count.items()):
    print(f"{lenght}|{"*" * count}|{count}")