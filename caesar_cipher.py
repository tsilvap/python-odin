def caesar_cipher(plain, shift):
    """Implement a Caesar cipher function.

    :param plain: Plain text to be encoded
    :param shift: Number of letters to shift
    :return cipher: Encrypted plain text (cipher text)
    """
    cipher = ""

    for char in plain:
        char_code = ord(char)

        if char_code >= ord("A") and char_code <= ord("Z"):
            mod_shift = (char_code + shift - ord("A")) % 26
            char_code = ord("A") + mod_shift
            cipher += chr(char_code)

        elif char_code >= ord("a") and char_code <= ord("z"):
            mod_shift = (char_code + shift - ord("a")) % 26
            char_code = ord("a") + mod_shift
            cipher += chr(char_code)

        else:
            cipher += char

    return cipher
