def search4vowels(phrase: str) -> set:
    """Search for vowels and return these values from a word"""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))


def search4letters(phrase: str, letters: str= 'aeiou') -> set:
    """Return the set of letters from 'letters' found in 'phrase'"""
    return set(letters).intersection(set(phrase))
