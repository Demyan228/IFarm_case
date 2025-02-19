from time import time

from langchain_community.document_loaders import WebBaseLoader
from newspaper import Article
from process.summarization import summarize


url = "https://www.mdpi.com/2076-328X/8/7/64"
t = time()
loader = WebBaseLoader(url)
article = Article(url)
article.download()
article.parse()
docs = loader.load()
print(time() - t)
summarized_text1 = summarize(docs)
#summarized_text2 = summarize(article.text)
print(summarized_text1)