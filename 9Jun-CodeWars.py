def find_missing_letter(letters):
    prev = ord(letters[0])
    print(f"Orig Prev: {prev}")

    for letter in letters[1:]:
        current = ord(letter)
        print(f"Current: {current}")
        if current - prev > 1:
            return chr(prev + 1)
        prev = current
        print(f"New Prev: {prev}")

    return None  # Or any other value to indicate no missing letter


print(find_missing_letter(["a", "b", "c", "d", "f"]))
