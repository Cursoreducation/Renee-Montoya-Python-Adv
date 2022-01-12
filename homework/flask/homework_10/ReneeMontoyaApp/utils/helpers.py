import hashlib


def convert_list(list):
    json_list = []
    for el in list:
        json_list.append(el.serialize)
    return json_list

def encrypt_string(hash_string):
    sha_signature = \
        hashlib.sha256(hash_string.encode()).hexdigest()
    return sha_signature
