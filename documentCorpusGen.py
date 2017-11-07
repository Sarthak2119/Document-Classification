import os

wordDocumentFreqPath = '/home/sarthak/4yr_project/word_doc_freq'
wordDocumentFreqData = open(wordDocumentFreqPath, "r").read().split('\n')

forbiddenWords = []
for line in wordDocumentFreqData:
    term = line.split(' ')[0]
    try:
        freq = int(line.split(' ')[1])
    except:
        continue

    if freq >= 10000 or freq <= 100 or len(term) <= 2:
        forbiddenWords.append(term)
forbiddenSet = set(forbiddenWords)

readParentPath = '/home/sarthak/4yr_project/tokenised/'
hash_with_text = '/home/sarthak/4yr_project/docText'

try:
    os.remove(hash_with_text)
except OSError:
    pass

for file in os.listdir(readParentPath):
    filePath = os.path.join(readParentPath, file)
    tokenList = open(filePath, "r").read().split(' ')

    allowedTokens = [w for w in tokenList if w not in forbiddenSet]
    tokens = ' '.join(allowedTokens)

    with open(hash_with_text, 'a') as f:
        f.write(file + ": " + tokens + '\n')
