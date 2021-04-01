import re

def build_galaxy(bookmarks, keywords):
    """
    Build galaxy map

    :param bookmarks: list of bookmarks
    :param keywords: list of keywords
    :return: None
    """
    print("GALAXY - build galaxy - bookmarks:", bookmarks, 'keywords:', keywords)
    count = dict.fromkeys(keywords, 0)
    for bookmark in bookmarks:
        for keyword in keywords:
            match = re.search(keyword, bookmark, re.IGNORECASE)  # TODO match all keywords and use group
            if match:
                count[keyword] += 1
    print("GALAXY - build galaxy - count:", count)

# if __name__ == "__main__":
#     pass
