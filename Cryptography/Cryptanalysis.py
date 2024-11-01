def create_cipher_table(common_letters):
    table = {}
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(len(alphabet)):
        table[common_letters[i]] = alphabet[i]
    return table

def crack_cipher_with_custom_table(ciphertext, table):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            if char.lower() in table:
                if char.islower():
                    decrypted_text += table[char.lower()]
                else:
                    decrypted_text += table[char.lower()].upper()
            else:
                # Nếu ký tự không có trong bảng thế, thêm vào văn bản giải mã với ký tự '?' (hoặc ký tự gốc)
                decrypted_text += char
        else:
            decrypted_text += char
    return table, decrypted_text

def main():
    # Tạo bảng thế mới
    common_letters = 'etaoinshrdlcumwfgypbvkjxqz'
    table = create_cipher_table(common_letters)

    # Nhập văn bản đã mã hoá
    ciphertext = input("Nhập văn bản đã mã hoá: ").lower()
    # Phá mã văn bản sử dụng bảng thế mới
    key, decrypted_text = crack_cipher_with_custom_table(ciphertext, table)
    print("Key tìm được:")
    print(key)
    print("Văn bản đã giải mã:", decrypted_text)

if __name__ == "__main__":
    main()
