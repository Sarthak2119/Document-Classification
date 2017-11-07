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
        text = ' '.join(filteredTokens)
        return text


readParentPath = '/home/sarthak/4yr_project/documents/'
writeParentPath = '/home/sarthak/4yr_project/tokenised/'

wordDocumentFreqMap = dict()

for file in os.listdir(readParentPath):
    readFilePath = os.path.join(readParentPath, file)
    tokens = getTokenisedFromHTML(readFilePath)
    writeFilePath = os.path.join(writeParentPath, file)

    with open(writeFilePath, 'w') as writeFile:
        writeFile.write(tokens)

    tokenList = tokens.split(sep=' ')
    tokenSet = set(tokenList)
    for term in tokenSet:
        if term not in wordDocumentFreqMap:
            wordDocumentFreqMap[term] = 0
        wordDocumentFreqMap[term] += 1

wordDocumentFreqPath = '/home/sarthak/4yr_project/word_doc_freq'
try:
    os.remove(wordDocumentFreqPath)
except OSError:
    pass
with open(wordDocumentFreqPath, 'a') as wordDocumentFreqFile:
    for term in sorted(wordDocumentFreqMap, key=wordDocumentFreqMap.get, reverse=True):
        wordDocumentFreqFile.write(term + " " + str(wordDocumentFreqMap[term]) + "\n")
