#unit converter, the user will select what they want to convert, then plug in number and that number will be converted to the unit that the user chose. 


#import the needed GUI stuff
import tkinter as tk 
from tkinter import ttk


#------declare windows------
mainWindow = tk.Tk()
weightWindow = tk.Toplevel()
temperatureWindow = tk.Toplevel()

#------declare methods------
def createNewWindow():
  if(unitChosen.get() == "Weight"):
    #establish the window
    weightWindow = tk.Toplevel()
    label = tk.Label(weightWindow, text = "Select units, then click the button to calculate")
    label.pack()
    toLabel = tk.Label(weightWindow, text = "to")
    toLabel.place(x=220, y=50)
    weightWindow.attributes('-fullscreen', True)
    #declare drop down menu1
    y = tk.StringVar()
    weightUnitChosen1 = ttk.Combobox(weightWindow, width = 15, textvariable = y)
    #add elements to the drop down menu
    weightUnitChosen1['values'] = ('kilograms',
                                   'pounds',
                                   'grams')
    #declare drop down menu2
    x = tk.StringVar()
    weightUnitChosen2 = ttk.Combobox(weightWindow, width = 15, textvariable = x)
    #add elements to the drop down menu2
    weightUnitChosen2['values'] = ('kilograms',
                                   'pounds',
                                   'grams')
    #text box for the user to enter input
    weightUserInput = tk.DoubleVar()
    weightInput = ttk.Entry(weightWindow, width= 10, textvariable = weightUserInput)
    #position widgets
    weightUnitChosen2.place(x=300, y=50)   
    #weightUnitChosen2.pack()
    weightUnitChosen1.place(x=9, y=50)             
    #weightUnitChosen1.pack()
    weightInput.place(x=200, y=150)

    
    def calculateWeightFunction():
      if(weightUnitChosen1.get() == "kilograms" and weightUnitChosen2.get() == "grams"):
       #resets the label that way it doesn't overlap with previous labels
        result = float(weightInput.get()) * 1000
        #labels to display calculations
        resultLabel = tk.Label(weightWindow, text = "= " + str(result) + " " + weightUnitChosen2.get())
        resultLabel.place(x=300, y=150)
      elif(weightUnitChosen1.get() == "kilograms" and weightUnitChosen2.get() == "pounds"):
        result = float(weightInput.get()) * 2.205
        #labels to display calculations
        resultLabel = tk.Label(weightWindow, text = "= " + str(result) + " " + weightUnitChosen2.get())
        resultLabel.place(x=300, y=150)
      elif(weightUnitChosen1.get() == "kilograms" and weightUnitChosen2.get() == "kilograms"):
        result = weightInput.get()
        #labels to display calculations
        resultLabel = tk.Label(weightWindow, text = "= " + str(result) + " " + weightUnitChosen2.get())
        resultLabel.place(x=300, y=150)
      elif(weightUnitChosen1.get() == "pounds" and weightUnitChosen2.get() == "kilograms"):
        result = float(weightInput.get()) / 2.205
        #labels to display calculations
        resultLabel = tk.Label(weightWindow, text = "= " + str(result) + " " + weightUnitChosen2.get())
        resultLabel.place(x=300, y=150)
      elif(weightUnitChosen1.get() == "pounds" and weightUnitChosen2.get() == "grams"):
        result = float(weightInput.get()) * 454
        #labels to display calculations
        resultLabel = tk.Label(weightWindow, text = "= " + str(result) + " " + weightUnitChosen2.get())
        resultLabel.place(x=300, y=150)
      elif(weightUnitChosen1.get() == "pounds" and weightUnitChosen2.get() == "pounds"):
        result = weightInput.get()
        #labels to display calculations
        resultLabel = tk.Label(weightWindow, text = "= " + str(result) + " " + weightUnitChosen2.get())
        resultLabel.place(x=300, y=150)
      elif(weightUnitChosen1.get() == "grams" and weightUnitChosen2.get() == "kilograms"):
        result = float(weightInput.get()) / 1000
        #labels to display calculations
        resultLabel = tk.Label(weightWindow, text = "= " + str(result) + " " + weightUnitChosen2.get())
        resultLabel.place(x=300, y=150)
      elif(weightUnitChosen1.get() == "grams" and weightUnitChosen2.get() == "pounds"):
        result = float(weightInput.get()) / 454
        #labels to display calculations
        resultLabel = tk.Label(weightWindow, text = "= " + str(result) + " " + weightUnitChosen2.get())
        resultLabel.place(x=300, y=150)
      elif(weightUnitChosen1.get() == "grams" and weightUnitChosen2.get() == "grams"):
        result = weightInput.get()
        #labels to display calculations
        resultLabel = tk.Label(weightWindow, text = "= " + str(result) + " " + weightUnitChosen2.get())
        resultLabel.place(x=300, y=150)
      

    calculateWeight = tk.Button(weightWindow,
                        text = "Calculate",
                        width=19,
                        height=3,
                        background = 'blue',
                        foreground = 'white',
                        command = calculateWeightFunction
                        )
    calculateWeight.place(x=150, y= 200)

    
    #delete stuff from old window
    confirmUnit.destroy()
    greeting.destroy()
    unitChosen.destroy()
    
    #Luis---
  elif(unitChosen.get() == "Distance"):
    distanceWindow = tk.Toplevel()
    label = tk.Label(distanceWindow, text = "Select units, then click the button to calculate")
    label.pack()
    toLabel = tk.Label(distanceWindow, text = "to")
    toLabel.place(x=220, y=50)
    distanceWindow.attributes('-fullscreen', True)
    #declare drop down menu1
    y = tk.StringVar()
    distanceUnitChosen1 = ttk.Combobox(distanceWindow, width = 15, textvariable = y)
    #add elements to the drop down menu
    distanceUnitChosen1['values'] = ('feet',
                                   'kilometers',
                                   'meters',
                                   'yards')
    #declare drop down menu2
    x = tk.StringVar()
    distanceUnitChosen2 = ttk.Combobox(distanceWindow, width = 15, textvariable = x)
    #add elements to the drop down menu2
    distanceUnitChosen2['values'] = ('feet',
                                   'kilometers',
                                   'meters',
                                   'yards')
    #text box for the user to enter input
    distanceUserInput = tk.DoubleVar()
    distanceInput = ttk.Entry(distanceWindow, width= 10, textvariable = distanceUserInput)
    #position widgets
    distanceUnitChosen2.place(x=300, y=50)   
    #weightUnitChosen2.pack()
    distanceUnitChosen1.place(x=9, y=50)             
    #weightUnitChosen1.pack()
    distanceInput.place(x=200, y=150)
    def calculateDistanceFunction():
      if(distanceUnitChosen1.get() == "feet" and distanceUnitChosen2.get() == "kilometers"):
       #resets the label that way it doesn't overlap with previous labels
        result = float(distanceInput.get()) / 3281
        #labels to display calculations
        resultLabel = tk.Label(distanceWindow, text = "= " + str(result) + " " + distanceUnitChosen2.get())
        resultLabel.place(x=300, y=150)
      elif(distanceUnitChosen1.get() == "feet" and distanceUnitChosen2.get() == "meters"):
        result = float(distanceInput.get()) / 3.281
        #labels to display calculations
        resultLabel = tk.Label(distanceWindow, text = "= " + str(result) + " " + distanceUnitChosen2.get())
        resultLabel.place(x=300, y=150)
      elif(distanceUnitChosen1.get() == "feet" and distanceUnitChosen2.get() == "yards"):
        result = float(distanceInput.get()) / 3
        #labels to display calculations
        resultLabel = tk.Label(distanceWindow, text = "= " + str(result) + " " + distanceUnitChosen2.get())
        resultLabel.place(x=300, y=150)
      elif(distanceUnitChosen1.get() == "feet" and distanceUnitChosen2.get() == "feet"):
        result = distanceInput.get()
        #labels to display calculations
        resultLabel = tk.Label(distanceWindow, text = "= " + str(result) + " " + distanceUnitChosen2.get())
        resultLabel.place(x=300, y=150)
      elif(distanceUnitChosen1.get() == "kilometers" and distanceUnitChosen2.get() == "feet"):
        result = float(distanceInput.get()) * 3281
        #labels to display calculations
        resultLabel = tk.Label(distanceWindow, text = "= " + str(result) + " " + distanceUnitChosen2.get())
        resultLabel.place(x=300, y=150)
      elif(distanceUnitChosen1.get() == "kilometers" and distanceUnitChosen2.get() == "meters"):
        result = float(distanceInput.get()) * 1000
        #labels to display calculations
        resultLabel = tk.Label(distanceWindow, text = "= " + str(result) + " " + distanceUnitChosen2.get())
        resultLabel.place(x=300, y=150)
      elif(distanceUnitChosen1.get() == "kilometers" and distanceUnitChosen2.get() == "yards"):
        result = float(distanceInput.get()) * 1094
        #labels to display calculations
        resultLabel = tk.Label(distanceWindow, text = "= " + str(result) + " " + distanceUnitChosen2.get())
        resultLabel.place(x=300, y=150)
      elif(distanceUnitChosen1.get() == "kilometers" and distanceUnitChosen2.get() == "kilometers"):
        result = distanceInput.get()
        #labels to display calculations
        resultLabel = tk.Label(distanceWindow, text = "= " + str(result) + " " + distanceUnitChosen2.get())
        resultLabel.place(x=300, y=150)
      elif(distanceUnitChosen1.get() == "meters" and distanceUnitChosen2.get() == "feet"):
        result = float(distanceInput.get()) * 3.281
        #labels to display calculations
        resultLabel = tk.Label(distanceWindow, text = "= " + str(result) + " " + distanceUnitChosen2.get())
        resultLabel.place(x=300, y=150)
      elif(distanceUnitChosen1.get() == "meters" and distanceUnitChosen2.get() == "kilometers"):
        result = float(distanceInput.get()) / 1000
        #labels to display calculations
        resultLabel = tk.Label(distanceWindow, text = "= " + str(result) + " " + distanceUnitChosen2.get())
        resultLabel.place(x=300, y=150)
      elif(distanceUnitChosen1.get() == "meters" and distanceUnitChosen2.get() == "yards"):
        result = float(distanceInput.get()) * 1.094
        #labels to display calculations
        resultLabel = tk.Label(distanceWindow, text = "= " + str(result) + " " + distanceUnitChosen2.get())
        resultLabel.place(x=300, y=150)
      elif(distanceUnitChosen1.get() == "meters" and distanceUnitChosen2.get() == "meters"):
        result = distanceInput.get()
        #labels to display calculations
        resultLabel = tk.Label(distanceWindow, text = "= " + str(result) + " " + distanceUnitChosen2.get())
        resultLabel.place(x=300, y=150)
      elif(distanceUnitChosen1.get() == "yards" and distanceUnitChosen2.get() == "feet"):
        result = float(distanceInput.get()) * 3
        #labels to display calculations
        resultLabel = tk.Label(distanceWindow, text = "= " + str(result) + " " + distanceUnitChosen2.get())
        resultLabel.place(x=300, y=150)
      elif(distanceUnitChosen1.get() == "yards" and distanceUnitChosen2.get() == "kilometers"):
        result = float(distanceInput.get()) / 1094
        #labels to display calculations
        resultLabel = tk.Label(distanceWindow, text = "= " + str(result) + " " + distanceUnitChosen2.get())
        resultLabel.place(x=300, y=150)
      elif(distanceUnitChosen1.get() == "yards" and distanceUnitChosen2.get() == "meters"):
        result = float(distanceInput.get()) / 1.094
        #labels to display calculations
        resultLabel = tk.Label(distanceWindow, text = "= " + str(result) + " " + distanceUnitChosen2.get())
        resultLabel.place(x=300, y=150)
      elif(distanceUnitChosen1.get() == "yards" and distanceUnitChosen2.get() == "yards"):
        result = distanceInput.get()
        #labels to display calculations
        resultLabel = tk.Label(distanceWindow, text = "= " + str(result) + " " + distanceUnitChosen2.get())
        resultLabel.place(x=300, y=150)
    #calculates distance
    calculateDistance = tk.Button(distanceWindow,
                        text = "Calculate",
                        width=19,
                        height=3,
                        background = 'blue',
                        foreground = 'white',
                        command = calculateDistanceFunction
                        )
    calculateDistance.place(x=150, y= 200)
      
    #delete stuff from old window
    confirmUnit.destroy()
    greeting.destroy()
    unitChosen.destroy()

    #Rose---
  elif(unitChosen.get() == "Temperature"):
    temperatureWindow = tk.Toplevel()
    label = tk.Label(temperatureWindow, text = "Select the units then press the button to calculate")
    label.pack()
    toLabel = tk.Label(temperatureWindow, text = "to")
    toLabel.place(x = 220, y= 50)
    temperatureWindow.attributes('-fullscreen', True)
   
    #declare drop down menu 1
    temperature = tk.StringVar()
    temperatureUnitChosen1 = ttk.Combobox(temperatureWindow, width = 15, textvariable = temperature)
    
    #add elements to the drop down menu
    temperatureUnitChosen1['values'] = ('Celsius',
                                        'Fahrenheit',
                                        'Kelvin')
  
    
   #declare drop down menu 2
    n = tk.StringVar()
    temperatureUnitChosen2 = ttk.Combobox(temperatureWindow, width = 15, textvariable = n)
    #add elements to the drop down menu
    temperatureUnitChosen2['values'] = ('Celsius',
                                        'Fahrenheit',
                                        'Kelvin')
    
    
    #textbox to type the value 
    temperatureUserInput = tk.DoubleVar()
    temperatureInput = ttk.Entry(temperatureWindow, width= 10, textvariable = temperatureUserInput)

    temperatureInput.place(x=200, y=150)

    temperatureUnitChosen1.place(x= 9, y=50)
    temperatureUnitChosen2.place( x = 300, y = 50)
    
    #calculations for the button 
    def calculateTemperatureFunction():
     print(temperatureUnitChosen1.get())
     if (temperatureUnitChosen1.get() == "Celsius" and temperatureUnitChosen2.get()== "Fahrenheit"):
       result = float(temperatureInput.get()) * 9/5 + 32
       print (result)
     elif (temperatureUnitChosen1.get() == "Celsius" and temperatureUnitChosen2.get()== "Kelvin"):
        result = float(temperatureInput.get()) * 5/9 - 32
        print(result)
     elif (temperatureUnitChosen1.get() == "Fahrenheit" and temperatureUnitChosen2.get()== "Celsius"):
        result = float(temperatureInput.get()) + 273.15
        print(result)
     elif (temperatureUnitChosen1.get() == "Fahrenheit" and temperatureUnitChosen2.get()== "Kelvin"):
        result = float(temperatureInput.get()) * 5/9 + 273.15
        print(result)
     elif (temperatureUnitChosen1.get() == "Kelvin" and temperatureUnitChosen2.get()== "Celsius"):
        result = float(temperatureInput.get()) - 273.15
        print(result)
     elif (temperatureUnitChosen1.get() == "Kelvin" and temperatureUnitChosen2.get()== "Fahrenheit"):
        result = float(temperatureInput.get()) * 9/5 + 32
        print(result)
       
    #this button calculates the value that they selected a unit to      
    temperatureCalculate = tk.Button                                  (temperatureWindow,
                        text = "Calculate",
                        width=19,
                        height=3,
                        background = 'blue',
                        foreground = 'white',
                        command = calculateTemperatureFunction
                        )
  
    temperatureCalculate.place ( x = 150, y = 200)
    #delete stuff from old window
    confirmUnit.destroy()
    greeting.destroy()
    unitChosen.destroy()
    

#------declare widgets------
greeting = tk.Label(
    text="Welcome, select the unit",
    width=20,
    height=2
)
#create the drop down menu in which the user will select the desired unit
n = tk.StringVar()
unitChosen = ttk.Combobox(mainWindow, width = 15, textvariable = n)
#add elements to the drop down menu
unitChosen['values'] = ('Distance',
                        'Weight',
                         'Temperature')

#this button confirms the unit and creates the new window with the corresponding unit      
confirmUnit = tk.Button(text = "Next",
                        width=15,
                        height=2,
                        background = 'blue',
                        foreground = 'white',
                        command = createNewWindow
                        )


#place and position widgets
#greeting.pack() 
greeting.place(x=0, y=0)
#unitChosen.pack()
unitChosen.place(x=9, y=35)
#confirmUnit.pack()
confirmUnit.place(x=5, y=65)

#title and set size of 1st window
mainWindow.geometry('350x200') #size of 1st window
mainWindow.title("Unit Converter")
mainWindow.mainloop()