import tkinter as tk
import nltk
from textblob import TextBlob
from newspaper import Article

def Summarize():

    url=utext.get('1.0', 'end').strip()

    article=Article(url)

    article.download()
    article.parse()

    article.nlp()
    
    title.config(state='normal')
    author.config(state='normal')
    publication.config(state='normal')
    summary.config(state='normal')
    sentiment.config(state='normal')

    title.delete('1.0', 'end')
    title.insert('1.0', article.title)

    author.delete('1.0', 'end')
    author.insert('1.0', article.authors)

    publication.delete('1.0', 'end')
    publication.insert('1.0', article.publish_date)

    summary.delete('1.0', 'end')
    summary.insert('1.0', article.summary)

    analysis=TextBlob(article.text)
    sentiment.delete('1.0', 'end')
    sentiment.insert('1.0',f'polarity: {analysis.polarity}, Sentiment: {'Positive' if analysis.polarity > 0 else 'Negative' if analysis.polarity < 0 else 'Neutral'}')

    title.config(state='disabled')
    author.config(state='disabled')
    publication.config(state='disabled')
    summary.config(state='disabled')
    sentiment.config(state='disabled')



root=tk.Tk()
root.title("NEWS SUMMARIZER")
root.geometry('1200x600')


tlabel=tk.Label(root, text="Title")
tlabel.pack()

title=tk.Text(root, height=2, width=200)
title.config(state='disabled', bg="#dddddd")
title.pack()


alabel=tk.Label(root, text="Author")
alabel.pack()

author=tk.Text(root, height=2, width=200)
author.pack()

plabel=tk.Label(root, text="Publication")
plabel.pack()

publication=tk.Text(root, height=2, width=200)
publication.config(state='disabled', bg='#dddddd')
publication.pack()

slabel=tk.Label(root, text="Summary")
slabel.pack()

summary=tk.Text(root, height=20, width=200)
summary.config(state='disabled', bg='#dddddd')
summary.pack()

selabel=tk.Label(root, text="Sentiment")
selabel.pack()

sentiment=tk.Text(root, height=2, width=200)
sentiment.config(state='disabled', bg='#dddddd')
sentiment.pack()

ulabel=tk.Label(root, text="URL")
ulabel.pack()

utext=tk.Text(root, height=2, width=200)
utext.pack()

btn=tk.Button(root, text="SUMMARIZE", command=Summarize)
btn.pack()

root.mainloop()

