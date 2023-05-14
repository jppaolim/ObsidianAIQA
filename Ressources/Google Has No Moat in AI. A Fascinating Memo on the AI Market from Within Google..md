author:: Bret Kinsella
source:: ["Google Has No Moat" in AI. A Fascinating Memo on the AI Market from Within Google.](https://synthedia.substack.com/p/google-has-no-moat-in-ai-a-fascinating?utm_source=post-email-title&publication_id=1057898&post_id=119720798&isFreemail=true&utm_medium=email)
clipped:: [[2023-05-08]]
published:: 

#clippings

[

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffe6b8091-59ec-4c64-92b7-ef0205b6a894_840x792.jpeg)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffe6b8091-59ec-4c64-92b7-ef0205b6a894_840x792.jpeg)

TLDR;

-   A Google researcher purportedly wrote a memo suggesting Google is being complacent while open source generative AI competitors are passing it by and may make it irrelevant.
    
-   The memo goes into depth about how quickly open source solutions are advancing the market and closing the gap with the giant foundation model providers like OpenAI and Google
    
-   The thesis about Google’s risk seems on point though the conclusion about what constitutes a moat and how the market will play out ignores several important factors.
    
-   Generative AI market dynamics not only pose a risk to Google, but represent an opportunity for Nvidia, Meta, and even Amazon, as well as open source independents.
    
-   However, the assumption that generative AI will be a winner-take-all market or a duopoly is not an inevitability today. There are several ways that competition could play out and fragmentation with specialization seems likely in the LLM segment.
    

“We have no moat. And Neither does OpenAI.” This is the opening line of what is said to be an internal Google memo. The Semianalysis newsletter located the document on a public Discord server and said it received permission from the anonymous poster to republish it. We may be unable to verify that a Google researcher wrote it, and some of the thesis is questionable, but the comments are intriguing nonetheless.

“We have no moat. And neither does OpenAI.”

The purported Google researcher surmised:

