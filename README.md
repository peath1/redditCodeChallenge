# redditCodeChallenge
run the decoder.py to extract all the symbols into a binary form. It will go through and split the image into 50x50 images (size of one symbol) and find the shapes present in the symbol. It then assigns a byte for that symbol based on the shapes present. the order of the bits is arbitrarily chosen, and is NOT neccessarily the correct order, I have yet to find the correct order

## ascii2.py
this file will take the results.csv output from the decoder and attempt to find the form of it. presently this tries all 8! combinations of the 8 bit positions, and attempts to translate them to ascii. the MSB is set to 0 regardless of value as otherwise the ascii translation will always be for numbers greater than 128 in the table, which aren't correct. By default this code will say that 0 acceptable lines were found because I was playing around with filtering out translations with special characters that are unlikely to be part of the translation. If you remove that filtering from the code you should get a csv of all the possible character translations.

Any bugs let me know ( there will be many, this code is mostly hastily GPT generated and modified, and as such is very ugly and very poorly formatted and commented)
Best of Luck!
ToastedToasty 
