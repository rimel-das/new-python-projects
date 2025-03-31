from tkinter import *
import speedtest  # Import the speedtest module

def check_speed():  # Renamed function to avoid conflicts
    st = speedtest.Speedtest()  # Now it correctly refers to the module
    st.get_servers()
    down = str(round(st.download() / (10**6), 3)) + " Mbps"
    up = str(round(st.upload() / (10**6), 3)) + " Mbps"
    lab_down.config(text=down)
    lab_up.config(text=up)

sp = Tk()
sp.title("Internet Speed Test")
sp.geometry("500x600")
sp.config(bg="#ffdab9")  

# Title
lab = Label(sp, text="INTERNET SPEED TEST", font=("Brush Script MT", 28, "bold"), 
            fg="#8b0000", bg="#ffdab9")  
lab.place(x=20, y=40, height=50, width=460)  

# Download Speed Label
lab = Label(sp, text="Downloading Speed", font=("Brush Script MT", 24, "bold"))  
lab.place(x=40, y=120, height=50, width=420)  

# Download Speed Value
lab_down = Label(sp, text="00", font=("Brush Script MT", 28, "bold"))  
lab_down.place(x=40, y=180, height=50, width=420)  

# Upload Speed Label
lab = Label(sp, text="Upload Speed", font=("Brush Script MT", 24, "bold"))  
lab.place(x=40, y=260, height=50, width=420)  

# Upload Speed Value
lab_up = Label(sp, text="00", font=("Brush Script MT", 28, "bold"))  
lab_up.place(x=40, y=320, height=50, width=420)  

# Check Speed Button
button = Button(sp, text="CHECK SPEED", font=("Brush Script MT", 28, "bold"), 
                relief=RAISED, bg="#d2691e", fg="white", command=check_speed)  

button.place(x=60, y=460, height=50, width=380)  

sp.mainloop()
