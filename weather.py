#!/usr/bin/env python
# coding: utf-8

# In[ ]:



#Install geopy
#pip install geopy
#install timezonefinder
#pip install timezonefinder
#install pytz
#pip install pytz


# In[ ]:


from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim                                # to locate the coordinates of addresses, cities, countries, and landmarks across the globe using third-party geocoder
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder                            # to determine the time zone of differnt cities in world
from datetime import datetime   
import requests
import pytz

Nishi=Tk()
Nishi.title('Weather App')                                           # title 
Nishi.resizable(True,True)                                           # to enable the screen resolution 

def getWeather():
    try:
        
        city=text_field.get()
    
        geolocator = Nominatim(user_agent="geoapiExercises")
        location=geolocator.geocode(city)
        obj=TimezoneFinder()
        result=obj.timezone_at(lng=location.longitude,lat=location.latitude)
        home=pytz.timezone(result)
        local_time=datetime.now(home)
        current_time=local_time.strftime("%I:%M: %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")
    
       # Weather
        api="https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=9086c0e1679bae305a5a1680c6547c93"
    
        json_data= requests.get(api).json()
        condition =json_data['weather'][0]['main']
        description=json_data['weather'][0]['description']
        temp=int(json_data['main']['temp']-273.15)
        pressure=json_data['main']['pressure']
        humidity=json_data['main']['humidity']
        wind=json_data['wind']['speed']
    
        t.config(text=(temp,"°"))
        c.config(text=(condition,"|","FEELS","LIKE",temp,"°"))
    
        w.config(text=wind)
        x.config(text=humidity)
        y.config(text=description)
        z.config(text=pressure)
        
    except Exception as e:
        messagebox.showerror('Weather App',"Invalid Entry")
        
# Search Box
search_img=PhotoImage(file='D:\Python Projects\Weather App\search.png')               # image path
img1=Label(image=search_img)
img1.place(x=20,y=20)

# Text Box
text_field=tk.Entry(Nishi,justify='center',width=17,font=('Impact',25,'bold'),bg='white',border=0,fg='black')
text_field.place(x=50,y=40)
text_field.focus()

# search_icon
search_icon=PhotoImage(file='D:\Python Projects\Weather App\magnifier.png')
img2=Button(image=search_icon,borderwidth=0,cursor='hand1',bg='skyblue',command=getWeather)
img2.place(x=400,y=34)
img2.set=""

# Logo
logo_image=PhotoImage(file='D:\Python Projects\Weather App\logo.png')
img3=Label(image=logo_image)
img3.place(x=240,y=175)

# Bottom Box
frame_image=PhotoImage(file='D:\Python Projects\Weather App\Big Box.png')
img4=Label(image=frame_image)
img4.pack(padx=10,pady=10,side=BOTTOM)


# time
name=Label(Nishi,font=("Arial",15,"bold"))
name.place(x=125,y=175)
clock=Label(Nishi,font=("Arial",15,"bold"))
clock.place(x=150,y=220)

# Labels for Final Output
label1=Label(Nishi,text='WIND',font=('Century',15,'bold'),fg='white',bg='gray')
label1.place(x=350,y=610)
label2=Label(Nishi,text='HUMIDITY',font=('Century',15,'bold'),fg='white',bg='gray')
label2.place(x=490,y=610)  
label3=Label(Nishi,text='DESCRIPTION',font=('Century',15,'bold'),fg='white',bg='gray')
label3.place(x=680,y=610)
label4=Label(Nishi,text='PRESSURE',font=('Century',15,'bold'),fg='white',bg='gray')
label4.place(x=890,y=610)

t=Label(font=('Arial',35,'bold'),fg='red')
t.place(x=580,y=230)
c=Label(font=('Arial',20,'bold'))
c.place(x=550,y=300)


w=Label(text='..',font=('Arial',15,'bold'),bg='white')
w.place(x=360,y=646)
x=Label(text='..',font=('Arial',15,'bold'),bg='white')
x.place(x=545,y=646)
y=Label(text='..',font=('Arail',15,'bold'),bg='white')
y.place(x=685,y=646)
z=Label(text='..',font=('Arial',15,'bold'),bg='white')
z.place(x=930,y=646)

Nishi.mainloop()


# In[ ]:




