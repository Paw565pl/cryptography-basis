import random
from argparse import ArgumentParser
from math import gcd
from pathlib import Path

INPUT_FILE_PATH = Path("./data/input.txt")
OUTPUT_FILE_PATH = Path("./data/output.txt")

PRIME_NUMBER_MESSAGE = "probably prime number"
COMPOSITE_NUMBER_MESSAGE = "composite number"


def fermat_test(n: int) -> None:
    with open(OUTPUT_FILE_PATH, "w") as output_file:
        random.seed(a=555)
        base = random.randint(2, n - 1)

        exponent = n - 1
        result = pow(base, exponent, n)

        if result != 1:
            output_file.write(COMPOSITE_NUMBER_MESSAGE)
        else:
            output_file.write(PRIME_NUMBER_MESSAGE)


def rabin_miller_test(
        n: int, helper1: int | None = None, helper2: int | None = None
) -> None:
    with open(OUTPUT_FILE_PATH, "w") as output_file:
        if helper2:
            exponent = (helper1 * helper2) - 1

            for _ in range(0, 40):
                power_of_two = 0
                previous_result = 0
                first = True
                random_number = random.randint(2, n - 1)

                if gcd(random_number, n) != 1:
                    gcd_result = gcd(random_number, n)
                    output_file.write(str(gcd_result))
                    return

                while exponent % 2 != 1:
                    power_of_two += 1
                    exponent //= 2

                result = pow(random_number, exponent, n)

                if result == 1 or result == n - 1:
                    continue

                for _ in range(0, power_of_two):
                    temp_result = result
                    result = pow(result, 2, n)
                    if result == 1 and first:
                        previous_result = temp_result
                        break

                gcd_result = gcd(previous_result - 1, n)
                if gcd_result != 1:
                    output_file.write(str(gcd_result))
                    return

            output_file.write(PRIME_NUMBER_MESSAGE)

        elif helper1:
            exponent = (helper1 * helper2) - 1

            for _ in range(0, 40):
                power_of_two = 0
                previous_result = 0
                first = True
                random_number = random.randint(2, n - 1)

                if gcd(random_number, n) != 1:
                    gcd_result = gcd(random_number, n)
                    output_file.write(str(gcd_result))
                    return

                while exponent % 2 != 1:
                    power_of_two += 1
                    exponent /= 2

                result = pow(random_number, exponent, n)

                if result != 1:
                    output_file.write(
                        f"this helper number: {helper1} is not a universal exponent: ({random_number}^{helper1}) mod {n} = {result}"
                    )
                    return

                if result == 1 or result == n - 1:
                    continue

                for _ in range(0, power_of_two):
                    temp_result = result
                    result = pow(result, 2, n)
                    if result == 1 and first:
                        previous_result = temp_result
                        break

                gcd_result = gcd(previous_result - 1, n)
                if gcd_result != 1:
                    output_file.write(str(gcd_result))
                    return

            output_file.write(PRIME_NUMBER_MESSAGE)

        elif n:
            exponent = n - 1

            for _ in range(0, 40):
                power_of_two = 0
                previous_result = 0
                first = True
                random_number = random.randint(2, n - 1)

                if gcd(random_number, n) != 1:
                    gcd_result = gcd(random_number, n)
                    output_file.write(str(gcd_result))
                    return

                while exponent % 2 != 1:
                    power_of_two += 1
                    exponent //= 2

                result = pow(random_number, exponent, n)

                if result == 1 or result == n - 1:
                    continue

                for _ in range(0, power_of_two):
                    temp_result = result
                    result = pow(result, 2, n)
                    if result == 1 and first:
                        previous_result = temp_result
                        break

                if result != 1:
                    output_file.write(COMPOSITE_NUMBER_MESSAGE)
                    return
                else:
                    if (previous_result - n) != -1:
                        gcd_result = gcd(previous_result - 1, n)
                        output_file.write(str(gcd_result))
                        return

            output_file.write(PRIME_NUMBER_MESSAGE)


def main():
    parser = ArgumentParser(description="Rabin-miller and Fermat test implementation")
    parser.add_argument("-f", help="Fermat test", action="store_true")
    args = parser.parse_args()

    with open(INPUT_FILE_PATH, "r") as input_file:
        n = int(input_file.readline())

        try:
            helper1 = int(input_file.readline())
        except ValueError:
            helper1 = None

        try:
            helper2 = int(input_file.readline())
        except ValueError:
            helper2 = None

    if args.f:
        fermat_test(n)
    else:
        rabin_miller_test(n, helper1, helper2)

    print("done!")


if __name__ == "__main__":
    main()
