# 20210815 pourquoi le ML n'est pas la solution en NLU

Tags : [litNote](litNote)
Date : [[../../journals/2021-08-10]]
Src :  [[Machine Learning Won't Solve Natural Language Understanding]]

## Idée

Le [[ML]] c'est de la compression, laisser des infos de côté (le common knowledge) alors que la compréhension du language [[NLU]]  c'est du décodage / décompression  d'infos ... et donc les tentatives sont vouées à l échec. Par exemple statistiquement les 2 propals sont équivalentes: 
La coupe ne rentrait pas dans la valise car elle était 
1/ trop petite
2/ trop grande 

Lien :  

 [Machine Learning Won't Solve Natural Language Understanding](https://thegradient.pub/machine-learning-wont-solve-the-natural-language-understanding-challenge/)

#Highlights 

> Consider the most common ‘downstream NLP’ tasks:
-summarization
-topic extraction
-named-entity recognition (NER)
-(semantic) search
-automatic tagging
-clustering
All of the above tasks are consistent with the Probably Approximately Correct (PAC) paradigm that underlies all machine learning approaches. Specifically, evaluating the output of some NLP system regarding the above tasks is subjective: there is no objective criteria to judge if one summary is better than another; or if the (key) topics/phrases extracted by some system are the better than those extracted by another system, etc. However, language understanding does not admit any degrees of freedom. A full understanding of an utterance or a question requires understanding the one and only one thought that a speaker is trying to convey
That optimization resulted in the speaker encoding the minimum possible information that is needed, while leaving out everything else that can be safely assumed to be information that is available for the listener. The information we (all!) tend to leave out is usually information that we can safely assume to be available for both speaker and listener, and this is precisely the information that we usually call common background knowledge
That is, for effective communication, we do not say what we can assume we all know! 
NLU is very very difficult, because a software program cannot fully understand the thoughts behind our linguistic utterances if they cannot somehow “uncover” all that stuff that humans leave out and implicitly assume in their linguistic communication. That, really, is the NLU challenge (and not parsing, stemming, POS tagging, named-entity recognition, etc.)
