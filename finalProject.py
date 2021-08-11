'''
Created on Apr 29, 2019

@author: samuelmaynard
'''
from tkinter import *
import tkinter.messagebox
import os.path
from idlelib.idle_test.test_configdialog import root
#creates window and buttons
class LaunchVehicleSelector(Frame):
    def __init__(self):
        '''Setup the window and widgets'''
        Frame.__init__(self)
        self.master.title("Launch Vehicle Selector")
        self.grid()
                
        self._pyldBtn = Button(self, text = "Payload Weight", command = self.Payload)
        self._pyldBtn.grid(row = 0, column = 3)
        
        self._pyldEnt = Text(self, height = 1, width = 15)
        self._pyldEnt.grid(row = 0, column = 4)
        
        self._altBtn = Button(self, text = "LEO/GTO", command = self.Altitude)
        self._altBtn.grid(row = 0, column = 0)
        
        self._altEnt = Text(self, height = 1, width = 15)
        self._altEnt.grid(row = 0, column = 2)
        
        self._enterBtn = Button(self, text = "Enter", command = self.Compute)
        self._enterBtn.grid(row = 0, column = 6)
        
        self._quitBtn = Button(self, text = "Quit", command = quit)
        self._quitBtn.grid(row = 1, column = 6)
        
        self._atlsBtn = Button(self, text = "Atlas-V", command = self.AtlasV)
        self._atlsBtn.grid(row = 1, column = 0)
        
        self._dltaBtn = Button(self, text = "Delta-IV", command = self.DeltaIV)
        self._dltaBtn.grid(row = 1, column = 2)
        
        self._flcnBtn = Button(self, text = "Falcon 9", command = self.Falcon9)
        self._flcnBtn.grid(row = 1, column = 4)
        
        self._textPane = Frame(self)
        self._textPane.grid(row = 5, column = 0, columnspan = 6, sticky = N+S+E+W)
        
        self._outputArea = Text(self._textPane, width = 65, height = 20)  
        self._outputArea.grid(row = 5, sticky = W+E+N+S) 
        tkinter.messagebox.showerror(title = "Instructions", message = "To determine a suitable launch vehicle, input 'GTO' or 'LEO' next to the button, then press the 'LEO/GTO' button. Then, enter your payload weight, no comma, in pounds and press the 'Payload Weight' button. Then press the 'Enter', or click on a launch vehicle button to find out more about it.")
 #Functions to get the data for Atlas V from file and output to GUI          
    def AtlasV(self):
        self._outputArea.delete("1.0", END)
        fileAtls = open("AtlasV.txt", 'r')
        for line in fileAtls:
            lstAtls = line.split(".")
            nameAtls = str(lstAtls[0])
            leoAtls = lstAtls[1]
            gtoAtls = str(lstAtls[2])
            launchSuccessAtls = str(lstAtls[3])
            costAtls = str(lstAtls[4])
            
            displayAtls = "The " + nameAtls + " can launch a " + leoAtls + "lbs payload to LEO, or " + \
                  gtoAtls + "lbs" + "\n" + "to Geostationary Orbit." + "\n" + \
                  "It has a " + launchSuccessAtls + "% successful launch rate." + "\n" + \
                  "It costs roughly $" + costAtls + "per launch."

            
        self._outputArea.insert("1.0", displayAtls)
        fileAtls.close() 
        
#Function to get the data for Delta IV from file and output to GUI      
    def DeltaIV(self):
        self._outputArea.delete("1.0", END)
        fileDlta = open("DeltaIV.txt", 'r')
        for line in fileDlta:
            lstDlta = line.split(".")
            nameDlta = str(lstDlta[0])
            leoDlta = lstDlta[1]
            gtoDlta = str(lstDlta[2])
            launchSuccessDlta = str(lstDlta[3])
            costDlta = str(lstDlta[4])
            
            displayDlta = "The " + nameDlta + " can launch a " + leoDlta + "lbs payload to LEO, or " + \
                  gtoDlta + "lbs" + "\n" + "to Geostationary Orbit." + "\n" + \
                  "It has a " + launchSuccessDlta + "% successful launch rate." + "\n" + \
                  "It costs roughly $" + costDlta + "per launch."
        
        self._outputArea.insert("1.0", displayDlta)
        fileDlta.close()
        
