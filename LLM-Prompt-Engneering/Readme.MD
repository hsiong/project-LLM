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

One of the standard tasks in natural language generation is text summarization. Text summarization can include many different flavors and domains. In fact, one of the most promising applications of language models is the ability to summarize articles and concepts into quick and easy-to-read summaries. Let's try a basic summarization task using prompts.

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

Here is an example of a prompt that extracts information from a given paragraph.

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

