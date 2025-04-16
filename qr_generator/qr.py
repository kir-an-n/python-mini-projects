import qrcode
import image
qr =qrcode.QRCode (
    version =8,
    box_size= 10,  #size of the box where qr code will be displayed
    border=5       #white part of the image
      )


data = "https://www.youtube.com/watch?v=VEZ_Ui6d9AM"

qr.add_data(data)
qr.make(fit =True)
img = qr.make_image(fill="black", back_color="white")
img.save("test.png")

            
     