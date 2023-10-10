def is_keyword(input_str):
    # List of reserved keywords
    keywords = ["int", "string", "float", "char", "long", "short", "double", "if", "else", "for", "while", "do", "break", "void", "continue"]

    if input_str in keywords:
        return True
    return False


def is_valid_identifier(input_str):
    # Check the first character
    if not (input_str[0].isalpha()):
        return False  # Doesn't start with a letter

    # Check the remaining characters
    for char in input_str[1:]:
        if not (char.isalnum() or char == '_'):
            return False  # Contains invalid characters
    return True  # It's a valid identifier


def main():
    flag = 0
    keyword = ["int", "string", "float", "char", "long", "if", "else", "for", "while", "do", "break", "default"]

    # Input
    a = input("Enter the identifier: ")

    if is_keyword(a):
        flag = 1
        print(f"{a} is not valid, since it's a keyword")
    else:
        flag = 0

    if a[0].isalpha():  # Checks if the first char is an alphabetical letter
        for char in a[1:]:  # Checks if every other char is an alphanumeric symbol or an underscore
            if not (char.isalnum() or char == '_'):
                flag = 1
                break
    else:
        flag = 1

    if flag == 0:
        print(f"{a} is a valid identifier.")
    else:
        print(f"{a} is not a valid identifier.")


if __name__ == "__main__":
    main()
