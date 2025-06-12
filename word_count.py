from pathlib import Path

def count_words(path):
    """Count the approximate words in a file."""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        #print(f"Sorry, the file {path} does not exist.")
        pass
    else: 
        words = contents.split()
        num_words = len(words)
        print(f"The file {path} has about {num_words} words.")

def word_freq(path, word):
    """Count the approximate words in a file."""
    try:
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        #print(f"Sorry, the file {path} does not exist.")
        pass
    else: 
        words = contents
        num_freq = words.lower().count(word)
        print(f"The file {path} has the word {word} a total of {num_freq} times.")

filenames = ['text_files/alice.txt','text_files/moby_dick.txt', 
             'text_files/siddartha.txt', 'text_files/little_women.txt']
for file in filenames:
    path = Path(file)
    word_freq(path,"poop")