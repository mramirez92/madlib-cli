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









