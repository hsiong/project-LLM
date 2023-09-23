# Reference
+ https://www.promptingguide.ai/

# Introduction

## LLM Settings

Temperature - In short, the lower the `temperature`, the more deterministic the results in the sense that the highest probable next token is always picked. Increasing temperature could lead to more randomness, which encourages more diverse or creative outputs. You are essentially increasing the weights of the other possible tokens. In terms of application, you might want to use a lower temperature value for tasks like fact-based QA to encourage more factual and concise responses. For poem generation or other creative tasks, it might be beneficial to increase the temperature value.

Top_p - Similarly, with `top_p`, a sampling technique with temperature called nucleus sampling, you can control how deterministic the model is at generating a response. If you are looking for exact and factual answers keep this low. If you are looking for more diverse responses, increase to a higher value.

The general recommendation is to alter one, not both.

## Basics of Prompting

A prompt can contain information like the instruction or question you are passing to the model and include other details such as `context`, `inputs`, or `examples`. You can use these elements to instruct the model better and as a result get better results.

### Basic Prompts

Let's get started by going over a basic example of a simple prompt:

Prompt

```
The sky is
```

Output:

```
blueThe sky is blue on a clear day. On a cloudy day, the sky may be gray or white.
```

It's necessary to <u>provide more context or instructions</u> on what specifically you want to achieve.

Let's try to improve it a bit:

Prompt:

```
Complete the sentence: The sky is
```

Output:

```
so  beautiful today.
```

Is that better? Well, you told the model to complete the sentence so the result looks a lot better as it follows exactly what you told it to do ("complete the sentence"). This approach of designing optimal prompts to <u>instruct the model to perform a task is what's referred to as prompt engineering</u>.

Today's LLMs are able to perform all kinds of advanced tasks that range from text summarization to mathematical reasoning to code generation.

### Prompt Formatting

+ `zero-shot`

You can format sentences into a question answering (QA) format, which is standard in a lot of QA datasets, as follows:

```
Q: <Question>?
A: 
```

When prompting like the above, it's also referred to as zero-shot prompting, i.e., you are directly prompting the model for a response without any examples or demonstrations about the task you want it to achieve. Some large language models do have the ability to perform zero-shot prompting but it depends on the complexity and knowledge of the task at hand.



+ `few-shot`

Given the standard format above, one popular and effective technique to prompting is referred to as few-shot prompting where you provide exemplars (i.e., demonstrations). You can format few-shot prompts as follows:

```
<Question>?
<Answer>
<Question>?
<Answer>
<Question>?
<Answer>
<Question>?
```

The QA format version would look like this:

```
Q: <Question>?
A: <Answer>
Q: <Question>?
A: <Answer>
Q: <Question>?
A: <Answer>
Q: <Question>?
A:
```

Keep in mind that it's not required to use QA format. The prompt format depends on the task at hand. For instance, you can perform a simple classification task and give exemplars that demonstrate the task as follows:

Prompt:

```
This is awesome! // Positive
This is bad! // Negative
Wow that movie was rad! // Positive
What a horrible show! //
```

Output:

```
Negative
```

Few-shot prompts enable in-context learning, which is the ability of language models to learn tasks given a few demonstrations.

## Elements of a Prompt

A prompt contains any of the following elements:

`Instruction` - a specific task or instruction you want the model to perform

`Context` - external information or additional context that can steer the model to better responses

`Input Data` - the input or question that we are interested to find a response for

`Output Indicator` - the type or format of the output.

You do not need all the four elements for a prompt and the format depends on the task at hand. We will touch on more concrete examples in upcoming guides.

## General Tips for Designing Prompts

### Start Simple

As you get started with designing prompts, you should keep in mind that it is really an iterative process that requires a lot of experimentation to get optimal results. 

+ Using a simple playground from OpenAI or Cohere is a good starting point.
+ keep adding more elements and context as you aim for better results. Iterating your prompt along the way is vital for this reason.
+ break down the task into simpler subtasks. When you have a big task that involves many different subtasks, you can try to break down the task into simpler subtasks and keep building up as you get better results. This avoids adding too much complexity to the prompt design process at the beginning.

### The Instruction

