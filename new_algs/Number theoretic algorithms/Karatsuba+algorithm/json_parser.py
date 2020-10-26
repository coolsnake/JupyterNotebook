"""
We have to implement a JSON parser (in less than 100 lines) that can parse arbitrary JSON string with the following limitations:

    - JSON primitives can be types: number, string
    - JSON data structures - list and dict which can be arbitrary nested
    - We don't support whitespaces between tokens
    - We don't support escape codes in strings.

Examples of the correct parse for some JSON strings:

'123' - 123 (number)

'"123"' - "123" (string)

'[1,2,"a"]' - [1,2,"a"] (python list)

Remember, JSON strings are always double quoted. So in the second example, we are given a string which is further enclosed in double quotes and hence
we must return a python string as output.

How does the parser work?

The driver function and the starting point of this parser is the parse function. Parse function looks at the first character of its
input and simply calls the corresponding functions. The semantics of the parse function and other parse_<type> functions are as
follows:

- Input is string
- Output is a two element array where:
    - First element is the data structure for the parsed input string
    - Second element is a string which is the part of the input string which has not been parsed

To give you a few example:
parse('123abc') = (123, "abc")

Here once the non-digit corrects are encountered, the parsing stops and the remaining string is returned in the second part of the output.

parse('"123"abc') = ("123", "abc")

Here the parsing stops once the closing double quote (") is encountered and the rest of string is returned as it is.


Hints:
 - We have given the implementation of parse_number as an example. Try implementing the parse_string function first and then move on to list and finally dict.
 - You should never need to call parse_<type> function from another parse_<type> function
 - For the list implementation, we need to parse arbitrary values inside lists and even nested lists of lists containing dictionaries.
    - But we already have a function which can parse arbitrary values. So you shouldn't have to parse values inside list.
    - parse_list function is about 10-15 lines of code. If you are writing more you are doing it wrong!

"""

class Token:
    STRING_BEGIN = STRING_END = '"'
    LIST_BEGIN = '['
    LIST_END = ']'
    LIST_DELIMITER = DICT_DELIMITER = ','
    DICT_SYMBOL = ':'
    DICT_BEGIN = '{'
    DICT_END = '}'
    WHITESPACE = ' '
    NEWLINE = '\n'

class ParserException(Exception):
    pass

def isdigit(s):
    return s in "01234567890"

def parse_string(string):
    """
    Parses first enclosing string in given string.

    Returns tuple with parsed string object and remaining literal part as
    string.
    """
    parsed = []
    for s in string[1:]:  # Skip first double quote
        if s == Token.STRING_END:
            break
        else:
            parsed.append(s)
    return ''.join(parsed), string[len(parsed) + 2:]  # Skip 2 double quotes

def parse_number(string):
    number = []
    for s in string:
        if s in "01234567890":
            number.append(s)
        else:
            break
    return int("".join(number)), string[len(number):]

def parse_list(string):
    """
    Parses first list literal in the given string. This also supports nested
    lists or any other data structure inside list.

    Returns tuple with parsed list and remaining unparsed literal as string.
    """
    # Find what part of string should be parsed
    to_be_parsed = []
    bracket_count = 0
    for s in string:
        to_be_parsed.append(s)
        if s == Token.LIST_BEGIN:
            bracket_count += 1
        elif s == Token.LIST_END:
            bracket_count -= 1
        if not bracket_count:  # When open and closing brackets are same
            break

    # Parse list
    n = 1
    parsed = []
    parsed_str = ''.join(to_be_parsed)
    unparsed = string[len(to_be_parsed):]
    while n < len(parsed_str):
      if parsed_str[n] in (Token.LIST_END, Token.LIST_DELIMITER):
        n += 1
        continue
      value = parse(parsed_str[n:])
      parsed.append(value[0])
      n += len(parsed_str[n:]) - len(value[1])
    return parsed, unparsed

def parse_dict(string):
    """
    Parses first dictionary literal in the given string. This also supports
    nested dictionaries or any other data structure inside dictionary.

    Returns tuple with parsed dictionary and remaining unparsed literal as
    string.
    """
    raise NotImplementedError

    """
    # Find what part of string should be parsed
    to_be_parsed = []
    bracket_count = 0
    for s in string:
        to_be_parsed.append(s)
        if s == Token.DICT_BEGIN:
            bracket_count += 1
        elif s == Token.DICT_END:
            bracket_count -= 1
        if not bracket_count:  # When open and closing brackets are same
            break

    # Parse dictionary
    n = 1
    parsed = {}
    parsed_str = ''.join(to_be_parsed)
    unparsed = string[len(to_be_parsed):]
    is_key = True
    while n < len(parsed_str):
      if parsed_str[n] in (Token.DICT_END, Token.DICT_DELIMITER):
        n += 1
        continue
      if parsed_str[n] == Token.DICT_SYMBOL:
        n += 1
        is_key = False
        continue

      value = parse(parsed_str[n:])
      parsed.append(value[0])
      n += len(parsed_str[n:]) - len(value[1])
    return parsed, unparsed
    """

def parse(string):
    s = string[0]
    if s == Token.STRING_BEGIN:
        return parse_string(string)
    elif s == Token.LIST_BEGIN:
        return parse_list(string)
    elif s == Token.DICT_BEGIN:
        return parse_dict(string)
    elif isdigit(s):
        return parse_number(string)
    else:
        raise ParserException("Unknown Token: %s" % s)

assert parse('123') == (123, '')
assert parse('123abc') == (123, 'abc')
assert parse('"123"abc') == ('123', 'abc')
assert parse('"abc"[123]') == ('abc', '[123]')
assert parse('[1,2,3]') == ([1,2,3], '')
assert parse('[1,2,3][abc]') == ([1,2,3], '[abc]')
assert parse('[[[]]]') == ([[[]]], '')
assert parse('[[],[[]]]') == ([[],[[]]], '')
assert parse('["a",123,["x","y"]]') == (["a", 123, ["x", "y"]], '')

# Other cases
assert parse('"123""hello"abc') == ('123', '"hello"abc')
assert parse('[]') == ([], '')
assert parse('[1,2,[3]]{1: 20}') == ([1,2,[3]], '{1: 20}')

# Dictionary
assert parse('{"a":1}') == ({"a": 1}, '')
assert parse('{"a":1,"b":2}') == ({"a":1,"b":2},'')
assert parse('{}') == ({}, '')
assert parse('{}abc') == ({}, 'abc')
assert parse('{"a":[[[]]]}') == ({"a":[[[]]]}, '')
assert parse('{"a":1,"b":[1,2,3],"c":{"d":1}}') == ({"a":1,"b":[1,2,3],"c":{"d":1}}, '')

assert parse('{"1":1}') == ({"1":1}, '')
