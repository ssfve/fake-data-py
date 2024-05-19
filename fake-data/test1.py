import re


def match_email(email):
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    # matches = re.findall(pattern, text)
    return bool(re.match(pattern, email))
    # return matches


if __name__ == "__main__":
    # read from a file
    with open("./email.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            # for each line match it to a email regular expression
            # write a pattern to match email address
            if match_email(line):
                print(line)
