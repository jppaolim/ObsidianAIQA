author:: Ethan Mollick
source:: [It is starting to get strange.](https://www.oneusefulthing.org/p/it-is-starting-to-get-strange)
clipped:: [[2023-05-07]]
published:: 

#clippings

OpenAI may be very good at many things, but it is terrible at naming stuff. I would have hoped that the most powerful AI on the planet would have had a cool name (Bing suggested EVE or Zenon), but instead it is called GPT-4. We need to talk about GPT-4.

But, you might ask, hasn’t GPT-4 been around forever (or at least for about a month, which is forever in AI terms)? Yes, but the last week has seen a massive expansion in the system’s capabilities, and that is starting to bring into focus how large an effect AI is going to have on work. What has happened is that a number of GPT-4 systems, from both OpenAI and Microsoft, have been given the ability to use tools, with dramatic effects on their abilities, and their relevance to real-world tasks.

When I open ChatGPT, I see some options you may not have, since I signed up to be an early tester (you can, too, I have no special access). Soon, these tools will be available to everyone. You will notice there is the usual GPT-3.5, which was released back in November, and GPT-4, the much more capable model that comes with ChatGPT Plus. But what about the other stuff? Most of them are very much proof-of-concepts. One is extraordinary.

[

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F43b7086e-0926-43d2-83ae-d758973d7185_358x363.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F43b7086e-0926-43d2-83ae-d758973d7185_358x363.png)

So as not to keep you in suspense, lets discuss that crazy model - Code Interpreter - first, and then I will circle back to the other models, as well as to the increasing capabilities of Microsoft’s GPT-4 tools, which are poised to even more dramatically affect millions of jobs very soon.

Code Interpreter is GPT-4 with three new capabilities: the AI can read files you upload (up to 100MB), it can let you download files, and it lets the AI run its own Python code. This may not seem like a huge advance, but, in practice, it is pretty stunning. And it works incredibly well without any technical knowledge or ability (I cannot code in Python, but I don’t need to).

Lets take an example: **I am writing a blog post about how amazing ChatGPT is at working with code right now. I would like you to create the perfect illustration, a GIF using Python, that represents this ability. Decide what an appropriate amazing GIF would be, then figure out how to create it and let me download it.** After its first attempt, I encouraged it to **do something even more creative.** It decided on a strategy, wrote software to enact its strategy given the constraints on its tools, executed the code, and gave me a download link to a GIF.

[

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F24f1e425-a49c-4870-a251-5344cd436133_1217x1021.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F24f1e425-a49c-4870-a251-5344cd436133_1217x1021.png)

Here’s the GIF, 100% created by, and conceived of, by ChatGPT (I also asked it to put its authorship on the bottom). It is made only with crude drawing tools, since it doesn’t have access to AI image creators yet. By the way, [it probably shouldn’t be able to make GIFs, or original images at all](https://arxiv.org/abs/2303.12712), based on how it was trained, but here we are.

[

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb6f5ecbf-3999-472b-beea-53372d35063e_600x450.gif)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb6f5ecbf-3999-472b-beea-53372d35063e_600x450.gif)

This creativity with tools is not limited to making GIFs. [I had it make a PDF story that it illustrated](https://twitter.com/emollick/status/1652527708507701251). I also asked the AI to do entirely novel tasks: to write programs to create something *numinous*, something *antediluvian*, something *cthonic*, as I figured no one had ever made a request like that before. It obliged in really creative ways. Take a look, I think you will find these are very interesting and insightful solutions.

[

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1d20b9bd-dd0c-4178-ae35-1e33984da433_2345x1413.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1d20b9bd-dd0c-4178-ae35-1e33984da433_2345x1413.png)

So the AI shows genuine creativity in problem solving. That seems like a big deal, but not actually the big deal I want to discuss. I want to show you that Code Interpreter has turned GPT into a first-rate data analyst. Not a data analysis tool, but a data analyst. It is capable of independently looking at a dataset, figuring out what is interesting, developing an analytical strategy, cleaning data, testing its strategy, adjusting to errors, and offering advice based on its results.

An example: I uploaded a Excel file, without providing any context, and asked three questions: **"Can you do visualizations & descriptive analyses to help me understand the data? "Can you try regressions and look for patterns?" "Can you run regression diagnostics?"** It did it all, interpreting the data and doing all of the work - a small sample of which is below. There were no errors in the software or analysis, but there were a couple of small mistakes in the text (it reported one result that was correct in the graph incorrectly in the text), so it isn’t perfect… but it is also pretty amazing.

[

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1a17257d-26b8-4b86-a45e-ab4de9d7d8a5_2868x2466.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1a17257d-26b8-4b86-a45e-ab4de9d7d8a5_2868x2466.png)

I have similarly uploaded a 60MB US Census dataset and asked the AI to explore the data, generate its own hypotheses based on the data, conduct hypotheses tests, and write a paper based on its results. It tested three different hypotheses with regression analysis, found one that was supported, and proceeded to check it by conducting quantile and polynomial regressions, and followed up by running diagnostics like Q-Q plots of the residuals. Then it wrote an academic paper about it. Here’s the abstract:

```
Regional Dynamics of Industry Characteristics: A Comprehensive Examination of Payroll, Employment, and Establishments Across Metropolitan and Micropolitan Areas
```

```
Abstract: An in-depth understanding of regional industry characteristics is fundamental to the formulation of economic policies and business strategies. In this paper, we empirically examine the relationship between key industry characteristics, namely annual payroll, employment, and establishment sizes, across different Metropolitan and Micropolitan Statistical Areas (MSAs) in the United States. Utilizing data from the County Business Patterns dataset, we derive and empirically test three hypotheses, each addressing a distinct aspect of regional industry dynamics. Our findings indicate a robust positive relationship between the total number of employees and total annual payroll across MSAs and highlight the presence of specific industries with higher representation in terms of establishment counts. These insights contribute to our understanding of regional economic heterogeneity, labor market composition, and industry clustering.
```

It is not a stunning paper (though the dataset I gave it did not have many interesting possible sources of variation, and I gave it no guidance), but it took just a few seconds, and it was completely solid. And that, again, is kind of amazing. I think we are going to see massive changes coming to academic publishing soon, as journals struggle under the weight of these sorts of real, but automatically generated, papers.

But this is not the end of the effects of these new capabilities, of course. ChatGPT is going to change how data is analyzed and understood. It can do work autonomously and with some real logic and skill (though mistakes creep in they are rarer than you expect). For example, it does every data visualization I can think of. Below, you can see a few - I actually asked it to generate fake data for these graphs to show them off, and it was happy to do so.

[

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F79e7cce5-c831-4243-945b-36745c558b9f_2136x1534.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F79e7cce5-c831-4243-945b-36745c558b9f_2136x1534.png)

I have only been playing with Code Interpreter for a few days, but I think the world of data analysis is about to become democratized in ways that were unimaginable a week ago.

There were other modes you saw in the image above - GPT with Plugins and GPT with Browsing. Both are very interesting, but don’t work very well yet. Plugins allow ChatGPT to work with other systems, most importantly the powerful math tool Wolfram Alpha, but also various travel and restaurant services. ChatGPT really struggles to make these work, as it does with web browsing. I have no doubt these will improve, but, for right now, they very much deserve their “alpha” label.

But, while we are looking at ChatGPT, Microsoft’s Bing (which uses GPT-4 in creative mode, as well as the less interesting precise mode), has been perfecting some of these features. I have written about [Bing’s weird powers](https://www.oneusefulthing.org/p/feats-to-astonish-and-amaze) before, but you can see how it performs relative to ChatGPT with browsing.

[

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F89dba24e-a044-4bf2-9850-19ac19038c3d_2685x2310.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F89dba24e-a044-4bf2-9850-19ac19038c3d_2685x2310.png)

Bing has also added the ability to create images with DALL-E (just ask for a picture), and, most interestingly, has, through the Bing Sidebar, gained the ability to read the text you are looking at. That means you can ask questions of PDFs.

[

![Image](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F02da3e42-eefb-4dd2-ac84-6911daa4d1fb_1802x1140.jpeg "Image")

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F02da3e42-eefb-4dd2-ac84-6911daa4d1fb_1802x1140.jpeg)

Bing Sidebar can also help with documents, a feature that Microsoft is planning on adding directly to Microsoft Office. For example, I can type this in a Word document:

\-The market for electric cars in the US is \_ in 2022  
\-The biggest players are in this table  
\-A strategy for a new company entering is

And say to Bing: **look up data on the US electric car market & finish this report, providing sources...** And my work is cut by 50% or more (of course, you need to check the answers, though the spot check here was correct)

[

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F26bb64e5-c78f-41f0-a7ba-0da60e4c8c57_2898x1040.png)

](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F26bb64e5-c78f-41f0-a7ba-0da60e4c8c57_2898x1040.png)

Microsoft is planning on adding these capabilities to every single Office program in the near future, so mass adoption of AI for work is going to be happening much sooner than you think. Expect automatic creation of Word documents, automated Excel analysis, PowerPoint created with a paragraph of text (with images generated by DALL-E), and a Microsoft Teams that send you to-dos and suggestions for improvement after every meeting. [This is not science fiction. All of these things are already announced.](https://www.microsoft.com/en-us/microsoft-365/blog/2023/03/16/introducing-microsoft-365-copilot-a-whole-new-way-to-work/)

If you thought of AI as a distant thing that would not touch how we work every day, I hope you see that this is not the case. Between the expanding capabilities of GPT-4, and the soon-to-be everywhere Microsoft Copilot, work is going to start changing in a matter of months, not years. There isn’t really time to prepare, and no new technologies, beyond the ones deployed right now, are required. If you thought that things with AI were weird already, they are about to get weirder.

I will offer my usual advice: embrace these systems. They offer both exciting opportunities and the possibility of worrying change, but they are going to be ubiquitous regardless of how we feel about them. So, the best way to adjust to a world of AI is to start using it whenever you can, for whatever tasks you can. It is the only way to learn what these systems do well, what they do badly, and how you will fit into the world of AI that is already here. I think you will find many ways in which they expand your capabilities and relieve you of your most annoying work, so that you can focus on the things that make you unique as a human being in a world of rapidly advancing AI.

[Share](https://www.oneusefulthing.org/p/it-is-starting-to-get-strange?utm_source=substack&utm_medium=email&utm_content=share&action=share)