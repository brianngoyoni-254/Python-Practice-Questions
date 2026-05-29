def caesar_encrypt(text, shift):
    result = ""

    for char in text:
        # Encrypt uppercase letters
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65)

        # Encrypt lowercase letters
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)

        # Keep spaces and symbols unchanged
        else:
            result += char

    return result


# Example
message = "Hello Collins"
shift = 3

encrypted = caesar_encrypt(message, shift)

print("Original:", message)
print("Encrypted:", encrypted)