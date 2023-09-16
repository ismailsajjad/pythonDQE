a= "homEwork: this iz your homework, copy these Text to variable. You NEED TO normalize it fROM letter CASES point of View. also, create one MORE senTENCE with LAST WORDS of each existING SENtence and add it to the END OF this Paragraph. it iz misspelling here. fix❝iZ\" with correct \"is\", but ONLY when it Iz a mistAKE. last iz TO calculate number Of Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87."

# print(a)

# Normalize the text
normalize_a = a.lower()
# print(normalize_a)

# Spliting the text into sentences
sentences = a.split(". ")
# print(sentences)

# Create a new sentence using the last words of each existing sentence
last_words = [sentence.split()[-1] for sentence in sentences]
new_sentence = " ".join(last_words) + "."

# Add the new sentence to the end of the paragraph
normalize_a += " " + new_sentence
print(normalize_a)

# Calculate the number of whitespace characters

whitespace_count = sum(1 for char in a if char.isspace())
print(a)
print(f"Number of whitespace characters: {whitespace_count}")
