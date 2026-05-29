def remove_duplicates(text):
    result = ""

    for char in text:
        if char not in result:
            result += char

    return result


# Example
string = "arsennal"

print("Original String:", string)
print("Without Duplicates:", remove_duplicates(string))