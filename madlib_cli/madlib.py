import re
import sys


def read_template(file_location):
    try:
        with open(file_location, 'r') as f:
            return f.read()
    except FileNotFoundError as Error_in_file:
        raise Error_in_file


def parse_template(string):
    # new_string = string

    parts = tuple(re.findall(r"\{(.*?)}", string))
    print(parts)
    for words in parts:
        # string = re.sub(r"\{(.*?)}", "{}", new_string)
        string = string.replace(words, "")

    # print(string, parts)
    return string, parts


def merge(str, tuple):
    return str.format(*tuple)


def mad_lib():
    print("Welcome to Madlibs: a game where you use random words and insert them into a story.\n")

    template = read_template('./assets/make_me_a_video_game_template.txt')

    string, parts = parse_template(template)

    user_words = []

    for word in parts:
        word_input = input(f"Please enter {word} > ")
        user_words.append(word_input)

    madlib = merge(string, user_words)
    print(f"\nYou created this madlib: {madlib}")
    with open("./assets/new_file.txt", 'w') as ff:
        ff.write(madlib)


def game_exit():
    print("\nThanks for playing!\n")
    exit()


if __name__ == "__main__":
    mad_lib()
    game_exit()

