import base64

def main():
    try:
        # Đọc chuỗi đã mã hóa từ file
        with open("data.txt", "r") as file:
            encoded_string = file.read().strip()

        # Giải mã base64
        decoded_bytes = base64.b64decode(encoded_string)
        decoded_string = decoded_bytes.decode("utf-8")

        print("String after decoding:", decoded_string)

    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
