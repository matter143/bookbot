def count_words(file_contents):

    count = file_contents.split()
    num = len(count)
    return num


def to_char(file_contents):
    to_lower = file_contents.lower()
    count_dict = {}
    for char in to_lower:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
    return count_dict
