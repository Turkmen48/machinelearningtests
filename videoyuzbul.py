import cv2
import imageio
face=cv2.CascadeClassifier("haarcascade-frontalface-default.xml")
eye=cv2.CascadeClassifier("haarcascade-eye.xml")
def yuzbul(resim):
    gri=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    yuzler=face.detectMultiScale(gri,1.3,5)#gri=resmi grileştir,1.3 resim ne kadar küçülcek 5 de en az 5 dikdörtgen o resimde yüz bulursa yüz var diye return yap
    for (x,y,w,h) in yuzler:
        cv2.rectangle(resim,(x,y),(x+w,y+h),(255,0,0),2)
        gri_yuz=gri[y:y+h,x:x+w] #burada gri yüz için alacağımız alanları belirledik
        renkli_yuz=resim[y:y+h,x:x+w]#burada renkli yüz için alacğmız alanlar yani resmin tamamının pikseli alıncak
        gozler=eye.detectMultiScale(gri_yuz,1.1,3)#gri=resmi grileştir,1.3 resim ne kadar küçülcek 5 de en az 5 dikdörtgen o resimde göz bulursa göz var diye return yap gri_yuz içinde arama yapcaz çünkü göz arıyoz sadece
        for (ex,ey,ew,eh) in gozler:
            cv2.rectangle(renkli_yuz,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
    return frame

reader=imageio.get_reader('1.mp4')#videoyu açtık
fps=reader.get_meta_data()['fps']#kaç fps video bakıyoz
writer=imageio.get_writer("output.mp4",fps=fps)#çıkış videomuz ile giriş videomuzun fpsini eşitledik
for i, frame in enumerate(reader):#her seferinde frame'ye yazdığmı fonksiyonu uygulicaz ve i ise sayaç kaçınıc framde detect yapiyoz enumerate fonksiyonu ise her frameye sayıatıyor
    frame=yuzbul(frame)
    writer.append_data(frame)
    print(i)
writer.close()






