def solution(s):

    #Easier to add the braille space
    words = list(s.split())
    translation = ''
    # list of chars that have a bump at corresponding index
    # A 'per char' lookup would be more efficient, but too manual.
    # Either way, you only have upto 50 characters, so the loop runs at most 300 times.
    dot_lookup = ['abcdefghklmnopqruvxyz', 'bfghijlpqrstvw', 'klmnopqrstuvxyz', 'cdfgijmnpqstwxy', 'deghjnoqrtwyz', 'uvwxyz']
    for word in words:
        capitalized = word.isupper()
        if capitalized:
            # Braille code for when the whole word is capitalized
            translation += '000001' * 2
        for char in word:
            if char.isupper() and not capitalized:
                # Braille code for when the character is capitalized
                translation += '000001'
            low_char = char.lower()
            for dot in dot_lookup:
                translation += str(int(low_char in dot))
        # Adding a space code after each word
        translation += '000000'
    # Removing the last extra space
    translation = translation[:-6]
    return translation
