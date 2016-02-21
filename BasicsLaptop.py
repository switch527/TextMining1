#imports
import string
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize as sentTok, word_tokenize as wordTok
from nltk.stem import PorterStemmer, LancasterStemmer
from sklearn.metrics import jaccard_similarity_score as jscore
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import Counter

#tool assignment
portStem = PorterStemmer()
lanStem = LancasterStemmer()
stopWords = set(stopwords.words("english"))

#importing documents
teslaSummary1 = open("C:\Users\steve\Google Drive\Grad School\UIC\MS-MIS\IDS566\Assignment2\IPOFiles-Folder 18\Tesla Motors Inc\Tesla Motors Inc_Analyzer1_Summary.txt", "r")
teslaSummary5 = open("C:\Users\steve\Google Drive\Grad School\UIC\MS-MIS\IDS566\Assignment2\IPOFiles-Folder 18\Tesla Motors Inc\Tesla Motors Inc_Analyzer5_Summary.txt", "r")
tesSum1 = teslaSummary1.read()
tesSum5 = teslaSummary5.read()
def removeNonAscii(s): return "".join(i for i in s if ord(i)<128)
removeNonAscii(tesSum1)
for char in tesSum1:
    if ord(char)>128:
        print char


for char in tesSum1:
    x = char
    if ord(char) > 127:
        tesSum1.replace(x, ".")

tesSum1 = tesSum1.lower()
tesSum5 = tesSum5.lower()

tesSum1 = tesSum1.translate(None, string.punctuation)
tesSum5 = tesSum5.translate(None, string.punctuation)

for char in tesSum5:
    if ord(char)>127:
        tesSum5.replace(char, ' ')


def clean(x):
    #make lowercase
    readFile = x.lower()
    #remove punctuation
    readFile = readFile.translate(None, string.punctuation)
    #fix ascii issues
    for char in readFile:
        if ord(char)>128:
            readFile.replace(char, ' ')
    #tokenize
    Tokens = wordTok(readFile)
    #remove stopwords
    Tokens2 = []
    for w in Tokens:
        if w not in stopWords:
            Tokens2.append(w)
    #fix ascii again, don't know whats happening here!
    for w in Tokens2:
        for char in w:
            if ord(char) > 128:
                w.
    #stemming
    Tokens3 = []
    for w in Tokens2:
        Tokens3.append(lanStem.stem(w))
    return Tokens3
    

test = clean(tesSum1)

#read files
tesSum1 = teslaSummary1.read()
tesSum5 = teslaSummary5.read()

#stpWrds = set(stopwords.words("english"))
#print stpWrds

sum1SentTok = sentTok(tesSum1)
sum2SentTok = sentTok(tesSum2)

sum1WordTok = wordTok(tesSum1)
sum2WordTok = wordTok(tesSum2)

for w in sum1WordTok:
tryAgain + LancasterStemmer.stem('stemming')
