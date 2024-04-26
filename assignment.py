import nltk
from nltk.corpus import webtext
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('webtext')
nltk.download('punkt')
english_stops = set(stopwords.words('english'))
print(english_stops)
def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()
file_path = "random_paragraphs.txt"
    # Read the contents of the file
text = read_file(file_path)
print(text)

from nltk.tokenize import word_tokenize,sent_tokenize
words= word_tokenize(text)
tokenz = []
for word in words:
    if word not in english_stops:
        tokenz.append(word)
        
print(tokenz[0:100])
k =tokenz
frequency={}
for i in k :
    if i not in frequency.keys():
        frequency[i] =0
    frequency[i] = frequency[i]+1
print(frequency)
        