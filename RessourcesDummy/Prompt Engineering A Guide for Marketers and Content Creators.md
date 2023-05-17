author:: Ethan Crump
source:: [Prompt Engineering: A Guide for Marketers and Content Creators](https://foundationinc.co/lab/prompt-engineering-guide-marketers/?utm_source=substack&utm_medium=email)
clipped:: [[2023-05-07]]
published:: 

#clippings

ChatGPT and other generative AI tools will change the world of work as we know it. 

But don’t take my word for it. 

Researchers from OpenAI, OpenResearch, and the University of Pennsylvania predict that [80% of the US workforce](https://arxiv.org/pdf/2303.10130.pdf) will see the impact of generative AI tools on at least 10% of their tasks. 

This means as AI tools evolve, more companies and employees will use these tools to automate certain tasks, increase efficiency, or even replace some jobs entirely. 

An example is a company that starts using ChatGPT, sees its value, and lets go of employees responsible for certain admin and customer communications tasks, and even marketing-related tasks to “save costs and get things done faster.” 

(It’s already happening 👇)

![An increase in the use of ChatGPT at companies is turning prompt engineering into an important skill.](https://foundationinc.co/wp-content/uploads/2023/04/1-7.png)

This likely happens when the executives feel the AI tool can do it faster and more accurately, despite warnings that these AI tools shouldn’t be relied on completely. 

But there’s a silver lining.

Getting meaningful output from generative AI tools requires a human touch. Tasks like programming, writing, translating, and analysis still rely on human input—the words, code, and context we use while “prompting the tool.” As a result, there’s a new career path in the works: prompt engineering.

This guide breaks down everything you need to know about prompt engineering, including what it is, tips on writing effective prompts and [using AI in your workflow](https://foundationinc.co/lab/artificial-intelligence-for-marketers/), and the skills you need to succeed in the field—whether you’re a marketer or creator. 

I’ll take you on a quick tour of the rapidly-developing field of prompt engineering. If you want to skip the preamble and get into the fun stuff, here’s exactly what I cover in this article: 

-   What Is Prompt Engineering
-   The Anatomy of a Prompt: Elements and Techniques
-   Tips for Effective Prompt Engineering
-   Prompt Engineering for Marketers and Content Creators

Let’s get into it!

## **What Is Prompt Engineering** 

Prompt engineering is the process of crafting and refining the instruction or query you feed to a generative AI tool to get a specific response. 

This concept has reached buzzword status since the rollout of ChatGPT in late 2022. From Forbes to Insider, tech and business publications are gushing over this new mysterious position that in some cases commands upwards of $350K. 

![Google shows an increase of new coverage on high-paying prompt engineering jobs.](https://foundationinc.co/wp-content/uploads/2023/04/2-5.png)

While the long-term viability of the prompt engineer career path is still up for debate, one thing isn’t: 

**Companies across all industries are scrambling to leverage generative AI tools to gain a competitive edge.**

Meta, Slack, Instacart, Shopify, Canva, and other tech giants have already hopped on the train with GPT-based products. But the buck doesn’t stop with SaaS; businesses across healthcare, real estate, and media are using it as well. 

But if you’ve used any GPT tool, you know its results aren’t always of the highest quality. Sure, they have some impressive capabilities and seem to improve regularly, but they give inaccurate information or irrelevant answers sometimes. 

Simply put, the quality of your prompts determines the quality of results you get from these tools. A well-engineered prompt effectively communicates your intent to the AI model, so it generates answers that accurately address your question. That’s why knowing how to wield these tools is incredibly valuable, particularly if you’re in the content creation or marketing game. 

Before we get into the meat of this piece, I want you to keep these 4 key steps of prompt engineering in mind:

-   **Defining the goal or objective:** All prompts contain a clearly defined goal or objective that states what the AI is expected to produce. This includes things like specifying the format, target audience, or desired tone of the content.

-   **Setting the context:** Providing background information and other context relevant to the topic helps the AI model better understand the output you want, enabling the model to generate more relevant and accurate responses.

-   **Providing examples and guidance:** Including examples in a prompt gives the AI model a template for how it should generate the desired content. This is especially helpful when you want the AI to follow a particular structure or adhere to specific guidelines.
-   **Iterating and refining:** Prompt engineering, like any form of communication, is an iterative approach. You need to test different variations of a prompt, evaluate the content it elicits, and refine the prompt based on how well it meets your goal or objective.

Whenever I find myself struggling to get quality output from a tool like [ChatGPT or Jasper](https://foundationinc.co/lab/vol-106/), I go back through these 4 steps to verify I’ve given the AI everything it needs. Remember: these tools are only as good as the inputs we provide!

Now let’s look at the specific prompt elements and prompting techniques you can use to engineer quality inputs.

## **The Anatomy of a Prompt: Elements and Techniques**

Prompts consist of several key components that work together to guide the generative AI tool towards the desired output. Understanding each component and, more importantly, how the AI model interprets them will help you get the results you desire. 

Here are four main components to keep in mind during the prompt writing process: 

### **Instructions**

The instruction portion outlines the task you want the AI to perform. It provides a clear and concise description of the desired action, such as summarizing, extracting, translating, classifying, or generating text. 

The clarity and specificity of the instructions are crucial, as they directly impact the relevance and accuracy of the AI-generated content. Generative AIs rely on these instructions to understand the user’s intent and generate responses that align with their expectations.

In the prompt below, I’ve given ChatGPT clear instructions about the output I want it to create: 10 blog post ideas that contain a title and introductory paragraph. 

![ChatGPT input with the instruction portion of the prompt highlighted.](https://foundationinc.co/wp-content/uploads/2023/04/3-5.png)

### **Context**

Context is an essential component of a prompt. It helps the AI model grasp the background information and subject matter relevant to the task. It may include details about the topic, genre, tone, target audience, or any specific constraints or guidelines. 

By establishing context, users can guide the AI model to generate content that is contextually appropriate and adheres to the given parameters.

In the same example prompt, I start off the prompt with a bit of context: “I need to write a blog post about the best CRM platforms for small businesses and startups.” 

![ChatGPT input with the context portion of the prompt highlighted.](https://foundationinc.co/wp-content/uploads/2023/04/4-5.png)

### **Input data**

Input data refers to the actual content or information that the AI model will process and use to generate the output. In some cases, this may be a piece of text that the AI should summarize or analyze; in others, it may be a set of data points or examples that the AI should consider when generating its response. 

Providing accurate and relevant input data is critical, as it forms the basis for the AI-generated content and ensures that the output is meaningful and informative.

Looking at our example prompt once again, we notice that the input data I include is an example output showing how I want ChatGPT to format and write the content. 

![ChatGPT input with the example data portion of the prompt highlighted](https://foundationinc.co/wp-content/uploads/2023/04/5-6.png)

### **Output indicators**

Output indicators help define the format, structure, or presentation of AI-generated content. They can include explicit instructions for organizing the output, such as specifying the number of bullet points, the order of information, or the required length. 

Output indicators also help guide the AI model in generating responses that are easy to read, well-structured, and aligned with the user’s desired format.

In the example prompt, I provide ChatGPT with multiple output indicators to direct how I want the content to look, including the number of items (10 total ideas), component parts (title and intro paragraph), and the number of sentences (4-5). 

![An engineered ChatGPT Prompt with the output indicators highlighted.](https://foundationinc.co/wp-content/uploads/2023/04/6-4.png)

When users craft a prompt that effectively incorporates these components, the generative AIs like ChatGPT and Jasper are better equipped to interpret the prompt and generate content that meets the user’s requirements. 

By understanding the anatomy of a prompt and the role each component plays, you can optimize your prompt engineering skills and harness the full potential of AI-driven content-generation tools.

### **Prompt Engineering Techniques**

Now let’s take a look at the main types of prompt engineering techniques, with a little visual support from our new friend ChatGPT. 

#### **Zero-shot Prompt**

A zero-shot prompt is one where the AI model has not been provided with any examples or context to help it understand the task it’s being asked to perform. The model is expected to complete the task based on its general knowledge and ability to interpret the prompt.

Zero-shot prompts are great when you’re simply looking for quick access to information like a definition or answer to a specific question. 

![An example of a Zero-shot prompt and ChatGPT's response.](https://foundationinc.co/wp-content/uploads/2023/04/7-4.png)

#### **One-shot Prompt** 

A one-shot prompt provides the AI model with a single example to demonstrate the desired task. This helps the model understand any pattern or format requirements to use in the response.

One-shot prompts are more effective when you have a specific example of how you want the AI to respond to your instructions, like a math problem.

![ An example of a one-shot prompt and ChatGPT's response.](https://foundationinc.co/wp-content/uploads/2023/04/8-4.png)

#### **Few-shot Prompt** 

A few-shot prompt is similar to a one-shot prompt, but it provides multiple examples to help the AI model better understand the desired output. This allows the model to generalize the task more effectively.

If you find you aren’t getting great results from a one-shot prompt, turning it into a few-shot prompt with more examples can help get your outputs closer to the desired format. 

![An example of a few-shot prompt and ChatGPT's response.](https://foundationinc.co/wp-content/uploads/2023/04/9-4.png)

#### **Chain-of-Thought Prompts**

A chain-of-thought prompt involves a series of connected questions or tasks, with the model’s responses to previous prompts influencing its understanding and answers to subsequent prompts. This type of prompt is useful for complex tasks or for maintaining context in a conversation.

My personal favorite, chain-of-thought prompts are great when you want to dive deeper into a topic without wasting time tweaking and formatting each individual prompt. ChatGPT and other AIs with a chat-like interface are capable of carrying over information, instructions, and context from previous entries and factoring them into the current output. 

![An example of a chain-of-thought prompt and ChatGPT's response.](https://foundationinc.co/wp-content/uploads/2023/04/10-4.png)

## **Tips for Effective Prompt Engineering**

Despite the highly-technical, scientific nature of these AI tools, the process of prompt engineering is still as much an art as it is a science. We’re still in the very early days of using AI tools like Jasper and ChatGPT, so optimizing prompts for better outputs is iterative and intuitive. 

Just like you play around with the wording in a blog post, Twitter thread, or LinkedIn post based on previous feedback from your audience, you’ll need to do the same with the outputs you get from generative AI tools. 

That said, there are a few general rules that experts from [OpenAI](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api) and [GitHub](https://www.promptingguide.ai/introduction/tips) have observed to help you inject some science into this process. 

Let’s take a look at a few. 

### **Be Clear and Specific in Your Wording**

Using ambiguous, unclear phrasing is guaranteed to water down the outputs from your AI tools. Remember, you are feeding instructions to an incredibly complex algorithm, so just give it the context and instructions it needs. 

When I’m writing prompts, I find that specifying the formatting and length of the desired output is particularly helpful. It’s also beneficial to connect the main topic of the desired output to some additional context. 

![](https://foundationinc.co/wp-content/uploads/2023/04/11-3.png)

### **Provide Examples in Your Prompt**

Providing an example of the output you want will give the AI an exact template for how it should format and generate the text. 

This is especially helpful when you are using the AI to create a list of output options like tweets or other social posts. 

### ![](https://foundationinc.co/wp-content/uploads/2023/04/12-3.png)

### **Focus on What You** ***Want*** **It To Do**

It’s easy to fall into the trap of listing off all the things you *don’t* want your generative AI tool to do, but this goes against the first cardinal rule of concision and specificity. Try wording your instructions in the affirmative instead. 

It may take slightly longer for you to write the prompt but it’ll be worth it when you get the exact outputs you’re looking for!

![](https://foundationinc.co/wp-content/uploads/2023/04/13-3.png)

### **Testing and Experimenting with Prompts**

Testing and iterating prompts is a crucial step in working with generative AI tools to obtain better outputs. By experimenting with various prompt structures, phrasings, and context, users can guide the AI toward more accurate, relevant, and coherent responses. This process involves refining the input prompt to make it more explicit or providing additional context or constraints to narrow down the AI’s focus. 

As you iterate through different prompts and analyze the resulting outputs, you get the hang of how the AI interprets and responds to various instructions. This iterative approach gives you a deeper understanding of how to effectively communicate with the AI, ultimately leading to improved performance and more desirable outcomes from the generative AI tool.

## **Prompt Engineering for Marketers and Content Creators**

Okay, we’ve done some due diligence and gone over some of the basic concepts and tips for prompt engineering. Now it’s time for the fun stuff. 

Well, almost time for the fun stuff—first, an important disclaimer: 

**You** ***always, always, always*** **need to vet the outputs you get from generative AI tools like ChatGPT and Jasper.** 

As good as the tools are at tasks involving reading comprehension and text generation, they are still far from perfect. There are plenty of stories circulating about AI creating [fictional research articles](https://gizmodo.com/meta-ai-bot-galactica-1849813665), historical inaccuracies, or just flat-out misinformation. As a responsible content creator, you need to do your due diligence and make sure you verify any and all outputs. 

Got it? Good. 

With that out of the way, let’s get into a few examples of how I’m using ChatGPT across the different marketing  and content creation tasks I come across in my everyday work. 

### **Ideation and Brainstorming** 

One of the most effective ways you can use generative AI tools is for ideation and brainstorming. With the massive amount of information used to train these models, they can easily and efficiently produce lists of semantically-related information. 

Here’s an example of a prompt I used in ChatGPT to generate a list of blog post titles on the topic of the best CRM platforms for small businesses and startups: 

![Engineering a prompt directing ChatGPT to assist with brainstorming and ideation.](https://foundationinc.co/wp-content/uploads/2023/04/14-2.png)

As you can see, I’ve engineered this one-shot prompt to include the context, formatting instructions, and example content it needs to provide me with some solid outputs. 

![ChatGPT's response to a brainstorming and ideation prompt.](https://foundationinc.co/wp-content/uploads/2023/04/15-2.png)

In just a few minutes, GPT-4 has provided me with 10 different title-intro combinations I can use to create my blog post. 

### **Background Research**

About a month ago I decided I needed to learn more about the academic side of machine learning and artificial intelligence (for obvious reasons). Instead of my typical process of using Google, Wikipedia, and academic journals, I decided to enlist ChatGPT as my assistant to kick off the research process. 

Here’s how it went.

![Engineering a prompt directing ChatGPT to assist with topic research](https://foundationinc.co/wp-content/uploads/2023/04/16-2.png)

In about 20 seconds, I had a list of the top researchers in the field, including where they study or work and a brief explanation of their relevance. 

Knowing that the tool can build off my previous prompts and use the responses as context, I decided to keep going.   

![Following up on a previous ChatGPT outputs using a chain-of-thought input](https://foundationinc.co/wp-content/uploads/2023/04/17-2.png)

Pretty cool, right? 

But, you can take it a step further. 

![Using prompts to continue ChatGPT's chain-of-though.](https://foundationinc.co/wp-content/uploads/2023/04/18-2.png)

Unreal. 

In just under 5 minutes ChatGPT, helped me gather a massive amount of information on my area of interest, including leading experts, a list of their most important contributions, and a brief summary of each contribution. 

And as you can see, the prompts were simple and straightforward. 

ChatGPT’s chain-of-thought prompt capabilities mean it carries context over from previous prompts, so I don’t have to worry about elaborate prompts eating into the token count. 

### **Persona Creation** 

[Buyer persona development](https://foundationinc.co/lab/b2b-persona/) is one of those time-intensive B2B marketing tasks where I find myself getting stuck in the early stages. But with a large language model and a straightforward prompt, it’s simple to get the ball rolling. 

For example, here’s a sample prompt I used to take a deep dive on potential buyers of Notion’s enterprise account.

![Engineering a prompt directing ChatGPT to assist with persona creation](https://foundationinc.co/wp-content/uploads/2023/04/19-2.png)

Now, there’s quite a bit more work to be done before these can actually be useful—verifying with product research, user surveys, mapping out the buyer journey, and all that. 

Still, in under a minute, GPT-4 has produced a list of 5 potential buyer personas complete with a goal and pain-point for each. Oh, and the use of alliteration is a nice bonus too.

### **Keyword Identification**

With a well-engineered prompt, you can also speed up your preliminary keyword identification process. 

For example, I was recently looking to find keywords for an enterprise time-tracking software company to target. Knowing ChatGPT can find relevant words much faster than I can, I fed it this prompt: 

![Engineering a prompt directing ChatGPT to assist with keyword research](https://foundationinc.co/wp-content/uploads/2023/04/20-2.png)

And here’s what GPT-4 gave me as the output: 

![ChatGPT output in response to a prompt about preliminary keyword research.](https://foundationinc.co/wp-content/uploads/2023/04/21-2.png)

A list of over 25 potential keywords in under a minute! 

Again, immediately after getting this list I went to ahrefs and vetted the results in terms of search volume and keyword difficulty. Still, ChatGPT proved a great starting point for identifying potential search terms that I could zero-in on for further analysis.

### **Brief and Framework Creation** 

Another place where marketers and content creators frequently get stuck is during brief and framework creation. But with generative AI, you can kick start the content marketing process with just three things:  
  
A topic idea, a target audience, and a handful of keywords. 

Want an example? Here’s a prompt I recently used to get some AI assistance on a brief I made for a blog post on TikTok marketing: 

![Engineering a prompt directing ChatGPT to assist with brief and framework creation](https://foundationinc.co/wp-content/uploads/2023/04/22.png)

As you can see, I engineered this prompt to provide the AI with all the information it needs regarding the goal, context, and formatting of the output. 

In this case, I even got a little ambitious with my formatting request, asking ChatGPT to use my included keywords as subheadings and to create the outline in bullet-point form.

Here’s the output it gave me:

![ChatGPT output in response to a prompt about creating a blog post brief](https://foundationinc.co/wp-content/uploads/2023/04/23.png)

As I hoped, the AI took my prompt and easily transformed it into a brief that I easily turned into a blog post—with a few tweaks and revisions, of course. 

## **Build Prompt Engineering Skills and Optimize Your Content Workflow**

As I’ve demonstrated in the latter half of this article, marketing and content creation most definitely fall into the 20% of jobs that will be greatly impacted by generative AI tools. 

Instead of looking at this through the lens of fear, you just need to treat it as another tool in the marketer’s toolkit: search engine optimization, social media marketing, demand generation, prompt engineering. 

Inflated salaries aside, the ability to create inputs that elicit better results from large language models is an important skill for marketers and content creators to learn. If the adoption of the ChatGPT API is any indicator, the majority of enterprise companies in SaaS and beyond will use generative AI tools. 

Remember, we’re still in the very early days of prompt engineering, and things are moving fast—very fast. So make sure you stay on top of the latest developments with tools like Jasper and ChatGPT, particularly concerning  how you can apply them in your everyday workflows. 

For another look at how generative AI tools like ChatGPT and DALL-E are revolutionizing content marketing, check out Ross’s [AI content workflow post](https://foundationinc.co/lab/ai-content-workflows) for Foundation Insiders. 

![](data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==)

## Did you enjoy this post?

Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est eopksio laborum. Sed ut perspiciatis unde omnis istpoe natus error sit voluptatem accusantium doloremque eopsloi