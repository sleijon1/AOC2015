with open("input.txt") as INP:
    strings = INP.readlines()
    characters = 0
    string_characters = 0
    new_enc_chars = 0
    for string in strings:
        string = string.strip()
        characters += len(string)
        i = 0
        new_enc_chars += len(string) + 2*string.count('"')
        while i < len(string):
            if string[i] == '\\':
                i += 1
                string_characters += 1
                if string[i] in ('"', '\\'):
                    if string[i] == '\\':
                        new_enc_chars += 2
                    i += 1
                elif string[i] == 'x':
                    new_enc_chars += 1
                    # read it
                    i += 3
            elif string[i] == '"':
                i += 1
                continue
            else:
                i += 1
                string_characters += 1
print(f"Solution part 1: {characters-string_characters}")
print(f"Solution part 2: {new_enc_chars-characters}")
