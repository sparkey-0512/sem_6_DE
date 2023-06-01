from django.shortcuts import render
from .models import Files
import os
import difflib
from difflib import SequenceMatcher

def CheckTheSimilOFText():
    first_file = "media/txtFiles/text1.txt"
    second_file = "media/txtFiles/text2.txt"

    first_file_lines = str(open(first_file).readlines())
    second_file_lines = str(open(second_file).readlines())

    first_file_lines1 = open(first_file).readlines()
    second_file_lines1 = open(second_file).readlines()

    difference = difflib.HtmlDiff(wrapcolumn=50).make_file(first_file_lines1, second_file_lines1, first_file, second_file)

    difference_report = open('templates/result/result.html', 'w')
    difference_report.write(difference)
    difference_report.close()

    def similar(a, b):
        return SequenceMatcher(None, a, b).ratio()

    val = similar(first_file_lines, second_file_lines)*100
    percentage = round(val, 2)
    print("\n Similarity Percentage :", percentage, "%")


def CheckTheTxtFile(txt_files):
    temp = [False,False]
    if len(txt_files) == 2:
        for index,txt in enumerate(txt_files):
            if txt.name.lower().endswith(('.txt')):
                temp[index] = True
        if temp[0] and temp[1]: return True
    return False


def TxtUploadPage(req):
    if req.method == 'POST':
        txt_file_path = 'media/txtFiles'
        for i in os.listdir(txt_file_path):
            os.remove(os.path.join(txt_file_path,i))
        txt_file = Files.objects.all()
        for i in txt_file:
            i.delete()
        txt_files = req.FILES.getlist('text_file')
        if CheckTheTxtFile(txt_files):
            for txt in txt_files:
                new_file = Files(txtFile = txt)
                new_file.save()
            txt_file = Files.objects.all()
            Text_File_list = []

            CheckTheSimilOFText()

            for i in txt_file:
                with open(os.path.join('media',str(i.txtFile))) as f:
                    Text_File_list.append(f.read())
            return render(req,'txt_Upload/txt_upload.html',{'txt_files':Text_File_list,'display':'flex','error':'none'})
        else:
            return render(req,'txt_Upload/txt_upload.html',{'display':'none','error':'flex'})
    return render(req,'txt_Upload/txt_upload.html',{'display':'none','error':'none'})


def TxtWritePast(req):
    if req.method == 'POST':
        text1 = req.POST.get('text1')
        text2 = req.POST.get('text2')

        file = open('media/txtFiles/text1.txt','w')
        file.write(text1)
        file.close()

        file = open('media/txtFiles/text2.txt','w')
        file.write(text2)
        file.close()

        CheckTheSimilOFText()

        return render(req,'txt_write_past/txt_write_past.html',{'text1':text1,'text2':text2,'display':'flex'})
    return render(req,'txt_write_past/txt_write_past.html',{'display':'none'})

def Result(req):
    return render(req,'result/result.html')