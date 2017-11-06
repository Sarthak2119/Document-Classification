import html2text
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import os
import pickle

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
        text  = ' '.join(filteredTokens)
        return text
        # termFrequencyMap = dict()

        # for token in filteredTokens:
        #     if token not in termFrequencyMap:
        #         termFrequencyMap[token] = 0
        #     termFrequencyMap[token] += 1

readParentPath = '../doc/'
writeParentPath = '../tokenised'
hash_with_text='docText'
os.remove(hash_with_text)

for file in os.listdir(readParentPath):
    filePath = os.path.join(readParentPath, file)
    tokens = getTokenisedFromHTML(filePath)
    
    with open(hash_with_text,'a') as f:
        f.write(file+": "+tokens+'\n')

    # new_file=file+'.pkl'
    # with open(new_file,'wb') as f:
    #     pickle.dump(token,f)




# for file in