multiplier_values = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]


def _encrypt_char(char: str, multiplier: int, shift: int) -> str:
    char_code = ord(char)

    if char_code in range(65, 91):
        return chr(((multiplier * (char_code - 65) + shift) % 26) + 65)
    elif char_code in range(97, 123):
        return chr(((multiplier * (char_code - 97) + shift) % 26) + 97)
    else:
        return char


def _decrypt_char(char: str, multiplier: int, shift: int) -> str:
    char_code = ord(char)
    multiplier_inv = pow(multiplier, -1, 26)

    if char_code in range(65, 91):
        return chr(((multiplier_inv * ((char_code - 65) - shift)) % 26) + 65)
    elif char_code in range(97, 123):
        return chr(((multiplier_inv * ((char_code - 97) - shift)) % 26) + 97)
    else:
        return char


def _get_key() -> tuple[int, int]:
    try:
        with open("./data/key.txt", "r") as file:
            content_list = file.read().split(" ")

        multiplier = int(content_list[0])
        shift = int(content_list[1])
        key = (multiplier, shift)
    except ValueError:
        print("invalid key")
        exit(1)

    if multiplier < 0 or shift < 0:
        print(f"invalid key: {key}")
        exit(1)

    return key


def encrypt():
    key = _get_key()

    with open("./data/plain.txt", "r") as file:
        plain_text = file.read()

    encrypted_text = ""
    for char in plain_text:
        encrypted_text += _encrypt_char(char, key[0], key[1])

    with open("./data/crypto.txt", "w") as file:
        file.write(encrypted_text)


def decrypt():
    key = _get_key()

    with open("./data/crypto.txt", "r") as file:
        encrypted_text = file.read()

    decrypted_text = ""
    for char in encrypted_text:
        decrypted_text += _decrypt_char(char, key[0], key[1])

    with open("./data/decrypt.txt", "w") as file:
        file.write(decrypted_text)


def find_key():
    with open("./data/crypto.txt", "r") as file:
        encrypted_text = file.read()

    with open("./data/extra.txt", "r") as file:
        helper_text = file.read()

    try:
        first_two_chars_of_encrypted_text = encrypted_text[0:2]
        first_two_chars_of_helper_text = helper_text[0:2]
    except IndexError:
        print("files are empty or too short!")
        exit(1)

    key = None
    for potential_multiplier in multiplier_values:
        for potential_shift in range(26):
            encrypted_first_two_chars_of_helper_text = ""
            for char in first_two_chars_of_helper_text:
                encrypted_first_two_chars_of_helper_text += _encrypt_char(
                    char, potential_multiplier, potential_shift
                )
            if (
                encrypted_first_two_chars_of_helper_text
                == first_two_chars_of_encrypted_text
            ):
                key = (potential_multiplier, potential_shift)
                break

    if key is None:
        print("unable to find key!")
        exit(1)

    with open("./data/key-new.txt", "w") as file:
        file.write(f"{key[0]} {key[1]}")

    decrypted_text = ""
    for char in encrypted_text:
        decrypted_text += _decrypt_char(char, key[0], key[1])

    with open("./data/decrypt.txt", "w") as file:
        file.write(decrypted_text)


def break_code():
    with open("./data/crypto.txt", "r") as file:
        encrypted_text = file.read()

    output = []
    for multiplier in multiplier_values:
        for shift in range(26):
            decrypted_text = ""
            for char in encrypted_text:
                decrypted_text += _decrypt_char(char, multiplier, shift)
            output.append(decrypted_text)

    with open("./data/decrypt.txt", "w") as file:
        file.write("\n".join(output))
