

import vigenereCipher
import difflib

dictionary2 = ['awesomeness', 'hearkened', 'aloneness', 'beheld', 'courtship', 'swoops', 'memphis', 'attentional', 'pintsized', 'rustics', 'hermeneutics', 'dismissive', 'delimiting', 'proposes', 'between', 'postilion', 'repress', 'racecourse', 'matures', 'directions', 'pressed', 'miserabilia', 'indelicacy', 'faultlessly', 'chuted', 'shorelines', 'irony', 'intuitiveness', 'cadgy', 'ferries', 'catcher', 'wobbly', 'protruded', 'combusting', 'unconvertible', 'successors', 'footfalls', 'bursary', 'myrtle', 'photocompose']


def main():
    ciphertext = input('Ciphertext:')
    possiblekeys = getPossibleKeyFirstWord(ciphertext)
#    print (possiblekeys)
    max_possiblePlaintext = 0
    max_possibleKey = ''
    Final_Plaintext = ''
    for possiblekey in possiblekeys:
        possiblePlaintext = getPlaintext(ciphertext,possiblekeys[possiblekey])
        if len(possiblePlaintext) > max_possiblePlaintext:
            max_possibleKey = possiblekey
            max_possiblePlaintext = len(possiblePlaintext)
            Final_Plaintext = possiblePlaintext
        #if len(possiblePlaintext) >1:
        #    print ("Key:",possiblekeys[possiblekey])
        #    print ("Plaintext:",possiblePlaintext)
    print("Key:", possiblekeys[max_possibleKey])
    print("Plaintext:",Final_Plaintext)

def getPossibleKeyFirstWord(ciphertext):
    firstDecryptedText = {}
    for word in dictionary2:
        firstDecryptedText[word] = vigenereCipher.decryptMessage(word,ciphertext[:len(word)])
    return firstDecryptedText

def getPlaintext(ciphertext,key):
    Plaintext = []
    counter = 0
    ciphertext_length = len(ciphertext)
    while counter < ciphertext_length:
        is_word = False
#    print("Testing Key:",key)
#    for i in range (len(ciphertext)):
        dec = vigenereCipher.decryptMessage(key,ciphertext[counter:counter+len(key)])
        if 'ESTONETWOTHR' in key:
            print(dec)
        dec_words = dec.split(' ')
        for dec_word in dec_words:
            for word in dictionary2:
                wordmatchscore = difflib.SequenceMatcher(None,dec_word.upper(),word.upper()).ratio()
                if wordmatchscore > 0.7:
#                print("decrypted:,",dec," Plaintext:",word)
                    Plaintext.append(word)
                    is_word = True
                    break
        
#        counter += 1 if not is_word else counter += len(Plaintext[-1])
            #if is_word:
            #    counter += len(Plaintext[-1])
        counter += 1
    return Plaintext


if __name__ == '__main__':
    main()

