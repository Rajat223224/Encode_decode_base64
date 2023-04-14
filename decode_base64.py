import base64

encoded_text = input("Enter text to decode: ")

# Convert the encoded text to bytes and decode it using Base64
decoded_bytes = base64.b64decode(encoded_text.encode('utf-8'))

# Convert the decoded bytes back to a string and print it
decoded_text = decoded_bytes.decode('utf-8')
print("Decoded text:", decoded_text)
