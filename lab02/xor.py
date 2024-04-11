from sys import argv

LINE_LENGTH = 64


def get_key() -> str:
    with open("./data/key.txt", "r") as file:
        key = file.read().strip()

    if len(key) != LINE_LENGTH:
        print(f"key is invalid! required length is {LINE_LENGTH}")
        exit(1)

    return key


def onetime_cypher(plain_text: str, key: str) -> str:
    # encrypted_text = ''.join(chr(ord(c) ^ ord(k)) for c, k in zip(plain_text, key))  # - non-binary version
    encrypted_text = "".join(
        bin(ord(c) ^ ord(k))[2:].zfill(8) for c, k in zip(plain_text, key)
    )

    return encrypted_text


def prepare_text():
    with open("./data/orig.txt", "r") as file:
        text = file.read().replace("\n", " ").strip()

    lines = [text[i: i + LINE_LENGTH] for i in range(0, len(text), LINE_LENGTH)]

    with open("./data/plain.txt", "w") as file:
        file.write("\n".join(lines))


def encrypt():
    key = get_key()

    with open("./data/plain.txt", "r") as file:
        plain_text_lines = file.readlines()

    encrypted_lines = [onetime_cypher(line, key) for line in plain_text_lines]

    with open("./data/crypto.txt", "w") as file:
        file.write("\n".join(encrypted_lines))


def cryptanalysis():
    with open("data/crypto.txt", "r") as f:
        text = [
            list(map("".join, zip(*[iter(line.replace("\n", ""))] * 8))) for line in f
        ]

    max_len = max(len(row) for row in text)

    for column_index in range(max_len):
        for row in text:
            if (
                    column_index < len(row)
                    and len(row[column_index]) > 1
                    and row[column_index][1] == "1"
            ):
                reset_char = row[column_index]
                for i in range(len(text)):
                    if column_index < len(text[i]):
                        coded_char = text[i][column_index]
                        try:
                            coded_line = "".join(
                                "1" if int(coded_char[j]) ^ int(reset_char[j]) else "0"
                                for j in range(8)
                            )
                            decoded_char = chr(int(coded_line, 2))
                            if decoded_char.isalpha() or decoded_char.isspace():
                                text[i][column_index] = decoded_char
                            else:
                                text[i][column_index] = "_"
                        except ValueError:
                            text[i][column_index] = "_"

    with open("data/decrypt.txt", "w") as f:
        for row in text:
            f.write("".join(row) + "\n")


def krypto_analysis():
    with open("data/crypto.txt", "r") as f:
        text = f.read()
        text = text.replace("\n", "*")
        text = text.split("*")
        text.pop(len(text) - 1)

    for index, line in enumerate(text):
        output = [line[i:i + 8] for i in range(0, len(line), 8)]
        text[index] = output

    for row_index, row in enumerate(text):
        for column_index, column in enumerate(row):
            reset_char = False
            if len(column) > 1:
                if column[1] == "1":
                    reset_char = column
                if reset_char:
                    for i in range(len(text)):
                        coded_char = text[i][column_index]
                        coded_line = ""
                        for j in range(8):
                            result = int(coded_char[j]) ^ int(reset_char[j])
                            if result:
                                coded_line += "1"
                            else:
                                coded_line += "0"
                        if coded_line == "00000000":
                            text[i][column_index] = " "
                        else:
                            text[i][column_index] = chr(int(coded_line, 2))

    with open("data/decrypt.txt", "w") as f:
        for row in text:
            for column in row:
                f.write(column)
            f.write("\n")
    return True


try:
    arg = argv[1]
except IndexError:
    print("please provide argument")
    exit(1)

arg_options = ["-p", "-e", "-k"]

if arg not in arg_options:
    print("invalid argument")
    exit(1)

args_to_function = {
    "-p": prepare_text,
    "-e": encrypt,
    "-k": krypto_analysis
}

args_to_function[arg]()
print("done!")
# TODO: fix cryptoanalysis
