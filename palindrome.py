word1 = "subi no onibus"
word2 = "subi no onibus"
def ispalindrome(word1,word2):
    ProcessedFirstWord = word1[::-1].replace(" ","").lower()
    ProcessedSecondWord = word2.replace(" ","").lower()

    if word1 == word2:
        return True
    else: return False
    

print(ispalindrome("subi no onibus", "subi no onibus"))
    
