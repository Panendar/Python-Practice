text = input("ENTER THE TEXT TO ANALYZE: ")
def filtering(text):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    filtered_text =[]
    for word in text:
        if word not in punctuations:
            filtered_text.append(word)
    return ''.join(filtered_text)

# punch_marks = "{}().,'#:"
# for mark in punch_marks:
#     paragraph = paragraph.replace (mark, " ")

# file = open("code.code", "r")
# # Read the file line by line
# lines = file.readlines() 

# print( [ line for line in lines if line.strip() == ''])

# file.close()

filtered_text = filtering(text)
print(f" THE FILTERED TEXT IS: {filtered_text}")
list_text = list(filtered_text.split())
print("========================================")
print(list_text)
total_words = print(f" TOTAL WORDS: {len(list_text)}")
print("========================================")

set_text = set(list_text)
print(f" UNIQUE WORDS: {len(set_text)}")
print("========================================")

def freq(text):
    dict_freq ={}
    for word in text:
        if word in dict_freq:
            dict_freq[word] += 1
        else:
            dict_freq[word] = 1
    return dict_freq

    
word_frequencies = freq(list_text)
print(f"WORD FREQUENCIES:{word_frequencies}")
print("========================================")

def top(text):
    sorted_words = sorted(word_frequencies.items(), key=lambda item: item[1], reverse=True)
    top_words = sorted_words[:3]
    return top_words

top_words =top(list_text)
print(f"the Top 3 words are: {top_words}")
print("========================================")