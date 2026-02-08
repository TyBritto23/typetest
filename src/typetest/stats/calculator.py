# Calculate stats 
# Time, WPM, Keystrokes, Errors, Accuracy

# Returns  a list containing stats
def getStats(current_input_str, targetWords, startTime, stopTime, keystrokes):
    stats = {} # WPM, accuracy, raw WPM, time, keystrokes
    totalTime = max(stopTime - startTime, 1)
    typedWords = current_input_str.split()
    allWords = targetWords.split()

    # Words per minute
    stats["wpm"] = getWPM(typedWords, allWords, totalTime)

    stats["accuracy"] = getAccuracy(typedWords, allWords)

    stats["raw wpm"] = (len(current_input_str) / 5) / (totalTime / 60)

    stats["time"] = totalTime

    stats["keystrokes"] = keystrokes

    return stats

# ["sdlfjs", "asdlf", ]
def getWPM(typedWords, allWords, totalTime):
    # only count words without typos as characters typed
    numChars = -1

    for i in range(len(allWords)):
        if i == len(typedWords) or i == len(allWords):
            break
        elif typedWords[i] == allWords[i]:
            numChars += len(typedWords[i])
        numChars += 1 # include spaces as typed chars

    wpm = (numChars / 5)  / (totalTime / 60)

    return wpm


def getAccuracy(typedWords, allWords):
    correctWordsNum = 0

    for i in range(len(allWords)):
        if i == len(typedWords) or i == len(allWords):
            break
        elif typedWords[i] == allWords[i]:
            correctWordsNum += 1

    return correctWordsNum / len(allWords)
