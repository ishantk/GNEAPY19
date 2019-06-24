import re

quote = "Search the candle rather than cursing the darkness"

# result = re.match("Search", quote)
# result = re.match("rather", quote)
# print(result)

# result = re.search("the", quote)
# print(result)

result = re.findall("the", quote)
print(result)

result = re.split("the", quote)
print(result)

result = re.sub("the", "a", quote)
print(result)

result = re.findall(".", quote)
print(result)

result = re.findall("\w", quote)
print(result)

result = re.findall("\w*", quote)
print(result)

result = re.findall("\w+", quote)
print(result)

# Assignment
# Create a word count matrix