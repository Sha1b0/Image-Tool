
import Mail
from Mail import *
from PIL import ImageOps,ImageFilter,ImageEnhance,ImageChops,ImageWin,ImageFont,ImageDraw
import PIL.Image


from PIL.ImageWin import  HDC
from win32 import  *
from tkinter import  *
import win32
from win32gui import *



try:

    win=Tk()
    while True:
        print('''
        
        
              _____                    _____           _____                    _____                   _____                   _____                               
             /\    \                 /\    \          /\    \                  /\    \                /::\    \                /\    \                 
            /::\    \               /::\____\        /::\    \                /::\____\              /::::\    \              /::\    \                
           /::::\    \             /:::/    /        \:::\    \              /:::/    /             /::::::\    \            /::::\    \               
          /::::::\    \           /:::/    /          \:::\    \            /:::/    /             /::::::::\    \          /::::::\    \              
         /:::/\:::\    \         /:::/    /            \:::\    \          /:::/    /             /:::/~~\:::\    \        /:::/\:::\    \             
        /:::/__\:::\    \       /:::/    /              \:::\    \        /:::/____/             /:::/    \:::\    \      /:::/__\:::\    \            
       /::::\   \:::\    \     /:::/    /               /::::\    \      /::::\    \            /:::/    / \:::\    \    /::::\   \:::\    \           
      /::::::\   \:::\    \   /:::/    /      _____    /::::::\    \    /::::::\    \   _____  /:::/____/   \:::\____\  /::::::\   \:::\    \          
     /:::/\:::\   \:::\    \ /:::/____/      /\    \  /:::/\:::\    \  /:::/\:::\    \ /\    \|:::|    |     |:::|    |/:::/\:::\   \:::\____\         
    /:::/  \:::\   \:::\____\:::|    /      /::\____\/:::/  \:::\____\/:::/  \:::\    /::\____\:::|____|     |:::|    /:::/  \:::\   \:::|    |        
    \::/    \:::\  /:::/    /:::|____\     /:::/    /:::/    \::/    /\::/    \:::\  /:::/    /\:::\    \   /:::/    /\::/   |::::\  /:::|____|        
     \/____/ \:::\/:::/    / \:::\    \   /:::/    /:::/    / \/____/  \/____/ \:::\/:::/    /  \:::\    \ /:::/    /  \/____|:::::\/:::/    /         
              \::::::/    /   \:::\    \ /:::/    /:::/    /                    \::::::/    /    \:::\    /:::/    /         |:::::::::/    /          
               \::::/    /     \:::\    /:::/    /:::/    /                      \::::/    /      \:::\__/:::/    /          |::|\::::/    /           
               /:::/    /       \:::\__/:::/    /\::/    /                       /:::/    /        \::::::::/    /           |::| \::/____/            
              /:::/    /         \::::::::/    /  \/____/                       /:::/    /          \::::::/    /            |::|  ~|                  
             /:::/    /           \::::::/    /                                /:::/    /            \::::/    /             |::|   |                  
            /:::/    /             \::::/    /                                /:::/    /              \::/____/              \::|   |                  
            \::/    /               \::/____/                                 \::/    /                ~~                     \:|   |                  
             \/____/                 ~~                                        \/____/                                         \|___|                  
                                                                                                                                                       
    
        
        
        
        
        
        
        
        
        ''')












        print('''
       _____ __          _ __             ________          __              __               __       
      / ___// /_  ____ _(_) /_  ____     / ____/ /_  ____ _/ /___________ _/ /_  ____  _____/ /___  __
      \__ \/ __ \/ __ `/ / __ \/ __ \   / /   / __ \/ __ `/ //_/ ___/ __ `/ __ \/ __ \/ ___/ __/ / / /
     ___/ / / / / /_/ / / /_/ / /_/ /  / /___/ / / / /_/ / ,< / /  / /_/ / /_/ / /_/ / /  / /_/ /_/ / 
    /____/_/ /_/\__,_/_/_.___/\____/   \____/_/ /_/\__,_/_/|_/_/   \__,_/_.___/\____/_/   \__/\__, /  
                                                                                             /____/   
    ''')
        print(" ############# #############  ")
        print(''' 
     $$$$$$$\              $$\     $$\                                 $$$$$$$\  $$\                  $$\                     $$$$$$$$\      $$\ $$\   $$\                         
    $$  __$$\             $$ |    $$ |                                $$  __$$\ $$ |                 $$ |                    $$  _____|     $$ |\__|  $$ |                        
    $$ |  $$ |$$\   $$\ $$$$$$\   $$$$$$$\   $$$$$$\  $$$$$$$\        $$ |  $$ |$$$$$$$\   $$$$$$\ $$$$$$\    $$$$$$\        $$ |      $$$$$$$ |$$\ $$$$$$\    $$$$$$\   $$$$$$\  
    $$$$$$$  |$$ |  $$ |\_$$  _|  $$  __$$\ $$  __$$\ $$  __$$\       $$$$$$$  |$$  __$$\ $$  __$$\\_$$  _|  $$  __$$\       $$$$$\   $$  __$$ |$$ |\_$$  _|  $$  __$$\ $$  __$$\ 
    $$  ____/ $$ |  $$ |  $$ |    $$ |  $$ |$$ /  $$ |$$ |  $$ |      $$  ____/ $$ |  $$ |$$ /  $$ | $$ |    $$ /  $$ |      $$  __|  $$ /  $$ |$$ |  $$ |    $$ /  $$ |$$ |  \__|
    $$ |      $$ |  $$ |  $$ |$$\ $$ |  $$ |$$ |  $$ |$$ |  $$ |      $$ |      $$ |  $$ |$$ |  $$ | $$ |$$\ $$ |  $$ |      $$ |     $$ |  $$ |$$ |  $$ |$$\ $$ |  $$ |$$ |      
    $$ |      \$$$$$$$ |  \$$$$  |$$ |  $$ |\$$$$$$  |$$ |  $$ |      $$ |      $$ |  $$ |\$$$$$$  | \$$$$  |\$$$$$$  |      $$$$$$$$\\$$$$$$$ |$$ |  \$$$$  |\$$$$$$  |$$ |      
    \__|       \____$$ |   \____/ \__|  \__| \______/ \__|  \__|      \__|      \__|  \__| \______/   \____/  \______/       \________|\_______|\__|   \____/  \______/ \__|      
              $$\   $$ |                                                                                                                                                          
              \$$$$$$  |                                                                                                                                                          
               \______/                                                                                                                                                                                                       
    ''')

        image1 =PIL.Image.open(input("File path of image:"))


        print('''What do you want to do with your image? 
                1.Deform The Image.
                2.Filter The image.
                3.Enhance The image.              
                4.Flip the Image   
                5.Scale the Image
                6.GrayScale the Image  
                7.Combine Images
                8.Change Pixel color of Any colour you want
                9.Rotate The Image
                10.Draw with 
                11.ImageFont Image (write in images)  ''')

        x=int(input("Enter value:"))


        if x is 1:
            print('''Which deform do you want ? 
            
                    1.Left Deformer
                    2.Right Deformer''')
            j=int(input("Enter value:"))
            if j is 1 :
                Mail.Deformer()
                j = ImageOps.deform(image1, Mail.Deformer())
                j.show()
                j.save(input("Enter name of image to save"))
            elif j is 2 :
                Mail.Right_Deformer()
                j=ImageOps.deform(image1,Mail.Right_Deformer())
                j.show()
                j.save(input("Enter name of image to save"))







        elif x is 2 :
                print(''' what do you want to do with the image ?
                1.Blur
                2.Contour
                3.Sharpen
                4.Smooth
                5.Emboss''')
                z=int(input("Enter value:"))
                if z is 1 :
                    image1.filter(ImageFilter.BLUR)
                    image1.show()
                    image1.save(input("Enter name of image to save:"))
                if z is 2 :
                    image1.filter(ImageFilter.CONTOUR)
                    image1.show()
                    image1.save(input("Enter name of image to save:"))
                if z is 3 :
                    image1.filter(ImageFilter.SHARPEN)
                    image1.show()
                    image1.save(input("Enter name of image to save:"))
                if z is 4 :
                    image1.filter(ImageFilter.SMOOTH)
                    image1.show()
                    image1.save(input("Enter name of image to save:"))
                if z is 5 :
                    image1.filter(ImageFilter.EMBOSS)
                    image1.show()
                    image1.save(input("Enter name of image to save:"))

        elif x is 3 :
            print(''' what do you want to do with the image ?
                    1.Color
                    2.Constrast
                    3.Brightness
                    4.Sharpness''')
            l=int(input("Enter value:"))
            if l is 1 :
                ImageEnhance.Color(image1)
                image1.show()
                image1.save(input("Enter name of image to save:"))
            if l is 2 :
                ImageEnhance.Contrast(image1)
                image1.show()
                image1.save(input("Enter name of image to save:"))
            if l is 3 :
                ImageEnhance.Brightness(image1)
                image1.show()
                image1.save(input("Enter name of image to save:"))
            if l is 4 :
                ImageEnhance.Sharpness(image1)
                image1.show()
                image1.save(input("Enter name of image to save:"))







        elif x is 4:
            k=int(input('''Which side do you prefer to flip?
            1.Right Flip
            2.Left Flip
            3.Both Flip
            
            '''))
            if k is 1 :
                k=ImageOps.deform(image1,Mail.Right_Flipper())
                k.show()
                k.save(input("Enter name of image to save:"))
            elif k is 2:
                k = ImageOps.deform(image1, Mail.Left_Flipper())
                k.show()
                k.save(input("Enter name of image to save:"))
            elif k is 3 :
                k=ImageOps.deform(image1,Mail.Both_Flipped())
                k.show()
                k.save(input("Enter name of image to save:"))





        elif x is 5:
            s=int(input("Enter a value to scale:"))
            h=ImageOps.scale(image=image1,factor=s)
            h.show()
            h.save(input("Enter name of image to save:"))

        elif x is 6 :
            k=ImageOps.grayscale(image1)
            k.show()
            k.save(input("Enter name of image to save:"))

        elif x is 7:
            h=image1
            k=PIL.Image.open(input("File path of another image:"))

            print('''
               1.image_overlay
               2.image_darker
               3.image_lighter
               4.image_soft_light
               5.image_hard_light
               6.image_difference
               7.image_modulo
               8.image_screen''')
            y=int(input("Enter a value:"))
            if y is 1 :
                p=ImageChops.overlay(h,k)
                p.show()
                p.save(input("Enter name of image to save:"))
            if y is 2 :
                p = ImageChops.darker(h, k)
                p.show()
                p.save(input("Enter name of image to save:"))
            if y is 3 :
                p = ImageChops.lighter(h, k)
                p.show()
                p.save(input("Enter name of image to save:"))
            if y is 4 :
                p = ImageChops.soft_light(h, k)
                p.show()
                p.save(input("Enter name of image to save:"))
            if y is 5:
                p = ImageChops.hard_light(h, k)
                p.show()
                p.save(input("Enter name of image to save:"))
            if y is 6:
                p = ImageChops.difference(h, k)
                p.show()
                p.save(input("Enter name of image to save:"))
            if y is 7 :
                p = ImageChops.add_modulo(h, k)
                p.show()
                p.save(input("Enter name of image to save:"))
            if y is 8:
                p = ImageChops.screen(h, k)
                p.show()
                p.save(input("Enter name of image to save:"))

        elif x is 8:
            f=int(input("Enter RGB value of Red"))
            o = int(input("Enter RGB value of Green"))
            l = int(input("Enter RGB value of Blue"))
            j=int(input("Enter which color do you want to change R(0)/G(1)/B(2)"))
            gg=int(input("Enter Range for the pixel to be changed , example :100/200 etc"))
            for i in range(image1.size[0]):
                for k in range(image1.size[1]):
                    if image1.getpixel((i,k))[j] >gg:
                        image1.putpixel((i,k),(f,o,l))
            image1.show()

        elif x is 9 :
            k=float(input("Enter the angle you want to rotate the pic:"))
            image1.rotate(k).show()

            image1.save(input("Enter name of the image to save :"))

        elif x is 10:
            dib=ImageWin.Dib(image1,(400,400))
            hwnd=int(ImageWin.HDC(win.winfo_id()))
            dib.draw(hwnd,(0,0,200,200,),src=(0,0,200,200))
            image1.show()

        elif x is 11:
            x=ImageDraw.Draw(image1)
            font=ImageFont.truetype("Debrosee.ttf",150)
            j=int(input("Enter x coords:"))
            l = int(input("Enter y coords:"))
            h=input("Enter your Text:")
            x.text((j,l),h,font=font)
            image1.show()
            image1.save(input("Enter image name:"))

except:
    print("Unknown picture extension there bud , try again with your brain cells ^_^")
    print("Close the program and try again.")



win.mainloop()

