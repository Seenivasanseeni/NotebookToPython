import json

def readNoteBook(path):
    file=open(path,"r")
    return json.load(file)

def appendToSouce(source,code):
        return source + code

def combineCode(codeArray):
    return "".join(codeArray) + "\n"

def makeComment(comment):
    return comment

def convertToPython(notebook):
    pythonSource=""
    for cell in notebook["cells"]:
            if cell["cell_type"]=="code":
                code=combineCode(cell["source"])
                pythonSource = appendToSouce(pythonSource,code)
    return pythonSource

def saveAndConvert(notebookPath):
    notebook = readNoteBook(notebookPath)
    sourceCode = convertToPython(notebook)
    file = open(notebookPath+".py","w")
    file.write(sourceCode)
    file.close()

def test():
    saveAndConvert('LinearRegression.ipynb')

def drive():
    import sys
    filename=sys.argv[1]
    saveAndConvert(filename)
drive()