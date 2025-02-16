import socket
import time
from threading import Thread
import cv2,pickle,struct
import numpy as np
import matplotlib.pyplot as plt


Client_logo="""
                                                          
                                                                                                    
                                                                                                    
             ||||||                    |||||||||||||||||||||                                        
            |||||||                   ||||||||||||||||||||||||                                      
            ||||||||                 |||||||||||||||||||||||||                                      
            |||  |||                 |||                   ||||                                     
            |||  |||                 |||                    |||                                     
            ||||||||                 |||                    |||                                     
            |||||||                  |||                    |||                                     
             |||||                   ||                     |||                                     
              ||||                   |||  |||||||||||||||   |||                                     
              ||||     |||||||||||||||||  |||||||||||||||   ||||||||||||||||                        
              |||||   |||||||||||||||||    |||||||||||||    |||||||||||||||||                       
              |||||   ||||||||||||||||||                    ||||||||||||||||||                      
              |||||  ||||            ||                     |||            |||                      
           || |||||  |||             ||                     |||            |||                      
          |||||||||  |||             ||                     |||            |||                      
          |  ||||||  |||             ||   |||||||||||||||   |||            |||                      
          || ||||||| |||  |||||||||  ||   |||||||||||||||   ||| |||||||||  |||                      
          |||| ||||| |||  |||||||||  |||   |||||||||||||    ||| |||||||||  |||                      
            ||  |||| |||             |||                    |||            |||                      
            ||  ||||||||             |||                    |||            |||                      
            ||  ||||| ||             |||                    |||            |||                      
             ||  |||| ||  |||||||||  |||   |||||||||||||    ||| |||||||||  |||                      
             ||  ||||| |  |||||||||  |||  |||||||||||||||   ||| |||||||||  |||                      
             ||  ||||| |             |||  |||||||||||||||   |||            |||                      
              ||  |||||              |||   |||||||||||||    |||            |||                      
              ||  |||||              |||                    |||            |||||                    
               ||  |||||  |||||||||  |||                    ||| |||||||||  |||||                    
               ||  |||||  |||||||||  |||                    ||| |||||||||  ||||||                   
                ||  |||||            |||    |||||||||||     |||            ||||||                   
                ||  ||||||           |||  |||||||||||||||   |||            |||||||                  
                 ||  |||||           |||  |||||||||||||||   |||            |||||||                  
                 |||  |||||          |||   |||||||||||||    ||| |||||||||  ||||||||                 
                  ||  ||||||         |||                    ||| |||||||||  ||||||||                 
                  |||  |||||         |||                    |||            ||| ||||                 
                   |||  |||||        |||                    |||            ||| ||||                 
                    ||  ||||||       |||                    |||            ||| |||||                
                    |||  ||||||      |||  |||||||||||||||   ||| |||||||||  ||| |||||                
                     |||  ||||||     |||  |||||||||||||||   ||| |||||||||  ||| |||||                
                      |||  ||||||    |||   |||||||||||||    |||            ||| |||||                
                       |||  ||||||   ||                     |||            ||| |||||                
                       ||||  ||||||  ||                     |||            ||| |||||                
                        ||||  |||||| |||                    |||            ||| ||||                 
                         ||||  |||||||                      |||            ||| ||||                 
                          ||||  |||||||                     |||            ||||||||                 
                           ||||  |||||||                    |||            || |||||                 
                            ||||  ||||||||                  |||            | |||||                  
                              |||   ||||||||                |||              |||||                  
                               ||||  |||||||||              |||             |||||                   
                                ||||  |||||||||             |||            |||||                    
                                 |||||  ||||||||||          |||          |||||||                    
                                   ||||   |||||||||||       |||         |||||||                     
                                    |||||   ||||||||||||     |       ||||||||| |                    
                                      |||||  |||||||||||||||||||||||||||||||| |                     
                                        ||||||  ||||||||||||||||||||||||||||||                      
                                          ||||||   ||||||||||||||||||||||| ||                       
                                            |||||||  |||||||||||||||||||||||                        
                                              |||||||||    ||||||||  ||||||                         
                                                 ||||||||||||||||||||||||                           
                                                    |||||||||||||||||||                             
                                                         |||||||||                                  
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
      |###||######  |#    |####| ######|     ||###|  |##||##|                  ||                   
     |##||#|||##||  |#|   |#||##|||##||      ####### |##| |||                 ##|                   
     |#       #|    ###   |#  |#|  ##       |##| |##||##| ||   ||||  ||| ||  |##||                  
     |##||    #|   |# #|  |#|||#|  ##       ###      |##||##| |##### |###### ####|                  
      |####|  #|   ## ##  |####|   ##       ###      |##||##||##| ##||######  ##|                   
          #|  #|  |#####| |# ##    ##       |##   #| |##||##||######||## |##  ##|                   
     |#| |#|  #|  |#####| |# |#|   ##       |##| |##||##||##||##     |## |##  ##|                   
     |#####   #|  ##   ## |#  |#|  ##        ######| |##||##| ###### |## |##  ###|                  
                                              |###|  |##||##|  |##|  |## |##  |##|                  
                                                                                                    
                                                                                          

"""

