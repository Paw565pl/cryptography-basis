def _encrypt_char(char: str, shift: int) -> str:
    char_code = ord(char)

    if char_code in range(65, 91):
        return chr((char_code + shift - 65) % 26 + 65)
    elif char_code in range(97, 123):
        return chr((char_code + shift - 97) % 26 + 97)
    else:
        return char


def _decrypt_char(char: str, shift: int) -> str:
    char_code = ord(char)

    if char_code in range(65, 91):
        return chr((char_code - shift - 65) % 26 + 65)
    elif char_code in range(97, 123):
        return chr((char_code - shift - 97) % 26 + 97)
    else:
        return char


def _get_key() -> int:
    try:
        with open("./data/key.txt", "r") as file:
            key = int(file.read().split(" ")[0])
    except ValueError:
        print("invalid key")
        exit(1)

    if key < 0:
        print(f"invalid key: {key}")
        exit(1)

    return key


def encrypt():
    key = _get_key()

    with open("./data/plain.txt", "r") as file:
        plain_text = file.read()

    encrypted_text = ""
    for char in plain_text:
        encrypted_text += _encrypt_char(char, key)

    with open("./data/crypto.txt", "w") as file:
        file.write(encrypted_text)


def decrypt():
    key = _get_key()

    with open("./data/crypto.txt", "r") as file:
        encrypted_text = file.read()

    decrypted_text = ""
    for char in encrypted_text:
        decrypted_text += _decrypt_char(char, key)

    with open("./data/decrypt.txt", "w") as file:
        file.write(decrypted_text)


def find_key():
    with open("./data/crypto.txt", "r") as file:
        encrypted_text = file.read()

    with open("./data/extra.txt", "r") as file:
        helper_plain_text = file.read()

    try:
        first_letter_of_encrypted_text = encrypted_text[0]
        first_letter_of_helper_plain_text = helper_plain_text[0]
    except IndexError:
        print("files are empty!")
        exit(1)

    key = None
    for potential_key in range(1, 26):
        encrypted_first_letter_of_helper_plain_text = _encrypt_char(
            first_letter_of_helper_plain_text, potential_key
        )
        if (
            encrypted_first_letter_of_helper_plain_text
            == first_letter_of_encrypted_text
        ):
            key = potential_key
            break

    if key is None:
        print("unable to find key!")
        exit(1)

    with open("./data/key-new.txt", "w") as file:
        file.write(str(key))

    decrypted_text = ""
    for char in encrypted_text:
        decrypted_text += _decrypt_char(char, key)

    with open("./data/decrypt.txt", "w") as file:
        file.write(decrypted_text)


def break_code():
    with open("./data/crypto.txt", "r") as file:
        encrypted_text = file.read()

    output = []
    for key in range(1, 26):
        decrypted_text = ""
        for char in encrypted_text:
            decrypted_text += _decrypt_char(char, key)
        output.append(decrypted_text)

    with open("./data/decrypt.txt", "w") as file:
        file.write("\n".join(output))
