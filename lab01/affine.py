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
    pass


def break_code():
    pass
