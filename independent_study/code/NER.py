from ParseXML import ParseXML as P
I = P('../dataset/books_txt/processed_punkt/book1_processed.txt.xml')
I.getroot()
print I.getNER()