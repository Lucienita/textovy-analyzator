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

USERS = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

SEPARATOR = "-" * 40

# přihlášení uživatele
username = input("username:")
password = input("password:")

if USERS.get(username) != password:
    print("unregistered user, terminating the program..")
    exit()

print(SEPARATOR)
print(f"Welcome to the app, {username}")
print(f"We have {len(TEXTS)} texts to be analyzed.")
print(SEPARATOR)

# výběr textu
choice = input(f"Enter a number btw. 1 and {len(TEXTS)} to select: ")

if not choice.isdigit():
    print("You did not enter a number, terminating the program..")
    exit()

choice = int(choice)

if not 1 <= choice <= len(TEXTS):
    print("Number out of range, terminating the program..")
    exit()

# rozdělení textu na slova a odstranění interpunkce
words = []
for word in TEXTS[choice - 1].split():
    cleaned = word.strip(".,:;!?\"'()")
    if cleaned:
        words.append(cleaned)

# analýza slov
titlecase = 0
uppercase = 0
lowercase = 0
numbers = []
lengths = {}

for word in words:
    if word.istitle():
        titlecase += 1
    elif word.isupper():
        uppercase += 1
    elif word.islower():
        lowercase += 1
    elif word.isnumeric():
        numbers.append(int(word))

    lengths[len(word)] = lengths.get(len(word), 0) + 1

print(SEPARATOR)
print(f"There are {len(words)} words in the selected text.")
print(f"There are {titlecase} titlecase words.")
print(f"There are {uppercase} uppercase words.")
print(f"There are {lowercase} lowercase words.")
print(f"There are {len(numbers)} numeric strings.")
print(f"The sum of all the numbers {sum(numbers)}")

# sloupcový graf četnosti délek slov
width = max(max(lengths.values()), 20)

print(SEPARATOR)
print(f"LEN|{'OCCURRENCES':^{width}}|NR.")
print(SEPARATOR)

for length in sorted(lengths):
    count = lengths[length]
    print(f"{length:>3}|{'*' * count:<{width}}|{count}")
