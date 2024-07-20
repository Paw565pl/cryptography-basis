def get_different_bits_number(s1: str, s2: str) -> int:
    return sum(c1 != c2 for c1, c2 in zip(s1, s2))


def hex_to_bin(hex_string: str) -> str:
    return bin(int(hex_string, 16))[2:].zfill(len(hex_string) * 4)


with open("hash.txt", "r") as f:
    lines = f.readlines()

hashes: dict[str, list[str]] = {}
hash_type: str | None = None
for line in lines:
    parts = line.strip().split()
    if len(parts) == 1:
        hash_type = parts[0]
    elif len(parts) == 2 and hash_type is not None:
        if hash_type in hashes:
            hashes[hash_type].append(parts[0])
        else:
            hashes[hash_type] = [parts[0]]

with open("diff.txt", "w") as f:
    for hash_type, (hash1, hash2) in hashes.items():
        bin_hash1 = hex_to_bin(hash1)
        bin_hash2 = hex_to_bin(hash2)
        distance = get_different_bits_number(bin_hash1, bin_hash2)
        percentage_difference = (distance / len(bin_hash1)) * 100
        f.write(
            f"{hash_type}\n{hash1}\n{hash2}\nDifference: {distance} bits ({percentage_difference:.2f}%)\n\n"
        )