#Function to get the data for Falcon 9 from file and output to GUI       
    def Falcon9(self):
        self._outputArea.delete("1.0", END)
        fileFlcn = open("Falcon 9.txt", 'r')
        for line in fileFlcn:
            lstFlcn = line.split(".")
            nameFlcn = str(lstFlcn[0])
            leoFlcn = lstFlcn[1]
            gtoFlcn = str(lstFlcn[2])
            launchSuccessFlcn = str(lstFlcn[3])
            costFlcn = str(lstFlcn[4])
            
            displayFlcn = "The " + nameFlcn + " can launch a " + leoFlcn + \
                 "lbs payload to LEO, or " + \
                  gtoFlcn + "lbs" + "\n" + "to Geostationary Orbit." + "\n" + \
                  "It has a " + launchSuccessFlcn + "% successful launch rate." + "\n" + \
                  "It costs roughly $" + costFlcn + "per launch."
            
        self._outputArea.insert("1.0", displayFlcn)
        fileFlcn.close()
#Gets the user input from the payload entry box
    def Payload(self):
        global payloadWeight
        payloadWeight = int(self._pyldEnt.get("1.0", "end-1c"))
        return payloadWeight
#Gets the user input from the LEO/GTO button              
    def Altitude(self):
        global altitude
        altitude = self._altEnt.get("1.0", "end-1c")
        return altitude
       
#Computes the best launch vehicle based on required altitude and payload weight    
    def Compute(self):
        self._outputArea.delete("1.0", END)
        gtoAtls = int(19620)
        gtoDlta = int(31350)
        gtoFlcn = int(18300)
#GTO would be a high altitude, so it has to carry a lower weight       
        if altitude == "GTO":
            if (payloadWeight <= gtoFlcn):
                flcnMessage = "The Falcon 9 is recommended for this payload."
                self._outputArea.insert("1.0", flcnMessage)
            elif (payloadWeight > gtoFlcn) and (payloadWeight <= gtoAtls):
                atlsMessage = "The Atlas-V is recommended for this payload."
                self._outputArea.insert("1.0", atlsMessage)
            elif (payloadWeight > gtoFlcn) and (payloadWeight > gtoAtls) and (payloadWeight <= gtoDlta):
                dltaMessage = "The Delta-IV is recommended for this payload."
                self._outputArea.insert("1.0", dltaMessage)
            else:
                noMessage = "There is no launch vehicle capable of carrying this payload."
                self._outputArea.insert("1.0", noMessage)
        else:
            incorrectEntry = "Make sure to enter GTO or LEO, then press the LEO/GTO button."   
                
        leoAtls = int(45240)
        leoDlta = int(63670)
        leoFlcn = int(50300)
#LEO is lower altitude, so it can carry a heavier weight
        if altitude == "LEO":
            if (payloadWeight <= leoFlcn):
                flcnMessage = "The Falcon 9 is recommended for this payload."
                self._outputArea.insert("1.0", flcnMessage)
            elif (payloadWeight > leoFlcn) and (payloadWeight <= leoAtls):
                atlsMessage = "The Atlas-V is recommended for this payload."
                self._outputArea.insert("1.0", atlsMessage)
            elif (payloadWeight > leoFlcn) and (payloadWeight > leoAtls) and (payloadWeight <= leoDlta):
                dltaMessage = "The Delta-IV is recommended for this payload."
                self._outputArea.insert("1.0", dltaMessage)
            else:
                noMessage = "There is no launch vehicle capable of carrying this payload."
                self._outputArea.insert("1.0", noMessage)
        else:
            incorrectEntry = "Make sure to enter GTO or LEO, then press the LEO/GTO button."   
                              
#Button to quit the program
    def quit(self):
        global root
        root.quit()
        
def main():
    LaunchVehicleSelector().mainloop()
main()