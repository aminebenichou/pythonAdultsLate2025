
def hash_password(password:str, encrypt_dict):
    result=""
    i=0
    while i<len(password):
        encrypted_letter = encrypt_dict[password[i]]
        result= result + encrypted_letter


        i += 1

    return result


encrypt_dict={
    'a':'1',
    'b':'2',
    'c':'3',
    'd':'4',
    'e':'5'
}

hashed_password = hash_password('ade', encrypt_dict)

print(hashed_password)
