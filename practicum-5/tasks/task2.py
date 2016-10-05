
# coding: utf-8

# # Building an inverted index
# 
#   - You are given a sample (1000 documents) from the [The Reuters-21578 data collection](http://www.daviddlewis.com/resources/testcollections/reuters21578/) in `data/reuters21578-000.xml`
#   - The code that parses the XML and extract a list of preprocessed terms (tokenized, lowercased, stopwords removed) is already given.
#   - You are also given an InvIndex class that manages the posting lists operations.
#   - Build an inverted index from the input collection with the term frequencies stored.
#   - Save the inverted index to a text file. E.g., `termID docID1:freq1 docID2:freq2 ...`.

# In[1]:

from xml.dom import minidom
from collections import Counter
import re


# ## Parsing documents

# Stopwords list

# In[2]:

stopwords = ["a", "an", "and", "are", "as", "at", "be", "but", "by", "for", "if", "in", "into", "is", "it", "no", "not", "of", "on", "or", "such", "that", "the", "their", "then", "there", "these", "they", "this", "to", "was", "will", "with"]


# Stripping tags inside <> using regex

# In[3]:

def striptags(text):
    p = re.compile(r'<.*?>')
    return p.sub('', text)


# Parse input text and return a list of indexable terms

# In[4]:

def parse(text):
    terms = []
    # Replace specific characters with space
    chars = ["'", ".", ":", ",", "!", "?", "(", ")"]
    for ch in chars:
        if ch in text:
            text = text.replace(ch, " ")

    # Remove tags
    text = striptags(text)

    # Tokenization
    for term in text.split():  # default behavior of the split is to split on one or more whitespaces
        # Lowercasing
        term = term.lower()
        # Stopword removal
        if term in stopwords:
            continue
        terms.append(term)

    return terms


# ## Processing the input document collection
# 
#   - The collection is given as a single XML file. 
#   - Each document is inside `<REUTERS ...> </REUTERS>`.
#   - We extract the contents of the `<DATE>`, `<TITLE>`, and `<BODY>` tags.
#   - After each extracted document, the provided callback function is called and all document data is passed in a single dict argument.

# In[5]:

def process_collection(input_file, callback):
    xmldoc = minidom.parse(input_file)
    # Iterate documents in the XML file
    itemlist = xmldoc.getElementsByTagName("REUTERS")
    doc_id = 0
    for doc in itemlist:
        doc_id += 1
        date = doc.getElementsByTagName("DATE")[0].firstChild.nodeValue
        # Skip documents without a title or body
        if not (doc.getElementsByTagName("TITLE") and doc.getElementsByTagName("BODY")):
            continue
        title = doc.getElementsByTagName("TITLE")[0].firstChild.nodeValue
        body = doc.getElementsByTagName("BODY")[0].firstChild.nodeValue
        callback({
            "doc_id": doc_id,
            "date": date,
            "title": title,
            "body": body
            })


# Prints a document's contents (used as a callback function passed to `process_collection`)

# In[6]:

def print_doc(doc):
    if doc["doc_id"] <= 5:  # print only the first 5 documents
        print("docID:", doc["doc_id"])
        print("date:", doc["date"])
        print("title:", doc["title"])
        print("body:", doc["body"])
        print("--")


# In[7]:

process_collection("../data/reuters21578-000.xml", print_doc)


# ## Inverted index
# 
#   - The inverted index is an object with methods for adding and fetching postings.
#   - The data is stored in a map, where keys are terms and values are lists of postings.
#   - Each posting is an object that holds the doc_id and an optional payload.

# In[8]:

class Posting(object):
    def __init__(self, doc_id, payload=None):
        self.doc_id = doc_id
        self.payload = payload


# In[9]:

class InvIndex(object):

    def __init__(self):
        self.index = {}

    # Add a document to the posting list of a term
    def add_posting(self, term, doc_id, payload=None):
        if term not in self.index:  # if term not in index, initialize empty posting list
            self.index[term] = []
        # append new posting to the posting list
        self.index[term].append(Posting(doc_id, payload))

    # Get the posting list for a given term
    def get_postings(self, term):
        if term in self.index:
            return self.index[term]
        return None

    # Returns all unique terms in the index
    def get_terms(self):
        return self.index.keys() 


# ### Creating an inverted index from the input collection

# In[10]:

ind = InvIndex()

def index_doc(doc):
    text = doc["title"] + " " + doc["body"]
    terms = parse(text)  # list of terms in the document
    if doc["doc_id"] <= 5:  # print preprocessed contents for the first 5 docs
        print("docID:", doc["doc_id"])        
        print(terms)

    # TODO index the document (add all terms with freqs using `ind.add_posting()`)
    
process_collection("../data/reuters21578-000.xml", index_doc)


# #### Saving inverted index to file

# In[11]:

# TODO


# ## Questions
# 
#   - How much space does the inverted index occupy?
#   - How much space would be needed if the same information was stored in a document-term matrix?
