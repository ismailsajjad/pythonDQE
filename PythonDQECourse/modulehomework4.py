# #write a code which will:
# #1. create a list of random number of dic (from 2 to 10),
# #dic random letter key should be letter
# #dict value should be a number
# #example [{'a':5,'b':7,'g':11},{'a':3,'c':35,'g':42}]

# #2.get previously generated list of dicts and create one common list:
# #if dic have same key, we will take max value, and rename key with dict number with max value
# #if key is only in onc dict take it as is,
# #example: {'a-1':5,'b':7,'c':35,'g_2':42}

# #==================================================================================
# #create a list of random numbers from dic (from 2 to 10)
import random
import string
def getting_list1():
    list_1 = {}
    for i in range(2,10):
        key = random.choice(string.ascii_lowercase)
        # print(key)
        value = random.randint(1, 10)  # Random integer value
        list_1[key] = value
        # print(list_1)
    return list_1

def getting_list2():
    list_2 = {}
    for i in range(2,10):
        key = random.choice(string.ascii_lowercase)
        # print(key)
        value = random.randint(1, 10)  # Random integer value
        list_2[key] = value
        # print(list_2)
    return list_2

# list_1 = {'d': 5, 'k': 5, 'u': 2, 'r': 5, 's': 8}  #created dictionary
# print(list_1)
# list_2 = {'l': 1, 'd': 8, 'i': 6,'u': 5}
# print(list_2)
# # Create a merged dictionary
def first_merged_dict(list_1):
    merged_dictionary = {}
    for key, value in list_1.items():  # Merge dict1 into merged_dict
        if key in merged_dictionary:
            merged_dictionary[key] = merged_dictionary[key], value
        else:
            merged_dictionary[key] = value
    return merged_dictionary
        # print(merged_dictionary)

# # Merge dict2 into merged_dict
def second_merged_dict(list_2,merged_dictionary):
    for key, value in list_2.items():
        if key in merged_dictionary:
            merged_dictionary[f'{key}_{1}'] = max(merged_dictionary[key], value) #adding -1 to max value in merged_dictionary
        else:
            merged_dictionary[key] = value
            # Print the merged dictionary
            # print(merged_dictionary)
    return merged_dictionary
list_1 = getting_list1()
print(list_1)
list_2 = getting_list2()
print(list_2)
combined_list = [list_1,list_2]
print(combined_list)
first_merged_dictionary = first_merged_dict(list_1)
print(first_merged_dictionary)
merged_list = second_merged_dict(list_2,first_merged_dictionary)
print(merged_list)

# #---------------------------

a= "homEwork: this iz your homework, copy these Text to variable. You NEED TO normalize it fROM letter CASES point of View. also, create one MORE senTENCE with LAST WORDS of each existING SENtence and add it to the END OF this Paragraph. it iz misspelling here. fix❝iZ\" with correct \"is\", but ONLY when it Iz a mistAKE. last iz TO calculate number Of Whitespace characteRS in this Text. caREFULL, not only Spaces, but ALL whitespaces. I got 87."

# print(a)
def sentence_lower(a):
    normalize_a = a.lower()
    return normalize_a

# Normalize the text
def spliting_sentence_into_text(a):
    splitted_sentences = a.split(". ") # Spliting the text into sentences
    # print(sentences)
    return splitted_sentences

# Create a new sentence using the last words of each existing sentence
def normalize_sentence(sentences):
    last_words = [sentence.split()[-1] for sentence in sentences]
    new_sentence = " ".join(last_words) + "."
    return new_sentence

    # Add the new sentence to the end of the paragraph
def add_new_sentence(normalize_a,new_sentence):
    normalize_a += " " + new_sentence
    print(normalize_a)
    return normalize_a

# Calculate the number of whitespace characters
def calculate_whitespace(a):
    whitespace_count = sum(1 for char in a if char.isspace())
    print(a)
    print(f"Number of whitespace characters: {whitespace_count}")
    return whitespace_count

lower_sentence = sentence_lower(a)
splitted_sentences = spliting_sentence_into_text(lower_sentence)
print(splitted_sentences)
new_sentence = normalize_sentence(splitted_sentences)
print(new_sentence)
last_result = add_new_sentence(lower_sentence,new_sentence)
print(last_result)
whitespaces = calculate_whitespace(a)
print(whitespaces)




