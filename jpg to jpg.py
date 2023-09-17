from PIL import Image    #Pillow
from PIL import ImageFont
from PIL import ImageDraw
from time import sleep
import os
def changeJpgToPng(srcPath,dstPath):
    image = Image.open(srcPath)

    png_name = str(dstPath)[0:-len('.jpg')] + '.png'
    # image.save(png_name)
    # print(png_name)

    # image = image.convert('RGBA')
    image = image.convert('RGB')
    image.save(png_name)
    pass

def caiImage(img_path, output_path, text,a,b,d):
    chang=a+1
    kuang=b+1
    qiandu=d
    img1 = Image.open(img_path)
    img1 = img1.convert('RGBA')
    # 新建一个和原图大小一样的水印覆盖层
    text_overlay = Image.new('RGBA', img1.size, (255, 255, 255, 0))
    # 创建一个画图对象
    image_draw = ImageDraw.Draw(text_overlay)
    # 加载字体，设置字体大小
    c = int(img1.size[0]/(12*chang))#自适应大小
    font = ImageFont.truetype('汉字之美神勇兔生肖体.ttf', c)  # ttf字体类型，别的ttf需要自己下载,c->字体大小
    # 在指定位置画上文字水印，160就是透明度
    print("高度:"+str(img1.size[0])+",宽度:"+str(img1.size[1]))

    for j in range(int(img1.size[0]/chang),int(img1.size[0]),int(img1.size[0]/chang)):
        for k in range(int(img1.size[1]/kuang),int(img1.size[1]),int(img1.size[1]/kuang)):
            image_draw.text((j,k), text, font=font, fill=(100, 100, 100, qiandu))# 水印字体RGB颜色
            img1 = Image.alpha_composite(img1, text_overlay)
    img1.save(output_path)

path = "输入" #输入文件夹目录
path2 = "输出"#输出目录
files= os.listdir(path)
i=1
for file in files: #遍历文件夹
    if '.jpg' in file:
        e_file = path +'/' + file
        changeJpgToPng(e_file,e_file)

for file in os.listdir(path):  # 遍历文件夹
    if '.png' in file:
        del_file = path + '/' + file
        caiImage(del_file, path2 + "/" + str(i) + ".png", 'text',3,3,10)#text->设置的字体  长有多少个水印 宽有多少个水印  不透明度（0-255）
        i=i+1
for file in os.listdir(path2):
    if '.png' in file:
        kaikai = path2+'/'+file
        img = Image.open(kaikai)
        #new_file = os.path.splitext(kaikai)[0] + '.jpg'
        new_file = str(kaikai)[0:-len('.png')] + '.jpg'
        img.convert('RGB').save(new_file)
for file in os.listdir(path):
    if '.png' in file:
        os.remove(path+'/'+file)
for file in os.listdir(path2):
    if '.png' in file:
        os.remove(path2+'/'+file)

print("finish"+str(i-1)+"page")







