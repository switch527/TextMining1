
#initial setup to get stop words and such
#import nltk
#nltk.download()

#import tools
import string
import math
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize as sentTok, word_tokenize as wordTok
from nltk.stem import PorterStemmer, LancasterStemmer
from sklearn.metrics import jaccard_similarity_score as jscore
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from collections import Counter

#assign tools
portStem = PorterStemmer()
lanStem = LancasterStemmer()
stopWords = set(stopwords.words("english"))
tfidf_vectorizer = TfidfVectorizer()

#print stopWords

#importing and reading the documents
teslaSummary1 = open("D:\Google Drive\Grad School\UIC\MS-MIS\IDS566\Assignment2\IPOFiles-Folder 18\Tesla Motors Inc\Tesla Motors Inc_Analyzer1_Summary.txt", "r")
teslaSummary5 = open("D:\Google Drive\Grad School\UIC\MS-MIS\IDS566\Assignment2\IPOFiles-Folder 18\Tesla Motors Inc\Tesla Motors Inc_Analyzer5_Summary.txt", "r")
tesSum1 = teslaSummary1.read()
tesSum5 = teslaSummary5.read()

#lower case
tesSum1 = tesSum1.lower()
tesSum5 = tesSum5.lower()

#remove punctuation
tesSum1 = tesSum1.translate(None, string.punctuation)
tesSum5 = tesSum5.translate(None, string.punctuation)

#print tesSum1
#print tesSum5

#sentence tokenization just for fun
#sum1Sent = sentTok(tesSum1)
#sum5Sent = sentTok(tesSum5)

#word tokenization
sum1Word = wordTok(tesSum1)
sum5Word = wordTok(tesSum5)
#print sum1Word
#print sum5Word
    
#filtering out stopwords from nltk.corpus
sum1Filtered = []
for w in sum1Word:
    if w not in stopWords:
        sum1Filtered.append(w)
#print sum1Filtered

sum5Filtered = []
for w in sum5Word:
    if w not in stopWords:
        sum5Filtered.append(w)
#print sum5Filtered

#loops to find and fix ascii decoding problems. Run first loop and if anything displays run second loop
for w in sum1Filtered:
    for char in w:
        if ord(char)>127:
             print char

for w in sum1Filtered:
    for char in w:
        if ord(char) > 127:
             sum1Filtered.remove(w)

for w in sum5Filtered:
    for char in w:
        if ord(char)>127:
             print char

for w in sum5Filtered:
    for char in w:
        if ord(char) > 127:
             sum5Filtered.remove(w)


#stemming experiments
sum1Stemmed = []
for w in sum1Filtered:
    sum1Stemmed.append(lanStem.stem(w))
#print sum1Stemmed

sum5Stemmed = []
for w in sum5Filtered:
    sum5Stemmed.append(portStem.stem(w))
#print sum5Stemmed

#word count
sum1TF = Counter(sum1Stemmed)
sum5TF = Counter(sum5Stemmed)

#sub linear TF Scaling
for key in sum1TF:
    x = sum1TF[key]
    if x > 0:
        sum1TF[key] =  1 + math.log(x)

for key in sum5TF:
    x = sum5TF[key]
    if x > 0:
        sum5TF[key] =  1 + math.log(x)


intersection = sum1TF & sum5TF
union = dict(sum1TF.items() + sum5TF.items())

#Calculating Jaccard Similarity
interSum = float(sum(intersection.values()))
#print interSum
unSum = float(sum(union.values()))
#print unSum
jaccard = interSum/unSum
#print jaccard

#calculating Cosine Similarity
sum1 = 
sum1Matrix = tfidf_vectorizer.fit_transform(sum1Stemmed, sum5Stemmed)
cosine_similarity(sum1Matrix[0:1], sum1Matrix)
