from sys import argv

import affine
import cesar

try:
    arg1 = argv[1]
    arg2 = argv[2]
except IndexError:
    print("please provide two arguments")
    exit(1)

first_arg_options = ["-c", "-a"]
second_arg_options = ["-e", "-d", "-j", "-k"]

if arg1 not in first_arg_options or arg2 not in second_arg_options:
    print("invalid arguments")
    exit(1)

args_to_function = {
    "-c": {
        "-e": cesar.encrypt,
        "-d": cesar.decrypt,
        "-j": cesar.find_key,
        "-k": cesar.break_code,
    },
    "-a": {
        "-e": affine.encrypt,
        "-d": affine.decrypt,
        "-j": affine.find_key,
        "-k": affine.break_code,
    },
}

args_to_function[arg1][arg2]()
print("done!")
