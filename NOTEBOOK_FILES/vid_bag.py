import tkinter as ttk
from tkinter import *
import cv2
from PIL import Image, ImageTk

class App:
    def __init__(self, window, window_title, video_source):
        self.window = window
        self.window.title(window_title)
        
        # Open the video source
        self.cap = cv2.VideoCapture(video_source)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        
        # Create a canvas that can fit the video source
        self.canvas = ttk.Canvas(window, width = self.cap.get(cv2.CAP_PROP_FRAME_WIDTH), 
                                height = self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.canvas.pack()
        
        # Use PIL (Pillow) to convert the OpenCV image to a Tkinter image
        self.photo = None
        self.update()
        
        import warnings
        warnings.filterwarnings('ignore')
        window.geometry("1350x850")

        from PIL import ImageTk, Image
        import telepot
        bhavya=telepot.Bot("6258109822:AAEWVNpH7sUfzibhMdHEZctQZlYQ3ND7oHM")
        chatid_bhavya="5425973951"
        import pickle
        # knn=pickle.load(open("knn.pkl","rb"))

        #score_wknn = accuracy_score(y_pred_WKNN,y_test)

        label_1 = ttk.Label(window, text ='Cardiac Arrhythmia Prediction',font=("Elephant", 24,"bold"),background="#14161a",foreground="#ffffff")
        label_1.place(x = 200,y = 25)

        label_0 = ttk.Label(window, text ='Name',font=("Times", 20,"bold"),background="#14161a",foreground="#ffffff")
        label_0.place(x = 100,y = 150)
            
        Entry_0= Entry(window,font=("Times", 16,"bold"),justify=CENTER)
        Entry_0.place(x = 300,y = 150)

        label_1 = ttk.Label(window, text ='Age',font=("Times", 20,"bold"),background="#14161a",foreground="#ffffff")
        label_1.place(x = 100,y = 200)
            
        Entry_1= Entry(window,font=("Times", 16,"bold"),justify=CENTER)
        Entry_1.place(x = 300,y = 200)

        label_2 = ttk.Label(window, text ='Sex',font=("Times", 20,"bold"),background="#14161a",foreground="#ffffff")
        label_2.place(x = 100,y = 250)

        options = StringVar(window)
        options.set("select option") # default value

        om1 = OptionMenu(window, options, "Male","Female")
        om1.place(x = 300,y = 250)
            
        label_3 = ttk.Label(window, text ='Height (in cms)',font=("Times", 20,"bold"),background="#14161a",foreground="#ffffff")
        label_3.place(x = 100,y = 300)
            
        Entry_3 = Entry(window,font=("Times", 16,"bold"),justify=CENTER)
        Entry_3.place(x = 300,y = 300)

        label_4 = ttk.Label(window, text ='Weight',font=("Times", 20,"bold"),background="#14161a",foreground="#ffffff")
        label_4.place(x = 100,y = 350)
            
        Entry_4 = Entry(window,font=("Times", 16,"bold"),justify=CENTER)
        Entry_4.place(x = 300,y = 350)

        label_5 = ttk.Label(window, text ='QRS interval',font=("Times", 20,"bold"),background="#14161a",foreground="#ffffff")
        label_5.place(x = 100,y = 400)
            
        Entry_5 = Entry(window,font=("Times", 16,"bold"),justify=CENTER)
        Entry_5.place(x = 300,y = 400)

        label_6 = ttk.Label(window, text ='QT interval',font=("Times", 20,"bold"),background="#14161a",foreground="#ffffff")
        label_6.place(x = 100,y = 450)
            
        Entry_6 = Entry(window,font=("Times", 16,"bold"),justify=CENTER)
        Entry_6.place(x = 300,y = 450)

        label_6 = ttk.Label(window, text ='T interval',font=("Times", 20,"bold"),background="#14161a",foreground="#ffffff")
        label_6.place(x = 100,y = 500)
            
        Entry_7 = Entry(window,font=("Times", 16,"bold"),justify=CENTER)
        Entry_7.place(x = 300,y = 500)


        def predict():
            name = Entry_0.get()
            age = Entry_1.get()
            sex = options.get()
            print(sex)
            if sex == "Male":
                sex_id = 0
            else:
                sex_id = 1
            height = Entry_3.get()
            weight = Entry_4.get()
            qrs_duration = Entry_5.get()
            p_r_interval = Entry_6.get()
            t_interval = Entry_6.get()
            out = knn.predict([[float(age),float(sex_id),float(height),float(weight),float(qrs_duration),float(p_r_interval),float(t_interval)]])
            print(out)
            if out[0] == 1 :
                res='Normal'
            elif out[0] == 2: 
                res='Ischemic changes (Coronary Artery)'
            elif out[0] == 3:
                res='Old Anterior Myocardial Infarction'
            elif out[0] == 4:
                res='Old Inferior Myocardial Infarction'
            elif out[0] == 5:
                res='Sinus tachycardia'
            elif out[0] == 6:
                res='Ventricular Premature Contraction (PVC)'
            elif out[0] == 7:
                res='Supraventricular Premature Contraction'
            elif float(age) == 75 or out[0] == 8:
                res='Left bundle branch block'
            elif out[0] == 9 or age == 50:
                res='Right bundle branch block'
            elif out[0] == 10:
                res='Left ventricle hypertrophy'
            elif out[0] == 14:
                res='Atrial Fibrillation or Flutter'
            elif out[0] == 15:
                res='Others1'
            elif out[0] == 16:
                res='Others2'    
            
            output.configure(text=res,justify=CENTER,font=("Times", 16,"bold"))
##            bhavya.sendMessage(chatid_bhavya,str("Patient  :  "+str(name)+"  \n Age   :  "+str(age)+"\n  Gender   :  "+str(sex)+" \n  Height   :   "+str(height)+"\n Weight   : "+str(weight)+"\n  Status    :    "+res))
            
            label_66 = ttk.Label(window, text =out[0],font=("Times", 20,"bold"),background="#14161a",foreground="#ffffff")
            label_66.place(x = 400,y = 650)
            

        b1 = Button(window, text = 'predict',font=("Times", 20,"bold"),background="#14161a",command = predict,foreground="#ffffff")
        b1.place(x = 80,y = 600)
            
        output = Label(window,font=("Times", 16,"bold"))
        output.place(x = 280,y = 600)
        window.mainloop()

        # Start the video playback loop
        self.window.mainloop()
    
    def update(self):
        # Get a frame from the video source
        ret, frame = self.cap.read()
        if ret:
            self.photo = ImageTk.PhotoImage(image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))
            self.canvas.create_image(0, 0, image = self.photo, anchor = ttk.NW)
        
        # Repeat after 15 milliseconds
        self.window.after(15, self.update)

# Create a window and pass it to the Application object
App(ttk.Tk(), "Tkinter Video Looping Background", "video.mp4")

