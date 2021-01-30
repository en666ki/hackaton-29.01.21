from nltk.stem import WordNetLemmatizer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import re
from string import punctuation

lemmatizer = WordNetLemmatizer()



def LemmaTextFromFile(fname):
    f = open(fname)
    rtxt = f.read()
    rtxt = re.sub(r"(<[^>]*>)([^<>]*?)(<\/[^>]*>)",'' , rtxt)
    rtxt = re.sub(r"((http|https):\/\/)*(www)*(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z0-9][a-z0-9-]{0,61}(\/*[a-zA-Z0-9]*)", "", rtxt)
    sentences = sent_tokenize(rtxt)
    txt = []
    for sentence in sentences:
        txt += [lemmatizer.lemmatize(w) for w in word_tokenize(sentence) if w not in stopwords.words('english') and w not in punctuation]
    return txt

def Similarity(lemma_text):
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.metrics.pairwise import linear_kernel
    vectorizer = TfidfVectorizer()
    vector = vectorizer.fit_transform(lemma_text)
    print(vector)


lemmatext = LemmaTextFromFile('rvision-hackathon-2021-q1/marked/Mandiant_APT1_Report.pdf.txt')
#vectorize(lemmatext)