import re
import numpy as np
import pandas as pd

                   
Input = open("input.txt","r").read().split()
Token = []            
for Input_Word in Input:
    

    if re.match("([1-9][0-9]*)|0", Input_Word):
        if Input_Word[len(Input_Word) - 1] == ';': 
            Token.append([Input_Word[:-1], "Constant"])
            Token.append([';', 'Semi-colon'])
        else: 
            Token.append([Input_Word, "Constant"])
    
    
    elif Input_Word in ['str', 'int', 'bool','float','char']: 
        Token.append([Input_Word, 'Datatype'])
    
    elif Input_Word in '><!*-/+%=':
        Token.append([Input_Word, "Operator"])
    

    elif Input_Word in ['if','for','break','elif','else','while','then','do',
    'return','void','case','private', 'public']:
        Token.append([Input_Word, "Keyword Word"])


    elif re.match("[a-zA-Z]+", Input_Word):
        if Input_Word[len(Input_Word) - 1] == ';':
            Token.append([Input_Word[:-1], "Identifier"])
            Token.append([';', 'Semi-colon'])
        else:
            Token.append([Input_Word, "Identifier"])


Token = np.array(Token)
Token = pd.DataFrame(Token, columns=['Value','Token'])
print(Token)