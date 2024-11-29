OpenAI APIと対話形式でコミュニケーションできるCLIツールです。
OpenAIライブラリを使ったコミュニケーションのためのロジック（履歴をmessagesに足していく）の把握と、OpenAI APIのデバッグのために作りました。

# 使い方

```
git clone https://github.com/shinobe179/openai-api-client.git
cd path/to/directory
export OPENAI_API_KEY=foobar
uv run main.py
```

# 出力例

```
$ uv run main.py
> こんにちは！あなたと会話するためのCLIツールを書いてみました。
ChatCompletion(id='chatcmpl-AYiqFYxRQwmQpuD0uyYL9vo7vX6sD', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='こんにちは！CLIツールを書くなんて素晴らしいですね。どんな機能を持ったツールなのか、ぜひ教えてください！また、何か質問やサポートが必要でしたら、遠慮なく聞いてくださいね。', refusal=None, role='assistant', audio=None, function_call=None, tool_calls=None))], created=1732838887, model='gpt-4o-mini-2024-07-18', object='chat.completion', service_tier=None, system_fingerprint='fp_3de1288069', usage=CompletionUsage(completion_tokens=54, prompt_tokens=28, total_tokens=82, completion_tokens_details=CompletionTokensDetails(accepted_prediction_tokens=0, audio_tokens=0, reasoning_tokens=0, rejected_prediction_tokens=0), prompt_tokens_details=PromptTokensDetails(audio_tokens=0, cached_tokens=0)))
*-*-* history *-*-*
{'role': 'system', 'content': ''}
{'role': 'user', 'content': 'こんにちは！あなたと会話するためのCLIツールを書いてみました。'}
{'role': 'assistant', 'content': 'こんにちは！CLIツールを書くなんて素晴らしいですね。どんな機能を持ったツールなのか、ぜひ教えてください！また、何か質問やサポートが必要でしたら、遠慮なく聞いてくださいね。'}
> 会話のコンテキストを維持しながら、CLI上で会話できるシンプルなツールです。
ChatCompletion(id='chatcmpl-AYiqjLsJI0Rg2VeCpaqPsPMcZSNO5', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='それは面白いですね！会話のコンテキストを維持することで、より自然なやり取りが可能になりますね。ツールの実装方法や使用している言語について詳しく教えていただけますか？また、構築中に直面した課題や感想などもあれば、ぜひお聞かせください。', refusal=None, role='assistant', audio=None, function_call=None, tool_calls=None))], created=1732838917, model='gpt-4o-mini-2024-07-18', object='chat.completion', service_tier=None, system_fingerprint='fp_0705bf87c0', usage=CompletionUsage(completion_tokens=79, prompt_tokens=119, total_tokens=198, completion_tokens_details=CompletionTokensDetails(accepted_prediction_tokens=0, audio_tokens=0, reasoning_tokens=0, rejected_prediction_tokens=0), prompt_tokens_details=PromptTokensDetails(audio_tokens=0, cached_tokens=0)))
*-*-* history *-*-*
{'role': 'system', 'content': ''}
{'role': 'user', 'content': 'こんにちは！あなたと会話するためのCLIツールを書いてみました。'}
{'role': 'assistant', 'content': 'こんにちは！CLIツールを書くなんて素晴らしいですね。どんな機能を持ったツールなのか、ぜひ教えてください！また、何か質問やサポートが必要でしたら、遠慮なく聞いてくださいね。'}
{'role': 'user', 'content': '会話のコンテキストを維持しながら、CLI上で会話できるシンプルなツールです。'}
{'role': 'assistant', 'content': 'それは面白いですね！会話のコンテキストを維持することで、より自然なやり取りが可能になりますね。ツールの実装方法や使用している言語について詳しく教えていただけますか？また、構築中に直面した課題や感想などもあれば、ぜひお聞かせください。'}
> 
