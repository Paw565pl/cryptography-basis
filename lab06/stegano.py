from argparse import ArgumentParser
from os import PathLike
from pathlib import Path
from sys import argv


class Steganography:
    KEY_LENGTH = 64
    MESSAGE_LENGTH_ERROR_MESSAGE = (
        f"Message must be exactly {KEY_LENGTH // 4} characters long."
    )
    CARRIER_LENGTH_ERROR_MESSAGE = "The carrier is too small."

    def __init__(
        self,
        message_file=Path("./data/mess.txt"),
        cover_file=Path("./data/cover.html"),
        watermark_file=Path("./data/watermark.html"),
        detect_file=Path("./data/detect.txt"),
    ):
        self.message_file = message_file
        self.cover_file = cover_file
        self.watermark_file = watermark_file
        self.detect_file = detect_file

    @staticmethod
    def read_file(file: int | str | bytes | PathLike[str] | PathLike[bytes]):
        with open(file, "r") as f:
            content = f.read()

        return content.strip()

    @staticmethod
    def read_file_lines(file: int | str | bytes | PathLike[str] | PathLike[bytes]):
        with open(file, "r") as f:
            content = f.readlines()

        return content

    @staticmethod
    def save_file(text: str, file: int | str | bytes | PathLike[str] | PathLike[bytes]):
        with open(file, "w", encoding="utf-8") as f:
            f.write(text)

    @staticmethod
    def base16_to_binary(hash_string):
        integer_value = int(hash_string, 16)
        binary_string = bin(integer_value)[2:]

        expected_length = len(hash_string) * 4
        if len(binary_string) < expected_length:
            binary_string = binary_string.zfill(expected_length)

        return binary_string

    @staticmethod
    def binary_to_base16(binary_string):
        integer_value = int(binary_string, 2)
        hex_string = hex(integer_value)[2:]

        expected_length = len(binary_string) // 4
        if len(hex_string) < expected_length:
            hex_string = hex_string.zfill(expected_length)

        return hex_string

    def encrypt_1(self):
        message = self.read_file(self.message_file)
        binary_hash = self.base16_to_binary(message)
        if len(binary_hash) != self.KEY_LENGTH:
            raise ValueError(self.MESSAGE_LENGTH_ERROR_MESSAGE)
        cover_html = self.read_file_lines(self.cover_file)
        if self.KEY_LENGTH > len(cover_html):
            raise Exception(self.CARRIER_LENGTH_ERROR_MESSAGE)
        updated_cover_html = ""
        for index, bit in enumerate(binary_hash):
            stripped_line = cover_html[index].replace("\n", "")
            if bit == "1":
                stripped_line += " \n"
            else:
                stripped_line += "\n"
            updated_cover_html += stripped_line
        updated_cover_html += " ".join(cover_html[self.KEY_LENGTH :])
        self.save_file(updated_cover_html, self.watermark_file)

    def decrypt_1(self):
        watermark_html = self.read_file_lines(self.watermark_file)
        binary_hash = ""
        for i in range(self.KEY_LENGTH):
            line = watermark_html[i].replace("\n", "")
            if line[-1] == " ":
                binary_hash += "1"
            else:
                binary_hash += "0"
        hex_hash = self.binary_to_base16(binary_hash)
        self.save_file(hex_hash, self.detect_file)

    def encrypt_2(self):
        message = self.read_file(self.message_file)
        binary_hash = self.base16_to_binary(message)
        if len(binary_hash) != self.KEY_LENGTH:
            raise ValueError(self.MESSAGE_LENGTH_ERROR_MESSAGE)
        cover_html = self.read_file_lines(self.cover_file)
        cover_html = "".join(cover_html).replace("  ", "")
        space_count = cover_html.count(" ")
        if self.KEY_LENGTH > space_count:
            raise Exception(self.CARRIER_LENGTH_ERROR_MESSAGE)
        updated_cover_html = ""
        cover_html = cover_html.split(" ")
        for i in range(self.KEY_LENGTH):
            bit = binary_hash[i]
            if bit == "1":
                cover_html[i] += " "
            updated_cover_html += cover_html[i] + " "
        updated_cover_html += " ".join(cover_html[self.KEY_LENGTH :])
        self.save_file(updated_cover_html, self.watermark_file)

    def decrypt_2(self):
        watermark_html = self.read_file_lines(self.watermark_file)
        binary_hash = ""
        watermark_html = "".join(watermark_html).split(" ")
        for i in range(len(watermark_html)):
            if watermark_html[i] == "":
                binary_hash += "1"
            else:
                binary_hash += "0"
        binary_hash = binary_hash.replace("01", "1")[: self.KEY_LENGTH]
        hex_hash = self.binary_to_base16(binary_hash)
        self.save_file(hex_hash, self.detect_file)

    def encrypt_3(self):
        message = self.read_file(self.message_file)
        binary_hash = self.base16_to_binary(message)
        if len(binary_hash) != self.KEY_LENGTH:
            raise ValueError(self.MESSAGE_LENGTH_ERROR_MESSAGE)
        cover_html = self.read_file_lines(self.cover_file)
        cover_html = [line.replace("styl=", "style=") for line in cover_html]
        style_attribute_count = "".join(cover_html).count("style=")
        if self.KEY_LENGTH > style_attribute_count:
            raise Exception(self.CARRIER_LENGTH_ERROR_MESSAGE)
        updated_cover_html = ""
        current_bit_index = 0
        for line in cover_html:
            if "style=" in line and current_bit_index < len(binary_hash):
                if binary_hash[current_bit_index] == "1":
                    line = line.replace("style=", "styl=")
                updated_cover_html += line
                current_bit_index += 1
            else:
                updated_cover_html += line
        self.save_file(updated_cover_html, self.watermark_file)

    def decrypt_3(self):
        watermark_html = self.read_file_lines(self.watermark_file)
        binary_hash = ""
        for line in watermark_html:
            if "style=" in line:
                binary_hash += "0"
            elif "styl=" in line:
                binary_hash += "1"
            if len(binary_hash) == self.KEY_LENGTH:
                break
        hex_hash = self.binary_to_base16(binary_hash)
        self.save_file(hex_hash, self.detect_file)

    def encrypt_4(self):
        message = self.read_file(self.message_file)
        binary_hash = self.base16_to_binary(message)
        if len(binary_hash) != self.KEY_LENGTH:
            raise ValueError(self.MESSAGE_LENGTH_ERROR_MESSAGE)
        cover_html = self.read_file_lines(self.cover_file)
        cover_html = [line.replace("<h1></h1>", "") for line in cover_html]
        h1_tag_count = "".join(cover_html).count("<h1>")
        if self.KEY_LENGTH > h1_tag_count:
            raise Exception(self.CARRIER_LENGTH_ERROR_MESSAGE)
        updated_cover_html = ""
        current_bit_index = 0
        for line in cover_html:
            if "<h1>" in line and current_bit_index < len(binary_hash):
                if binary_hash[current_bit_index] == "1":
                    line = line.replace("<h1>", "<h1></h1><h1>")
                elif binary_hash[current_bit_index] == "0":
                    line = line.replace("</h1>", "</h1><h1></h1>")
                updated_cover_html += line
                current_bit_index += 1
            else:
                updated_cover_html += line
        self.save_file(updated_cover_html, self.watermark_file)

    def decrypt_4(self):
        watermark_html = self.read_file_lines(self.watermark_file)
        binary_hash = ""
        for line in watermark_html:
            if "<h1></h1><h1>" in line:
                binary_hash += "1"
            elif "</h1><h1></h1>" in line:
                binary_hash += "0"
            if len(binary_hash) == self.KEY_LENGTH:
                break
        hex_hash = self.binary_to_base16(binary_hash)
        self.save_file(hex_hash, self.detect_file)


