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


user_words = []

def user_input():
    adjective_one = input("Please enter an adjective and press enter: ")
    adjective_two = input("Please enter another adjective and press enter: ")
    noun = input("Please enter a noun and enter: ")
    user_words.extend((adjective_one, adjective_two, noun))


user_input()
print(user_words)








# user_input()








