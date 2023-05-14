# Answering Question About your Documents Using LangChain (and NOT OpenAI)
author:: Fabio Matricardi
source:: [Answering Question About your Documents Using LangChain (and NOT OpenAI)](https://artificialcorner.com/answering-question-about-your-documents-using-langchain-and-not-openai-2f75b8d639ae)
clipped:: [[2023-05-07]]
published:: 

#clippings

## How to use Hugging Face LLM (open source LLM) to talk to your documents, pdfs and also articles from webpages.

[

![Fabio Matricardi](https://miro.medium.com/v2/resize:fill:88:88/1*p4ShYlP7zymOUeIZ5DSbfg.png)









](https://medium.com/@fabio.matricardi?source=post_page-----2f75b8d639ae--------------------------------)[

![Artificial Corner](https://miro.medium.com/v2/resize:fill:48:48/1*e1-WDgc0KCMKp_rHX9TyQQ.png)











](https://artificialcorner.com/?source=post_page-----2f75b8d639ae--------------------------------)

This is the first step, finally. I have been searching for months everywhere.

All the articles, tutorials and youtube videos only teach you how to do things… with OpenAI. But honestly this is quite frustrating. First of all the basis for all the AI models come from academics: and secondly I cannot believe that we are forced to do things when there is a big community working behind the scenes.

![](https://miro.medium.com/v2/resize:fit:1400/1*YuQ5UkFGbQm5Tj1u43OeRQ.jpeg)

image modified by the author: original Photo by [Levart\_Photographer](https://unsplash.com/@siva_photography?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/photos/drwpcjkvxuU?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

Here I am going to show how to use a free tier of Google Colab Notebook to interact with any documents (I will cover here text files, pdf files and website url) without using OpenAI at all. Due to the computational limitation we are going to use Hugging Face API and completely open sources LLM to interact with our documents leveraging LangChain library.

I am intrigued in the technology behind text generation, and as an engineer I want to experiment. But also as a human and as a teacher I believe is more important to know the tools and have the thinking tools about Artificial Intelligence.

I strongly recommend you to read the amazing article from James Plunkett “On generative AI and not being free”. Quoting him:

> Is technology really the neutral tool that we often imagine it to be? i.e. is technology something we invent and then decide how to use?

Spoiler alert: the answer is no.

So I believe our struggles to understand and know what happens in the black box of the AI thing is the first step to be able to ask the correct questions and open the debate. A discussion where ethical and philosophical implications cannot be avoided and must be declined with sociology, politics and economical concepts.

**And now let’s go to our python code**

PS: the code of this article is on my github repo and you can [take it from here](https://github.com/fabiomatricardi/cdQnA/blob/acae54d6e6746f7a783320109b451f510fcc8f91/TalkToYourDocumentsWithHuggingFaceLLM.ipynb).

We will use Google Colab notebook to ask question on our set of documents. What you will need:

-   be registered in Hugging Face website (https://huggingface.co/)
-   create an Hugging Face Access Token (like the OpenAI API,but free)

Go to [Hugging Face](https://huggingface.co/) and register to the website

![](https://miro.medium.com/v2/resize:fit:1400/1*CavHcoH8iDoz5RfhiTHcuA.png)

1.  Go to your *profile icon* (top right corner)
2.  Select *Settings*
3.  On the left panel select *Access Token*
4.  Click on New Token
5.  *Show* or *copy* to save it in a secret place… (and for using it in this tutorial)

Google colab is amazing. Even in the free tier you have access to a runtime with 12 Gb of RAM, and you have also 1 (random) GPU runtime, but you cannot choose what kind of GPU…

or this tutorial there is no need of GPU, only CPU. In the next article I will try to use a local LLM, so in that case we will need it.

Open a new Notebook and let’s start with the installation of all the packages and libraries required. The idea is that we will bind LangChain to the HuggingFace Embeddings, feed the pipeline with Similarity Search into a brand new created vectorized database with our documents, give it to LLM with the HuggingFace Access Token together with our question, and get the answer.

!pip install langchain  
!pip install huggingface\_hub  
!pip install sentence\_transformers  
!pip install faiss-cpu  
!pip install unstructured  
!pip install chromadb  
!pip install Cython  
!pip install tiktoken  
!pip install unstructured\[local-inference\]

*LangChain*, *Huggingface\_hub* and *sentence\_transformers* are the core of the interaction with our data and with the LLM model. *FAISS-Cpu* is a library for efficient similarity search and clustering of dense vectors. It contains algorithms that search in sets of vectors of any size, up to ones that possibly do not fit in RAM. It also contains supporting code for evaluation and parameter tuning. Faiss is written in C++ with complete wrappers for Python/numpy. It is developed by Facebook AI Research.

*Unstructured* and *chromadb* are strictly related to database vectorization and we will use it specifically on the pdf part.

The installation may take some time (on my colab around 2 minutes…)

![](https://miro.medium.com/v2/resize:fit:1400/1*TvHo2YNkcQM9l-vAzZpVaQ.png)

After the installation is completed RESTART the RUNTIME (anyway Colab will tell you…)

![](https://miro.medium.com/v2/resize:fit:1400/1*LPEMc3sK6yu0I8xrLIZtRQ.png)

Let’s import the libraries and set our Access Token for Hugging Face

import os  
import requests  
os.environ\["HUGGINGFACEHUB\_API\_TOKEN"\] = "XXXXXXXXXXXXXXX"

replace the XXXXXXX with your access token (should start with `hf_..` )

from langchain.document\_loaders import TextLoader    
from langchain.text\_splitter import CharacterTextSplitter   
from langchain.embeddings import HuggingFaceEmbeddings   
  
from langchain.vectorstores import FAISS    
from langchain.chains.question\_answering import load\_qa\_chain  
from langchain import HuggingFaceHub  
from langchain.document\_loaders import UnstructuredPDFLoader    
from langchain.indexes import VectorstoreIndexCreator   
from langchain.chains import RetrievalQA  
from langchain.document\_loaders import UnstructuredURLLoader 

You can see I commented next to the import instruction with a hint of what is the use of it…

For this part I used the text of the product [Hierarchy 4.0](https://hierarchy40.com/), directly form the video. From my github repo we download it and then we use the LangChain library to load it.

import requests  
url2 = "https://github.com/fabiomatricardi/cdQnA/raw/main/KS-all-info\_rev1.txt"  
res = requests.get(url2)  
with open("KS-all-info\_rev1.txt", "w") as f:  
  f.write(res.text)

On the right panel if you refresh the directory structure you can find the new file

![](https://miro.medium.com/v2/resize:fit:1400/1*YEO9Js953XKC-_ybKzjkLQ.png)

now that the file is our notebook main directory let’s load it and prepare a function to wrap the text in chunks (anyway langchain has also a method for this…)

  
from langchain.document\_loaders import TextLoader  
loader = TextLoader('./KS-all-info\_rev1.txt')  
documents = loader.load()  
import textwrap  
def wrap\_text\_preserve\_newlines(text, width=110):  
      
    lines = text.split('\\n')  
      
    wrapped\_lines = \[textwrap.fill(line, width=width) for line in lines\]  
      
    wrapped\_text = '\\n'.join(wrapped\_lines)  
    return wrapped\_text

If we go on a blank line and we run simply `documents` the txt files will be printed on the output of the executed cell.

![](https://miro.medium.com/v2/resize:fit:1400/1*Mid25CpyYfGg6bYIs-0qTQ.png)

LLM cannot accept long instructions. You may be already aware of this, if you have ever worked with ChatGPT or others… there is a token limitation.

Now we have our document next we want to divide it into smaller chunks so that we can fit this into our large language models or embeddings. Each model has a specific token size so in this case we are choosing a token size of 1000 and you want to make sure that it doesn’t exceed the token limit of the model that you’re going to be working with

For the same reason we are going to split the text in chunks and we can also set some overlap parameters (since we count to 1000 without looking at words split into half, we can set some characters backward to cover this issue). In our case we will set chunks to 1000 and overlap to 10.

  
from langchain.text\_splitter import CharacterTextSplitter  
text\_splitter = CharacterTextSplitter(chunk\_size=1000, chunk\_overlap=10)  
docs = text\_splitter.split\_documents(documents)

The results are stored in the variable docs, that is a list. If we run `len(docs)` we will get the length of the list.

NOTE: you may get a Warning during the text splitter… don’t freak out, you can forget about it.

An embedding is a numerical representation of a piece of information, for example, text, documents, images, audio, etc. The representation captures the semantic meaning of what is being embedded, making it robust for many industry applications.

Given the text “What is the meaning of elephant?”, an embedding of the sentence could be represented in a vector space, for example, with a list of 220 numbers (for example, \[0.84, 0.42, …, 0.02\]). Since this list captures the meaning, we can do exciting things, like calculating the distance between different embeddings to determine how well the meaning of two sentences matches.

Embeddings are not limited to text! You can also create an embedding of an image (for example, a list of 220 numbers) and compare it with a text embedding to determine if a sentence describes the image. This concept is under powerful systems for image search, classification, description, and more!

How are embeddings generated? The open-source library called [**Sentence Transformers**](https://www.sbert.net/index.html) and this is exactly what we are going to use.

  
from langchain.embeddings import HuggingFaceEmbeddings  
embeddings = HuggingFaceEmbeddings()

As soon as you run the code you will see that few files are going to be downloaded (around 500 Mb…). This are the binaries required to create the embeddings for HuggingFace models.

![](https://miro.medium.com/v2/resize:fit:1400/1*54EQIs1mEht7IWTjKnAH_g.png)

Now we need a Vector Store for our embeddings. We need to feed our chunked documents in a vector store for information retrieval and then we will embed them together with the similarity search on this database as a context for our LLM query.

Here we are using FAISS-cpu, and we already talked about it in the installation phase.

  
  
from langchain.vectorstores import FAISS  
db = FAISS.from\_documents(docs, embeddings)

We can now apply a similarity search directly on the database and without the use of any LLM we will receive the best hits on our search based only on semantic similarity. By default we got 4 different documents similarities, but we can specify more (or less) than that.

NOTE: you can use this method to have the references of the documents that contain a specific topic…

query = "What is Hierarchy 4.0?"  
docs = db.similarity\_search(query)

If you run the 2 cells below you can see what was the result of the search and the dimension of the docs list.

![](https://miro.medium.com/v2/resize:fit:1400/1*L2DzygKbA2j015yN2IXZFQ.png)

What we have done so far was a preparation for what’s coming next: ask a Large Language Model from Hugging Face to interact with us putting together our knowledge base and our questions.

The 2 calls required for the job and the 2 instructions are quite straight forward:

from langchain.chains.question\_answering import load\_qa\_chain  
from langchain import HuggingFaceHub

Then we define the LLM to be used with our Access Token and we tell python to start the request on our similarity search embedded with our question to the selected LLM

llm=HuggingFaceHub(repo\_id="google/flan-t5-xl", model\_kwargs={"temperature":0, "max\_length":512})  
chain = load\_qa\_chain(llm, chain\_type="stuff")

For the purpose of this test I am showing you flan-t5-xl. First of all because this is the example I got inspired from; and then because among the open-source LLM flan-t5 is strangely underrated, but really powerful. I got inspired by a youtube video by [Prompt Engineering channel](https://www.youtube.com/@engineerprompt): he is the pioneer, I just followed and experiment on that.

Ok, now we created a question-answer chain called “stuff“, to be sent to our llm (declared just above). How we ask our question? It is very easy! we give or input our question, create aa similarity search on the vectorized db and we run the chain putting all of this together,

query = "What the actual issues and drawbacks ?"  
docs = db.similarity\_search(query)  
chain.run(input\_documents=docs, question=query)

If you want an interactive question change the first line in something like this:

query = input("What is your question: ")

The result is quite good

The actual method is time consuming due to the involvement of several   
specialists and other maintenance activities have been delayed as a result.   
The new method is more efficient and can be used to solve the issue in few   
simple steps.

NOTE: the first run may be a little slow. If it takes more than 5 minutes means that you are going to get an error from the API to Hugging Face. Stop the run of the cell and try to run another one, and then run it again.

![](https://miro.medium.com/v2/resize:fit:1400/1*p_YYMZKefqyHEPuTalnnhA.png)

You can try some more questions and evaluate the answers. I believe this is already a good result.

Well why don’t we try some other Models? This was what triggered me in the first place, by the way. So first thing I thought was to use a Vicuna model (they say it has more than 90% quality of the famous GPT-4.

So I went on Hugging Face and took one good Vicuna model (eachadea/legacy-ggml-vicuna-13b-4bit) and tried it. It is very easy:

llm1=HuggingFaceHub(repo\_id="eachadea/legacy-ggml-vicuna-13b-4bit", model\_kwargs={"temperature":0, "max\_length":512})  
chain = load\_qa\_chain(llm1, chain\_type="stuff")  
  
query = "What is the case study challenge"  
docs = db.similarity\_search(query)  
chain.run(input\_documents=docs, question=query)

And here my hopes were crushed. I got an error, unexpected for me: so I tried to understand it and what I got is that you can do this search (pipeline con do specific things only…) only with text2text-generation or text-generation models.

![](https://miro.medium.com/v2/resize:fit:1400/1*DIJZLwSuxljIXPXm_sDQgw.png)

So I started browsing [HuggingFace for text2text-generation models](https://huggingface.co/models?pipeline_tag=text2text-generation&sort=downloads) . As you can see there are really a lot of them (12k).

![](https://miro.medium.com/v2/resize:fit:1400/1*9F7qT77fpa7CW96KPBPujg.png)

You will see in the [github notebook](https://github.com/fabiomatricardi/cdQnA/blob/acae54d6e6746f7a783320109b451f510fcc8f91/TalkToYourDocumentsWithHuggingFaceLLM.ipynb) all my tests: I tried out a bunch of them, and surprisingly I found some relatively small parameters models really performant (MBZUAI/LaMini-Flan-T5–783M is one of them…)

One more note: if you pick a Model too large, more likely the API is not going to be accepted and goes in timeout.

Tip&Tricks: alway verify that the model you are testing as the Inference API active/enabled. See the pictures (the first is ok, the second it is NOT ok…)

![](https://miro.medium.com/v2/resize:fit:1400/1*_PvJPKhtYoNJDcckYaA50A.png)

API ok

![](https://miro.medium.com/v2/resize:fit:1400/1*AZVPJwte0yd-cSIDGq2IKg.png)

API NOT ok

In my test I saw a lot of bad answers, but also some partially very good. Do your own attempts and choose the better for you.

llm6=HuggingFaceHub(repo\_id="MBZUAI/LaMini-Flan-T5-783M", model\_kwargs={"temperature":0, "max\_length":512})  
chain = load\_qa\_chain(llm6, chain\_type="stuff")

the results here was not bad a part some repetitions

query = "What the actual issues and drawbacks ?"  
docs = db.similarity\_search(query)  
chain.run(input\_documents=docs, question=query)

The actual issues and drawbacks of using the actual method are: 1) possibility of human error 2) incorrect impact analysis report 3) time consuming troubleshooting process 4) delayed maintenance activities 5) lack of a comprehensive overview of all signals allocated in the specified controller 6) lack of a user-friendly interface 7) lack of a comprehensive database of all the data 8) lack of a user-friendly interface 9) lack of a user-friendly interface 10) lack of a user-friendly interface

In the end I picked declare-lab/flan-alpaca-large. It works fine and there are no hallucination.

from langchain.chains.question\_answering import load\_qa\_chain  
from langchain import HuggingFaceHub  
llm2=HuggingFaceHub(repo\_id="declare-lab/flan-alpaca-large", model\_kwargs={"temperature":0, "max\_length":512})  
chain = load\_qa\_chain(llm2, chain\_type="stuff")  
query = "What the actual issues and drawbacks ?"  
docs = db.similarity\_search(query)  
chain.run(input\_documents=docs, question=query)

the results are quite good!😁

The actual method is time consuming due to the involvement of several   
specialists and other maintenance activities have been delayed as a result.   
The new method is more efficient and can be used to solve the issue in   
few simple steps.

LangChain is really an amazing library. It helps you out of the box to connect to a really big variety of documents (google docs, spreadsheets, obsidian notes…)

Ful documentation [here…](https://python.langchain.com/en/latest/modules/indexes/document_loaders.html)

In the referenced GitHub notebook I put a section for pdf and one for url. The mechanism is the same, it only changed the loader (not anymore text loader but pdf-loader\[UnstructuredPDFLoader\] and url-loader\[UnstructuredURLLoader).

For the pdf section I took from github the printed pdf of 2 articles of mine from Medium: then I copied them in a specific folder and asked UnstructuredPDFLoader to load all of them.

!wget https://github.com/fabiomatricardi/cdQnA/raw/main/PLC\_mediumArticle.pdf  
!wget https://github.com/fabiomatricardi/cdQnA/raw/main/BridgingTheGaap\_fromMedium.pdf  
!mkdir pdfs  
!cp \*pdf '/content/pdfs'

  
  
  
import os  
pdf\_folder\_path = '/content/pdfs'  
os.listdir(pdf\_folder\_path)

loaders = \[UnstructuredPDFLoader(os.path.join(pdf\_folder\_path, fn)) for fn in os.listdir(pdf\_folder\_path)\]  
loaders

After that we use *chromadb* as a vector-index database for our embeddings (without forgetting to use the *textsplitter* for our token-chunks)

index = VectorstoreIndexCreator(  
    embedding=HuggingFaceEmbeddings(),  
    text\_splitter=CharacterTextSplitter(chunk\_size=1000, chunk\_overlap=0)).from\_loaders(loaders)

  
llm2=HuggingFaceHub(repo\_id="declare-lab/flan-alpaca-large", model\_kwargs={"temperature":0, "max\_length":512})  
  
from langchain.chains import RetrievalQA  
chain = RetrievalQA.from\_chain\_type(llm=llm2,   
                                    chain\_type="stuff",   
                                    retriever=index.vectorstore.as\_retriever(),   
                                    input\_key="question")  
  
chain.run('What is the difference between a PLC and a PC?')

I found the result good

PLCs are built to operate in industrial settings with varying temperatures,   
vibrations, and humidity levels, and are highly resistant to electrical noise.

For the webpage section I selected 2 website related to PLC programming and add the urls into a list

urls = \[  
    "https://basicplc.com/plc-programming/",  
    "https://www.learnrobotics.org/blog/plc-programming-languages/"  
\]

With the same principles this time we use *UnstructuredURLLoader* to load our website content and vectorize it.

from langchain.document\_loaders import UnstructuredURLLoader  
urls \= \[  
    "https://basicplc.com/plc-programming/",  
    "https://www.learnrobotics.org/blog/plc-programming-languages/"  
\]  
loader2 = \[UnstructuredURLLoader(urls=urls)\]

*Chromadb* will throw you a warning, but well, we know we are working with a temporary db…

index2 = VectorstoreIndexCreator(  
    embedding=HuggingFaceEmbeddings(),  
    text\_splitter=CharacterTextSplitter(chunk\_size=1000, chunk\_overlap=0)).from\_loaders(loader2)

Now it is time for putting together our selected llm with the embedded vector index and our questions.

llm2=HuggingFaceHub(repo\_id="declare-lab/flan-alpaca-large", model\_kwargs={"temperature":0, "max\_length":512})  
from langchain.chains import RetrievalQA  
chain = RetrievalQA.from\_chain\_type(llm=llm2,   
                                    chain\_type="stuff",   
                                    retriever=index2.vectorstore.as\_retriever(),   
                                    input\_key="question")  
chain.run('What is ladder diagram?')

The results, in my opinion are quite good…

Ladder Logic Programming is a PLC programming language that is   
used to create a diagram that shows the connections between   
inputs and outputs. It is derived from the Relay Logic Diagrams   
and uses almost the same context.

Well that’s it for now.

The entire code of this article is [here](https://github.com/fabiomatricardi/cdQnA/blob/acae54d6e6746f7a783320109b451f510fcc8f91/TalkToYourDocumentsWithHuggingFaceLLM.ipynb) .

I suggest you to open directly it in Google Colab and save a copy.

What I would like to do next is to be able to use on Google Colab a Local Model (without any external API token) like Vicuna, Koala or Alpaca.

LangChain has the ability to connect to llama.cpp, the problem is that I don’t know how to do it.

If the community helps me I will share it gladly (how to put Vicuna up and running, how to enable the API service, activate agents and make them interact).

And why not also create a User Interface!

I will continue my quest, anyway!

If this story provided value and you wish to show a little support, you could:

1.  Clap 50 times for this story (this really, really helps me out)
2.  Follow me on Medium
3.  read my latest articles ([https://medium.com/@fabio.matricardi](https://medium.com/@fabio.matricardi))