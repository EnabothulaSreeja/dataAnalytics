#password
import re
password_pattern = r"\b(?=\S{8,})(?=\S*[A-Z])(?=\S*[a-z])(?=\S*\d)(?=\S*[@#$%^&+=!])\S+\b"
text = "Please use the password Example@123"
match = re.search(password_pattern, text)
if match:
    print('Password is valid.')
else:
    print('Password is invalid.')

#url
import re
url_pattern = r"https?://(?:www\.)?[a-zA-Z0-9-]+\.[a-zA-Z]{2,6}(/[\w\-\./?%&=]*)?"
text = "Visit our site at https://www.example.com for more info."
match = re.search(url_pattern, text)
if match:
    print('Valid URL found:', match.group())
else:
    print('No valid URL found.')

#exception
def demonstrate_exceptions():
    # ZeroDivisionError
    try:
        print("ZeroDivisionError Example:")
        result = 10 / 0
    except ZeroDivisionError as e:
        print(f"Caught an exception: {e}")

    # FileNotFoundError
    try:
        print("\nFileNotFoundError Example:")
        with open('non_existent_file.txt', 'r') as file:
            content = file.read()
    except FileNotFoundError as e:
        print(f"Caught an exception: {e}")

    # IndexError
    try:
        print("\nIndexError Example:")
        my_list = [1, 2, 3]
        print(my_list[5])  # Accessing an invalid index
    except IndexError as e:
        print(f"Caught an exception: {e}")

    # ValueError
    try:
        print("\nValueError Example:")
        number = int("not_a_number")
    except ValueError as e:
        print(f"Caught an exception: {e}")

    # KeyError
    try:
        print("\nKeyError Example:")
        my_dict = {'name': 'Alice', 'age': 30}
        print(my_dict['address'])  # Key doesn't exist
    except KeyError as e:
        print(f"Caught an exception: {e}")

    # TypeError
    try:
        print("\nTypeError Example:")
        result = "string" + 10  # Adding a string and an integer
    except TypeError as e:
        print(f"Caught an exception: {e}")

    # AttributeError
    try:
        print("\nAttributeError Example:")
        my_str = "hello"
        my_str.append(' world')  # Strings do not have 'append' method
    except AttributeError as e:
        print(f"Caught an exception: {e}")

    # ImportError
    try:
        print("\nImportError Example:")
        import non_existent_module
    except ImportError as e:
        print(f"Caught an exception: {e}")

    # Exception (generic catch-all)
    try:
        print("\nGeneric Exception Example:")
        raise Exception("This is a custom exception!")
    except Exception as e:
        print(f"Caught a generic exception: {e}")

if __name__ == "__main__":
    demonstrate_exceptions()

