answer1 = '''“What is machine learning?” It’s a question that opens the door to a new era of technology—one where computers can learn and improve on their own, much like humans. Imagine a world where computers don’t just follow strict rules but can learn from data and experiences. This is the essence of machine learning.
From suggesting new shows on streaming services based on your viewing history to enabling self-driving cars to navigate safely, machine learning is behind these advancements. It’s not just about technology; it’s about reshaping how computers interact with us and understand the world around them. As artificial intelligence continues to evolve, machine learning remains at its core, revolutionizing our relationship with technology and paving the way for a more connected future.'''


answer2 = '''“What is machine learning?” It’s a question that opens the door to a new era of technology—one where computers can learn and improve on their own, much like humans. Imagine a world where computers don’t just follow strict rules but can learn from data and experiences. This is the essence of machine learning.
From suggesting new shows on streaming services based on your viewing history to enabling self-driving cars to navigate safely, machine learning is behind these advancements. It’s not just about technology; it’s about reshaping how computers interact with us and understand the world around them. As artificial intelligence continues to evolve, machine learning remains at its core, revolutionizing our relationship with technology and paving the way for a more connected future.'''

#tokenization - extract words from string
token1 = answer1.split()
token2 = answer2.split()
#Remove Stop words is,am,are

'''
import nltk
nltk.download('stopwords')
'''
from nltk.corpus import stopwords
st = stopwords.words('english')
print(st)

#Change TOkens to Sets
set1 = set(token1)
set2 = set(token2)
print(len(set1),len(set2))
#remove stopwords from sets
for i in st:
    if i in set1:
        set1.discard(i)
    if i in set2:
        set2.discard(i)

print(len(set1),len(set2))
#Jaccards Index
union_res = set1.union(set2)
int_res = set1.intersection(set2)
print(len(int_res)/len(union_res)*100)
