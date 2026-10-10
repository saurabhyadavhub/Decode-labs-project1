# Project Report: Rule-Based AI Chatbot

**Organization:** DecodeLabs  
**Training:** Artificial Intelligence — Project 1  
**Project title:** Rule-Based AI Chatbot  
**Technology:** Python 3

## 1. Aim
To create a simple rule-based chatbot that responds to predefined user inputs using conditional statements and a continuous interaction loop.

## 2. Objectives
- Accept text input from a user.
- Recognize selected greetings, help requests, simple topics, and exit commands.
- Select responses through `if`, `elif`, and `else` statements.
- Continue the conversation until an exit command is entered.

## 3. Requirements
**Software:** Python 3.8 or later and a terminal/command prompt.  
**Libraries:** Python standard library only; no installation is required.

## 4. Working
The program reads a line of input, trims surrounding whitespace, and converts it to lowercase for matching. It then checks the input against predefined conditions. The matching branch returns a response. If no rule matches, a fallback response is displayed. The main loop repeats this process until an exit phrase is entered. `EOFError` and `KeyboardInterrupt` are also handled gracefully.

## 5. Algorithm
1. Start the program and display instructions.
2. Read the user's message.
3. Normalize the message by trimming whitespace and converting it to lowercase.
4. Check the message against the predefined rules.
5. Display the selected response.
6. If the input is an exit command, stop; otherwise return to Step 2.

## 6. Concepts Used
- **Control flow:** conditional branching with `if` / `elif` / `else`.
- **Looping:** `while True` maintains the conversation.
- **Functions:** `get_response()` separates response logic from interaction.
- **String handling:** `strip()` and `lower()` make matching more consistent.
- **Input/output:** `input()` receives messages and `print()` displays replies.

## 7. Test Cases
| Input | Expected behavior |
|---|---|
| `hello` | Greeting response |
| `WHAT IS YOUR NAME` | Returns chatbot identity (case-insensitive) |
| `help` | Displays supported capabilities |
| `what is AI` | Returns a short AI definition |
| `python` | Returns a short Python description |
| `thanks` | Returns a courtesy response |
| `unknown phrase` | Displays fallback response |
| `bye` | Says goodbye and ends the loop |
| Empty input | Asks the user to type something |

## 8. Limitations
The chatbot does not learn from conversations and cannot understand arbitrary natural language. It only responds to the patterns explicitly coded in its rules. Some topic rules use keyword matching, so any message containing those keywords may trigger the corresponding response.

## 9. Possible Enhancements
- Add more intents and response patterns.
- Store rules in a separate JSON file.
- Add a graphical user interface.
- Add unit tests and conversation logging (with appropriate privacy safeguards).

## 10. Conclusion
The project demonstrates a basic conversational interface using deterministic rules. It fulfills the supplied Project 1 requirements: handling greetings and exit commands, using if-else logic, and running in a continuous loop.
