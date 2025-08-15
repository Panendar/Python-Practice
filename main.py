import ai_utils
sample_text = "  Hello   World  From AI  "
numbers = [85, 92, 78, 96, 88]

print(ai_utils.clean_text(sample_text))
print(ai_utils.count_words(sample_text))
print(ai_utils.get_average(numbers))
print(ai_utils.percentage(25, 100))