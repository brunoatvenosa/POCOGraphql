import string

commentToken = "#"

wordUnion = "union"
wordType = "type"
headerPublicClass = "namespace Contracts \n" \
                    "public class "
headerPublicInterface = "namespace Contracts \n" \
                        "public interface "

schemaFileName = "schema.graphql"

knownTypes = []


def fillClass(file, fileClass, lineNumber):
    for i, lineStr in enumerate(file, lineNumber):
        print(f"fillClass {lineStr}")
        if lineStr.startswith(commentToken):
            lineStr = lineStr.replace(commentToken, "//")
            print(f"fillClass write")
            fileClass.write(lineStr)
            

        if (lineStr.startswith("}")):
            return
        # split = lineStr.split(" ")
        # print(split[0])
        # print(split[1])

def resolveType(schemaFile, objectName, lineNumber):
    with open("contracts/"+objectName+".cs", "w+") as contractFile:
        contractFile.write(headerPublicClass + objectName + "{")
        for i, line in enumerate(schemaFile, lineNumber):
            if(not line.contains("(") and not line.contains("[")):
                print("simple var")
                
                
                
        contractFile.write("}")

def createFiles():
    # Use a breakpoint in the code line below to debug your script.
    schemaFile = open(schemaFileName, "r")

    for i, line in enumerate(schemaFile, 0):

        if line.startswith(wordUnion):
            fnName = "I"+line[wordType.__len__():].split(" ")[1]
            outputFile = headerPublicInterface + fnName + "{"
            print(f"{fnName} {i}")
            with open("contracts/"+fnName+".cs", "w+") as contractFile:
                contractFile.write(outputFile)
                contractFile.write("}")

        if line.startswith(wordType):
            fnName = line[wordType.__len__():].split(" ")[1]
            outputFile = headerPublicClass + fnName + "{"
            print(f"{fnName} {i}")
            resolveType(schemaFile,fnName,i)
            # with open("contracts/"+fnName+".cs", "w+") as contractFile:
            #     contractFile.write(outputFile)
            #     contractFile.write("outputFile")
                
                # for interatorForClass, lineStr in enumerate(file, i):
                #     print(f"fillClass {lineStr}")
                #     if lineStr.startswith(commentToken):
                #         lineStr = lineStr.replace(commentToken, "//")
                #         print(f"fillClass write")
                #         fileClass.write(lineStr)
                        

                # if (lineStr.startswith("}")):
                #     return
                
                # contractFile.write("}")
                



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    createFiles()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
