from tkinter import *
from tkinter import ttk 
import requests



def data_get():
  city= city_name.get()
  data = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=df3d2bff838aea658ca0fa012d349384").json()
  w_label1.config(text=data["weather"][0]["main"])
  wd_label1.config(text=data["weather"][0]["description"])
  tem_label1.config(text=str(int(data[ "main"]["temp"]-273.15)))
  per_label1.config(text=data[ "main"]["pressure"])

# tkinter Graphics User Interface (GUI) ka liya use krty ha 
win = Tk()

# title name ko likhna ha 
win.title("Weather App in python") 

# Backgroung color lagany ka liya 
win.config(bg="#ADD8E6") 

# Pyhton ma win open krny ka liya 
win.geometry("500x530")



# Label banany ka liya 
name_label= Label(win , text="Weather App" , font=("Time New Roman" , 40 , "bold"))

name_label.place(x=20 , y=50 , height=50 , width=450)


# Pakistan ma country ki list
list_name = pakistan_cities = [
        "Lahore", "Rawalpindi", "Multan", "Faisalabad", "Gujranwala", "Sialkot", "Bahawalpur", "Sargodha"
    

        "Karachi", "Hyderabad", "Sukkur", "Larkana", "Mirpur Khas", "Nawabshah", "Dadu"


        "Peshawar", "Mardan", "Abbottabad", "Swat", "Kohat", "Dera Ismail Khan", "Bannu"
    
        "Quetta", "Gwadar", "Khuzdar", "Turbat", "Zhob", "Sibi"

    
        "Islamabad"

    
        "Gilgit", "Skardu", "Hunza", "Gahkuch", "Khaplu"
    
            "Muzaffarabad", "Mirpur", "Rawalakot", "Bagh", "Kotli"
    ]



# input ma country list add krny ka liya 
city_name=StringVar()
com = ttk.Combobox(win , text="Weather App" ,values= list_name ,font=("Time New Roman" , 20 , "bold"), textvariable=city_name)

com.place(x=20 , y=120 , height=50 , width=450)



#  weather Climate
w_label= Label(win , text="Weather Climate" , font=("Time New Roman" , 20 ))

w_label.place(x=20 , y=260 , height=50 , width=210)
w_label1= Label(win , text="" , font=("Time New Roman" , 20 ))

w_label1.place(x=250 , y=260 , height=50 , width=210)





# weather descrintion
wd_label= Label(win , text="Weather Describtion" , font=("Time New Roman" , 17 ))

wd_label.place(x=20 , y=330 , height=50 , width=210)
wd_label1= Label(win , text="" , font=("Time New Roman" , 20 ))

wd_label1.place(x=250 , y=330 , height=50 , width=210)





# weather Temprature
tem_label= Label(win , text="Temprature" , font=("Time New Roman" , 20 ))

tem_label.place(x=20 , y=400 , height=50 , width=210)
tem_label1= Label(win , text="" , font=("Time New Roman" , 15 ))

tem_label1.place(x=250 , y=400 , height=50 , width=210)





# weather pressure
per_label= Label(win , text="Pressure" , font=("Time New Roman" , 20 ))

per_label.place(x=20 , y=470 , height=50 , width=210)
per_label1= Label(win , text="" , font=("Time New Roman" , 20 ))

per_label1.place(x=250 , y=470 , height=50 , width=210)



# button bnana ka liya 
done_button = Button(win ,text="Click Here",font=("Time New Roman" , 10 , "bold"),command=data_get)

done_button.place(y=190,height=50 , width=100 , x=200)




win.mainloop()