from hashlib import md5
from secrets import randbelow as random

from PIL import Image


def save_image(original_image: Image, data: list[int], save_path: str) -> None:
    bytes_data = bytes(data)

    output_image = original_image.copy()
    output_image.frombytes(bytes_data)
    output_image.save(save_path)


def generate_keys(key_count: int) -> list[bytes]:
    keys = [
        md5(str(random(100) * x).encode("UTF-8")).digest() for x in range(key_count)
    ]
    return keys


def cipher_ecb(image: Image, keys: list[bytes], block_size: int) -> None:
    image_bytes = image.tobytes()
    encrypted_data = []

    for x in range(image.size[0]):
        for y in range(image.size[1]):
            pixel_position = x * image.size[0] + y
            original_pixel = image_bytes[pixel_position]
            pixel_to_add = original_pixel ^ keys[x % block_size][y % block_size]
            encrypted_data.append(pixel_to_add)

    save_image(image, encrypted_data, "./data/ecb_crypto.bmp")


def cipher_cbc(image: Image, keys: list[bytes], key: int) -> None:
    image_bytes = image.tobytes()
    size = image.size

    encrypted_data = [image_bytes[0] ^ key]
    for x in range(size[0] * size[1]):
        encrypted_data.append(
            encrypted_data[x - 1] ^ image_bytes[x] ^ keys[x % 64 // 8][x % 8]
        )

    save_image(image, encrypted_data, "./data/cbc_crypto.bmp")


def main():
    plain_image = Image.open("./data/plain.bmp")

    block_size = 8
    keys = generate_keys(block_size)

    cipher_ecb(plain_image, keys, block_size)
    cipher_cbc(plain_image, keys, 13)

    print("done!")


if __name__ == "__main__":
    main()
