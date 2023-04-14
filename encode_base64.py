import base64

text = input("Enter text to encode: ")

# Convert the text to bytes and encode it using Base64
encoded_bytes = base64.b64encode(text.encode('utf-8'))

# Convert the encoded bytes back to a string and print it
encoded_text = encoded_bytes.decode('utf-8')
print("Encoded text:", encoded_text)
