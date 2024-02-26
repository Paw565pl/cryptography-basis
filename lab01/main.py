from sys import argv

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


def hi():
    print("hi")


args_to_function = {
    "-c": {"-e": hi, "-d": hi, "-j": hi, "-k": hi},
    "-a": {"-e": hi, "-d": hi, "-j": hi, "-k": hi},
}

args_to_function[arg1][arg2]()
print("done!")
