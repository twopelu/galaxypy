import re


def read_bookmarks(file):
    """
    Read bookmarks file

    :param file: path of the file
    :return: list of bookmarks
    """
    print("GALAXY - read bookmarks - file:", file)
    bookmarks = []
    with open(file) as reader:
        lines = reader.readlines()
        for line in lines:
            bookmark = parse_bookmark(line)
            if bookmark:
                bookmarks.append(bookmark)
    print("GALAXY - read bookmarks - total:", len(bookmarks))
    return bookmarks


def parse_bookmark(string):
    """
    Parse bookmark string

    :param string: line of the bookmarks file representing an html element
    :return: if the line is a bookmark return the href attribute; else None
    """
    match = re.search(r'<A HREF=.+?"', string)
    if match:
        return match.group(0).split('"')[1]
    else:
        return None

# if __name__ == "__main__":
#     pass
