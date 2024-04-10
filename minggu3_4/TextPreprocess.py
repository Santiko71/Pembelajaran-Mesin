# TAUFIK NUR SANTIKO
# A11.2022.14184
# PEMBELAJARAN MESIN

# Dasar Text-Preprocessing

# Case Folding: Lowercase

print()

kalimat = "Berikut ini adalah 5 negara dengan pendidikan terbaik di dunia adalah Korea Selatan, Jepang, Singapura, Hong Kong, dan Finlandia."
lower_case = kalimat.lower()
print(lower_case)

print()

# Case Folding: Removing Number
import re
kalimat2 = "Berikut ini adalah 5 negara dengan pendidikan terbaik di dunia adalah Korea Selatan, Jepang, Singapura, Hong Kong, dan Finlandia."

hasil = re.sub(r"\d+", "", kalimat2)
print(hasil)

print()

# Case Folding: Removing Punctuation
import string

kalimat3 = "Ini &adalah [contoh] kalimat? {dengan} tanda. baca?!!"
hasil2 = kalimat3.translate(str.maketrans("","",string.punctuation))
print(hasil2)

print()

# Case Folding: Removing Whitespace
kalimat4 = " \t     ini kalimat contoh \t     \n"
hasil3 = kalimat4.strip()

print(hasil3)

print()

# Separating Sentences with Split () Method
kalimat5 = "rumah idaman adalah rumah uang bersih"
pisah = kalimat5.split()

print(pisah)

print()

# Tokenizing: Word Tokenizing Using NLTK Module
import nltk
from nltk.tokenize import word_tokenize

kalimat6 = "Andi kerap melakukan transaksi rutin secara daring atau online."

tokens = ntlk.tokenize.word_tokenize(kalimat6)
print(tokens)

print()

# Tokenizing with Case Folding
from nltk.tokenize import word_tokenize

kalimat7 = "Andi kerap melakukan transaksi rutin secara daring atau online."
kalimat7 = kalimat7.translate(str.maketrans('','',string.punctuation)).lower()

tokens2 = nltk.tokenize.word_tokenize(kalimat7)
print(tokens2)

print()

# Frequency Distribution
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

kalimat8 = "Andi kerap melakukan transaksi rutin secara daring atau online."
kalimat8 = kalimat8.translate(str.maketrans('','',string.punctuation)).lower()

tokens3 = nltk.tokenize.word_tokenize(kalimat8)
kemunculan = nltk.FreqDist(tokens3)

print(kemunculan.most_common())

print()

# Frequency Distribution Visualization with Matplotlib
import matplotlib.pyplot as plt

kemunculan.plot(30, cumulative = False)

plt.show()

print()

# Tokenizing: Sentences Tokenizing Using NLTK Module
from nltk.tokenize import sent_tokenize

kalimat9 = "Andi kerap melakukan transaksi rutin secara daring atau online. Menurut Andi belanja online lebih praktis & murah."

tokens4 = nltk.tokenize.sent_tokenize(kalimat9)

print(tokens4)

print()

# Filtering using NLTK
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

kalimat10 = "Andi dan icha kerap melakukan transaksi rutin secara daring atau online. Menurut Andi belanja online lebih praktis & murah."
kalimat10 = kalimat10.translate(str.makestrans('','',string.punctuation)).lower()

tokens5 = word_tokenize(kalimat10)
listStopword = set(stopwords.words('Indonesian'))

removed = []
for t in tokens5:
    if t not in listStopword:
        removed.append(t)

print(removed)

print()

# Filtering using Sastrawi: Stopword list
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

factory = StopWordRemoverFactory()
stopwords = factory.get_stop_words()
print(stopwords)

print()

# Filtering using Sastrawi
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from nltk.tokenize import word_tokenize

factory = StopWordRemoverFactory()
stopwords = factory.create_stop_word_remover()

kalimat11 = "Andi dan icha kerap melakukan transaksi rutin secara daring atau online. Menurut Andi belanja online lebih praktis & murah."
kalimat11 = kalimat11.translate(str.maketrans('','',string.punctuation)).lower()

stop = stopwords.remove(kalimat11)
tokens6 = nltk.tokenize.word_tokenize(stop)

print(tokens6)

print()

# Add Custom Stopword
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from nltk.tokenize import word_tokenize

# ambil stopword bawaan
stop_factory = StopWordRemoverFactory().get_stop_words()
more_stopword = ['daring', 'online']

kalimat12 = "Andi dan icha kerap melakukan transaksi rutin secara daring atau online. Menurut Andi belanja online lebih praktis & murah."
kalimat12 = kalimat12.translate(str.maketrans('','',string.punctuation)).lower()

# menggabungkan stopword
data = stop_factory + more_stopword

dictionary = ArrayDictonary(data)
str = StopWordRemover(dictionary)
tokens7 = nltk.tokenize.word_tokenize(str.remove(kalimat12))

print(tokens7)

print()

# Stemming : Porter Stemming ALgorithm using NLTK
from nltk.stem import PorterStemmer
ps = PorterStemmer()

kata = ["program", "programs", "programer", "programing", "programers"]

for k in kata:
    print(k, " : ", ps.stem(k))

print()

# Stemming Bahasa Indonesia using Sastrawi
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
factory = StemmerFactory()
stemmer = factory.create_stemmer()

kalimat13 = "Andi dan icha kerap melakukan transaksi rutin secara daring atau online. Menurut Andi belanja online lebih praktis & murah."

hasil4 = stemmer.stem(kalimat13)


print(hasil4)

print()