def main():
    parser = ArgumentParser(
        description="steganography implementation with html file as carrier"
    )

    operation_group = parser.add_mutually_exclusive_group(required=True)
    operation_group.add_argument("-e", help="encrypt", action="store_true")
    operation_group.add_argument("-d", help="decrypt", action="store_true")

    mode_group = parser.add_mutually_exclusive_group(required=True)
    mode_group.add_argument(
        "-1",
        help="each bit of the hidden message will be conveyed as an additional space at the end of each line",
        action="store_true",
    )
    mode_group.add_argument(
        "-2",
        help="each bit of the hidden message will be hidden as a single or double space",
        action="store_true",
    )
    mode_group.add_argument(
        "-3",
        help="bits of the hidden message will be conveyed as false typos in attribute names",
        action="store_true",
    )
    mode_group.add_argument(
        "-4",
        help="bits of the hidden message will be encoded as unnecessary opening and closing tag sequences",
        action="store_true",
    )

    parser.parse_args()

    operation_argument = argv[1]
    mode_argument = argv[2]

    s = Steganography()
    args_to_function = {
        "-e": {
            "-1": s.encrypt_1,
            "-2": s.encrypt_2,
            "-3": s.encrypt_3,
            "-4": s.encrypt_4,
        },
        "-d": {
            "-1": s.decrypt_1,
            "-2": s.decrypt_2,
            "-3": s.decrypt_3,
            "-4": s.decrypt_4,
        },
    }

    args_to_function[operation_argument][mode_argument]()
    print("done!")


if __name__ == "__main__":
    main()
