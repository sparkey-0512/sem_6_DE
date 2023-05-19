from django.shortcuts import render
from .models import Files
import os

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
            for i in txt_file:
                with open(os.path.join('media',str(i.txtFile))) as f:
                    Text_File_list.append(f.read())
            return render(req,'txt_Upload/txt_upload.html',{'txt_files':Text_File_list})
        else:
            print("Please Check your Image or You were not uploaded 2 Images")
    return render(req,'txt_Upload/txt_upload.html')


def TxtWritePast(req):
    if req.method == 'POST':
        text1 = req.POST.get('text1')
        text2 = req.POST.get('text2')
        return render(req,'txt_write_past/txt_write_past.html',{'text1':text1,'text2':text2})
    return render(req,'txt_write_past/txt_write_past.html')