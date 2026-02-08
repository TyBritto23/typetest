# Generate a fixed-length string of random words
from pathlib import Path
from random import randint

def getWordsList(length):
    file_dir = Path(__file__).resolve().parent
    file_path = file_dir / "../data/words.txt"
    words = []
    try:
        with open(file_path, 'r') as f:
            for line in f:
                words.append(line.strip())
        
        words = shuffleTextFile(words, len(words))

        string = " ".join(words[:length])

        return string


    except FileNotFoundError:
        print("Error the file was not found")
    except Exception as e:
        print(f"An error occured: {e}")

def shuffleTextFile(arr, n):
    for i in range(n-1, 0, -1):
        j = randint(0, i+1)

        arr[i], arr[j] = arr[j], arr[i]

    return arr
            
