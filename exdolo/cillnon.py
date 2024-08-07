# Define the punctuation characters to remove
PUNCT_TO_REMOVE = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

# Sample text
text = "Hello, world! This is an example: text with punctuation."

# Replace punctuation with spaces
text = text.translate(str.maketrans(PUNCT_TO_REMOVE, ' ' * len(PUNCT_TO_REMOVE)))

# Output the result
print(text)
