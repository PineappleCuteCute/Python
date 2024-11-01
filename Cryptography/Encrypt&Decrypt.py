def create_cipher_table(common_letters):
    # Tạo bảng thế từ chuỗi các ký tự thường gặp
    table = {}
    key = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(len(key)):
        table[key[i]] = common_letters[i]
    return table

def encrypt_with_custom_table(plaintext, table):
    # Mã hoá văn bản sử dụng bảng thế đã tạo
    encrypted_text = ""
    for char in plaintext:
        if char.isalpha():
            if char.islower():
                encrypted_text += table[char]
            else:
                encrypted_text += table[char.lower()].upper()
        else:
            encrypted_text += char
    return encrypted_text

def decrypt_with_custom_table(ciphertext, table):
    # Giải mã văn bản sử dụng bảng thế đã tạo
    decrypted_text = ""
    reverse_table = {v: k for k, v in table.items()}
    for char in ciphertext:
        if char.isalpha():
            if char.islower():
                decrypted_text += reverse_table[char]
            else:
                decrypted_text += reverse_table[char.lower()].upper()
        else:
            decrypted_text += char
    return decrypted_text

def main():
    # Tạo bảng thế mới
    common_letters = 'etaoinshrdlcumwfgypbvkjxqz'
    table = create_cipher_table(common_letters)

    # Nhập văn bản cần mã hoá
    plaintext = input("Nhập văn bản cần mã hoá: ")
    # Mã hoá văn bản sử dụng bảng thế mới
    ciphertext = encrypt_with_custom_table(plaintext, table)
    print("Văn bản đã mã hoá:", ciphertext)

    # Nhập văn bản cần giải mã
    ciphertext_input = input("Nhập văn bản cần giải mã: ")
    # Giải mã văn bản sử dụng bảng thế mới
    decrypted_text = decrypt_with_custom_table(ciphertext_input, table)
    print("Văn bản đã giải mã:", decrypted_text)

if __name__ == "__main__":
    main()
