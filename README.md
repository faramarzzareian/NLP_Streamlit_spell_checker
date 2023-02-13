# Spell Checker GUI Application

This is a simple spell checker GUI application written in Python using the tkinter and pyspellchecker libraries.
## Requirements

    Python 3
    tkinter
    pyspellchecker

## Usage

#### To run the spell checker GUI application, simply clone the repository and run the following command:

python spell_checker.py

The GUI application will launch and you can start typing in the text area. To check the spelling, click the "Check Spelling" button. The application will automatically correct any spelling errors in the text.
## Code Overview

The code creates a SpellCheckerApp class that implements the spell checker functionality. The create_widgets method creates the text area and the "Check Spelling" button in the GUI. The check_spelling method splits the text into words, checks the spelling of each word, and corrects any spelling errors. The corrected text is then displayed in the text area.
