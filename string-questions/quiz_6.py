def insert_spaces(word):
    result = ""

    for char in word:
        # Add space before capital letters (except the first character)
        if char.isupper() and result:
            result += " "

        result += char

    return result


# Examples
print(insert_spaces("PlayingFootball"))
print(insert_spaces("Playing"))
print(insert_spaces("PlayingFootballAndPes"))