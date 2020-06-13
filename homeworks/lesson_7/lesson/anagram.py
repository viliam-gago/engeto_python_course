def all_anagrams(words):
    if words:
        starter = set(words[0])
        for word in words:
            if set(word) != starter:
                return False
        return True
    return False


print(all_anagrams(['ship','hips']))