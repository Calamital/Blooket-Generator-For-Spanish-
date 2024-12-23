from deep_translator import GoogleTranslator
import random
translator = GoogleTranslator(source = "es", target = "en")
eswords: list[str] = []
enwords: list[str] = []

with open("Blooket-Generator-For-Spanish-\input.txt", "r") as inputfile:
    eswords = "".join(list(inputfile)).split("\n")
    for index in range(len(eswords)):
        eswords[index] = eswords[index].replace(",", " /")
    inputfile.close()
for word in eswords:
    enwords.append(translator.translate(word))

with open("Blooket-Generator-For-Spanish-\output.csv", "w") as outputfile:
    outputfile.write(
        """\"Blooket
Import Template\",,,,,,,
Question #,Question Text,Answer 1,Answer 2,\"Answer 3
(Optional)\",\"Answer 4
(Optional)\",\"Time Limit (sec)
(Max: 300 seconds)\",\"Correct Answer(s)
(Only include Answer #)\"
"""
    )
    
    for question in range(len(eswords)):
        answers: list[str] = ["", "", ""]
        escopy = eswords[:]
        del escopy[escopy.index(eswords[question])]
        for index in range(len(answers)):
            randword: str = escopy[random.randrange(0, len(escopy))]
            answers[index] = randword
            del escopy[escopy.index(randword)]
    
        outputfile.write(
            str(question + 1) + "," +   # Question Number
            enwords[question] + "," +   # Question
            answers[0] + "," +          # Answer 1
            answers[1] + "," +          # Answer 2
            answers[2] + "," +          # Answer 3
            eswords[question] + "," +   # Answer 4
            "299," +                    # Time Limit
            "4\n"                       # Correct Answer
        )
    outputfile.close()
