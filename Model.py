from textblob import TextBlob
#from gingerit import GingerIt


class SpellCheckerModel:
    def __init__(self):
        self.spell_check = TextBlob("")
        #self.grammar_check = GingerIt()
        
    def correct_spell(self, text):
        words = text.split()
        corrected_words = []
        for word in words:
            correct_word = str(TextBlob(word).correct())
            corrected_words.append(correct_word)
        return " ".join(corrected_words)
    
    def correct_grammar(self, text):
        matches = self.grammar_check.parse(text)

        foundmistakes = []
        for error in matches['corrections']:
            foundmistakes.append(error['text'])
        return foundmistakes

        
    
    
        
if __name__ == "__main__":
    model = SpellCheckerModel()
    text = "Ths is a smple txt with sme speling erors."
    print("Corrected Text:", model.correct_spell(text))
    grammar_text = "She go to the store yesterday."
    print("Grammar Mistakes:", model.correct_grammar(grammar_text))