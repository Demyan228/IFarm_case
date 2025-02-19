from openai import OpenAI
import time
from functools import wraps


def timer(func):
    @wraps(func)
    def inner(*args, **kwargs):
        start_time = time.time()
        retval = func(*args, **kwargs)
        print(f"{time.time() - start_time:.2f} seconds elapsed")
        return retval
    return inner

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key="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",
)
summarize_prompt = """As a professional summarizer, create a detailed and comprehensive summary of the provided text, be it an article, post, conversation, or passage, while adhering to these guidelines:
1. Craft a summary that is detailed, thorough, in-depth, and complex, while maintaining clarity.

2. Incorporate main ideas and essential information, eliminating extraneous language and focusing on critical aspects.

3. Rely strictly on the provided text, without including external information.

4. Format the summary in paragraph form for easy understanding.

5.Conclude your notes with [End of Notes, Message #X] to indicate completion, where "X" represents the total number of messages that I have sent. In other words, include a message counter where you start with #1 and add 1 to the message counter every time I send a message.

By following this optimized prompt, you will generate an effective summary that encapsulates the essence of the given text in a clear, detailed, and reader-friendly manner. Optimize output as markdown file.

"{text}"

DETAILED SUMMARY:"""


@timer
def summarize(text):
  completion = client.chat.completions.create(
    model="qwen/qwen2.5-vl-72b-instruct:free",
    messages=[
      {
        "role": "user",
        "content": summarize_prompt.format(text=text)
      }
    ]
  )
  if completion.choices is None:
      raise ValueError(completion.choices)
  return completion.choices[0].message.content
