# ZeeBot

**ZeeBot** is a simple Rule-Based python chatbot that includes a GUI built using tkinter library.  I was inspired by this [video](https://youtu.be/CkkjXTER2KE?si=oRzaePWg4eV9KWuY) to make the chatbot. **ZeeBot** is designed to communicate with the user in *brainrot* slang. 

## ⚙️ Prerequisites:

+ Python 3.x
+ tkinter library
+ json library

## 🛠️ Function:

+ The bot reads the text entry in chat window's text box.
+ The `find_best_match` method in `main.py` compares the user entry with the pre-defined text in `knowledge_base.json`.
+ The method `get_answer_for_question` retrieves the corresponding answer to the text from `knowledge_base.json`.
+ If the text entered does not match with any text recorded in `knowledge_base.json` then the bot prompts the user to teach it how to respond to that particular text.
+ A new entry is recorded in `knowledge_base.json` in *question and answer* format using the `save_knowledge_base` method.

## 🏗️ Running ZeeBot:

Navigate to the directory where `main.py` is located and run it in `terminal`.
```
D:\> cd ZeeBot
D:\ZeeBot> python main.py
```

> [!NOTE]
> Fork this repository to add new responses and customize the GUI. This project was built on a whim but I learnt much in the process. I plan on building better and more smarter bots in the future. Thank you for checking out this repo! ☺️

# Screenshots
