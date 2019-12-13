def main():
    document = open("document for christmas list.txt","w+")  #Created a text file in Python

    document.write("I want a motherboard"+ "\n" + "I want a monitor"+"\n" +   #Put context in the document
     "I also want to be with family")
    document.close()  #Closed the document

main()  #Called the main function
