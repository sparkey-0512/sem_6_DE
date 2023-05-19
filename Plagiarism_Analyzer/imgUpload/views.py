from django.shortcuts import render
from .models import Files
from scripts.Image import image_pl 
import os
from Plagiarism_Analyzer.settings import BASE_DIR

def CheckTheImage(images):
    temp = [False,False]
    if len(images) == 2:
        for index,img in enumerate(images):
            if img.name.lower().endswith(('.png', '.jpg', '.jpeg')):
                temp[index] = True
        if temp[0] and temp[1]: return True
    return False


def ImgUploadPage(req):
    if req.method == 'POST':
        img_path = 'media/file/'
        for i in os.listdir(img_path):
            os.remove(os.path.join(img_path,i))
        imgs = Files.objects.all()
        for i in imgs:
            i.delete()
        files = req.FILES.getlist('imgs')
        if CheckTheImage(files):
            for img in files:
                new_file = Files(imgs = img)
                new_file.save()
            imgs = Files.objects.all()
            img1 = imgs[0].imgs.url
            img2 = imgs[1].imgs.url
            print(img1,img2)
            result = image_pl.Image_Plagiarism(os.path.join(str(BASE_DIR) + img1),os.path.join(str(BASE_DIR) + img2))
            similarity = result[0]
            plagiarism = result[1]

            difference_image = '/media/file/difference_image.jpg'
            return render(req,'Image_Upload/img_upload.html',{'images':imgs,'diff_img':difference_image,'similarity':similarity,'plagiarism':plagiarism,'error':'none','show':'flex'})
        else:
            return render(req,'Image_Upload/img_upload.html',{'error':'flex','show':'none'})
            print("Please Check your Image or You were not uploaded 2 Images")
    return render(req,'Image_Upload/img_upload.html',{'error':'none','show':'none'})
