---
title:   Exploring Data Generation Methods for the Story Cloze Test
created: 2021-04-27
---

- Meta :  [[AI]] [[NLP Paper]] [[NLP Paper]]
- URL:  https://www.aclweb.org/anthology/W17-0908.pdf
- Summary : comment générer des autres fins sur le data set de ROC
- Date : [[2021-04-27]]
- paper-published: [[[[2017|]]-0
- 5]]
- **------------------------------------------------**

- [[Abstract]]: We propose a sentence-level language model which selects the next sentence in a story from a finite set of fluent alternatives. Since it does not need to model fluency, the sentence-level language model can focus on longer range dependencies, which are crucial for multi-sentence coherence. Rather than dealing with individual words, our method treats the story so far as a list of pre-trained sentence embeddings and predicts an embedding for the next sentence, which is more efficient than predicting word embeddings. Notably this allows us to consider a large number of candidates for the next sentence during training. We demonstrate the effectiveness of our approach with state-of-the-art accuracy on the unsupervised Story Cloze task and with promising results on larger-scale next sentence prediction tasks.
- [[paper-authors]]: [[Daphne Ippolito]], [[David Grangier]], [[Douglas Eck]], [[Chris Callison-Burch]],
- [paper link here](https://arxiv.org/abs/2005.05255)
- [[make]]:wide-xx [[make]]:long-xxl {{pdf: https://arxiv.org/pdf/2005.05255.pdf}}
- **# Notes**