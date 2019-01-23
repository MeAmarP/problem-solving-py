mapData = {'G':'C',
           'C':'G',
           'T':'A',
           'A':'U'}
           
keyData = mapData.keys()
def JadooDNATrans(InputData):
    outStr = ""
    for char in InputData:
        if char in keyData:            
            outStr = outStr + mapData[char]
        else:
            outStr = "Invalid Input"
            break
    return(outStr)

print(JadooDNATrans(input()))