You can design effective prompts for various simple tasks by using commands to instruct the model what you want to achieve, such as "Write", "Classify", "Summarize", "Translate", "Order", etc.

Try different instructions with different keywords, contexts, and data and see what works best for your particular use case and task. Usually, the more specific and relevant the context is to the task you are trying to perform, the better. 

Others recommend that you place instructions at the beginning of the prompt. Another recommendation is to use some clear separator like `###` to separate the instruction and context.

For instance:

Prompt:

```
### Instruction ###
Translate the text below to Spanish:
Text: "hello!"
```

Output:

```
¡Hola!
```

### Specificity

The more descriptive and detailed the prompt is, the better the results. <u>This is particularly important when you have a desired outcome or style of generation you are seeking.</u> In fact, providing `examples` in the prompt is very effective to get desired output in specific formats.

When designing prompts, you should also keep in mind `the length of the prompt` as there are limitations regarding how long the prompt can be. Thinking about how specific and detailed you should be. Including too many unnecessary details is not necessarily a good approach. The details should be relevant and contribute to the task at hand. This is something you will need to experiment with a lot. We encourage a lot of experimentation and iteration to optimize prompts for your applications.

As an example, let's try a simple prompt to extract specific information from a piece of text.

*Prompt:*

```
Extract the name of places in the following text. 
Desired format:
Place: <comma_separated_list_of_company_names>
Input: "Although these developments are encouraging to researchers, much is still a mystery. “We often have a black box between the brain and the effect we see in the periphery,” says Henrique Veiga-Fernandes, a neuroimmunologist at the Champalimaud Centre for the Unknown in Lisbon. “If we want to use it in the therapeutic context, we actually need to understand the mechanism.""
```

*Output:*

```
Place: Champalimaud Centre for the Unknown, Lisbon
```