> We’ve done a lot of looking over our shoulders at OpenAI. Who will cross the next milestone? What will the next move be?
> 
> But the uncomfortable truth is, *we aren’t positioned to win this arms race and neither is OpenAI*. While we’ve been squabbling, a third faction has been quietly eating our lunch.
> 
> I’m talking, of course, about open source. Plainly put, they are lapping us. **Things we consider “major open problems” are solved and in people’s hands today.**
> 
> …
> 
> While our models still hold a slight edge in terms of quality, the [gap is closing astonishingly quickly](https://arxiv.org/pdf/2303.16199.pdf). Open-source models are faster, more customizable, more private, and pound-for-pound more capable. They are [doing things with $100 and 13B params](https://lmsys.org/blog/2023-03-30-vicuna/) that we struggle with at $10M and 540B. And they are doing so in weeks, not months. This has profound implications for us:
> 
> -   **We have no secret sauce.** Our best hope is to learn from and collaborate with what others are doing outside Google. We should prioritize enabling 3P integrations.
>     
> -   **People will not pay for a restricted model when free, unrestricted alternatives are comparable in quality.** We should consider where our value add really is.
>     
> -   **Giant models are slowing us down.** In the long run, the best models are the ones which can be iterated upon quickly. We should make small variants more than an afterthought, now that we know what is possible in the <20B parameter regime.
>     

[

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8dc9b2ea-56f6-4a9d-9a26-5c8d3909e31c_1200x517.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8dc9b2ea-56f6-4a9d-9a26-5c8d3909e31c_1200x517.png)

To fully embrace this thesis, you must believe that open source will win the day in this market. Open source has indeed won the day or been a close second in a number of markets. Some examples of clear open-source successes include operating systems, web servers, databases, and content management.

In addition, open source has generally done better in infrastructure segments than at the application layer. Generative AI foundation models are infrastructure and so appear to be good candidates for open source dominance. We even have an objective example in this space that the memo highlights.

> In many ways, this shouldn’t be a surprise to anyone. The current renaissance in open source LLMs comes hot on the heels of a renaissance in image generation. The similarities are not lost on the community, with many calling this the “[Stable Diffusion moment](https://simonwillison.net/2023/Mar/11/llama/)” for LLMs.
> 
> In both cases, low-cost public involvement was enabled by a vastly cheaper mechanism for fine tuning called [low rank adaptation](https://arxiv.org/abs/2106.09685), or LoRA, combined with a significant breakthrough in scale ([latent diffusion](https://arxiv.org/abs/2112.10752) for image synthesis, [Chinchilla](https://arxiv.org/abs/2203.15556) for LLMs). In both cases, access to a sufficiently high-quality model kicked off a flurry of ideas and iteration from individuals and institutions around the world. In both cases, this quickly outpaced the large players.
> 
> These contributions were pivotal in the image generation space, setting Stable Diffusion on a different path from Dall-E. Having an open model led to [product integrations](https://github.com/AbdullahAlfaraj/Auto-Photoshop-StableDiffusion-Plugin), [marketplaces](https://civitai.com/), [user interfaces](https://github.com/AUTOMATIC1111/stable-diffusion-webui), and [innovations](https://stablediffusionweb.com/ControlNet) that didn’t happen for Dall-E.
> 
> The effect was palpable: [rapid domination](https://trends.google.com/trends/explore?date=2022-08-01%202023-04-10&q=Stable%20Diffusion,Dall-E&hl=en) in terms of cultural impact vs the OpenAI solution, which became increasingly irrelevant. Whether the same thing will happen for LLMs remains to be seen, but the broad structural elements are the same.

The memo also talks about some important technical and cost considerations, such as:

> -   Retraining models from scratch is the hard part
>     
> -   Large models aren’t more capable in the long run if we can iterate faster on small models
>     
> -   Data quality scales better than data size
>     

There are many categories of competitive moats in business. Some categories of these competitive advantages include:

-   Technology - capabilities that others cannot match
    
-   Cost - a lower cost to operate at a comparable level of quality
    
-   Capital - access to capital or lower cost of capital
    
-   Network - partners aligned with your business helping drive adoption, generally in distribution or applications but also in co-creation
    
-   Customers - a large and loyal customer base, or at least one with significant switching costs
    
-   Regulation - government protection that raises barriers to new competition
    

The memo suggests that the leaders in generative AI no longer have a technology moat. Open-source foundation models like Meta’s LLaMA offered a strong enough starting point for independent LLM developers to iterate and close the technology gap with well-financed leaders such as Google and OpenAI.

It also suggests that new techniques for model evolution diminish the importance of model re-training and dramatically reduce the cost of iterative model improvement. The progress of smaller models with high-quality datasets further reduces the cost of development and quality improvement, which may, in turn, create a disadvantage for the companies like Google and OpenAI that promote large and higher cost foundation models. And, you may note that both training and inference costs are higher when using larger models.

There is a prominent hypothesis that access to capital and low-cost computing resources provides a moat because so few companies can afford to build their own foundation models. If smaller open-source models provide adequate quality, this advantage could largely disappear.

You could surmise from the memo that Stable Diffusion has a competitive moat from a network effect of so many companies incorporating it into their products. That seems largely true. DALL-E’s market share is minimal compared to Stable Diffusion as an open-source foundation model, and Stability AI offers an enterprise-class API for that model as well.

At the same time, OpenAI’s GPT models dominate today, and it is unclear what open-source models might challenge its market position. Surely, this competition is forming, but there is no clear open source leader or large proprietary competitor in the category.

In the large language model (LLM) segment, OpenAI appears to have competitive advantages in customers, network, and potentially technology though the latter gap may be closing. OpenAI is a default, and other model makers today are competing to be the top alternative choice.

If you embrace the Google memo thesis, the moat that could save the large model technology providers is regulation. The more regulation is imposed, the harder it is for smaller companies to compete. This is a key argument against restrictive regulation today as it will lead to a higher market share concentration.

An interesting angle that is not covered in the memo is whether a rise in open source LLM model adoption could actually work out in Meta’s favor. Meta CEO Mark Zuckerberg said in a Facebook post announcing [LLaMA](https://www.facebook.com/zuck/posts/pfbid02x6hgoKQoyEK77TkrjdZR5vMX8bDvqs6U9ymQd44ZzbPE7mnK1r5PBBCmkdMPpJoil):

> Meta is committed to this open model of research and we'll make our new model available to the AI research community.

You may recall that in 2022, Meta released a much larger LLM for researchers to employ. Silcon Angle [characterized](https://siliconangle.com/2022/05/03/meta-ai-shares-opt-175b-large-language-model-ai-research-community/#:~:text=Meta%20AI%20said%20it%E2%80%99s%20aiming%20to%20democratize%20access,the%20code%20needed%20to%20train%20and%20use%20them.) that introduction saying:

> Meta AI said it’s aiming to democratize access to LLMs by sharing OPT-175B, which is an exceptionally large model with 175 billion parameters that’s trained on [publicly available data sets](https://github.com/facebookresearch/metaseq/). It said it’s the first model of this size that’s being shared with both the pretrained models and the code needed to train and use them.

There is a lot of activity around LLaMA today and that could create some network effects for Meta if its underlying foundation models become the leading choice of open source developers. What Meta decides to do with this momentum is an open question.

Nvidia could also be in this position with NeMo which is based on the original open source NeMo Megatron model. The company announced several new [smaller models](https://synthedia.substack.com/p/nvidia-is-becoming-the-giant-of-generative) in March, but they are part of a new Nvidia service. Nvidia is well positioned to be a strong competitor in the open source LLM segment but turning the open source foundation model technology into proprietary service offerings may inhibit adoption.

Please share this post. Spread knowledge, karma, and Synthedia. Thanks!

[Share](https://synthedia.substack.com/p/google-has-no-moat-in-ai-a-fascinating?utm_source=substack&utm_medium=email&utm_content=share&action=share&token=eyJ1c2VyX2lkIjoyMTk4NDUyLCJwb3N0X2lkIjoxMTk3MjA3OTgsImlhdCI6MTY4MzQ5OTE4OCwiZXhwIjoxNjg2MDkxMTg4LCJpc3MiOiJwdWItMTA1Nzg5OCIsInN1YiI6InBvc3QtcmVhY3Rpb24ifQ.PuSo4KqimM3fciBHFEqGny3oifMF0QslNQrntiM3zI4)

This may leave an open lane for Meta. Stability AI could build on its Stable Diffusion success with StableLM, but it is unclear that the success in image generation will translate directly into text. Microsoft and OpenAI are tightly joined, so they will not compete significantly in the open source segment. Hugging Face could be well positioned given its “model hub” approach, BLOOM, and willingness to build on top of other models.

Then there is Google. The company seems focused entirely on offering proprietary solutions, but would be far more formidable quickly, if it turned PaLM, or some smaller variants, into the Android of LLMs. That is essentially the thesis of the memo. If Google maintains the proprietary focus, there is an interesting opportunity for Meta, Nvidia, Hugging Face, or even Amazon to really shake up the LLM competitive landscape.

The internet age has led us to constantly view everything through the lens of network effects and increasing returns to scale. AI segments look like these factors could also apply, but it is not as clear. If size really matters in terms of performance or cost, then I would expect concentration. However, if smaller models and lower cost are on the near horizon, we could wind up with a highly fragmented market with no dominant players.

The Google researcher memo is well reasoned, but does not argue effectively that generative AI will result in “winner-take-all” market segments. It assumes Google is similar to OpenAI because they are both pursuing a similar strategy. However, OpenAI is far ahead of Google on too many product and market metrics to count. The memo is really about Google and how its current strategy provides a very narrow route to success given the market dynamics.

It seems unlikely that the LLM segment will be winner-take-all. More likely we are looking at a duopoly as the most concentrated potential outcome or what they used to call a Snow White and the Seven Dwarves model in the mainframe computing era where one leader is surrounded by a handful of smaller, but meaningful competitors.

OpenAI could disappear as a market lead much like Netscape Navigator did during the browser wars, but that seems unlikely given its LLM momentum and Microsoft support. Right now everyone in the LLM space is competing for the leading challenger spot.

With that said, what is increasingly clear is that generative AI is not a single market and the same is true for the LLM segment. The reason that fragmentation may take hold is that there is so much room for LLM specialization in different use cases and domains. This is clearly true at the application layer but also looks like it is true at the foundation model layer.

OpenAI has 22 different foundation LLM APIs available today and more are planned with some of the existing models scheduled for deprecation. Some of these are differentiated based on their size while others differ in their function. The turbo models are optimized for chat, there are moderation models, translation and speech recognition models, code generation models, and generalized models. AI21 has [six different task-specific APIs](https://synthedia.substack.com/p/ai21-labs-ramps-up-competition-with) for its LLM offerings as well as different model sizes. Alignment is happing at the model layer as well as the application layer.

[

![https://storage.googleapis.com/gweb-cloudblog-publish/original_images/workbench-2x.gif](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_lossy/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F30b3318f-bf87-4e3f-826c-1ec687416b29_1434x772.gif "https://storage.googleapis.com/gweb-cloudblog-publish/original_images/workbench-2x.gif")

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F30b3318f-bf87-4e3f-826c-1ec687416b29_1434x772.gif)

Google has problems. Open source competition is definitely one vector of competition it must confront. However, I have seen predictions of inevitable open source dominance of a sector that never materialized. In the conversational assistant space Rasa has had some success but is nowhere near dominant and Mycroft is out of business. Firefox has not displaced Chrome nor has another browser based on Chromium.

Google needs to get something in the market that works and people can access. Recent announcements of [Med-PaLM 2](https://cloud.google.com/blog/topics/healthcare-life-sciences/sharing-google-med-palm-2-medical-large-language-model) and [Cloud Security AI Workbench](https://cloud.google.com/blog/products/identity-security/rsa-google-cloud-security-ai-workbench-generative-ai) suggests it may actually be heading down this path of a specialization portfolio. With that said, Google is still very restrictive in granting access to anything and that is the most telling critique in the memo. While Google distributes solutions for very limited use, the market is passing it by with models that offer permissive use and are also very capable.

Google’s history as an exceptional fast-follower and its vast customer base and distribution assets means it could reclaim lost ground quickly. However, the window of opportunity is not unlimited and may be closing quickly. Its slow reaction has been a gift to OpenAI and all of the other would-be LLM competitors. Will it be the gift that keeps on giving?

Let me know what you think in the comments please.

[Share](https://synthedia.substack.com/p/google-has-no-moat-in-ai-a-fascinating?utm_source=substack&utm_medium=email&utm_content=share&action=share&token=eyJ1c2VyX2lkIjoyMTk4NDUyLCJwb3N0X2lkIjoxMTk3MjA3OTgsImlhdCI6MTY4MzQ5OTE4OCwiZXhwIjoxNjg2MDkxMTg4LCJpc3MiOiJwdWItMTA1Nzg5OCIsInN1YiI6InBvc3QtcmVhY3Rpb24ifQ.PuSo4KqimM3fciBHFEqGny3oifMF0QslNQrntiM3zI4)

*If you have time, I recommend you read the entire memo. Even though I have quoted it extensively here, it is a small sample of the piece. You can see the Semianalysis reposting [here](https://www.semianalysis.com/p/google-we-have-no-moat-and-neither). If for some reason that link is taken down or put behind a payment gate, let me know and I can post the full text of the memo in another location.*

![ChatGPT Plugins Alpha - Conversational Commerce, Images and UX Issues [VIDEOS]](https://substackcdn.com/image/youtube/w_728,c_limit/6wDuaEDDZck)

![Nvidia is Becoming the Giant of Generative AI](https://substackcdn.com/image/fetch/w_1300,h_650,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa8a5731f-b523-4a62-8ab6-7b9a760d2ce3_1411x797.jpeg)

Nvidia is making dozens of announcements today, and many are directly related to hardware, software, and services for generative AI. A January post by Andreessen Horowitz stated: Behind the scenes, running the vast majority of AI workloads, is perhaps the biggest winner in generative AI so far: Nvidia … They’ve built strong moats arou…