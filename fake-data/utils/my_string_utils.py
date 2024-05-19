import hashlib
import random
import string


def get_string_md5(data):
    # Create a md5 hash object
    md5_hash = hashlib.md5()

    # Update the hash object with the encoded string
    md5_hash.update(data.encode())

    # Get the hexadecimal representation of the hash
    return md5_hash.hexdigest()


def generate_salt(length):
    """
    Generate a random salt string of the given length, composed of alphanumeric characters.

    :param length: The length of the salt string to generate.
    :return: A string containing the generated salt.
    """
    if length <= 0:
        raise ValueError("Length must be a positive integer.")

    # Combine ASCII letters (both lowercase and uppercase) with digits
    characters = string.ascii_letters + string.digits

    # Use random.choices to pick 'length' random characters from the combined set
    salt = ''.join(random.choices(characters, k=length))

    return salt
