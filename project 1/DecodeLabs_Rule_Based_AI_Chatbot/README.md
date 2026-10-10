# DecodeLabs Project 1 — Rule-Based AI Chatbot

A simple command-line chatbot built with Python and explicit `if` / `elif` / `else` rules. It runs in a continuous loop and exits when the user enters an exit command.

## Requirements
- Python 3.8 or later
- No third-party packages required

## Run
Open a terminal in this folder and execute:

```bash
python chatbot.py
```

If your system uses `python3`, run `python3 chatbot.py`.

## Example
```text
You: hello
Bot: Hello! I'm your DecodeLabs rule-based chatbot. How can I help you?
You: what is AI
Bot: Artificial intelligence (AI) is the field of creating computer systems that perform tasks associated with human intelligence.
You: bye
Bot: Goodbye! Thanks for chatting. Have a great day!
```

## Supported input examples
- Greetings: `hi`, `hello`, `hey`, `good morning`
- Identity/help: `who are you`, `what can you do`, `help`
- Topics: `what is AI`, questions containing `artificial intelligence` or `python`
- Courtesy: `thanks`, `thank you`
- Exit: `bye`, `goodbye`, `exit`, `quit`, `stop`

This is a rule-based program, not a machine-learning model. Its responses are determined by rules written in the source code.
