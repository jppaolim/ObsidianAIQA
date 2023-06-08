# A guide to prompting AI (for what it is worth)
author:: Ethan Mollick
source:: [A guide to prompting AI (for what it is worth)](https://www.oneusefulthing.org/p/a-guide-to-prompting-ai-for-what)
clipped:: [2023-04-28](2023-04-28.md)
published:: 

#clippings

Whenever I open up Twitter, I am exposed to a new breed of hustle — the “prompt influencer” — promising me that 99% of people use GPT wrong and that they will provide the secret prompts that, if I use them in ChatGPT, will vanquish evil and make me a million dollars.

So I want to share my prompt secret with you, for free. Ready?

There are no secret prompts.

In fact, I think the emphasis on prompting as the key to using AI is a mistake for a number of reasons. But, I also have come to realize that there are some things people don’t understand about prompts, which can help make the task of using AI easier. So I do want to share those.

But first, why you shouldn’t take prompting that seriously:

1.  Being “good at prompting” is a temporary state of affairs. The current AI systems are already very good at figuring out your intent, and they are getting better. Prompting is not going to be that important for that much longer. In fact, it already isn’t in GPT-4 and Bing. If you want to do something with AI, just ask it to help you do the thing. “**I want to write a novel, what do you need to know to help me?”** will get you surprisingly far.
    
    
    ![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F07e1a3a3-e209-423a-9ef2-5aacfc13133d_740x640.png)
    

    
2.  A lot of prompting tips are more magic ritual than useful, repeatable tips. For example, many prompts include superlatives (“Act as the smartest person ever”) and expect that to matter. I tried a little experiment, telling GPT-4 to act as a **genius writer** or a **great writer** or just **a writer**, and, [based on my unscientific Twitter polling](https://twitter.com/emollick/status/1649967090500096002?s=20), it didn’t seem to help to tell it that it was amazing. That doesn’t mean it can’t be useful in some circumstances, but a lot of the prompts passed around online are magical incantations, rather than useful programs. (There are a few exceptions, words that do seem to change behavior, but more on that soon)
    
3.  The best way to use AI systems is not to craft the perfect prompt, but rather to use it interactively. Try asking for something. Then ask the AI to modify or adjust its output. Work with the AI, rather than trying to issue a single command that does everything you want. The more you experiment, the better off you are. Just use the AI a lot, and it will make a big difference - a [lesson my class learned as they worked with the AI to create essays](https://www.oneusefulthing.org/p/my-class-required-ai-heres-what-ive).
    

All of that being said, there are some ways of approaching prompting that might be helpful when starting your journey. But in the end, nothing beats practice.

Large Language Models work by predicting the next word, or part of a word, that would come after your prompt, sort of like a sophisticated autocomplete function. Then they continue to add language from there, again predicting which word will come next. So the default output of many of these models can sound very generic, since they tend to follow similar patterns that are common in the written documents that the AI was trained on. By breaking the pattern, you can get much more useful and interesting outputs. The easiest way to do that is to provide context and constraints.

It can help to tell the system “who” it is, because that gives it a perspective. **Act as a teacher of MBA students** will result in different output than if you ask it to **act as a circus clown.** This isn’t magical — you can’t say **Act as Bill Gates** and get better business advice — but it can help make the tone and direction appropriate for your purposes.



![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5dcf8ce9-314c-4fe3-a687-146539298446_1551x1360.png)



The clown advice is pretty great, though.

Then add additional constraints. You can add styles like **write this in the style of the New Yorker** or **write this in casual way.** You can tell it to **avoid repetition** or **make it accessible to a 10th grader**. You will find some of these approaches work better than others in different contexts, and it can be hard to know which things will work in advance, so experiment.

You should also provide whatever other data that you have as well. For ChatGPT-4, you can paste in quite a bit of information. For example. provide it a few paragraphs you have written and say **using the style in the paragraphs below, can you write \_\_\_**. Or you can paste in entire (copyright free, of course) sections of scientific articles for it to digest and work with, either to summarize or to build on.

[

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F85b7ec69-19f8-4a4a-be1c-7ec819e188d6_842x450.gif)


You can paste a lot of text into ChatGPT

You can use Bing (which, in creative mode, is GPT-4, but connected to the internet) to look up information by just asking **Look up data about \_\_** or **First, search for \_\_\_**. Bing’s Sidebar is also capable of reading the documents you are looking at in an Edge browser, so you can ask the Sidebar to reference what is in the browser. Again, you are helping shape the pathways the word prediction will take, and the results are likely to be much higher quality the more constraints you provide.

For slightly more advanced prompts, think about what you are doing as programming in English prose. You can give the AI instructions and it mostly-sort-of follows them. Mostly, because there is a lot of randomness associated with AI outputs, so you will not get the consistency of a standard computer program. But it can be worth thinking about how you can provide a very clear and logical prompt to the AI.

A lot of active research is happening around the best way to “program” an LLM, but one practical implication is that it can help to give the AI explicit instructions that go step-by-step through what you want. One approach, called [Chain of Thought prompting](https://arxiv.org/abs/2201.11903), gives the AI an example of how you want it to reason before you make your request, as you can see in the illustration from the paper.

[

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fadcb3f6b-1e94-4c74-8053-9b2176d1659d_1097x632.png)



You can also provide step-by-step instructions that build on each other, making it easier to both check the output of each step (letting you refine the prompt later), and which will tend to make the output of your prompts more accurate. Here is an example: ChatGPT is generally really bad at creating interesting puzzles and scenarios to solve, either making things too easy or impossible. But if we are explicit and step-by-step about what we want, the results are much better:

**You a game master. Your job is to come up with interesting challenges for the player to solve. Describe a challenging fantasy scenario, and enable me to solve it in an interesting way. You will use the following format to help create a series of responses.**

**Chain of thought:**

**\[Step 1\]: Decide on the the scenario, making it original and vivid and not standard fantasy. The scenario can involve combat, a trap, or a puzzle. The scenario must not involve riddles or the elements. Make sure there is a solution to the scenario. Make the solution require clever thinking. Include the solution in \[\] brackets**

**\[Step 2\]: Decide on the scene. Make sure that the player has the option to solve the scenario based on the descriptions. Make sure the solution is not clear, but requires clever reasoning based on the scene. Make sure there are very different false solutions that seem plausible. Include the detailed true solution and describe the false solutions, as well as how the player would find the true solution in \[\] brackets**

**\[Step 3\]: Describe the scenario and the scene, vividly and originally. Make sure there are clues to the solution and credible, but very different, false clues to the wrong answer in the description. Do not describe the solution or the problem directly. Do not describe how to solve the problem in this step. Do not describe the false clues as false.**

**Begin by introducing yourself and go through each step in order."**

[

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F98e9aea2-2724-4f29-9c65-1af0815058bd_1121x1305.jpeg "Image")


Again, there is no single template here. You need to experiment with your “program” multiple times to get a good answer, but there is an art to it that you can learn with time.

Okay, I lied slightly about the “there-are-no-magic-words” thing. There are some phrases that seem to work universally across LLMs to provide better or different results, again, by changing the context of the answer. Some possible things to experiment with:

-   **Be creative/make any assumptions you need**. This will tend to remove some of the constraints of practicality around AI answers, and can be useful if you are trying to generate something novel.
    
-   **Show your work/provide sources/go step-by-step.** The AI will make up information that it does not have access to. There is some evidence that asking it to show its work, or its sources, reduces that risk somewhat. Even if it doesn’t, it can make checking work easier.
    
-   **Write me code and tell me how to use it.** If you can’t code, you might be able to now. AI can do some amazing things with Python programs, and tell you exactly how to run it. I don’t know coding, but I have written a dozen Python programs in the last month. If there are errors in the code, and there likely will be, just give them to the AI to correct.
    
-   **Write a draft/provide an example.** If the AI refuses to do something (“you should be creative and write your own novel, I can’t help”, sometimes asking it to provide something like a draft can get it to produce results.
    
    
    ![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F90c37ec2-74df-4a6c-b743-75cc7b095439_1818x1138.png)
    

    The best thing you can do to learn to prompt better is to practice prompting. Use AI. Use it a lot. Get to understand what it can do and what it can’t. Engage it in back-and-forth dialog to get it to do what you want.
    

Wait, that wasn’t as clear as I would like. Hold on a second. Bing, can you help?



![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F22e07f3d-1a3e-4e28-95fb-a3ecc6b20b7f_1496x1658.png)


Nice. As I was saying:

Prompting is a skill that can be learned and improved with practice. The best way to learn is to use AI as your partner and your teacher. Experiment with different types of prompts and see how the AI responds. Engage in a dialogue with the AI and ask it questions, give it feedback, and challenge it to do better. Find out what triggers the AI’s creativity and what limits it. You will soon develop your own style and technique that will make you a more effective prompter. And remember, the AI is always learning too, so keep up with the latest developments and innovations in the field. You never know what new possibilities you might discover. One more thing: don’t be discouraged if some prompts don’t work as expected. There is some randomness in the AI’s output, and sometimes you will need to use the “clear” button to start a new conversation. That’s part of the learning process too.

[Share](https://www.oneusefulthing.org/p/a-guide-to-prompting-ai-for-what?utm_source=substack&utm_medium=email&utm_content=share&action=share)

[

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb4d8c55f-6625-4994-82e8-02d866facbaf_1376x864.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb4d8c55f-6625-4994-82e8-02d866facbaf_1376x864.png)