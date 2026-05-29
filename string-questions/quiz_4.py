def delete_character(text, char_to_delete):
    return text.replace(char_to_delete, "")


# Example
string = "Delete all occurrences of a specified character in a given string"
character = "a"

print("Original string:")
print(string)

modified_string = delete_character(string, character)

print("\nModified string:")
print(modified_string)