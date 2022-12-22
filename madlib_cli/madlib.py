import re


def read_template(file_location):
    with open(file_location, 'r') as f:
        contents = f.read()
        return contents


def parse_template(string):
    new_string = string

    parts = tuple(re.findall(r"\{(.*?)}", new_string))
    string = re.sub(r"\{(.*?)}", "{}", new_string)

    print(string, parts)
    return string, parts


def merge(str, tuple):
  return str.format(*tuple)


if __name__ == "__main__":
    path = 'assets/dark_and_stormy_night_template.txt'
    print(read_template(path))


def greeting():
    print("Welcome to Madlibs: a game where you use random words and insert them into a story")


greeting()

template = read_template('../assets/dark_and_stormy_night_template.txt')


string, parts = parse_template(template)

user_words = []


for word in parts:
    word_input = input("Please enter a enter a word > ")
    user_words.append(word_input)


madlib = merge(string, user_words)


with open("../assets/new_file.txt", 'w') as ff:
    ff.write(madlib)


print(f"You created this madlib: {madlib}")









