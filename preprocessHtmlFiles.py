import html2text
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import os

def getTokenisedFromHTML(path):
    with open(path, 'r') as contentFile:
        content = contentFile.read()
        textVersion = html2text.html2text(content)
        refinedText = ""
        for char in textVersion:
            if char.isalpha():
                refinedText += char
            else:
                refinedText += " "

        lowerText = refinedText.lower()
        stopWords = set(stopwords.words('english'))
        wordTokens = word_tokenize(lowerText)
        filteredTokens = [w for w in wordTokens if (w not in stopWords and len(w) > 1)]

        termFrequencyMap = dict()

        for token in filteredTokens:
            if token not in termFrequencyMap:
                termFrequencyMap[token] = 0
            termFrequencyMap[token] += 1

readParentPath = '/home/sarthak/4yr_project/documents'
writeParentPath = '/home/sarthak/4yr_project/tokenised'

for file in os.listdir(readParentPath):
    filePath = os.path.join(readParentPath, file)
    tokens = getTokensFromHTML(filePath)


for file in