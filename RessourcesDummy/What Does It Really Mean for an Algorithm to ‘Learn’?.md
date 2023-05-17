author:: Andre Ye
source:: [What Does It Really Mean for an Algorithm to ‘Learn’?](https://towardsdatascience.com/what-does-it-really-mean-for-an-algorithm-to-learn-1f3e5e8d7884)
clipped:: [[2023-05-01]]
published:: 

#clippings

![](https://miro.medium.com/v2/resize:fit:700/1*IBBOFvm0hwxa5t1O1U4H8w.png)

## Two general perspectives and some psychology

[

![Andre Ye](https://miro.medium.com/v2/resize:fill:44:44/1*FJ_mJhXaY26AzEw8OSl0pA.jpeg)









](https://andre-ye.medium.com/?source=post_page-----1f3e5e8d7884--------------------------------)[

![Towards Data Science](https://miro.medium.com/v2/resize:fill:24:24/1*CJe3891yB1A1mzMdqemkdg.jpeg)











](https://towardsdatascience.com/?source=post_page-----1f3e5e8d7884--------------------------------)

When one first encounters machine learning, one often rushes through algorithm after algorithm, technique after technique, equation after equation. But it is afterwards that one can reflect on the general trends across the knowledge that they have acquired.

What it means to ‘learn’ is a very abstract concept. The goal of this article is to provide two general interpretations of what it means for a machine to learn. These two interpretations are, as we will see, two sides of the same coin, and they are treated ubiqitously across machine learning.

Even if you are experienced in machine learning, you may gain something from temporarily stepping away from specific mechanics and considering the concept of learning at an abstract level.

There are broadly two key interpretations of learning in machine learning, which we will term ***loss-directed parameter update*** and ***manifold mapping***. As we will see, they have substantive connections to psychology and philosophy of mind.

Some of the machine learning algorithms previously discussed adopt a ***tabula-rasa*** approach: they begin from a ‘blank slate’ random guess and iteratively improve their guess. This paradigm seems intuitive to us: when we’re trying to acquire a new skill, like learning to ride a bike or to simplify algebraic expressions, we make many mistakes and just get better ‘with practice’. However, from an algorithmic perspective, we need to explicitly recognize the presence of two entities: a ***state*** and a ***loss***.

An algorithm’s ***state*** is defined by the values of its set of *parameters*. Parameters are, in this context, non-static values that determine how an algorithm behaves. For instance, consider trying to optimize your bowling game. There are several parameters at hand: the weight of the bowling ball, the configuration of your fingers in the fingerholes, your velocity when getting ready to bowl, the velocity of your arm, the angle at which you bowl, the spin at the moment of release, and so on. Every time you bowl, you define a new *state* since you — as an optimization algorithm — are trying out new parameters (unless you bowled exactly the same as previously, in which case you are returning to a previous state, but this is a rare occurrence both in bowling and in machine learning).

Each of the coefficients in linear regression and logistic regression is a parameter. Tree-based models don’t have a static number of parameters, since their depth is adaptive. Rather, they can create more or fewer conditions as is needed to optimize for information gain criteria, but these are all parameters.

However, tree-based models — and all algorithms — are subject to ***hyperparameters***. These are the system-level constraints that the parameters themselves must act within. The maximum depth of a decision tree and the number of trees in a random forest ensemble are both examples of hyperparameters. In our bowling example, meta-parameters could include the humidity of the building, the quality of the bowling shoes you were given, and the crowdedness of the bowling lanes. As an optimization algorithm, you exist *within* these conditions and must optimize your internal parameters (which bowling ball you choose, how you bowl, etc.) even if you cannot change the underlying conditions.

The ***loss***, on the other hand, is the ‘badness’ or error of any given state. A loss must formulate how to derive the badness of a model from its behavior. For instance, say I adopt a certain state — I choose a 6.3-inch diameter bowling ball, release the ball at 18 miles per hour at a 9-degree angle relative to the lane edges, beginning four feet away from the lane, and so on — and knock down 6 pins. The behavior of my state is that I knocked down 6 pins. To quantify the badness of the state, we calculate how many pins I *didn’t* knock down — 4 pins, given a bowling ball released with those exact state parameters. To minimize my badness, I adjust my parameters the next time I bowl.

![](https://miro.medium.com/v2/resize:fit:700/1*kYnMRBPztf6gP5H_LVgugw.png)

Speaking in terms of algorithms, the state is usually a set of coefficients or criteria that transform an input into a prediction, and the loss is a mathematical quantification of the difference between a model’s prediction and its desired output. Say a model has *n* parameters, denoted by `{x_1, x_2, ..., x_n}` . These might be the coefficients of a linear regression model, the center of the clusters in the *k*\-means model or represent the split-off criteria in a decision tree model. We can derive an error this model incurs on some set of data — for instance, mean squared error. If the model iteratively adjusts its parameter set to improve its loss, then we say it is *learning*.

![](https://miro.medium.com/v2/resize:fit:700/1*se9234XiBryXmNZZF0pQRw.png)

While we might roughly call this entire process learning, the actual learning *algorithm* occurs in the conversion from loss to parameter update. The evaluation of the current state (i.e. the conversion or derivation from parameter to loss) might be considered ‘feeling’ or an ‘intelligent’ process.

One psychologically and evolutionarily informed hypothesis suggests that we as humans are constantly playing an optimization game conceptually similar to that of models learning via the loss-directed parameter update paradigm: we are continually observing the ‘badness’ of our state and seeing to improve the badness by adjusting our state. However, our measures of badness are more complicated than a mean-square-error calculation: we are simultaneously juggling a variety of signals, internal and external, visceral and calculated, and trying to make sense of it all in relationship to our current set of changeable characteristics. For instance, when you’re bowling, you may not be directly trying to optimize the number of pins you knock down, even if you try to. Instead, you might be trying to minimize social anxiety or maximize how impressed your date or friends are, which does not necessarily result in the same optimal configuration of states as that of maximizing the number of pins knocked down.

Keeping this idea in mind — that we can view our own behavior as a constant updating of changeable states in response to evaluations of our states’ badness — allows us to better understand problems and phenomena in how loss-based parameter update behave. For one, people aren’t always changing their state, even if they are necessarily constantly evaluating their state. This demonstrates *convergence* — those people have reached a set of states for which no feasible change to the state will decrease badness.

Alternatively, some people are sadly trapped in recurring destructive behavior of poor conditions because of addiction (to substances, to gambling, to social media scrolling, and so on) or crippling paranoia (of falling into financial debt, of losing prized possessions, of losing respect, of large crowds, and so on). In the technical language of learning, we refer to these as ***local minima***. These are places of convergence that agents arrive at and ‘choose’ not to leave either because it is easier to stay there than to make any immediate step away from it (e.g. breaking from an addiction) or because, equivalently, it is worse to make any immediate step away than to remain (i.e. a paranoia of damage or worsening of one’s state given some change).

Algorithms often demonstrate similar behavior, although of course in less immediately human-like ways. We often conceptualize the relationship between the loss and the state in loss-directed parameter update in a geometric and quantitative way through the idea of a ***loss landscape***. The loss landscape is a geometric space with one axis for each parameter and an additional axis for the loss. The loss landscape allows us to map each set of parameter values to a loss value incurred for that loss.

To illustrate this crucial concept, let’s say that you are trying to learn the optimal study strategy for a test. We’ll just consider the problem of learning *one parameter* — how many hours you study for the test. Say you’ve taken four tests before, so — assuming for the sake of illustration that these tests are environmentally comparable — you have four data points to learn from. For each of these four tests, you studied a different number of hours and correspondingly obtained different performance: 60% when not studying at all, around 75% when studying for 1.5 hours, around 70% when studying for 4 hours, and around 60% when studying for 6 hours. We’ll plot these out as follows by showing how the loss — which conventionally has the property of being more desirable when smaller, so in this case will be the *error rate* (one minus performance) — changes with the parameter being optimized.

![](https://miro.medium.com/v2/resize:fit:700/1*iVSmb3Y3ZN-iDwCo0JiBlQ.png)

Using this information, we want to find the optimal number of hours to study to obtain the smallest error rate. From the information we’ve collected so far, it looks like the optimal parameter value will be somewhere near two hours. But how can we be sure? How do we think about close answers or far answers? How do we characterize this process of looking at our data and searching for a minimum loss?

The loss landscape is a conceptual tool to help us think about learning in a physical, quantitative sense. We imagine that we have access to the exact, true relationship between every parameter value and its corresponding error rate. This allows us to draw a curve, or ‘landscape’, throughout our parameter-loss space. We can understand each of the known points as being ‘sampled’ from the landscape. It should be repeated that, in practice, we do not have access to this landscape. It is rather a theoretical model to aid reasoning and understanding.

![](https://miro.medium.com/v2/resize:fit:700/1*dTIYTCMeTNOG-hFjMzzjHg.png)

Now, imagine you are looking at a two-dimensional-world hill. Say you’re a little traveler standing on the surface of this hill, seeking out the place of lowest altitude. You can move however you want — you could use your teleporter and jump randomly all over the place, you could take slow steps, you could take large jumps. As you explore this hill, you might find that none of the new places you’re visiting are lower than the lowest previous place you’ve visited. After some amount of unfruitful exploration, you may decide just to settle with that previously visited lowest location. This would indicate convergence.

Algorithms can be differentiated by how they make use of and navigate the loss landscape. You can think of each algorithm as its own personality of traveler. One dumb learning algorithm is just to randomly change parameters a large number of times and revert to the best-performing one — random search. This is an erratic traveler that may have drunk a little too much, jumping all over the loss landscape in their teleporter.

Alternatively, a conservative learning algorithm would be to search every set of parameter values with a certain set granularity. This is a very diligent but inefficient traveler, which slowly walks every ‘inch’ of the loss landscape, taking notes and meticulous measurements.

A smarter traveler might try to devise metrics for the gain in making a certain decision, or by analyzing the slope of the ground they are currently standing on to determine which direction leads to the fastest descent.

The loss landscape also lets us consider phenomena like local minima, in which the learning algorithm converges to a solution which appears to be the best compared to ‘nearby’ solutions, but which is worse than some other ‘global’ minimum. In our previous example of optimizing the number of hours spent studying, we would identify studying two hours as a local minima. This will yield a superior exam error rate compared to, say, studying half an hour or four hours. However, the true global minima is studying 10 hours, which gives us a perfect exam error rate of zero. Think of local minima as a problem of *sight*: the traveler, navigating the hilly landscape, can only see the mountains ahead but not the deeper valleys which might lie beyond and decides the shallow valley right in front of them must suffice.

Consider a pragmatic example. We have a very simple model with just one parameter *m* that controls the line *y = mx*, and we want to find the value of *m* which best fits a dataset of points (i.e. minimizes the average difference between the line and a point).

![](https://miro.medium.com/v2/resize:fit:700/1*_DjCx8izK6DjwPmgGHEy0g.png)

The loss landscape looks as follows, for slope values from 0 to 4.

![](https://miro.medium.com/v2/resize:fit:700/1*m1QGHpPyXPf9XjRKLPKRfQ.png)

Let’s consider the process of travelling this loss landscape and the corresponding effect on fine-tuning our model. We’ll begin high up on this landscape, with a very small slope value of 0.1316. This is clearly not a great fit for our dataset, and correspondingly we are on ‘very high ground’ on the loss landscape.

![](https://miro.medium.com/v2/resize:fit:700/1*pbMdvH9xebiPjk_0vd2vfQ.png)

Let’s “learn”. Say we look a little bit to the ‘right’ and correspondingly find lower ground.

![](https://miro.medium.com/v2/resize:fit:700/1*5eJzovsxptWRePiCnUO9Tw.png)

Encouraged by the successful first leg of the journey, we’ll step again in the same direction two more times, arriving at the minimum error using a model with a slope of 2.1053.

![](https://miro.medium.com/v2/resize:fit:700/1*LIkbrrtkAoQYuhq9kDeIEw.png)

Say we step one more further and end up climbing instead of descending our loss landscape, resulting in a worse model. This is where our learning has stumbled into a mistake; we might want to either keep on exploring (and maybe find a better solution further down) or revert back to the previous best solution. Such is a mistake and a correction in the process of learning.

![](https://miro.medium.com/v2/resize:fit:700/1*q5v8LM4zSjmav32TVWpvmw.png)

Practically speaking, however, machine learning models have many more parameters than one parameter. Even a linear regression model — about the simplest type of model there is — has about as many parameters as there are variables in the dataset.

We can generalize this idea, albeit a little bit less intuitively, to higher dimensional spaces. For instance, consider a model instead with two parameters. The loss landscape would correspondingly have three dimensions, showing how every combination of the two parameter values maps to a certain loss. We now have a three-dimensional ‘landscape’ that we can imagine attempting to navigate.

![](https://miro.medium.com/v2/resize:fit:700/1*l41LsjjvoKuV6o-N-2xTDg.png)

Most modern machine learning models have dozens, hundreds, or even billions (in the case of deep learning) parameters. We can conceptually understand their process of *learning* — the ‘learning’ in “machine learning” or “deep learning” — as this navigation of the corresponding dozen-, hundred- and billion- dimensional loss landscapes, searching across the hills for the ‘location of lowest ground’, the combination of parameter values which minimizes the loss.

Loss-directed Parameter Update is an intuitive way to understand learning: we update our internal parameters in response to feedback signals, which can be evaluated internally or externally (by, say, an environment). The concept of the loss landscape allows us to translate the abstract problem of learning into a more physical space and offers concrete explanations of observed phenomena in the learning process, like convergence to subpar states (local minima).

Loss-directed Parameter Update is a *model-centric learning interpretation*: the loss landscape space is physically defined by components of the model (the parameter value axes) and the aggregate performance of those components (the loss axis). On the other hand, the Manifold Mapping interpretation is *data-centric*. Rather than defining learning in terms of the model as an agent, we observe learning as occurring within the data. (Of course, as you will see, these are two sides of the same coin).

Suppose you are the caretaker for Hal 9001, who is still bitter about being passed over in favor of its older sibling for a role in *2001: A Space Odyssey*. As Hal 9001’s caretaker, one responsibility is to predict whether Hal will be satisfied or not with today’s temperature. You have some data on previous temperatures and Hal 9001’s corresponding satisfaction. Today’s temperature is 64 degrees. Can you predict whether Hal 9001 will be satisfied or not?

![](https://miro.medium.com/v2/resize:fit:700/1*SJE36bk28Jsg40xrKn5T7g.png)

A glimpse at the data suggests that Hal 9001 will (thankfully) be satisfied. How did you make this inference? You implicitly *constructed a* ***manifold*** in the *feature space*. Since our data here only has one feature, temperature (Hal 9001’s satisfaction is *target*, not a feature), the feature space has only one dimension. This amounts to a number line:

![](https://miro.medium.com/v2/resize:fit:700/1*Fsg_kWscwGwO0E1j9Qhz3g.png)

Loosely speaking, we can draw a *manifold* to separate the data along some point. In this case, we can perfectly separate the data by drawing the following manifold:

![](https://miro.medium.com/v2/resize:fit:700/1*3ijChg2cioNr_UqYUskD2w.png)

We can also refer to a manifold as a **decision boundary**, for intuitive reasons. The manifold is the boundary which separates space and allows us to make decisions as to which class we associate with which point in the feature space.

The crucial insight here is that the manifold is not just relevant to that thin ‘strip’ of space it occupies in the feature space: instead, it affects the entire feature space. It defines which swathes belong to which classes. Moreover, it defines how you perform inference on points you have not seen before. If we are to mark the point ‘64’ in this feature space, we see that it falls into the satisfaction category ‘Yes’.

![](https://miro.medium.com/v2/resize:fit:700/1*pCYt0bErHlJgFv1T1-vYHg.png)

Let’s consider another example in two-dimensional space. Figure 2-x shows a two-dimensional feature space (this would represent a dataset with two features/columns) and the points are shaded by their class.

![](https://miro.medium.com/v2/resize:fit:700/1*Cm0MbBx2KRaiP_KpOjMoIw.png)

We could draw the following manifold to separate the data. It fits the dataset perfectly; that is, it perfectly separates the data into their respective classes.

![](https://miro.medium.com/v2/resize:fit:700/1*Eifq86MDd2dj7aRx_hJ-ww.png)

We can also draw many other valid manifolds, however. These also perfectly separate the data.

![](https://miro.medium.com/v2/resize:fit:700/1*JZ5rApyrCXy4U6EPpAVDvQ.png)

While these manifolds all have the same *training-set performance* in that they obtain equivalently perfect performance separating different-classed items in the feature space, they are markedly different in how they affect the entire feature space. The point at coordinate (1, 7) would be classified as a different class in the top mapping than in the bottom mapping because the manifold had a different direction.

Similarly, returning to our one-dimensional example, we could have drawn our boundary in different ways which would have been equally good at separating the known data.

![](https://miro.medium.com/v2/resize:fit:700/1*RW4wMJ__vCFfhbw3psIKPg.png)

![](https://miro.medium.com/v2/resize:fit:700/1*F164wvkspxLvsjzHIYbzeA.png)

This, too, affects how we make decisions for new data. Say it happens to be 55 degrees out; the top manifold predicts Hal 9001 will be satisfied but the bottom predicts Hal 9001 will not be satisfied.

This sort of arbitrariness is something important to think about. It suggests that there are many different equally good solutions to any problem that can be learned by the system. Usually, however, we want the model to learn a ‘true manifold’. This is what we imagine to be the ‘real manifold’ which perfectly (or at least optimally) separates not just the known points in the dataset, but all the points that we would ever collect. This concept is inextricably tied to the phenomenon we are collecting data from.

The process of learning, then, is that of *generalizing differences* in the feature space; to draw the manifold snaking through feature space in a way that meaningfully separates different data points. In the process, we learn general rules in the dataset.

Crucially, the manifold-mapping interpretation of learning helps us emphasize how learning ‘affects’ the dataset. Even though the model is only trained on a finite number of points, we indeed understand that it is relevant to every point in the feature space. Therefore, the manifold-mapping interpretation allows us to understand how models *generalize* — how they learn the rules we want them to learn (the ‘real manifold’) rather than learning short-cuts to cheaply separate data in the feature space which do not accurately reflect the true underlying phenomena.

Let’s consider an example of manifold-mapping in three dimensions:

![](https://miro.medium.com/v2/resize:fit:700/1*IRB7MUYqqNKEVZiY4Vvlgw.png)

A manifold in three-dimensional space that separates these points is a ‘surface’ in the more familiar sense of the word; it acts like a blanket draping over the space, real meaningful relationships between features (ideally) manifesting in every arc and curve in its trajectory across the feature space.

![](https://miro.medium.com/v2/resize:fit:700/1*3MNkxvp420HP7OxDcyfA3g.png)

Now, consider a model which classifies a 100-by-100 pixel image — which is fairly low quality — as either that of a dog or a cat. Assuming this image is in grayscale, there are 10,000 unique pixels in this image. Each one of these pixels is a dimension in this feature space. The objective of such a cat/dog classifier would be to discover the manifold in 10,000-dimensional space which, too, arcs and bends throughout this massive theoretical space, capturing the relevant visual relationships differentiating images of dogs and cats in the topological shape of this surface.

This is a complex idea. It is less intuitive than the loss-directed parameter update interpretation, but an important idea to think about.

## Contributions from Psychology and Philosophy of Mind

The loss-directed parameter update interpretation describes learning as the iterative update of an internal set of state in response to a loss, or feedback signal describing the badness of the current state. The manifold mapping interpretation describes learning as the formation of a manifold (decision boundary, surface) in the feature space which optimally separates different data points but also ostensibly makes ‘predictions’ (generalizations) throughout the entire space.

These seem like reasonable and perhaps even natural ways to interpret the process of learning in this context. However, even though these are dominantly mathematical, technical, and abstract descriptions of the concept of ‘learning’, it is important to recognize that such a description still affirms or conforms towards a certain philosophical perspective or worldview.

There are many different philosophical stances and theories on what ‘learning’ is, on what it means to ‘learn’. A common misconception is to associate the apparent internal consistency of fields like mathematics and the sciences (which, upon closer investigation, is not really quite so consistent after all) with the implicit label of ‘objectivity’ and ‘truth’. As we will further explore in later chapters, this misconception often leads towards misplaced or over-placed trust in computational or mathematical systems like AI.

We begin this process of identifying AI’s various implicit philosophical assumptions early on, by briefly understanding how ‘learning’ has been philosophically approached and which paths the loss-directed parameter update and manifold mapping interpretations conform to.

**Associationism** is a theory of learning with a long history of development, from Locke and Hume in the eighteenth century to its modern significance in relationship to Artificial Intelligence. It suggests that organisms learn based on a history of causal inferences: through experiencing the world presented to them, they begin to *associate* some phenomena with some other phenomena if they have often previously encountered the two linked in some manner previously.

![](https://miro.medium.com/v2/resize:fit:700/1*hmbSsvtjOuMf3EnfR_H6gw.png)

For instance, every time Isaac throws an apple in the air, it falls back down. In associationist lens, Isaac has developed a piece of learned knowledge: every time an apple is thrown in the air, it falls back down. Isaac might throw an orange in the air a few times and find that it too falls back down every time. After trying this same routine with several other objects, Isaac would learn to *generalize the association*: the quality of falling back down after being thrown in the air is not inherent to the object of the apple but to objects in general.

Associationists posit that there is only one core mental process: the association of ideas through experience. Ivan Pavlov’s work in psychology is perhaps the most well-known evidence in favor of associative learning. Pavlov’s dogs automatically salivated when encountering the smell of meat due to the historically established association between smelling meat (before eating it) and salivating.

In more popular culture, Jim exploits associative learning processes against Dwight on *The Office*. Every time Jim restarts his PC — playing the iconic Windows ‘unlock workstation’ sound — Jim offers Dwight a mint. Dwight accepts every time, to the point where he instinctively presents his hand upon hearing the sound. One day, Jim restarts his computer, and Dwight reaches out, expecting the routine mint. Jim asks Dwight what he is doing, to which Dwight responds “I don’t know” — then grimaces and makes salivary mouth-sounds as he asks why his mouth suddenly tastes so poorly.

After Pavlov, Edward Thorndike proposed the “Law of Effect” in 1911. This suggested that behaviors which are associated with a feeling of satisfaction will lead to repetition of that behavior. The Law of Effect goes beyond Pavlovian passive associative learning towards active learning: an organism actively engages in (or represses) behaviors to maximize satisfaction or reward. This is the logic used with training dogs’ good behavior, for instance: the dog is presented with a reward for a desired behavior (and a punishment for poor behavior, which is arguably the negation of reward).

The loss-directed parameter update paradigm is directly in alignment with this associative account of learning. Through the reinforcement of which behaviors (i.e. the state, the aggregate of parameters) are ‘good’ (low loss) and ‘bad’ (high loss), the model seeks to move towards better behaviors and away from worse ones.

Two additional concepts from psychological learning theory are differentiation and unitization. In differentiation, subjects perceive the difference between properties which were perceived as a singular property before; in unitization; in unitization, subjects perceive one property which was perceived as multiple properties previously. This dual system of separation and unification help to make sense of information — to be able to find meaningful nuances which differentiate seemingly uniform phenomena, and to be able to group together concepts which may appear on the surface level to be different but are somehow meaningfully connected.

![](https://miro.medium.com/v2/resize:fit:700/1*TgK7bNvYAz3STmCKCmb70g.png)

The manifold mapping interpretation of learning is a direct mathematical analog to the dual concepts of differentiation and unitization. The objective of the manifold is most obviously to separate space, but also to determine which space *not to separate* — that is, to unify.

![](https://miro.medium.com/v2/resize:fit:700/1*kJ6wn78S8Gz3ki5tXc7Lvw.png)

Given that manifold mapping and loss-directed parameter update are two-sides of the same coin — that the parameters of a model determine how the manifold is drawn, and that the manifold is shaped to minimize loss but by optimally separating — we can also see the links between associative learning theory and the differentiation-unitization dyad of perceptive learning theory. This is one example of how the applied can inform the theoretical. There is a substantive body of work throughout the early and modern arc of AI development which similarly applies technical AI advancements to guide new research inquiry in philosophy, psychology, and neuroscience.

## In conclusion…

We can think of learning as *loss-directed parameter update* — an agent attempting to adjust various free variables to minimize error — and also as *manifold mapping* — discovering general rules that apply across the observational space, thereby separating some samples while unitizing others. As we saw, these two interpretations are two sides of the same coin: one is model-centric, and the other is data-centric. Although both are commonly used in machine learning, we can also find uses in other fields, such as the behavioral sciences.

Thanks for reading!

*All images created by author.*