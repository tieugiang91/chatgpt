import openai

response = openai.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "user", "content": "The cat says "}
    ],
    max_tokens=5,
)
# ChatCompletion(id='chatcmpl-9f1Fj37PEBLdDYfiA2eSLcDuvBEF3', choices=[Choice(finish_reason='length', index=0, logprobs=None, message=ChatCompletionMessage(content='"meow."\n\nCats', role='assistant', function_call=None, tool_calls=None))], created=1719563291, model='gpt-4o-2024-05-13', object='chat.completion', service_tier=None, system_fingerprint='fp_d576307f90', usage=CompletionUsage(completion_tokens=5, prompt_tokens=11, total_tokens=16))
print(response.choices[0].message.content)