# Steganography implementation with html file as carrier

### How to use this program?

Launch like this:

```shell
python stegano.py [action] [method]
```

### Available options

action

- `-e` for encryption
- `-d` for decryption

method

- `-1` each bit of the hidden message will be conveyed as an additional space at the end of each line
- `-2` each bit of the hidden message will be hidden as a single or double space
- `-3` bits of the hidden message will be conveyed as false typos in attribute names
- `-4` bits of the hidden message will be encoded as unnecessary opening and closing tag sequences
