# Two error have been found and fixed

def to_upper(string):
    result = []

    for char in string:
        if 97 <= ord(char) <= 122:
            result.append(chr(ord(char) - 32))
        else:
            result.append(char)

    return "".join(result)

def to_lower(string):
    result = []
    for char in string:
        if 65 <= ord(char) <= 90:

            # error on the below line fixed, 32 have to be plus
            result.append(chr(ord(char) + 32))

        else:
            result.append(char)
    return "".join(result)

def capitalize(string):
    result = ""
    
    # error on the below line fixed, the if condition should be based on the value of string
    if string:

        result += to_upper(string[0])
    result += to_lower(string[1:])

    return result
