#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk
from tkinter import ttk
from spellchecker import SpellChecker

class SpellCheckerApp:
    def __init__(self, root):
        self.root = root
        self.spell = SpellChecker(language='en')
        self.root.title("Spell Checker")
        self.create_widgets()
    
    def create_widgets(self):
        self.text = tk.Text(self.root, height=20, width=50)
        self.text.pack(side="left", fill="both", expand=True)
        self.scrollbar = tk.Scrollbar(self.root)
        self.scrollbar.pack(side="right", fill="y")
        self.scrollbar.config(command=self.text.yview)
        self.text.config(yscrollcommand=self.scrollbar.set)
        self.check_button = ttk.Button(self.root, text="Check Spelling", command=self.check_spelling)
        self.check_button.pack(side="bottom")
    
    def check_spelling(self):
        text = self.text.get("1.0", "end")
        words = text.split()
        corrected_words = []
        for word in words:
            if word not in self.spell:
                correction = self.spell.correction(word)
                corrected_words.append(correction)
            else:
                corrected_words.append(word)
        corrected_text = " ".join(corrected_words)
        self.text.delete("1.0", "end")
        self.text.insert("1.0", corrected_text)

root = tk.Tk()
app = SpellCheckerApp(root)
root.mainloop()