class CLİENT():
    def __init__(self):
        self.HOST ="45.10.151.158" # Standard loopback interface address (localhost)
        self.PORT =9999     # Port tqxo listen on (non-privileged ports are > 1023)
        self.server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #self.package_size=3

        self.pakcket_size=2*1024

        self.prev_frame_time=0
        self.deneme_img=r"D:\program files\GITHUB\GIF_EDITOR\img_and_gift\DRAGON.jpg"

    def encoding_arr(self,msg):
        msg = pickle.dumps(msg)
        return struct.pack("Q",len(msg))+msg
    def encoding_str(self,msg):
        return bytes(msg)
    def decoding(self,msg):
        return msg.decode("utf-8")
    def CONNECT(self):
        self.server.connect((self.HOST,self.PORT))
        print(" \n connect to : ",self.server.getsockname())
    def sends(self,msg):
        self.server.send(self.encoding(msg))
    def take(self):
        while self.takes:
            msg=self.server.recv(self.package_size)
            print(self.decoding(msg))
    def FPS(self,time,img):
        #################################### fps
        try:
            fps = 1/(time-self.prev_frame_time)
        except:
            fps=1
        self.prev_frame_time=time
        cv2.putText(img, "FPS : "+str(int(fps)), (20,20), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (100, 255, 0),1)
        return img

    def REKLAM(self,img):
        #################################### fps
        cv2.putText(img, "Tum haklari saklidir © 2020 | yalcinyazilimciik", (img.shape[1]-700,
                                                                             img.shape[0]-13), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (100, 255, 0),1)
        return img
    def shows(self,frame):
        try:
            cv2.imshow("RECEIVING VIDEO",frame)
        except:
            pass

    def decode_arr(self,image_bytes):
        # Verinin uzunluğunu kontrol et
        a = image_bytes.find(b"\xff\xd8")
        b = image_bytes.find(b"\xff\xd9")
        if a != -1 and b != -1:
            jpg = image_bytes[a:b+2]
            image_bytes = image_bytes[b+2:]

            # Görüntüyü decode et
            image = cv2.imdecode(np.frombuffer(jpg, dtype=np.uint8), cv2.IMREAD_COLOR)
        else:
            return False,image_bytes
        return image,image_bytes

    def take_msg (self):
        basla=True
        while basla:
            # Görüntüyü al
            image_bytes = b""
            while True:
                # Biraz veri al
                chunk = self.server.recv(self.pakcket_size)
                if not chunk:
                    break
                image_bytes += chunk

                img,image_bytes=self.decode_arr(image_bytes)
                if type(img)!=type(False):
                    new_time=time.time()
                    img=self.FPS(new_time,img)
                    # Görüntüyü göster
                    cv2.imshow("Frame", img)
                    if cv2.waitKey(1) & 0xFF == ord("q"):
                        basla=False
                        break
        cv2.destroyAllWindows()
    def send_arr(self,reklam=True):
        camera = cv2.VideoCapture(0)

        fps = camera.get(cv2.CAP_PROP_FPS)
        width = camera.get(cv2.CAP_PROP_FRAME_WIDTH)
        height = camera.get(cv2.CAP_PROP_FRAME_HEIGHT)
        print(f"\n webcam max  fps :  {int(fps)}  ( {int(width)} X {int(height)} ) ")
        star=True
        while star:
            # Görüntüyü al
            ret, frame = camera.read()
            frame=cv2.resize(frame,(1280,720))
            if reklam:
                frame=self.REKLAM(frame)
            # Görüntüyü JPEG formatta sıkıştır
            ret, jpeg = cv2.imencode(".jpg", frame)

            # Görüntüyü sockete gönder
            try:
                self.server.sendall(jpeg.tobytes())
                time.sleep(0.01)
            except:
                star=False

        # Kamerayı ve socketi kapat
        camera.release()


def take_video():
    print(Client_logo)

    client=CLİENT()
    client.CONNECT()
    client.take_msg()
    client.server.close()

def send_video():
    print(Client_logo)

    client=CLİENT()
    client.CONNECT()
    client.send_arr()
    client.server.close()

if __name__=="__main__":
   send_video()