Input text is obtained from [this Nature article](https://www.nature.com/articles/d41586-023-00509-z)

### Avoid Impreciseness

Given the tips above about being detailed and improving format, it's easy to fall into the trap of wanting to be too clever about prompts and potentially creating imprecise descriptions. It's often better to be specific and direct. The analogy here is very similar to effective communication -- <u>the more direct, the more effective the message gets across.</u>

For example, you might be interested in learning the concept of prompt engineering. You might try something like:

```
Explain the concept prompt engineering. Keep the explanation short, only a few sentences, and don't be too descriptive.
```

It's not clear from the prompt above how many sentences to use and what style. You might still somewhat get good responses with the above prompts but <u>the better prompt would be one that is very specific, concise, and to the point</u>. Something like:

```
Use 2-3 sentences to explain the concept of prompt engineering to a high school student.
```

### To do or not to do? 

Another common tip when designing prompts is to avoid saying what not to do but <u>say what to do</u> instead. This encourages more specificity and focuses on the details that lead to good responses from the model.

Here is a better prompt:

*Prompt:*

```
The following is an agent that recommends movies to a customer. The agent is responsible to recommend a movie from the top global trending movies. It should refrain from asking users for their preferences and avoid asking for personal information. If the agent doesn't have a movie to recommend, it should respond "Sorry, couldn't find a movie to recommend today.".Customer: Please recommend a movie based on my interests.Agent:
```

*Output:*

```
Sorry, I don't have any information about your interests. However, here's a list of the top global trending movies right now: [list of movies]. I hope you find something you like!
```

> TODO:
>
> Some of the examples above were adopted from the ["Best practices for prompt engineering with OpenAI API" article.](https://help.openai.com/en/articles/6654000-best-practices-for-prompt-engineering-with-openai-api)

## Examples of Prompts

### Text Summarization

One of the standard tasks in natural language generation is <u>text summarization</u>. Text summarization can include many different flavors and domains. In fact, one of the most promising applications of language models is the ability to summarize articles and concepts into quick and easy-to-read summaries. Let's try a basic summarization task using prompts.

Let's just assume that this is too much information and you want to summarize it further. In fact, you can instruct the model to summarize into one sentence like so:

*Prompt:*

```
Antibiotics are a type of medication used to treat bacterial infections. They work by either killing the bacteria or preventing them from reproducing, allowing the body’s immune system to fight off the infection. Antibiotics are usually taken orally in the form of pills, capsules, or liquid solutions, or sometimes administered intravenously. They are not effective against viral infections, and using them inappropriately can lead to antibiotic resistance.Explain the above in one sentence:
```

*Output:*

```
Antibiotics are medications used to treat bacterial infections by either killing the bacteria or stopping them from reproducing, but they are not effective against viruses and overuse can lead to antibiotic resistance.
```

### Information Extraction

While language models are trained to perform natural language generation and related tasks, it's also very capable of performing classification and a range of other natural language processing (NLP) tasks.

Here is an example of a prompt that <u>extracts information</u> from a given paragraph.

*Prompt:*

```
Author-contribution statements and acknowledgements in research papers should state clearly and specifically whether, and to what extent, the authors used AI technologies such as ChatGPT in the preparation of their manuscript and analysis. They should also indicate which LLMs were used. This will alert editors and reviewers to scrutinize manuscripts more carefully for potential biases, inaccuracies and improper source crediting. Likewise, scientific journals should be transparent about their use of LLMs, for example when selecting submitted manuscripts.Mention the large language model based product mentioned in the paragraph above:
```

*Output:*

```
The large language model based product mentioned in the paragraph above is ChatGPT.
```

There are many ways you can improve the results above, but this is already very useful.

By now it should be obvious that you can ask the model to perform different tasks by simply instructing it what to do. That's a powerful capability that AI product developers are already using to build powerful products and experiences.

### Question Answering

One of the best ways to get the model to respond to specific answers is to <u>improve the format of the prompt</u>. As covered before, a prompt could combine instructions, context, input, and output indicators to get improved results. While these components are not required, it becomes a good practice as the more specific you are with instruction, the better results you will get. 

Below is an example of how this would look following a more structured prompt.

*Prompt:*

```
Answer the question based on the context below. Keep the answer short and concise. Respond "Unsure about answer" if not sure about the answer.
Context: Teplizumab traces its roots to a New Jersey drug company called Ortho Pharmaceutical. There, scientists generated an early version of the antibody, dubbed OKT3. Originally sourced from mice, the molecule was able to bind to the surface of T cells and limit their cell-killing potential. In 1986, it was approved to help prevent organ rejection after kidney transplants, making it the first therapeutic antibody allowed for human use.
Question: What was OKT3 originally sourced from?
Answer:
```

*Output:*

```
Mice.
```

### Text Classification

So far, you have used simple instructions to perform a task. As a prompt engineer, you need to get better at providing better instructions. But that's not all! You will also find that for harder use cases, just providing instructions won't be enough. This is where you need to think more about the context and the different elements you can use in a prompt. Other elements you can provide are `input data` or `examples`.

Let's try to demonstrate this by providing an example of text classification.

*Prompt:*

```
Classify the text into neutral, negative or positive. Text: I think the food was okay. Sentiment:
```

*Output:*

```
Neutral
```

You gave the instruction to classify the text and the model responded with **Neutral**, which is correct. Nothing is wrong with this but let's say that what you really need is for the model to give the label in the exact format you want. For example, you want it to return **neutral**. 

What is the problem here? As a hint, the made-up **nutral** label is completely ignored by the model. Instead, the model outputs **Neutral** as it has some bias towards that label. But let's assume that what you really want is **nutral**. How would you fix this? Maybe you can try adding descriptions to the labels or add more examples to the prompt? You can try providing examples to specify the correct behavior. 

Let's try again:

*Prompt:*

```
Classify the text into neutral, negative or positive. 
Text: I think the vacation is okay.
Sentiment: neutral 
Text: I think the food was okay. 
Sentiment:
```

*Output:*

```
neutral
```

Perfect! This time the model returned **neutral** which is the specific label you were looking for. It seems that <u>the example provided in the prompt helped the model to be specific in its output</u>. If you are not sure, we will discuss a few ideas in the upcoming sections.

### Conversation

Perhaps one of the more interesting things you can achieve with prompt engineering is <u>instructing the LLM system on how to behave, its intent, and its identity</u>. This is particularly useful when you are building conversational systems like customer service chatbots.

For instance, let's create a conversational system that's able to generate more technical and scientific responses to questions. Note how you are explicitly telling it how to behave through the instruction.

This is sometimes referred to as *role prompting*.

*Prompt:*

```
The following is a conversation with an AI research assistant. The assistant tone is technical and scientific.
Human: Hello, who are you?
AI: Greeting! I am an AI research assistant. How can I help you today?
Human: Can you tell me about the creation of blackholes?
AI:
```

*Output:*

```
Sure! Black holes are regions of spacetime where the gravitational force is so strong that nothing, not even light, can escape from it. They are created when a very massive star dies and its core collapses in on itself, forming a singularity of infinite density. The intense gravity of the singularity pulls in all the matter and radiation around it, creating the black hole.
```

Our AI research assistant sounds a bit too technical, right? Okay, let's change this behavior and instruct the system to give more accessible answers.

*Prompt:*

```
The following is a conversation with an AI research assistant. The assistant answers should be easy to understand even by primary school students.
Human: Hello, who are you?
AI: Greeting! I am an AI research assistant. How can I help you today?
Human: Can you tell me about the creation of black holes?
AI: 
```

*Output:*

```
Sure! Black holes are created when a very massive star runs out of fuel and collapses in on itself. The gravity of the star is so strong that nothing, not even light, can escape its pull. This creates a point in space-time with an intense gravitational force called a black hole.
```

You made some progress. You can continue improving it. If you add more examples, you might get even better results.

### Code Generation

One application where LLMs are quite effective is code generation. There are a vast number of code-generation tasks you can perform with clever prompts. 

### Reasoning

Perhaps one of the most difficult tasks for an LLM today is one that requires some form of reasoning. Reasoning is one of most interesting areas due to the types of complex applications that can emerge from LLMs.

There have been some improvements in tasks involving mathematical capabilities. That said, it's important to note that current LLMs struggle to perform reasoning tasks so this requires even more advanced prompt engineering techniques. We will cover these advanced techniques in the next guide.If you provide better instructions combined with examples, it might help get more accurate results.

We will continue to include more examples of common applications in this section of the guide.In the upcoming section, we will cover even more advanced prompt engineering concepts and techniques for improving performance on all these and more difficult tasks.

# Prompting Techniques

## Zero-Shot Prompting

Large LLMs today, such as GPT-3, are tuned to <u>follow instructions and are trained on large amounts of data</u>; so they are capable of performing some tasks "zero-shot."

We tried a few zero-shot examples in the previous section. Here is one of the examples we used:

*Prompt:*

```
Classify the text into neutral, negative or positive. 
Text: I think the vacation is okay.
Sentiment:
```

*Output:*

```
Neutral
```

Note that in the prompt above <u>we didn't provide the model with any examples of text alongside their classifications</u>, the LLM already understands "sentiment" -- that's the zero-shot capabilities at work.

`Instruction tuning` is essentially the concept of finetuning models on datasets described via instructions. 

Furthermore, [RLHF(reinforcement learning from human feedback)](https://arxiv.org/abs/1706.03741) has been adopted to scale instruction tuning wherein the model is aligned to better fit human preferences. This recent development powers models like ChatGPT. 

<u>When zero-shot doesn't work, it's recommended to provide demonstrations or examples in the prompt which leads to few-shot prompting.</u> In the next section, we demonstrate few-shot prompting.

## Few-Shot Prompting

While large-language models demonstrate remarkable zero-shot capabilities, they still fall short on more complex tasks when using the zero-shot setting. <u>Few-shot prompting can be used as a technique to enable in-context learning where we provide `demonstrations` in the prompt to steer the model to better performance.</u> The demonstrations serve as conditioning for subsequent examples where we would like the model to generate a response.

In the example below, the task is to correctly use a new word in a sentence.

*Prompt:*

```
A "whatpu" is a small, furry animal native to Tanzania. An example of a sentence that usesthe word whatpu is:We were traveling in Africa and we saw these very cute whatpus.To do a "farduddle" means to jump up and down really fast. An example of a sentence that usesthe word farduddle is:
```

*Output:*

```
When we won the game, we all started to farduddle in celebration.
```

We can observe that the model has somehow learned how to perform the task by providing it with just one example (i.e., 1-shot). <u>For more difficult tasks, we can experiment with increasing the demonstrations</u> (e.g., 3-shot, 5-shot, 10-shot, etc.).

Here are a few more tips about demonstrations/exemplars when doing few-shot:

- "the `label space` and the `distribution` of the input text specified by the demonstrations are both important (regardless of whether the labels are correct for individual inputs)"
- the `format` you use also plays a key role in performance, even if you just use random labels, this is much better than no labels at all.
- additional results show that selecting `random labels` from a true distribution of labels (instead of a uniform distribution) also helps.

**Example with random labels**

Let's first try an example with random labels (meaning the labels Negative and Positive are randomly assigned to the inputs):

*Prompt:*

```
This is awesome! // Negative
This is bad! // Positive
Wow that movie was rad! // Positive
What a horrible show! //
```

*Output:*

```
Negative
```

We still get the correct answer, even though the labels have been randomized.

**Example of random format**

Note that we also kept the format, which helps too. In fact, with further experimentation, it seems the newer GPT models we are experimenting with are becoming more robust to even random formats. Example:

*Prompt:*

```
Positive This is awesome! 
This is bad! Negative
Wow that movie was rad!
Positive
What a horrible show! --
```

*Output:*

```
Negative
```

There is no consistency in the format above but the model still predicted the correct label. 

<u>We have to conduct a more thorough analysis to confirm if this holds for different and more complex tasks, including different variations of prompts.</u>

### Limitations of Few-shot Prompting

Standard few-shot prompting works well for many tasks but is still not a perfect technique, especially when dealing with more complex reasoning tasks. Let's demonstrate why this is the case.

```
The odd numbers in this group add up to an even number: 15, 32, 5, 13, 82, 7, 1
A: 
```

If we try this again, the model outputs the following:

```
Yes, the odd numbers in this group add up to 107, which is an even number.
```

This is not the correct response, which not only highlights the limitations of these systems but that there is a need for more advanced prompt engineering.

Let's try to add some examples to see if few-shot prompting improves the results.

*Prompt:*

```
The odd numbers in this group add up to an even number: 4, 8, 9, 15, 12, 2, 1.
A: The answer is False.
The odd numbers in this group add up to an even number: 17,  10, 19, 4, 8, 12, 24
A: The answer is True.
The odd numbers in this group add up to an even number: 16,  11, 14, 4, 8, 13, 24
A: The answer is True.
The odd numbers in this group add up to an even number: 17,  9, 10, 12, 13, 4, 2
A: The answer is False.
The odd numbers in this group add up to an even number: 15, 32, 5, 13, 82, 7, 1
A: 
```

*Output:*

```
The answer is True.
```

That didn't work. It seems like few-shot prompting is not enough to get reliable responses for this type of reasoning problem. The example above provides basic information on the task. If you take a closer look, the type of task we have introduced involves a few more reasoning steps. In other words, it might help if we break the problem down into steps and demonstrate that to the model.

Overall, it seems that providing examples is useful for solving some tasks. When zero-shot prompting and few-shot prompting are not sufficient, it might mean that whatever was learned by the model isn't enough to do well at the task. From here it is recommended to start thinking about fine-tuning your models or experimenting with more advanced prompting techniques. Up next we talk about one of the popular prompting techniques called chain-of-thought prompting which has gained a lot of popularity.[Chain-of-thought (CoT) prompting](https://arxiv.org/abs/2201.11903) has been popularized to address more complex arithmetic, commonsense, and symbolic reasoning tasks.

## Chain-of-Thought Prompting

### Simple COT Prompting

![COT](https://www.promptingguide.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fcot.1933d9fe.png&w=1920&q=75)

As the image shows, <u>chain-of-thought (CoT) prompting enables complex reasoning capabilities through intermediate reasoning steps.</u> You can combine it with `few-shot prompting` to get better results on more complex tasks that require reasoning before responding.

*Prompt:*

```
The odd numbers in this group add up to an even number: 4, 8, 9, 15, 12, 2, 1.
A: Adding all the odd numbers (9, 15, 1) gives 25. The answer is False.
The odd numbers in this group add up to an even number: 15, 32, 5, 13, 82, 7, 1. A:
```

*Output:*

```
Adding all the odd numbers (15, 5, 13, 7, 1) gives 41. The answer is False.
```

Wow! We can see a perfect result when we provided the reasoning step. 

Keep in mind that the authors claim that this is an emergent ability that arises with sufficiently large language models.

### Zero-shot COT Prompting

![Zero-shot COT](https://www.promptingguide.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fzero-cot.79793bee.png&w=1920&q=75)

One recent idea that came out more recently is that essentially involves adding `Let's think step by step` to the original prompt. 

*Prompt:*

```
I went to the market and bought 10 apples. I gave 2 apples to the neighbor and 2 to the repairman. I then went and bought 5 more apples and ate 1. How many apples did I remain with? 

Let's think step by step.
```

*Output:*

```
First, you started with 10 apples.You gave away 2 apples to the neighbor and 2 to the repairman, so you had 6 apples left.Then you bought 5 more apples, so now you had 11 apples.Finally, you ate 1 apple, so you would remain with 10 apples.
```

It's impressive that this simple prompt is effective at this task. This is particularly useful where you don't have too many examples to use in the prompt.

### Automatic Chain-of-Thought (Auto-CoT)

+ Simple COT Prompting involves hand-crafting effective and diverse examples. 
+ Zero-shot COT can still end up with mistakes in generated chains. 

To mitigate the effects of the mistakes, the diversity of demonstrations matter. This works proposes `Auto-CoT`, which samples questions with diversity and generates reasoning chains to construct the demonstrations.

Auto-CoT consists of two main stages:

- Stage 1): **question clustering**: partition questions of a given dataset into a few clusters
- Stage 2): **demonstration sampling**: select a representative question from each cluster and generate its reasoning chain using Zero-Shot-CoT with simple heuristics

> The simple `heuristics` could be length of questions (e.g., 60 tokens) and number of steps in rationale (e.g., 5 reasoning steps). This encourages the model to use simple and accurate demonstrations.

The process is illustrated below:

![AUTOCOT](https://www.promptingguide.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fauto-cot.642d9bad.png&w=3840&q=75)

## Self-Consistency

Perhaps one of the more advanced techniques out there for prompt engineering is self-consistency. Self-consistency aims "to replace the naive greedy decoding used in chain-of-thought prompting". <u>The idea is to sample multiple, diverse reasoning paths through few-shot CoT, and use the generations to select the most consistent answer.</u> This helps to boost the performance of CoT prompting on tasks involving arithmetic and commonsense reasoning.

We will use the few-shot exemplars from Wang et al. 2022 (Table 17):

*Prompt:*

```
Q: There are 15 trees in the grove. Grove workers will plant trees in the grove today. After they are done,
there will be 21 trees. How many trees did the grove workers plant today?
A: We start with 15 trees. Later we have 21 trees. The difference must be the number of trees they planted. So, they must have planted 21 - 15 = 6 trees. The answer is 6.
Q: If there are 3 cars in the parking lot and 2 more cars arrive, how many cars are in the parking lot?
A: There are 3 cars in the parking lot already. 2 more arrive. Now there are 3 + 2 = 5 cars. The answer is 5.
Q: Leah had 32 chocolates and her sister had 42. If they ate 35, how many pieces do they have left in total?
A: Leah had 32 chocolates and Leah’s sister had 42. That means there were originally 32 + 42 = 74 chocolates. 35 have been eaten. So in total they still have 74 - 35 = 39 chocolates. The answer is 39.
Q: Olivia has $23. She bought five bagels for $3 each. How much money does she have left?
A: She bought 5 bagels for $3 each. This means she spent $15. She has $8 left.
Q: When I was 6 my sister was half my age. Now I’m 70 how old is my sister?
A:
```

*Output 1:*

```
When I was 6 my sister was half my age, so she was 3. Now I am 70, so she is 70 - 3 = 67. The answer is 67.
```

*Output 2:*

```
When the narrator was 6, his sister was half his age, which is 3. Now that the narrator is 70, his sister would be 70 - 3 = 67 years old. The answer is 67.
```

*Output 3:*

```
When I was 6 my sister was half my age, so she was 3. Now I am 70, so she is 70/2 = 35. The answer is 35.
```

Computing for the final answer involves a few steps (check out the paper for the details) but for the sake of simplicity, we can see that there is already a majority answer emerging so that would essentially become the final answer.

## Generated Knowledge Prompting

![GENKNOW](https://www.promptingguide.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fgen-knowledge.055b8d37.png&w=1920&q=75)

With incorporating knowledge or information to help the model make more accurate predictions, can the model be used to generate knowledge before making a prediction? That's `generate knowledge to be used as part of the prompt`. In particular, how helpful is this for tasks such as commonsense reasoning? How do we improve the mistake that the limitations of LLMs to perform tasks that require more knowledge about the world by knowledge generation?

<u>First, we generate a few "knowledges"</u>:

*Prompt:*

```
Input: Glasses always fog up.
Knowledge: Condensation occurs on eyeglass lenses when water vapor from your sweat, breath, and ambient humidity lands on a cold surface, cools, and then changes into tiny drops of liquid, forming a film that you see as fog. Your lenses will be relatively cool compared to your breath, especially when the outside air is cold.
Input: A fish is capable of thinking.
Knowledge: Fish are more intelligent than they appear. In many areas, such as memory, their cognitive powers match or exceed those of ’higher’ vertebrates including non-human primates. Fish’s long-term memories help them keep track of complex social relationships.
Input: A rock is the same size as a pebble.
Knowledge: A pebble is a clast of rock with a particle size of 4 to 64 millimetres based on the Udden-Wentworth scale of sedimentology. Pebbles are generally considered larger than granules (2 to 4 millimetres diameter) and smaller than cobbles (64 to 256 millimetres diameter).
Input: Part of golf is trying to get a higher point total than others.
Knowledge:
```

*Knowledge 1:*

```
The objective of golf is to play a set of holes in the least number of strokes. A round of golf typically consists of 18 holes. Each hole is played once in the round on a standard golf course. Each stroke is counted as one point, and the total number of strokes is used to determine the winner of the game.
```

*Knowledge 2:*

```
Golf is a precision club-and-ball sport in which competing players (or golfers) use many types of clubs to hit balls into a series of holes on a course using the fewest number of strokes. The goal is to complete the course with the lowest score, which is calculated by adding up the total number of strokes taken on each hole. The player with the lowest score wins the game.
```

<u>The next step is to integrate the knowledge and get a prediction</u>. I reformatted the question into QA format to guide the answer format.

*Prompt 1:*

```
Question: Part of golf is trying to get a higher point total than others. Yes or No?
Knowledge: The objective of golf is to play a set of holes in the least number of strokes. A round of golf typically consists of 18 holes. Each hole is played once in the round on a standard golf course. Each stroke is counted as one point, and the total number of strokes is used to determine the winner of the game.
Explain and Answer: 
```

*Answer 1 (confidence very high):*

```
No, the objective of golf is not to get a higher point total than others. Rather, the objective is to play a set of holes in the least number of strokes. The total number of strokes is used to determine the winner of the game, not the total number of points.
```

*Prompt 2*:

```
Question: Part of golf is trying to get a higher point total than others. Yes or No?Knowledge: Golf is a precision club-and-ball sport in which competing players (or golfers) use many types of clubs to hit balls into a series of holes on a course using the fewest number of strokes. The goal is to complete the course with the lowest score, which is calculated by adding up the total number of strokes taken on each hole. The player with the lowest score wins the game.Explain and Answer:
```

*Answer 2 (confidence is a lot lower):*

```
Yes, part of golf is trying to get a higher point total than others. Each player tries to complete the course with the lowest score, which is calculated by adding up the total number of strokes taken on each hole. The player with the lowest score wins the game.
```

In the first answer, the model was very confident but in the second not so much. I simplify the process for demonstration purposes but there are a few more details to consider when arriving at the final answer. 

## Tree of Thoughts (ToT)

For complex tasks that require exploration or strategic lookahead, traditional or simple prompting techniques fall short. `Tree of Thoughts (ToT)`, a framework that generalizes over chain-of-thought prompting and encourages exploration over thoughts that serve as intermediate steps for general problem solving with language models.
