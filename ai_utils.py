def clean_text(text):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    filtered_text = []
    for char in text:
        if char not in punctuations:
            filtered_text.append(char)
    return ''.join(filtered_text).lower()

def count_words(text):
    cleaned = clean_text(text)
    list_text = cleaned.split()
    return len(list_text)

def percentage(part, whole):
    return (float(part) / float(whole)) * 100

def get_average(numbers):
    return sum(numbers) / len(numbers)