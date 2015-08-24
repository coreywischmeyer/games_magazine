import re
__author__ = 'Corey Wischmeyer'

IMDB_FILE = "movies.list"
MOVIE_TITLE_LENGTH = 17
MOVIE_TITLE_WORDS = 3

TITLE_SET = set()

letters = {'A', 'B', 'D', 'E', 'F',
           'G', 'H', 'I', 'J', 'L',
           'M', 'N', 'O', 'P', 'R',
           'S', 'T', 'U', 'V',
           'W', 'Y', '\'', ' '}

def process_title(title):
    #Take in a title, get the title bit, (before the year)
    #Remove the Parens
    #Get only unique titles
    pattern = re.compile("(.*)?\(\d")
    if re.match(pattern, title):
        m = pattern.findall(title)[0]
        m = m.replace('"', '')
        if is_ascii(m) and len(m.split()) == 3\
                and letters.issuperset(set(m.upper()))\
                and count_letters(m) == 17:
            return m

def count_letters(word):
    return len(word) - word.count(' ') - word.count('\'')

def is_ascii(s):
    return all(ord(c) < 128 for c in s)


with open(IMDB_FILE, 'r') as f:
    for item in f:
        TITLE_SET.add(process_title(item))

for i in TITLE_SET:
    print(i)


