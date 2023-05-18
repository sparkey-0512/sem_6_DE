# Program 1.0
# This Program 1.0 creates a Html file that shows difference between texts in both the files using colors.

from difflib import SequenceMatcher
import difflib
import os

first_file = "txt1.txt"
second_file = "txt2.txt"

first_file_lines = str(open(first_file, encoding="utf8").readlines())
second_file_lines = str(open(second_file, encoding="utf8").readlines())

first_file_lines1 = open(first_file, encoding="utf8").readlines()
second_file_lines1 = open(second_file, encoding="utf8").readlines()

# d = difflib.HtmlDiff()
# print d.make_table(text1_lines, text2_lines)
difference = difflib.HtmlDiff(wrapcolumn=50).make_file(first_file_lines1, second_file_lines1, first_file, second_file)

difference_report = open('result.html', 'w')
difference_report.write(difference)
difference_report.close()

os.system("google-chrome-stable result.html")
# Program 2.0 starts here
# This Program 2.0 prints only plagiarized text.


#file1 = open("txt1.txt","r")
#text1 = file1.readlines()
## print("Content of text file 1 in List:")
## print(text1)
#
#
#file2 = open("txt2.txt","r")
#text2 = file2.readlines()
## print("\n\nContent of text file 2 in List:")
## print(text2)
#
## Convert list to string
#
#str1=''.join(text1)
#str2=''.join(text2)
#
## print("\n\nContent of text file 1:")
## print(str1)
## print("\n\nContent of text file 2:")
## print(str2)
#
#
## Split the string
#
#sent_text1 = str1.split('.')
#sent_text2 = str2.split('.')
## print(sent_text1)
## Create a for loop that compares two lists
#
#final_list=[]
#for z in sent_text1:
#    for y in sent_text2:
#        if z == y:
#            final_list.append(z)
#
#
#print("\n Plagiarized Content Below:\n")
#print(final_list)

# Program 3.0 for finding similarity percentage


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


val = similar(first_file_lines, second_file_lines)*100
percentage = round(val, 2)
print("\n Similarity Percentage :", percentage, "%")

print("\nNow,Check for difference report Html file.")
