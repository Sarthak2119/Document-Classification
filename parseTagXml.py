import xml.etree.ElementTree as ET

xmlTree = ET.parse("../tag-data.xml")
articles = xmlTree.getroot()

# map between tags and their counts
tagMap = dict()

# This loop makes a map between all the tags and count of their occurrences
for tag in articles.iter('tag'):
    tagName = tag.find('name').text
    if tagName not in tagMap:
        tagMap[tagName] = 0
    tagMap[tagName] += 1

sortedTags = []

for tagName in sorted(tagMap, key = tagMap.get, reverse = True):
    pair = [tagName, tagMap[tagName]]
    sortedTags.append(pair)

for i in range(50):
    print(sortedTags[i])

chosenClasses = ['history', 'science', 'programming', 'people', 'culture', 'art', 'politics', 'language',
                 'books', 'music', 'technology', 'religion', 'computer', 'business', 'health']