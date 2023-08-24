#!/usr/bin/env python3
class MyString:

  def __init__(self,value=""):
    if isinstance(value,str):
      self.value=value
    else:
      print("value must be a string")
    
  def is_sentence(self):
        return self.value.endswith('.')

  def is_question(self):
        return self.value.endswith('?')

  def is_exclamation(self):
        return self.value.endswith('!')

  def count_sentences(self):
        # Replace all punctuation marks with a common delimiter, then split on that delimiter
        delimiters = ['.', '?', '!']
        for delimiter in delimiters:
            self.value = self.value.replace(delimiter, '.')
        sentences = self.value.split('.')
        print(sentences)
        
        # Count the non-empty sentences
        count = 0
        for sentence in sentences:
            if sentence.strip():  # Check if the sentence is not just whitespace
                count += 1
        return count