from tkinter import *
import tkinter as tk
import tkinter as tk  
from tkinter import ttk          
from tkinter import font  as tkfont 
import os 
import numpy as np
import sys
import webbrowser
# import ctypes

# try:
#     ctypes.windll.shcore.SetProcessDpiAwareness(True)
# except:
#     pass

## Create a pop-up to notify "out of range"
def popupmsg_OCR():
    popup_OCR=tk.Tk()
    popup_OCR.wm_title("ATTENTION!")
    popup_OCR.geometry("520x100")
    popup_OCR.iconbitmap(resource_path("logo.ico"))
    label1=tk.Label(popup_OCR, text="Out of the calibration range or the uncertainty of INPUT is too important!", bg='yellow', fg="red", font=("bold", 12))
    label1.pack(side="top", fill="x")
    label2=tk.Label(popup_OCR, text="Obtained results may be aberrant or contain larger errors.", bg='yellow')
    label2.pack(side="top", fill="x")
    label3=tk.Label(popup_OCR, text="Check the calibration curve(s) in the related references to see the range of INPUT parameters.", bg='yellow')
    label3.pack(side="top", fill="x")
    btn1=tk.Button(popup_OCR, text="Understood!", bg='yellow', font=("bold", 13), width=80, command=popup_OCR.destroy)
    btn1.pack()
    #popupmsg_OCR.mainloop() i j


### Create a "resource path" which is a relative directory path in order to open references and PDF documents in any computer
def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

#The codes below are for opening the internet link of the references
new=1
url_ref1 = "https://doi.org/10.1021/acs.analchem.9b02803"
url_ref2 = "https://doi.org/10.1016/j.chemgeo.2020.119783"
url_ref3 = "https://doi.org/10.1016/j.chemgeo.2014.03.016"

def open_url_ref1():
    webbrowser.open(url_ref1,new=new)
def open_url_ref2():
    webbrowser.open(url_ref2,new=new)
def open_url_ref3():
    webbrowser.open(url_ref2,new=new)

#The codes below are for opening directly the PDF files of the references

# def OpenRef1():
#     os.startfile(resource_path('Le2019.pdf'))
# def OpenRef2():
#     os.startfile(resource_path('Le2020.pdf'))    
# def OpenRef3():
#     os.startfile(resource_path('caumon2014.pdf'))

#### Home screen that display several module (pure CH4, CO2, CO2N2, etc.)
class FRAnCIs: 
	def __init__(self, master):
		self.master = master
		self.master.title("FRAnCIs v.1.0.1, GeoRessouces Lab")
		self.master.geometry("470x560")
		#self.master.resizable(width=False, height=False)
		self.master.iconbitmap(resource_path("logo.ico"))
		
		self.frame=tk.Frame(self.master)
		self.frame.pack()
		self.label = ttk.Label(self.frame, text="FRAnCIs", font=("bold", 15))
		self.label.pack(side="top")
		self.label = ttk.Label(self.frame, text="(Fluid: Raman Analysis Composition of Inclusions)", font=("bold", 10))
		self.label.pack(side="top")

		self.label = ttk.Label(self.frame, text="Select an option!", font=("bold", 13))
		self.label.pack(side="top", pady=10)
		
		# create buttons for opening each modules.
		self.butnew("1. Pure CO₂ [1]", "1", module1)	
		self.butnew("2. Pure CH₄ [2]", "2", module2)
		self.butnew("3. CO₂ - N₂ Mixtures [1]", "3", module3)	
		self.butnew("4. CH₄ - N₂ Mixtures [2]", "4", module4)
		self.butnew("5. CO₂ - CH₄ Mixtures [2]", "5", module5)
		self.butnew("6. CO₂ - CH₄ - N₂ Mixtures [1,2]", "6", module6)
		self.butnew("7. CH₄ dissolved and non-dissolved in H₂O [3]", "7", module7)

		self.label = ttk.Label(self.frame, text="_ References : _____________________________", font=("bold", 11))
		self.label.pack(side="top", pady=6, anchor='w')

		## creat 3 button for opening references
		self.btn_ref1 = ttk.Button(self.frame, text="[1] Le et al., J. Anal. Chem. 2019, 91 (22), 14359–14367.", width=70,command=open_url_ref1).pack(pady=3, anchor='w')
		self.btn_ref2 = ttk.Button(self.frame, text="[2] Le et al., J. Chem. Geol. 2020, 522, 119783.", width=70, command=open_url_ref2).pack(pady=3,anchor='w')
		self.btn_ref3 = ttk.Button(self.frame, text="[3] Caumon et al., Chem. Geol. 2014, 378, 52–61.", width=70, command=open_url_ref3).pack(pady=3,anchor='w')
        
      
	def butnew(self, text, number, _class):
		ttk.Button(self.frame, text=text, width=40, command=lambda: self.new_window(number, _class)).pack(padx=6, pady=10)

	#### creat an action "opening new windows" that is assigned to the 7 button created above. 
	def new_window(self, number, _class):
		self.new=tk.Toplevel(self.master)
		_class(self.new, number)

    

#########################################
########### Module Pure CO2 #############
#########################################
class module1: 
	def __init__(self, master, number):
		self.master = master
		self.master.geometry("580x510")
		self.master.title("FRAnCIs v.1.0.1 - (pure CO₂)")
		self.master.resizable(width=False, height=False)
		self.master.iconbitmap(resource_path("logo.ico"))
		self.frame=tk.Frame(self.master)
		self.frame.grid()
		
		##############################
        ##### CREATE INTERFACE #######
        ##############################
        
		self.label= tk.Label(self.frame, text="Calculation for Pure CO₂", font=('bold', 18))
		self.label.grid(row=0, column=1, columnspan=7, pady=10,sticky="W")
		self.label= tk.Label(self.frame, text="The CO₂ Fermi diad splitting (and its uncertainty) of the sample (\u0394_sample) and of the standard (\u0394_std) ")
		self.label.grid(row=1, column=0, columnspan=7, padx=10, sticky="W")
		self.label= tk.Label(self.frame, text="  at near-zero pressure are needed for pressure and density determinations")
		self.label.grid(row=2, column=0, columnspan=7, padx=10, sticky="W")
		
		#self.label= tk.Label(self.frame, text="_______________________________________________________________________________________________________________________________________")
		#self.label.grid(row=3, column=0, columnspan=5, padx=10, sticky="W")
        
		self.label_remark = tk.Label(self.frame, text="Remarks:", font=('bold', 12))
		self.label_remark.grid(row=4, column=0, columnspan=7, padx=10,  sticky="W")
		self.label = tk.Label(self.frame, text="   - If the Dassin spectrometer (at GeoRessouces lab) is selected, (\u0394_std) is not required, and so type 0.")
		self.label.grid(row=5, column=0, columnspan=7, sticky="W")
		self.label = tk.Label(self.frame, text="   - The calibrations were made over 5-600 bars, out of this range may cause larger errors or aberrant values.")
		self.label.grid(row=6, column=0, columnspan=7, sticky="W")
		self.label = tk.Label(self.frame, text="   - \u0394_std must be measured at least at the beginning and at the end of the experiment section.")
		self.label.grid(row=7, column=0, columnspan=7, sticky="W")
		#self.label = tk.Label(self.frame, text="   - The measured uncertainty (1\u03C3) is the total uncertainty arising from the calibration equation and the")
		#self.label.grid(row=8, column=0, columnspan=7, sticky="W")
		#self.label = tk.Label(self.frame, text="      uncertainty of the CO₂ Fermi diad spitting ifself.")
		#self.label.grid(row=8, column=0, columnspan=7, sticky="W")
		# self.label = tk.Label(self.frame, text="   - Click 'Supplement document' button below for more detail.")
		# self.label.grid(row=9, column=0, columnspan=7, sticky="W")		
		
		###############################
        ##### Select Température ######
        ###############################
		#self.label = tk.Label(self.frame, text="______________________________________________")
		#self.label.grid(row=10, column=3, columnspan=4,  sticky="W") 

		self.label_input = tk.Label(self.frame, text="__________ INPUT:", font=('bold', 10))
		self.label_input.grid(row=10, column=0, padx=10, pady=10, sticky="E")   


		self.label = tk.Label(self.frame, text="Select temperature :")
		self.label.grid(row=11, column=0,  padx=10, sticky="W") #remove (side="top", fill="x",)

		temperature = tk.IntVar()
		temperature.set(22)

		def selected_temperature():
		    print(temperature.get())

		self.Rbtn1=tk.Radiobutton(self.frame, text="22 °C", variable=temperature, value=22, padx = 20,  command=selected_temperature).grid(row=11, column=1, padx=10,  sticky="W")
		self.Rbtn2=tk.Radiobutton(self.frame, text="32 °C", variable=temperature, value=32, padx = 20,  command=selected_temperature).grid(row=11, column=3, padx=10,  sticky="W")

		###############################
		##### Select Instrument #####
		###############################

		self.label = tk.Label(self.frame, text="Select spectrometers :")
		self.label.grid(row=12, column=0, padx=10, sticky="W") #remove (side="top", fill="x",)

		instrument = tk.IntVar()
		instrument.set(1) #Dassin = 1, other spectrometers= 2

		def selected_instrument():
			print(instrument.get())

		self.Rbtn1=tk.Radiobutton(self.frame, text="Dassin ", variable=instrument, value=1, padx = 20,  command=selected_instrument).grid(row=12, column=1,  padx=10, sticky="W")
		self.Rbtn1=tk.Radiobutton(self.frame, text="Other Spectrometers", variable=instrument, value=2, padx = 20,  command=selected_instrument).grid(row=12, column=3,  padx=10, sticky="W")

		##############################
		self.label = tk.Label(self.frame, text="\u0394_sample ± uncertainty")
		self.label.grid(row=15, pady=5, padx=10, column=0, sticky="W")
		self.label = tk.Label(self.frame, text="\u0394_std")
		self.label.grid(row=16, column=0, padx=10, sticky="W")
		self.label = tk.Label(self.frame, text="(cm\u207b\u00B9)")
		self.label.grid(row=15, column=4, sticky="W")
		self.label = tk.Label(self.frame, text="(cm\u207b\u00B9)")
		self.label.grid(row=16, column=4, sticky="W")


		###############################
		##### INPUT values ############
		###############################
		self.FDS_entry = tk.Entry(self.frame, width = 20)
		self.FDS_entry.grid(row=15, column=1)
		#FDS_entry.get()
		self.label = tk.Label(self.frame, text="±")
		self.label.grid(row=15, column=2)
		self.unc_FDS_entry = tk.Entry(self.frame, width = 20)
		self.unc_FDS_entry.grid(row=15, column=3)


		self.FDS_std_entry = tk.Entry(self.frame, width = 20)
		self.FDS_std_entry.grid(row=16, column=1)
		# self.label = tk.Label(self.frame, text="±")
		# self.label.grid(row=16, column=2)
		# self.unc_FDS_std_entry = tk.Entry(self.frame, width = 20)
		# self.unc_FDS_std_entry.grid(row=16, column=3)
		#unc_FDS_entry.get()
		
		###############################
		##### OUTPUT #####
		###############################
		self.label = tk.Label(self.frame, text="________ OUTPUT:", font=('bold', 10))
		self.label.grid(row=17, column=0, padx=10, sticky="E")
		#self.label = tk.Label(self.frame, text="____________________________________________________________________")
		#self.label.grid(row=17, column=2, columnspan=4,  sticky="W")        

		self.label = tk.Label(self.frame, text="Pressure")
		self.label.grid(row=18, column=0, padx=10, pady=5, sticky="W")
		self.label = tk.Label(self.frame, text="Density")
		self.label.grid(row=19, column=0, padx=10, pady=5, sticky="W")
		self.label = tk.Label(self.frame, text="Molar Volume")
		self.label.grid(row=20, column=0, padx=10, pady=5, sticky="W")

		self.label = tk.Label(self.frame, text="±")
		self.label.grid(row=18, column=2, padx=10, pady=5)
		self.label = tk.Label(self.frame, text="±")
		self.label.grid(row=19, column=2, padx=10, pady=5)
		self.label = tk.Label(self.frame, text="±")
		self.label.grid(row=20, column=2, padx=10, pady=5)

		self.label = tk.Label(self.frame, text="(bar)")
		self.label.grid(row=18, column=4,  sticky="W")
		self.label = tk.Label(self.frame, text="(g.cm\u207b\u00B3)")
		self.label.grid(row=19, column=4,  sticky="W")
		self.label = tk.Label(self.frame, text="(cm\u00B3.mol\u207b\u00B9)")
		self.label.grid(row=20, column=4, sticky="W")

        ###############################
        ##### Caculation #######
        ###############################

        #### Make a clear-button for input field
		def clear_field_inputs(): 
			self.FDS_entry.delete(0, tk.END)
			self.unc_FDS_entry.delete(0, tk.END)
			self.FDS_std_entry.delete(0, tk.END)
			# self.unc_FDS_std_entry.delete(0, tk.END)

		#### Make a clear-button for output field
		def clear_field_results():
			pressure.delete(0, tk.END)
			density.delete(0, tk.END)
			molarvolume.delete(0, tk.END)
			uncer_pressure.delete(0, tk.END)
			uncer_density.delete(0, tk.END)
			uncer_molarvolume.delete(0, tk.END)

		def calculCO2pure():
			clear_field_results()
			FDS =float(self.FDS_entry.get())
			FDS_std =float(self.FDS_std_entry.get())
			uncer_FDS =float(self.unc_FDS_entry.get())
			
			# uncer_FDS_std =float(self.unc_FDS_std_entry.get())

			if temperature.get() == 22 and instrument.get() ==1:

				#Fermi diad spliting (FDS) normalisation
				FDS_normalized_1=((FDS+uncer_FDS)-104.5)/0.8408
				FDS_normalized_2=((FDS-uncer_FDS)-104.5)/0.8408


				## Calibration equation's coeff of CO2 pur at 22C
				p0= 49.09
				p1= 95.64
				p2= 221.9
				p3= 114.8
				p4= -3.781
				p5= -7.596

				d0=  0.7516
				d1=  0.3569
				d2= -0.05899
				d3= -0.01534 
				d4= 0.005858 
				d5= 0

				pressure1 = p5*FDS_normalized_1**5 + p4*FDS_normalized_1**4 + p3*FDS_normalized_1**3 + p2*FDS_normalized_1**2 +p1*FDS_normalized_1**1 + p0
				pressure2 = p5*FDS_normalized_2**5 + p4*FDS_normalized_2**4 + p3*FDS_normalized_2**3 + p2*FDS_normalized_2**2 +p1*FDS_normalized_2**1 + p0
				pressure_final = (pressure1 + pressure2)/2
				uncer_pressure_final = 5.7 + (max(pressure1, pressure2) - min(pressure1, pressure2))/(2*np.sqrt(3))  


				density1 = d5*FDS_normalized_1**5 + d4*FDS_normalized_1**4 + d3*FDS_normalized_1**3 + d2*FDS_normalized_1**2 + d1*FDS_normalized_1**1 + d0
				density2 = d5*FDS_normalized_2**5 + d4*FDS_normalized_2**4 + d3*FDS_normalized_2**3 + d2*FDS_normalized_2**2 + d1*FDS_normalized_2**1 + d0
				density_final = (density1 + density2)/2
				uncer_density_final = 0.003 + (max(density1,density2)-min(density1,density2))/(2*np.sqrt(3)) 

				molarvolume1 = 1/(max(density1,density2)/44)
				molarvolume2 = 1/(min(density1,density2)/44)
				molarvolume_final = (molarvolume1 + molarvolume2) / 2
				uncer_molarvolume_final = (molarvolume2 - molarvolume1) / (2*np.sqrt(3))
				

				#print('Max_Pressure', max_pressure)
				print('pressure1', pressure1)
				print('pressure2', pressure2)

				print("molarvolume1", molarvolume1)
				print("molarvolume2", molarvolume2)

				print('density =', density1)
				print('density =', density2)

				if pressure_final > 650 or pressure1 >650 or pressure2 >650 or pressure_final <-10 or pressure1 <-10 or pressure2 <-10 or density1<-0.005 or density2<-0.005 or density_final <-0.005:
					popupmsg_OCR()

			if temperature.get() == 32 and instrument.get() ==1:

				#Fermi diad spliting (FDS) normalisation
				FDS_normalized_1=((FDS+uncer_FDS)-104.2)/0.7694
				FDS_normalized_2=((FDS-uncer_FDS)-104.2)/0.7694

				## Calibration equation's coeff of CO2 pur at 32C
				p0= 72.46
				p1= 21.77
				p2= 91.49
				p3= 81.3
				p4= 8.731
				p5= -3.473

				d0= 0.6055
				d1= 0.3664
				d2= -0.01545
				d3= -0.02307
				d4= -0.00088519
				d5= 0

				pressure1 = p5*FDS_normalized_1**5 + p4*FDS_normalized_1**4 + p3*FDS_normalized_1**3 + p2*FDS_normalized_1**2 +p1*FDS_normalized_1**1 + p0
				pressure2 = p5*FDS_normalized_2**5 + p4*FDS_normalized_2**4 + p3*FDS_normalized_2**3 + p2*FDS_normalized_2**2 +p1*FDS_normalized_2**1 + p0
				pressure_final = (pressure1 + pressure2)/2
				uncer_pressure_final = 5.7 + (max(pressure1, pressure2) - min(pressure1, pressure2))/(2*np.sqrt(3))  


				density1 = d5*FDS_normalized_1**5 + d4*FDS_normalized_1**4 + d3*FDS_normalized_1**3 + d2*FDS_normalized_1**2 + d1*FDS_normalized_1**1 + d0
				density2 = d5*FDS_normalized_2**5 + d4*FDS_normalized_2**4 + d3*FDS_normalized_2**3 + d2*FDS_normalized_2**2 + d1*FDS_normalized_2**1 + d0
				density_final = (density1 + density2)/2
				uncer_density_final = 0.003 + (max(density1,density2)-min(density1,density2))/(2*np.sqrt(3)) 

				molarvolume1 = 1/(max(density1,density2)/44)
				molarvolume2 = 1/(min(density1,density2)/44)
				molarvolume_final = (molarvolume1 + molarvolume2) / 2
				uncer_molarvolume_final = (molarvolume2 - molarvolume1) / (2*np.sqrt(3))

				print('pressure1', pressure1)
				print('pressure2', pressure2)

				print("molarvolume1", molarvolume1)
				print("molarvolume2", molarvolume2)

				print('density =', density1)

				if pressure_final > 650 or pressure1 >650 or pressure2 >650 or pressure_final <-10 or pressure1 <-10 or pressure2 <-10 or density1<-0.005 or density2<-0.005 or density_final <-0.005:
					popupmsg_OCR()


			if temperature.get() == 22 and instrument.get() ==2:

				#Fermi diad spliting (FDS) normalisation
				FDS_normalized_1=(FDS - FDS_std) + uncer_FDS
				FDS_normalized_2=(FDS - FDS_std) - uncer_FDS


				## Calibration equation's coeff of CO2 pur at 22C
				

				p0= 0
				p1= 174.3532
				p2= -58.1268
				p3= -147.5050
				p4= +96.3113
				p5= -11.3004
				
				d0= 0
				d1= +0.31273
				d2= +0.11155
				d3= -0.01843
				d4= -0.0044
				d5= 0

				pressure1 = p5*FDS_normalized_1**5 + p4*FDS_normalized_1**4 + p3*FDS_normalized_1**3 + p2*FDS_normalized_1**2 +p1*FDS_normalized_1**1 + p0
				pressure2 = p5*FDS_normalized_2**5 + p4*FDS_normalized_2**4 + p3*FDS_normalized_2**3 + p2*FDS_normalized_2**2 +p1*FDS_normalized_2**1 + p0
				pressure_final = (pressure1 + pressure2)/2
				uncer_pressure_final = 8.7 + (max(pressure1, pressure2) - min(pressure1, pressure2))/(2*np.sqrt(3))  #uncertainty=8


				density1 = d5*FDS_normalized_1**5 + d4*FDS_normalized_1**4 + d3*FDS_normalized_1**3 + d2*FDS_normalized_1**2 + d1*FDS_normalized_1**1 + d0
				density2 = d5*FDS_normalized_2**5 + d4*FDS_normalized_2**4 + d3*FDS_normalized_2**3 + d2*FDS_normalized_2**2 + d1*FDS_normalized_2**1 + d0
				density_final = (density1 + density2)/2
				uncer_density_final = 0.006 + (max(density1,density2)-min(density1,density2))/(2*np.sqrt(3)) #uncertainty = 0.003

				molarvolume1 = 1/(max(density1,density2)/44)
				molarvolume2 = 1/(min(density1,density2)/44)
				molarvolume_final = (molarvolume1 + molarvolume2) / 2
				uncer_molarvolume_final = (molarvolume2 - molarvolume1) / (2*np.sqrt(3))
				

				#print('Max_Pressure', max_pressure)
				print('pressure1', pressure1)
				print('pressure2', pressure2)

				print("molarvolume1", molarvolume1)
				print("molarvolume2", molarvolume2)

				print('density1 =', density1)
				print('density2 =', density2)

				if pressure_final > 650 or pressure1 >650 or pressure2 >650 or pressure_final <-10 or pressure1 <-10 or pressure2 <-10 or density1<-0.005 or density2<-0.005 or density_final <-0.005:
					popupmsg_OCR()

			if temperature.get() == 32 and instrument.get() ==2:

				#Fermi diad spliting (FDS) normalisation
				FDS_normalized_1=(FDS - FDS_std) + uncer_FDS
				FDS_normalized_2=(FDS - FDS_std) - uncer_FDS

				## Calibration equation's coeff of CO2 pur at 32C
			

				p0= 0
				p1= 148.73
				p2= 20.946
				p3= -180.85
				p4= 96.503
				p5= -9.8157

				d0= 0
				d1= +0.31273
				d2= +0.11155
				d3= -0.01843
				d4= -0.0044
				d5= 0

				pressure1 = p5*FDS_normalized_1**5 + p4*FDS_normalized_1**4 + p3*FDS_normalized_1**3 + p2*FDS_normalized_1**2 +p1*FDS_normalized_1**1 + p0
				pressure2 = p5*FDS_normalized_2**5 + p4*FDS_normalized_2**4 + p3*FDS_normalized_2**3 + p2*FDS_normalized_2**2 +p1*FDS_normalized_2**1 + p0
				pressure_final = (pressure1 + pressure2)/2
				uncer_pressure_final = 8.7 + (max(pressure1, pressure2) - min(pressure1, pressure2))/(2*np.sqrt(3))  #uncertainty=8


				density1 = d5*FDS_normalized_1**5 + d4*FDS_normalized_1**4 + d3*FDS_normalized_1**3 + d2*FDS_normalized_1**2 + d1*FDS_normalized_1**1 + d0
				density2 = d5*FDS_normalized_2**5 + d4*FDS_normalized_2**4 + d3*FDS_normalized_2**3 + d2*FDS_normalized_2**2 + d1*FDS_normalized_2**1 + d0
				density_final = (density1 + density2)/2
				uncer_density_final = 0.006 + (max(density1,density2)-min(density1,density2))/(2*np.sqrt(3)) #uncertainty = 0.003

				molarvolume1 = 1/(max(density1,density2)/44)
				molarvolume2 = 1/(min(density1,density2)/44)
				molarvolume_final = (molarvolume1 + molarvolume2) / 2
				uncer_molarvolume_final = (molarvolume2 - molarvolume1) / (2*np.sqrt(3))

				print('pressure1', pressure1)
				print('pressure2', pressure2)

				print("molarvolume1", molarvolume1)
				print("molarvolume2", molarvolume2)

				print('density =', density1)

				if pressure_final > 650 or pressure1 >650 or pressure2 >650 or pressure_final <-10 or pressure1 <-10 or pressure2 <-10 or density1<-0.005 or density2<-0.005 or density_final <-0.005:
					popupmsg_OCR()

			pressure.insert(tk.END, "%.1f" % pressure_final)
			density.insert(tk.END, "%.3f" % density_final)
			molarvolume.insert(tk.END, "%.3f" % molarvolume_final)

			uncer_pressure.insert(tk.END, "%.1f" % uncer_pressure_final)
			uncer_density.insert(tk.END, "%.3f" % uncer_density_final)
			uncer_molarvolume.insert(tk.END, "%.3f" % uncer_molarvolume_final)

		################################    
		########  display results ######
		################################ 
		pressure= tk.Entry(self.frame, width = 20) #, state='disabled'
		pressure.grid(row=18, column=1)
		density = tk.Entry(self.frame, width = 20) 
		density.grid(row=19, column=1)
		molarvolume = tk.Entry(self.frame,  width = 20)
		molarvolume.grid(row=20, column=1)

		######## display uncertainty ########
		uncer_pressure = tk.Entry(self.frame,  width = 20) #, state='disabled'
		uncer_pressure.grid(row=18, column=3)
		uncer_density = tk.Entry(self.frame,  width = 20) 
		uncer_density.grid(row=19, column=3)
		uncer_molarvolume = tk.Entry(self.frame,  width = 20) 
		uncer_molarvolume.grid(row=20, column=3)


		#############################
		######### Buttons ###########
		#############################

		self.button1_1 = tk.Button(self.frame, text="Clear Input", command=clear_field_inputs)
		self.button1_1.grid(row=10, column=1, padx=10)

		self.button1_2 = tk.Button(self.frame, text="Calculate", bg="green", width=10, command=calculCO2pure)
		self.button1_2.grid(row=17, column=1, padx=10, pady=10)

		self.button1_3 = tk.Button(self.frame, text="Clear Results", width=10, command=clear_field_results)
		self.button1_3.grid(row=21, column=1, pady=10)

		# def OpenSuppDoc_CO2():
		# 	os.startfile(resource_path('SuppDoc_CO2.pdf'))
		# self.button1_4 = tk.Button(self.frame, text="Supplement document", bg="orange", command=OpenSuppDoc_CO2)
		# self.button1_4.grid(row=21, column=0, padx=10)


		self.quit = tk.Button(self.frame, text="Close", width=15, command=self.close_window)	
		self.quit.grid(row=21, column=3, padx=10)

	def close_window(self):
		self.master.destroy()


#########################################
########### Module Pure CH4 #############
#########################################
class module2: 
	def __init__(self, master, number):
		self.master = master
		self.master.title("FRAnCIs v.1.0.1 - (pure CH₄)")
		self.master.geometry("600x500")
		self.master.resizable(width=False, height=False)
		self.master.iconbitmap(resource_path("logo.ico"))
		self.frame=tk.Frame(self.master)
		self.frame.grid()


		#### Create the UI of windows of module 2

		self.label = tk.Label(self.frame, text="Calculation for Pure CH₄", font=('bold', 18))
		self.label.grid(row=0, column=0, columnspan=8, padx=150, pady=10, sticky="W") #remove (side="top", fill="x",)        

		self.label = tk.Label(self.frame, text="The CH₄ \u03BD₁ band position of the sample (\u03BD₁_sample) and of the standard at near-zero pressure (\u03BD₁_std)")
		self.label.grid(row=1, column=0, columnspan=8, padx=10, sticky="W") #remove (side="top", fill="x",)   
		self.label = tk.Label(self.frame, text="   and their uncertainty are needed for pressure and density determination.")
		self.label.grid(row=2, column=0, columnspan=8,padx=10, sticky="W") #remove (side="top", fill="x",)
		#self.label = tk.Label(self.frame,text="________________________________________________________________________________________________________________________________")
		#self.label.grid(row=3, column=0, padx=10, columnspan=8, sticky="E")

		self.label_remark = tk.Label(self.frame, text="Remarks:", font=('bold', 12))
		self.label_remark.grid(row=5, column=0, columnspan=8, padx=10,  sticky="W")

		self.label = tk.Label(self.frame, text="   - The fitted peak position of CH₄ should be corrected by two neon emission lines at ~2851.38 and")
		self.label.grid(row=6, column=0, columnspan=8, sticky="W")
		self.label = tk.Label(self.frame, text="       ~2972.44 cm\u207b\u00B9 (relative to 514.53 nm) to minimize the error.")
		self.label.grid(row=7, column=0, columnspan=8, sticky="W")

		self.label = tk.Label(self.frame, text="   - The calibrations were made over 5-600 bars, out of this range may cause larger errors or aberrant values.")
		self.label.grid(row=8, column=0, columnspan=8, sticky="W")
		#self.label = tk.Label(self.frame, text="   - The uncertainty (1\u03C3) of measured results is the total uncertainty arising from the calibration equation and the uncertainty of CH₄ peak position.")
		#self.label.grid(row=9, column=0, columnspan=8, sticky="W")
		# self.label = tk.Label(self.frame, text="   - Click 'Supplement document' button below for more detail.")
		# self.label.grid(row=10, column=0, columnspan=8, sticky="W")

		
		###################################
        ########## INPUT ##################
        ###################################

		self.label_input = tk.Label(self.frame, text="_______     INPUT:", font=('bold', 10))
		self.label_input.grid(row=11, column=0, pady=10,  sticky="E") 
		#self.label = tk.Label(self.frame,text="__________________________________________________________________")
		#self.label.grid(row=11, column=1, padx=10, columnspan=8, sticky="E")



		###############################
		##### Select Température #####
		###############################
		self.label = tk.Label(self.frame, text="Select temperature :")
		self.label.grid(row=12, column=0, columnspan=2, padx=10, pady=10,sticky="W") #remove (side="top", fill="x",)

		temperature = tk.IntVar()
		temperature.set(22)

		def selected_temperature():
			print(temperature.get())

		self.Rbtn1=tk.Radiobutton(self.frame, text="22 °C", variable=temperature, value=22, padx = 20,  command=selected_temperature).grid(row=12, column=1,  padx=10, sticky="E")
		self.Rbtn1=tk.Radiobutton(self.frame, text="32 °C", variable=temperature, value=32, padx = 20,  command=selected_temperature).grid(row=12, column=3,  padx=10, sticky="W")      


		self.label = tk.Label(self.frame, text="\u03BD₁_sample (cm\u207b\u00B9)")
		self.label.grid(row=13, column=1)
		self.label = tk.Label(self.frame, text="\u03BD₁_std (cm\u207b\u00B9)")
		self.label.grid(row=13, column=3)

		self.label = tk.Label(self.frame, text="Uncertainty (cm\u207b\u00B9)")
		self.label.grid(row=13, column=5, sticky="W")
		#self.label = tk.Label(self.frame, text="(type 0 if unknown)")
		#self.label.grid(row=13, column=6)


		############ creat entry frame for input

		self.nuCH4_sample_entry = tk.Entry(self.frame, width = 20)
		self.nuCH4_sample_entry.grid(row=14, column=1)
		self.nuCH4_sample_entry.get()
		self.nuCH4_std_entry = tk.Entry(self.frame, width = 20)
		self.nuCH4_std_entry.grid(row=14, column=3)
		self.nuCH4_std_entry.get()

		self.label = tk.Label(self.frame, text="±")
		self.label.grid(row=14, column=4, padx=10, sticky="W")

		self.unc_nuCH4_entry = tk.Entry(self.frame, width = 10)
		self.unc_nuCH4_entry.grid(row=14, column=5, sticky="W")
		self.unc_nuCH4_entry.get()

		###################################
		########## OUTPUT #################
		###################################

		self.label = tk.Label(self.frame, text="_______  OUTPUT:", font=('bold', 10))
		self.label.grid(row=15, column=0,  sticky="E")
		#self.label = tk.Label(self.frame, text="______________________________________________________________________________________________________")
		#self.label.grid(row=15, column=1, columnspan=6,  sticky="E")       

		self.label = tk.Label(self.frame, text="Pressure")
		self.label.grid(row=16, column=0, padx=10, pady=5, sticky="W")
		self.label = tk.Label(self.frame, text="Density")
		self.label.grid(row=17, column=0, padx=10, pady=5, sticky="W")
		self.label = tk.Label(self.frame, text="Molar Volume")
		self.label.grid(row=18, column=0, padx=10, pady=5, sticky="W")

		self.label = tk.Label(self.frame, text="±")
		self.label.grid(row=16, column=2, padx=10, pady=5)
		self.label = tk.Label(self.frame, text="±")
		self.label.grid(row=17, column=2, padx=10, pady=5)
		self.label = tk.Label(self.frame, text="±")
		self.label.grid(row=18, column=2, padx=10, pady=5)

		self.label = tk.Label(self.frame, text="(bar)")
		self.label.grid(row=16, column=5, pady=5, sticky="W")
		self.label = tk.Label(self.frame, text="(g.cm\u207b\u00B3)")
		self.label.grid(row=17, column=5,  pady=5, sticky="W")
		self.label = tk.Label(self.frame, text="(cm\u00B3.mol\u207b\u00B9)")
		self.label.grid(row=18, column=5,  pady=5, sticky="W")


		###############################
		##### Caculation #######
		###############################

		#### Make a clear-button for input field
		def clear_field_inputs(): 
			self.nuCH4_sample_entry.delete(0, tk.END)
			self.nuCH4_std_entry.delete(0, tk.END)
			self.unc_nuCH4_entry.delete(0, tk.END)
		#### Make a clear-button for output field
		def clear_field_results():
			pressure.delete(0, tk.END)
			density.delete(0, tk.END)
			molarvolume.delete(0, tk.END)
			uncer_pressure.delete(0, tk.END)
			uncer_density.delete(0, tk.END)
			uncer_molarvolume.delete(0, tk.END)


		def calculCH4pure():
			clear_field_results()
			nuCH4_sample    =float(self.nuCH4_sample_entry.get())
			nuCH4_std   =float(self.nuCH4_std_entry.get())
			unc_nuCH4 =float(self.unc_nuCH4_entry.get())

			if temperature.get() == 22:

				#Fermi diad spliting (FDS) normalisation
				DeltaPCH4= nuCH4_sample - nuCH4_std
				DeltaPCH4_1 = DeltaPCH4 + unc_nuCH4
				DeltaPCH4_2 = DeltaPCH4 - unc_nuCH4

				## Calibration equation's coeff of CH4 pur at 22C
				p1= 0.84299
				p2= 7.59453
				p3= 21.32662
				p4= -27.03755
				p5= 10.40897

				# Calibration equation fitted from all data published in the litterature
				d0= 0
				d1= -0.0373
				d2=0.0011
				d3=0.000402328
				d4=0.0000584981


				# Calibration equation fitted from GeoRessources's data only
				#d4= 0.00004142
				#d3= 0.0002762
				#d2= 0.001152
				#d1= -0.03468
				#d0= 0.004426

				pressure1 = p1*DeltaPCH4_1**4 + p2*DeltaPCH4_1**3 + p3*DeltaPCH4_1**2 + p4*DeltaPCH4_1**1 +p5
				pressure2 = p1*DeltaPCH4_2**4 + p2*DeltaPCH4_2**3 + p3*DeltaPCH4_2**2 + p4*DeltaPCH4_2**1 +p5
				pressure_final = (pressure1 + pressure2)/2
				uncer_pressure_final = 5.7 + (max(pressure1, pressure2) - min(pressure1, pressure2))/(2*np.sqrt(3)) #uncertainty = 5

				density1 = d4*DeltaPCH4_1**4 + d3*DeltaPCH4_1**3 + d2*DeltaPCH4_1**2 + d1*DeltaPCH4_1**1 +d0
				density2 = d4*DeltaPCH4_2**4 + d3*DeltaPCH4_2**3 + d2*DeltaPCH4_2**2 + d1*DeltaPCH4_2**1 +d0
				density_final = (density1 + density2)/2
				uncer_density_final = 0.003 + (max(density2,density1) -min(density2,density1))/(2*np.sqrt(3)) #uncertainty = 0.001

				molarvolume1 = 1/(max(density2,density1)/16)
				molarvolume2 = 1/(min(density2,density1)/16)
				molarvolume_final = (molarvolume2 + molarvolume1) / 2
				uncer_molarvolume_final = (molarvolume2 - molarvolume1) / (2*np.sqrt(3))

				print('pressure1', pressure1)
				print('pressure2', pressure2)

				print("molarvolume1", molarvolume1)
				print("molarvolume2", molarvolume2)

				print('density 1=', density1)
				print('density 2=', density2)

				if pressure_final > 650 or pressure1 >650 or pressure2 >650 or pressure_final <0 or pressure1 <0 or pressure2 <0 or density1<0 or density2<0 or density_final <0:
				    popupmsg_OCR()

			if temperature.get() == 32:

				 ## Calibration equation's coeff of CH4 pur at 32C

				DeltaPCH4= nuCH4_sample - nuCH4_std
				DeltaPCH4_1 = DeltaPCH4 + unc_nuCH4
				DeltaPCH4_2 = DeltaPCH4 - unc_nuCH4

				p1= 0.83453
				p2= 6.90357
				p3= 17.54440
				p4= -35.29858
				p5= 9.94956

				# Calibration equation fitted from all data published in the litterature
				d0= 0
				d1= -0.0373
				d2=0.0011
				d3=0.000402328
				d4=0.0000584981


				# Calibration equation fitted from GeoRessources's data only
				#d1= 0.000007227
				#d2= -0.0002615
				#d3= -0.001281
				#d4= -0.03819
				#d5= 0.004075

				pressure1 = p1*DeltaPCH4_1**4 + p2*DeltaPCH4_1**3 + p3*DeltaPCH4_1**2 + p4*DeltaPCH4_1**1 +p5
				pressure2 = p1*DeltaPCH4_2**4 + p2*DeltaPCH4_2**3 + p3*DeltaPCH4_2**2 + p4*DeltaPCH4_2**1 +p5
				pressure_final = (pressure1 + pressure2)/2
				uncer_pressure_final = 5.7 + (max(pressure1, pressure2) - min(pressure1, pressure2))/(2*np.sqrt(3)) #uncertainty =5

				density1 = d4*DeltaPCH4_1**4 + d3*DeltaPCH4_1**3 + d2*DeltaPCH4_1**2 + d1*DeltaPCH4_1**1 +d0
				density2 = d4*DeltaPCH4_2**4 + d3*DeltaPCH4_2**3 + d2*DeltaPCH4_2**2 + d1*DeltaPCH4_2**1 +d0
				density_final = (density1 + density2)/2
				uncer_density_final = 0.003 + (max(density2,density1) - min(density2,density1))/(2*np.sqrt(3)) #uncertainty = 0.001

				molarvolume1 = 1/(max(density2,density1)/16)
				molarvolume2 = 1/(min(density2,density1)/16)
				molarvolume_final = (molarvolume1 + molarvolume2) / 2
				uncer_molarvolume_final = (molarvolume2 - molarvolume1) / (2*np.sqrt(3))

				print('pressure1', pressure1)
				print('pressure2', pressure2)

				print("molarvolume1", molarvolume1)
				print("molarvolume2", molarvolume2)

				print('density 1=', density1)
				print('density 2=', density2)

				if pressure_final > 650 or pressure1 >650 or pressure2 >650 or pressure_final <0 or pressure1 <0 or pressure2 <0 or density1<0 or density2<0 or density_final <0:
				    popupmsg_OCR()


			pressure.insert(tk.END, "%.1f" % pressure_final)
			density.insert(tk.END, "%.3f" % density_final)
			molarvolume.insert(tk.END, "%.3f" % molarvolume_final)

			uncer_pressure.insert(tk.END, "%.1f" % uncer_pressure_final)
			uncer_density.insert(tk.END, "%.3f" % uncer_density_final)
			uncer_molarvolume.insert(tk.END, "%.3f" % uncer_molarvolume_final)

		# ################################    
		# ########  display results ######
		# ################################ 
		pressure= tk.Entry(self.frame, width = 20) #, state='disabled'
		pressure.grid(row=16, column=1)
		density = tk.Entry(self.frame, width = 20) 
		density.grid(row=17, column=1)
		molarvolume = tk.Entry(self.frame,  width = 20)
		molarvolume.grid(row=18, column=1)

		######## display uncertainty ########
		uncer_pressure = tk.Entry(self.frame,  width = 20) #, state='disabled'
		uncer_pressure.grid(row=16, column=3)
		uncer_density = tk.Entry(self.frame,  width = 20) 
		uncer_density.grid(row=17, column=3)
		uncer_molarvolume = tk.Entry(self.frame,  width = 20) 
		uncer_molarvolume.grid(row=18, column=3)   


		#############################
		######### Buttons ###########
		#############################

		self.button1_1 = tk.Button(self.frame, text="Clear Input", command=clear_field_inputs)
		self.button1_1.grid(row=11, column=1, padx=10)
		self.button1_2 = tk.Button(self.frame, text="Calculate", bg="green", width=10, command=calculCH4pure)
		self.button1_2.grid(row=15, column=1, padx=20, pady=10, sticky="W")
		
		self.button1_3 = tk.Button(self.frame, text="Clear Results", width=10, command=clear_field_results)
		self.button1_3.grid(row=19, column=1, padx=20, pady=10, sticky="W")

		# def OpenSuppDoc_CH4():
		# 	os.startfile(resource_path('SuppDoc_CH4.pdf'))
		# button1_4 = tk.Button(self.frame, text="Supplement document", bg="orange", command=OpenSuppDoc_CH4)
		# button1_4.grid(row=19, column=0, padx=10,  sticky="E")
		
		# self.label=tk.Label(self.frame,text="fOR TESTING ONLY")
		# self.label.grid()
		
		self.quit = tk.Button(self.frame, text="Close", width=13, command=self.close_window)	
		self.quit.grid(row=19, column=3, padx=10)

	def close_window(self):
		self.master.destroy()

#########################################
########### Module CO2 - N2 #############
#########################################
class module3: 
	def __init__(self, master, number):
		self.master = master
		self.master.title("FRAnCIs v.1.0.1 - (CO₂-N₂ mixtures)")
		self.master.geometry("690x630")
		self.master.resizable(width=False, height=False)
		self.master.iconbitmap(resource_path("logo.ico"))
		self.frame=tk.Frame(self.master)
		self.frame.grid()

		### Create the UI of windows of module 3 
		self.label = tk.Label(self.frame, text="Calculation for CO₂-N₂ mixtures", font=('bold', 18))
		self.label.grid(row=0, column=1, columnspan=10, padx=10, pady=10, sticky="W") #remove (side="top", fill="x",)        

		self.label = tk.Label(self.frame, text="The area of the N₂ (area_N2) and two CO₂ bands (area_CO2) are needed for composition determination. The CO₂ Fermi diad ")
		self.label.grid(row=1, column=0, columnspan=10, padx=10, sticky="W") #remove (side="top", fill="x",)   

		self.label = tk.Label(self.frame, text=" splitting (and its uncertainty) of the sample (\u0394_sample) and of the standard (\u0394_std) for pressure and density determination.")
		self.label.grid(row=2, column=0, columnspan=10,padx=10, sticky="W") #remove (side="top", fill="x",)
		#self.label = tk.Label(self.frame,text="____________________________________________________________________________________________________________________________________")
		#self.label.grid(row=3, column=0, padx=10, columnspan=6, sticky="E")

		self.label_remark = tk.Label(self.frame, text="Remarks:", font=('bold', 12))
		self.label_remark.grid(row=7, column=0, columnspan=10, padx=10,  sticky="W")

		self.label = tk.Label(self.frame, text="   - The area of the atmospheric N₂ band (area_N2_atm) must be excluded from that of N₂ within the sample (area_N2_sample)")
		self.label.grid(row=8, column=0, columnspan=10, sticky="W")

		self.label = tk.Label(self.frame, text="   - If the Dassin spectrometer (at GeoRessouces lab) is selected, (\u0394_std) is not required, and so type 0.")
		self.label.grid(row=9, column=0, columnspan=8, sticky="W")
		# self.label = tk.Label(self.frame, text="       to minimize the error.")
		# self.label.grid(row=10, column=0, columnspan=8, sticky="W")

		self.label = tk.Label(self.frame, text="   - The calibrations were made over 5-600 bars, out of this range may cause larger errors or aberrant values.")
		self.label.grid(row=11, column=0, columnspan=10, sticky="W")
		self.label = tk.Label(self.frame, text="   - The uncertainty (1\u03C3) of the measured composition is ~ ±0.5 mol%")
		self.label.grid(row=12, column=0, columnspan=10, sticky="W")  
		#self.label = tk.Label(self.frame, text="         and the uncertainty of the CO₂ Fermi diad splitting (\u0394).")
		#self.label.grid(row=13, column=0, columnspan=10, sticky="W")

		# self.label = tk.Label(self.frame, text="   - Click 'Supplement document' button below for more detail.")
		# self.label.grid(row=14, column=0, columnspan=10, sticky="W")		

		###############################
		##### INPUT section #####
		###############################

		self.label_input = tk.Label(self.frame, text="____________     INPUT:", font=('bold', 10))
		self.label_input.grid(row=16, column=0, pady=10, sticky="E")
		#self.label = tk.Label(self.frame,text="___________________________________________________________________________________________________________")
		#self.label.grid(row=16, column=1, columnspan=6,padx=10, sticky="E")

		###############################
		##### Select Temperature #####
		###############################
		self.label = tk.Label(self.frame, text="Select temperature :")
		self.label.grid(row=25, column=0, columnspan=2, padx=10, sticky="W") #remove (side="top", fill="x",)

		temperature = tk.IntVar()
		temperature.set(22)

		def selected_temperature():
			print(temperature.get())

		self.Rbtn1=tk.Radiobutton(self.frame, text="22 °C", variable=temperature, value=22, padx = 20,  command=selected_temperature).grid(row=25, column=1,  padx=10, stick="W")
		self.Rbtn1=tk.Radiobutton(self.frame, text="32 °C", variable=temperature, value=32, padx = 20,  command=selected_temperature).grid(row=25, column=2,  padx=10, stick="W")

		###############################
		##### Select Instrument #####
		###############################

		self.label = tk.Label(self.frame, text="Select spectrometers :")
		self.label.grid(row=26, column=0, columnspan=2, padx=10, sticky="W") #remove (side="top", fill="x",)

		instrument = tk.IntVar()
		instrument.set(1) #Dassin = 1, other spectrometers= 2

		def selected_instrument():
			print(instrument.get())

		self.Rbtn1=tk.Radiobutton(self.frame, text="Dassin", variable=instrument, value=1, padx = 20,  command=selected_instrument).grid(row=26, column=1,  padx=10, stick="W")
		self.Rbtn1=tk.Radiobutton(self.frame, text="Other Spectrometers", variable=instrument, value=2, padx = 20, pady = 5, command=selected_instrument).grid(row=26, column=2,columnspan=2, stick="W",  padx=10)
		
		####################################
		##### Select Laser wavelength #####
		####################################

		self.label = tk.Label(self.frame, text="Laser wavelength (nm):")
		self.label.grid(row=25, column=3, columnspan=2, padx=30, stick="W") #remove (side="top", fill="x",)

		# options = {"488 nm": 488, "514 nm": 514, "532 nm": 532, "633 nm": 633, "785 nm": 785}
		options=[488, 514, 532, 633, 785]
		laser_wavelength = tk.IntVar()
		laser_wavelength.set(514)
		
		# self.menu = OptionMenu(self.frame, laser_wavelength, *options.keys()).grid(row=26, column=4, stick="W")
		self.menu = OptionMenu(self.frame, laser_wavelength, *options).grid(row=25, column=4)

		
		######### ENTRY ##########

		##entry N2 spectroscopic data 
		self.label = tk.Label(self.frame, text="area_N2_sample")
		self.label.grid(row=27, column=1, padx=10)
		self.label = tk.Label(self.frame, text="area_N2_atm")
		self.label.grid(row=27, column=2, padx=10)
		self.label = tk.Label(self.frame, text="Spectroscopic data of N₂:")
		self.label.grid(row=28, column=0, padx=10, sticky="W")
		
		self.area_N2_entry_sample = tk.Entry(self.frame, width = 15)
		self.area_N2_entry_sample.grid(row=28, column=1)
		self.area_N2_entry_atm = tk.Entry(self.frame, width = 15)
		self.area_N2_entry_atm.grid(row=28, column=2)

		##entry CO2 spectroscopic data 

		self.label = tk.Label(self.frame, text="area_CO2")
		self.label.grid(row=29, column=1, padx=10)
		self.label = tk.Label(self.frame, text="\u0394_sample (cm\u207b\u00B9)")
		self.label.grid(row=29, column=2, padx=10)
		self.label = tk.Label(self.frame, text="\u0394_std (cm\u207b\u00B9)")
		self.label.grid(row=29, column=3, padx=10)
		self.label = tk.Label(self.frame, text="\u0394_uncertainty (cm\u207b\u00B9)")
		self.label.grid(row=29, column=4, padx=10)

		self.label = tk.Label(self.frame, text="Spectroscopic data of CO₂")
		self.label.grid(row=30, column=0, padx=10, sticky="E")
		
		self.area_CO2_entry = tk.Entry(self.frame, width = 15)
		self.area_CO2_entry.grid(row=30, column=1)
		self.FDS_entry = tk.Entry(self.frame, width = 15)
		self.FDS_entry.grid(row=30, column=2)
		self.FDS_entry_std = tk.Entry(self.frame, width = 15)
		self.FDS_entry_std.grid(row=30, column=3)
		self.unc_FDS_entry = tk.Entry(self.frame, width = 15)
		self.unc_FDS_entry.grid(row=30, column=4)

		#self.label = tk.Label(self.frame, text="(cm\u207b\u00B9)")
		#self.label.grid(row=30, column=5, padx=10) 
		

		self.label = tk.Label(self.frame, text="____________  OUTPUT:", font=('bold', 10))
		self.label.grid(row=33, column=0,  sticky="E")
		#self.label = tk.Label(self.frame, text="_________________________________________________________________________________________")
		#self.label.grid(row=30, column=1, columnspan=6, padx=10, sticky="E")        


		self.label = tk.Label(self.frame, text="(mol% CO₂)")
		self.label.grid(row=34, column=1, padx=10)
		self.label = tk.Label(self.frame, text="(mol% N₂)")
		self.label.grid(row=34, column=3, padx=10)
		
		self.label = tk.Label(self.frame, text="Composition")
		self.label.grid(row=35, column=0, padx=10,  sticky="W")
		self.label = tk.Label(self.frame, text="(±0.5 mol%)")
		self.label.grid(row=35, column=4, padx=10, sticky="W")
		self.label = tk.Label(self.frame, text="and")
		self.label.grid(row=35, column=2, padx=10)
		self.label = tk.Label(self.frame, text="------------------------------------------------------")
		self.label.grid(row=36, column=1, columnspan=3, padx=5)

		self.label = tk.Label(self.frame, text="Pressure")
		self.label.grid(row=39, column=0, padx=10, pady=5, sticky="W")
		self.label = tk.Label(self.frame, text="Density")
		self.label.grid(row=40, column=0, padx=10, pady=5, sticky="W")
		self.label = tk.Label(self.frame, text="Molar Volume")
		self.label.grid(row=41, column=0, padx=10, pady=5, sticky="W")

		self.label = tk.Label(self.frame, text="±")
		self.label.grid(row=39, column=2, padx=10, pady=5)
		self.label = tk.Label(self.frame, text="±")
		self.label.grid(row=40, column=2, padx=10, pady=5)
		self.label = tk.Label(self.frame, text="±")
		self.label.grid(row=41, column=2, padx=10, pady=5)

		self.label = tk.Label(self.frame, text="(bar)")
		self.label.grid(row=39, column=4, padx=10, pady=5, sticky="W")
		self.label = tk.Label(self.frame, text="(g.cm\u207b\u00B3)")
		self.label.grid(row=40, column=4, padx=10, pady=5, sticky="W")
		self.label = tk.Label(self.frame, text="(cm\u00B3.mol\u207b\u00B9)")
		self.label.grid(row=41, column=4, padx=10, pady=5, sticky="W")


		###############################
		##### Caculation ##############
		###############################

		#### Make a clear-button for input field
		def clear_field_inputs(): 
			self.area_CO2_entry.delete(0, tk.END)
			self.area_N2_entry_sample.delete(0, tk.END)
			self.area_N2_entry_atm.delete(0, tk.END)
			self.FDS_entry.delete(0, tk.END)
			self.FDS_entry_std.delete(0, tk.END)
			self.unc_FDS_entry.delete(0, tk.END)
			
			
		#### Make a clear-button for output field
		def clear_field_results():
			composition_CO2_display.delete(0, tk.END)
			composition_N2_display.delete(0, tk.END)
			pressure.delete(0, tk.END)
			density.delete(0, tk.END)
			molarvolume.delete(0, tk.END)
			uncer_pressure.delete(0, tk.END)
			uncer_density.delete(0, tk.END)
			uncer_molarvolume.delete(0, tk.END)


		def calculCO2N2():
			clear_field_results()
			area_N2_sample         = float(self.area_N2_entry_sample.get())
			area_N2_atm        = float(self.area_N2_entry_atm.get())
			area_CO2        = float(self.area_CO2_entry.get())
			FDS    			= float(self.FDS_entry.get())
			FDS_std  			= float(self.FDS_entry_std.get())
			unc_FDS       = float(self.unc_FDS_entry.get())
			
			#Composition calculation
			
			if laser_wavelength.get() == 488:
				RRSCS_CO2 = 2.30
				RRSCS_CH4 = 7.80
			if laser_wavelength.get() == 514:
				RRSCS_CO2 = 2.29
				RRSCS_CH4 = 7.73
			if laser_wavelength.get() == 532:
				RRSCS_CO2 = 2.27
				RRSCS_CH4 = 7.69
			if laser_wavelength.get() == 633:
				RRSCS_CO2 = 2.20
				RRSCS_CH4 = 7.44
			if laser_wavelength.get() == 785:
				RRSCS_CO2 = 2.09
				RRSCS_CH4 = 7.05
			
			print('the wavelength of the selected laser is', laser_wavelength.get(), 'nm')
			print('RRSCS_CH4=', RRSCS_CH4)		
			print('RRSCS_C02=', RRSCS_CO2)

			composition_CO2 = ((area_CO2/RRSCS_CO2)/((area_CO2/RRSCS_CO2) + ((area_N2_sample - area_N2_atm)/1)))
			composition_N2 = 1 - composition_CO2
						

			if temperature.get() == 22 and composition_CO2 >= 0.5 and instrument.get() ==1: 

				## Calibration equation's coeff of CO2-N2 at 22 °C over 5-500 bars


				# normalisation of concentration and of Fermi diad splitting
				composition_CO2_normalized_1 = (composition_CO2 + 0.005 - 0.76444)/0.17554
				composition_CO2_normalized_2 = (composition_CO2 - 0.005 - 0.76444)/0.17554
				FDS_normalized_1 = (FDS + unc_FDS - 103.82)/0.79435
				FDS_normalized_2 = (FDS - unc_FDS - 103.82)/0.79435
				
				p00= 132.737333
				p10= -97.87543837
				p01= 118.8159698
				p20= 52.48193614
				p11= -214.9144587
				p02= 156.1857227
				p30= -23.2742455
				p21= 101.6493196
				p12= -182.0409482
				p03= 122.9468574
				p31= -18.8741818
				p22= 48.57346341
				p13= -55.41887799
				p04= 11.58755259

				d00= 0.506428629
				d10= -0.08233871
				d01= 0.419517371
				d20= 0.01221691
				d11= -0.03625585
				d02= -0.006580948
				d30= -0.003308056
				d21= -0.007634737
				d12= 0.045147691
				d03= -0.036154129
				d31= 0.002204595
				d22= -0.01695751
				d13= 0.015373196
				d04= -0.003243828

				#### pressure calculation
				pressure1 = (p00*composition_CO2_normalized_1**0*FDS_normalized_1**0 
				+ p10*composition_CO2_normalized_1**1*FDS_normalized_1**0 
				+ p01*composition_CO2_normalized_1**0*FDS_normalized_1**1 
				+ p20*composition_CO2_normalized_1**2*FDS_normalized_1**0 
				+ p11*composition_CO2_normalized_1**1*FDS_normalized_1**1 
				+ p02*composition_CO2_normalized_1**0*FDS_normalized_1**2 
				+ p30*composition_CO2_normalized_1**3*FDS_normalized_1**0 
				+ p21*composition_CO2_normalized_1**2*FDS_normalized_1**1
				+ p12*composition_CO2_normalized_1**1*FDS_normalized_1**2 
				+ p03*composition_CO2_normalized_1**0*FDS_normalized_1**3 
				+ p31*composition_CO2_normalized_1**3*FDS_normalized_1**1 
				+ p22*composition_CO2_normalized_1**2*FDS_normalized_1**2
				+ p13*composition_CO2_normalized_1**1*FDS_normalized_1**3 
				+ p04*composition_CO2_normalized_1**0*FDS_normalized_1**4)

				pressure2 = (p00*composition_CO2_normalized_2**0*FDS_normalized_2**0 
				+ p10*composition_CO2_normalized_2**1*FDS_normalized_2**0 
				+ p01*composition_CO2_normalized_2**0*FDS_normalized_2**1 
				+ p20*composition_CO2_normalized_2**2*FDS_normalized_2**0
				+ p11*composition_CO2_normalized_2**1*FDS_normalized_2**1 
				+ p02*composition_CO2_normalized_2**0*FDS_normalized_2**2
				+ p30*composition_CO2_normalized_2**3*FDS_normalized_2**0 
				+ p21*composition_CO2_normalized_2**2*FDS_normalized_2**1
				+ p12*composition_CO2_normalized_2**1*FDS_normalized_2**2 
				+ p03*composition_CO2_normalized_2**0*FDS_normalized_2**3 
				+ p31*composition_CO2_normalized_2**3*FDS_normalized_2**1 
				+ p22*composition_CO2_normalized_2**2*FDS_normalized_2**2
				+ p13*composition_CO2_normalized_2**1*FDS_normalized_2**3 
				+ p04*composition_CO2_normalized_2**0*FDS_normalized_2**4)

				pressure3 = (p00*composition_CO2_normalized_1**0*FDS_normalized_2**0 
				+ p10*composition_CO2_normalized_1**1*FDS_normalized_2**0 
				+ p01*composition_CO2_normalized_1**0*FDS_normalized_2**1 
				+ p20*composition_CO2_normalized_1**2*FDS_normalized_2**0
				+ p11*composition_CO2_normalized_1**1*FDS_normalized_2**1 
				+ p02*composition_CO2_normalized_1**0*FDS_normalized_2**2 
				+ p30*composition_CO2_normalized_1**3*FDS_normalized_2**0 
				+ p21*composition_CO2_normalized_1**2*FDS_normalized_2**1
				+ p12*composition_CO2_normalized_1**1*FDS_normalized_2**2 
				+ p03*composition_CO2_normalized_1**0*FDS_normalized_2**3 
				+ p31*composition_CO2_normalized_1**3*FDS_normalized_2**1 
				+ p22*composition_CO2_normalized_1**2*FDS_normalized_2**2
				+ p13*composition_CO2_normalized_1**1*FDS_normalized_2**3 
				+ p04*composition_CO2_normalized_1**0*FDS_normalized_2**4)

				pressure4 = (p00*composition_CO2_normalized_2**0*FDS_normalized_1**0 
				+ p10*composition_CO2_normalized_2**1*FDS_normalized_1**0 
				+ p01*composition_CO2_normalized_2**0*FDS_normalized_1**1 
				+ p20*composition_CO2_normalized_2**2*FDS_normalized_1**0
				+ p11*composition_CO2_normalized_2**1*FDS_normalized_1**1 
				+ p02*composition_CO2_normalized_2**0*FDS_normalized_1**2 
				+ p30*composition_CO2_normalized_2**3*FDS_normalized_1**0 
				+ p21*composition_CO2_normalized_2**2*FDS_normalized_1**1
				+ p12*composition_CO2_normalized_2**1*FDS_normalized_1**2 
				+ p03*composition_CO2_normalized_2**0*FDS_normalized_1**3 
				+ p31*composition_CO2_normalized_2**3*FDS_normalized_1**1 
				+ p22*composition_CO2_normalized_2**2*FDS_normalized_1**2
				+ p13*composition_CO2_normalized_2**1*FDS_normalized_1**3 
				+ p04*composition_CO2_normalized_2**0*FDS_normalized_1**4)

				########################
				#### density calculation

				density1 = (d00*composition_CO2_normalized_1**0*FDS_normalized_1**0 
				+ d10*composition_CO2_normalized_1**1*FDS_normalized_1**0 
				+ d01*composition_CO2_normalized_1**0*FDS_normalized_1**1 
				+ d20*composition_CO2_normalized_1**2*FDS_normalized_1**0 
				+ d11*composition_CO2_normalized_1**1*FDS_normalized_1**1 
				+ d02*composition_CO2_normalized_1**0*FDS_normalized_1**2 
				+ d30*composition_CO2_normalized_1**3*FDS_normalized_1**0 
				+ d21*composition_CO2_normalized_1**2*FDS_normalized_1**1
				+ d12*composition_CO2_normalized_1**1*FDS_normalized_1**2 
				+ d03*composition_CO2_normalized_1**0*FDS_normalized_1**3 
				+ d31*composition_CO2_normalized_1**3*FDS_normalized_1**1 
				+ d22*composition_CO2_normalized_1**2*FDS_normalized_1**2
				+ d13*composition_CO2_normalized_1**1*FDS_normalized_1**3 
				+ d04*composition_CO2_normalized_1**0*FDS_normalized_1**4)

				density2 = (d00*composition_CO2_normalized_2**0*FDS_normalized_2**0 
				+ d10*composition_CO2_normalized_2**1*FDS_normalized_2**0 
				+ d01*composition_CO2_normalized_2**0*FDS_normalized_2**1 
				+ d20*composition_CO2_normalized_2**2*FDS_normalized_2**0
				+ d11*composition_CO2_normalized_2**1*FDS_normalized_2**1 
				+ d02*composition_CO2_normalized_2**0*FDS_normalized_2**2
				+ d30*composition_CO2_normalized_2**3*FDS_normalized_2**0 
				+ d21*composition_CO2_normalized_2**2*FDS_normalized_2**1
				+ d12*composition_CO2_normalized_2**1*FDS_normalized_2**2 
				+ d03*composition_CO2_normalized_2**0*FDS_normalized_2**3 
				+ d31*composition_CO2_normalized_2**3*FDS_normalized_2**1 
				+ d22*composition_CO2_normalized_2**2*FDS_normalized_2**2
				+ d13*composition_CO2_normalized_2**1*FDS_normalized_2**3 
				+ d04*composition_CO2_normalized_2**0*FDS_normalized_2**4)

				density3 = (d00*composition_CO2_normalized_1**0*FDS_normalized_2**0 
				+ d10*composition_CO2_normalized_1**1*FDS_normalized_2**0 
				+ d01*composition_CO2_normalized_1**0*FDS_normalized_2**1 
				+ d20*composition_CO2_normalized_1**2*FDS_normalized_2**0
				+ d11*composition_CO2_normalized_1**1*FDS_normalized_2**1 
				+ d02*composition_CO2_normalized_1**0*FDS_normalized_2**2 
				+ d30*composition_CO2_normalized_1**3*FDS_normalized_2**0 
				+ d21*composition_CO2_normalized_1**2*FDS_normalized_2**1
				+ d12*composition_CO2_normalized_1**1*FDS_normalized_2**2 
				+ d03*composition_CO2_normalized_1**0*FDS_normalized_2**3 
				+ d31*composition_CO2_normalized_1**3*FDS_normalized_2**1 
				+ d22*composition_CO2_normalized_1**2*FDS_normalized_2**2
				+ d13*composition_CO2_normalized_1**1*FDS_normalized_2**3 
				+ d04*composition_CO2_normalized_1**0*FDS_normalized_2**4)

				density4 = (d00*composition_CO2_normalized_2**0*FDS_normalized_1**0 
				+ d10*composition_CO2_normalized_2**1*FDS_normalized_1**0 
				+ d01*composition_CO2_normalized_2**0*FDS_normalized_1**1 
				+ d20*composition_CO2_normalized_2**2*FDS_normalized_1**0
				+ d11*composition_CO2_normalized_2**1*FDS_normalized_1**1 
				+ d02*composition_CO2_normalized_2**0*FDS_normalized_1**2 
				+ d30*composition_CO2_normalized_2**3*FDS_normalized_1**0 
				+ d21*composition_CO2_normalized_2**2*FDS_normalized_1**1
				+ d12*composition_CO2_normalized_2**1*FDS_normalized_1**2 
				+ d03*composition_CO2_normalized_2**0*FDS_normalized_1**3 
				+ d31*composition_CO2_normalized_2**3*FDS_normalized_1**1 
				+ d22*composition_CO2_normalized_2**2*FDS_normalized_1**2
				+ d13*composition_CO2_normalized_2**1*FDS_normalized_1**3 
				+ d04*composition_CO2_normalized_2**0*FDS_normalized_1**4)              

				pressure_final = (max(pressure1, pressure2, pressure3, pressure4) + min(pressure1, pressure2, pressure3, pressure4))/2 #pressure max - pressure min
				uncer_pressure_final = 7.1 + (max(pressure1, pressure2, pressure3, pressure4) - min(pressure1, pressure2, pressure3, pressure4))/(2*np.sqrt(3)) #uncer = 10

				density_final = (max(density1, density2, density3, density4) + min(density1, density2, density3, density4))/2 #density max - density min
				uncer_density_final = 0.0042 + (max(density1, density2, density3, density4) - min(density1, density2, density3, density4))/(2*np.sqrt(3)) #uncer = 0.006

				molarvolume1 = 1/(max(density1, density2, density3, density4)/(44*composition_CO2 + 28*composition_N2))
				molarvolume2 = 1/(min(density1, density2, density3, density4)/(44*composition_CO2 + 28*composition_N2))
				
				molarvolume_final = (molarvolume1 + molarvolume2)/2

				uncer_molarvolume_final = (molarvolume2 - molarvolume1)/(2*np.sqrt(3))

				##### verify if measured pressure < 160 bar, if it is, re-recalculte using calibration data for 5-160 bar range.
				if pressure_final <= 150: 

					## Calibration equation's coeff of CO2-N2 at 22 °C over 5-160 bars
					# normalisation of concentration and of Fermi diad splitting
					
					composition_CO2_normalized_1 = (composition_CO2 + 0.005 - 0.77632)/0.18027
					composition_CO2_normalized_2 = (composition_CO2 - 0.005 - 0.77632)/0.18027
					FDS_normalized_1 = (FDS + unc_FDS - 103.4)/0.69548
					FDS_normalized_2 = (FDS - unc_FDS - 103.4)/0.69548
										
					p00= 96.04521259
					p10= -37.64345175
					p01= 59.6284227
					p20= 13.03677947
					p11= -61.06487393
					p02= -19.9683198
					p30= -4.75652517
					p21= 23.80817957
					p12= -37.44444918
					p03= 32.33006119
					p31= -3.837992187
					p22= 8.303532695
					p13= -16.87991622
					p04= 9.516399693

					d00= 0.291506042
					d10= -0.04488858
					d01= 0.345009126
					d20= 0.003754508
					d11= -0.050522777
					d02= 0.024506871
					d30= -0.013553702
					d21= 0.002377929
					d12= 0.02365643
					d03= -0.027150512
					d31= -0.014003719
					d22= -0.006231591
					d13= 0.031093488
					d04= -0.008939409

					#### pressure calculation
					pressure1 = (p00*composition_CO2_normalized_1**0*FDS_normalized_1**0 
					+ p10*composition_CO2_normalized_1**1*FDS_normalized_1**0 
					+ p01*composition_CO2_normalized_1**0*FDS_normalized_1**1 
					+ p20*composition_CO2_normalized_1**2*FDS_normalized_1**0 
					+ p11*composition_CO2_normalized_1**1*FDS_normalized_1**1 
					+ p02*composition_CO2_normalized_1**0*FDS_normalized_1**2 
					+ p30*composition_CO2_normalized_1**3*FDS_normalized_1**0 
					+ p21*composition_CO2_normalized_1**2*FDS_normalized_1**1
					+ p12*composition_CO2_normalized_1**1*FDS_normalized_1**2 
					+ p03*composition_CO2_normalized_1**0*FDS_normalized_1**3 
					+ p31*composition_CO2_normalized_1**3*FDS_normalized_1**1 
					+ p22*composition_CO2_normalized_1**2*FDS_normalized_1**2
					+ p13*composition_CO2_normalized_1**1*FDS_normalized_1**3 
					+ p04*composition_CO2_normalized_1**0*FDS_normalized_1**4)

					pressure2 = (p00*composition_CO2_normalized_2**0*FDS_normalized_2**0 
					+ p10*composition_CO2_normalized_2**1*FDS_normalized_2**0 
					+ p01*composition_CO2_normalized_2**0*FDS_normalized_2**1 
					+ p20*composition_CO2_normalized_2**2*FDS_normalized_2**0
					+ p11*composition_CO2_normalized_2**1*FDS_normalized_2**1 
					+ p02*composition_CO2_normalized_2**0*FDS_normalized_2**2
					+ p30*composition_CO2_normalized_2**3*FDS_normalized_2**0 
					+ p21*composition_CO2_normalized_2**2*FDS_normalized_2**1
					+ p12*composition_CO2_normalized_2**1*FDS_normalized_2**2 
					+ p03*composition_CO2_normalized_2**0*FDS_normalized_2**3 
					+ p31*composition_CO2_normalized_2**3*FDS_normalized_2**1 
					+ p22*composition_CO2_normalized_2**2*FDS_normalized_2**2
					+ p13*composition_CO2_normalized_2**1*FDS_normalized_2**3 
					+ p04*composition_CO2_normalized_2**0*FDS_normalized_2**4)

					pressure3 = (p00*composition_CO2_normalized_1**0*FDS_normalized_2**0 
					+ p10*composition_CO2_normalized_1**1*FDS_normalized_2**0 
					+ p01*composition_CO2_normalized_1**0*FDS_normalized_2**1 
					+ p20*composition_CO2_normalized_1**2*FDS_normalized_2**0
					+ p11*composition_CO2_normalized_1**1*FDS_normalized_2**1 
					+ p02*composition_CO2_normalized_1**0*FDS_normalized_2**2 
					+ p30*composition_CO2_normalized_1**3*FDS_normalized_2**0 
					+ p21*composition_CO2_normalized_1**2*FDS_normalized_2**1
					+ p12*composition_CO2_normalized_1**1*FDS_normalized_2**2 
					+ p03*composition_CO2_normalized_1**0*FDS_normalized_2**3 
					+ p31*composition_CO2_normalized_1**3*FDS_normalized_2**1 
					+ p22*composition_CO2_normalized_1**2*FDS_normalized_2**2
					+ p13*composition_CO2_normalized_1**1*FDS_normalized_2**3 
					+ p04*composition_CO2_normalized_1**0*FDS_normalized_2**4)

					pressure4 = (p00*composition_CO2_normalized_2**0*FDS_normalized_1**0 
					+ p10*composition_CO2_normalized_2**1*FDS_normalized_1**0 
					+ p01*composition_CO2_normalized_2**0*FDS_normalized_1**1 
					+ p20*composition_CO2_normalized_2**2*FDS_normalized_1**0
					+ p11*composition_CO2_normalized_2**1*FDS_normalized_1**1 
					+ p02*composition_CO2_normalized_2**0*FDS_normalized_1**2 
					+ p30*composition_CO2_normalized_2**3*FDS_normalized_1**0 
					+ p21*composition_CO2_normalized_2**2*FDS_normalized_1**1
					+ p12*composition_CO2_normalized_2**1*FDS_normalized_1**2 
					+ p03*composition_CO2_normalized_2**0*FDS_normalized_1**3 
					+ p31*composition_CO2_normalized_2**3*FDS_normalized_1**1 
					+ p22*composition_CO2_normalized_2**2*FDS_normalized_1**2
					+ p13*composition_CO2_normalized_2**1*FDS_normalized_1**3 
					+ p04*composition_CO2_normalized_2**0*FDS_normalized_1**4)

					########################
					#### density calculation

					density1 = (d00*composition_CO2_normalized_1**0*FDS_normalized_1**0 
					+ d10*composition_CO2_normalized_1**1*FDS_normalized_1**0 
					+ d01*composition_CO2_normalized_1**0*FDS_normalized_1**1 
					+ d20*composition_CO2_normalized_1**2*FDS_normalized_1**0 
					+ d11*composition_CO2_normalized_1**1*FDS_normalized_1**1 
					+ d02*composition_CO2_normalized_1**0*FDS_normalized_1**2 
					+ d30*composition_CO2_normalized_1**3*FDS_normalized_1**0 
					+ d21*composition_CO2_normalized_1**2*FDS_normalized_1**1
					+ d12*composition_CO2_normalized_1**1*FDS_normalized_1**2 
					+ d03*composition_CO2_normalized_1**0*FDS_normalized_1**3 
					+ d31*composition_CO2_normalized_1**3*FDS_normalized_1**1 
					+ d22*composition_CO2_normalized_1**2*FDS_normalized_1**2
					+ d13*composition_CO2_normalized_1**1*FDS_normalized_1**3 
					+ d04*composition_CO2_normalized_1**0*FDS_normalized_1**4)

					density2 = (d00*composition_CO2_normalized_2**0*FDS_normalized_2**0 
					+ d10*composition_CO2_normalized_2**1*FDS_normalized_2**0 
					+ d01*composition_CO2_normalized_2**0*FDS_normalized_2**1 
					+ d20*composition_CO2_normalized_2**2*FDS_normalized_2**0
					+ d11*composition_CO2_normalized_2**1*FDS_normalized_2**1 
					+ d02*composition_CO2_normalized_2**0*FDS_normalized_2**2
					+ d30*composition_CO2_normalized_2**3*FDS_normalized_2**0 
					+ d21*composition_CO2_normalized_2**2*FDS_normalized_2**1
					+ d12*composition_CO2_normalized_2**1*FDS_normalized_2**2 
					+ d03*composition_CO2_normalized_2**0*FDS_normalized_2**3 
					+ d31*composition_CO2_normalized_2**3*FDS_normalized_2**1 
					+ d22*composition_CO2_normalized_2**2*FDS_normalized_2**2
					+ d13*composition_CO2_normalized_2**1*FDS_normalized_2**3 
					+ d04*composition_CO2_normalized_2**0*FDS_normalized_2**4)

					density3 = (d00*composition_CO2_normalized_1**0*FDS_normalized_2**0 
					+ d10*composition_CO2_normalized_1**1*FDS_normalized_2**0 
					+ d01*composition_CO2_normalized_1**0*FDS_normalized_2**1 
					+ d20*composition_CO2_normalized_1**2*FDS_normalized_2**0
					+ d11*composition_CO2_normalized_1**1*FDS_normalized_2**1 
					+ d02*composition_CO2_normalized_1**0*FDS_normalized_2**2 
					+ d30*composition_CO2_normalized_1**3*FDS_normalized_2**0 
					+ d21*composition_CO2_normalized_1**2*FDS_normalized_2**1
					+ d12*composition_CO2_normalized_1**1*FDS_normalized_2**2 
					+ d03*composition_CO2_normalized_1**0*FDS_normalized_2**3 
					+ d31*composition_CO2_normalized_1**3*FDS_normalized_2**1 
					+ d22*composition_CO2_normalized_1**2*FDS_normalized_2**2
					+ d13*composition_CO2_normalized_1**1*FDS_normalized_2**3 
					+ d04*composition_CO2_normalized_1**0*FDS_normalized_2**4)

					density4 = (d00*composition_CO2_normalized_2**0*FDS_normalized_1**0 
					+ d10*composition_CO2_normalized_2**1*FDS_normalized_1**0 
					+ d01*composition_CO2_normalized_2**0*FDS_normalized_1**1 
					+ d20*composition_CO2_normalized_2**2*FDS_normalized_1**0
					+ d11*composition_CO2_normalized_2**1*FDS_normalized_1**1 
					+ d02*composition_CO2_normalized_2**0*FDS_normalized_1**2 
					+ d30*composition_CO2_normalized_2**3*FDS_normalized_1**0 
					+ d21*composition_CO2_normalized_2**2*FDS_normalized_1**1
					+ d12*composition_CO2_normalized_2**1*FDS_normalized_1**2 
					+ d03*composition_CO2_normalized_2**0*FDS_normalized_1**3 
					+ d31*composition_CO2_normalized_2**3*FDS_normalized_1**1 
					+ d22*composition_CO2_normalized_2**2*FDS_normalized_1**2
					+ d13*composition_CO2_normalized_2**1*FDS_normalized_1**3 
					+ d04*composition_CO2_normalized_2**0*FDS_normalized_1**4)              

					pressure_final = (max(pressure1, pressure2, pressure3, pressure4) + min(pressure1, pressure2, pressure3, pressure4))/2 #pressure max - pressure min
					uncer_pressure_final = 2.12 + (max(pressure1, pressure2, pressure3, pressure4) - min(pressure1, pressure2, pressure3, pressure4))/(2*np.sqrt(3))

					density_final = (max(density1, density2, density3, density4) + min(density1, density2, density3, density4))/2 #density max - density min
					uncer_density_final = 0.002 + (max(density1, density2, density3, density4) - min(density1, density2, density3, density4))/(2*np.sqrt(3))

					molarvolume1 = 1/(max(density1, density2, density3, density4)/(44*composition_CO2 + 28*composition_N2))
					molarvolume2 = 1/(min(density1, density2, density3, density4)/(44*composition_CO2 + 28*composition_N2))
				
					molarvolume_final = (molarvolume1 + molarvolume2 )/ 2
					uncer_molarvolume_final = (molarvolume2 - molarvolume1) / (2*np.sqrt(3))

				print('pressure1', pressure1)
				print('pressure2', pressure2)
				print('pressure3', pressure3)
				print('pressure4', pressure4)

				print('density 1=', density1)
				print('density 2=', density2)
				print('density 3=', density3)
				print('density 4=', density4)

				print("molarvolume1", molarvolume1)
				print("molarvolume2", molarvolume2)

				if pressure_final > 650 or pressure1 >650 or pressure2 >650 or pressure_final < -20 or pressure1 <-20 or pressure2 <-20 or density2<0 or density1 <0 or density3<0 or density4<0 or density_final <0:
					popupmsg_OCR()
			

			if temperature.get() == 22 and composition_CO2 < 0.5 and instrument.get() ==1: 

				## Calibration equation's coeff of CO2-N2 at 22 °C over 5-500 bars


				# normalisation of concentration and of Fermi diad splitting
				composition_CO2_normalized_1 = (composition_CO2 + 0.005 - 0.3)/0.14207
				composition_CO2_normalized_2 = (composition_CO2 - 0.005 - 0.3)/0.14207
				FDS_normalized_1 = (FDS + unc_FDS - 103.08)/0.28273
				FDS_normalized_2 = (FDS - unc_FDS - 103.08)/0.28273
				
				p00= 170.1797482
				p10= -77.91652847
				p01= 157.7783087
				p20= 48.92637063
				p11= -117.851987
				p02= 37.8190835
				p30= -19.71210412
				p21= 73.33809699
				p12= -65.0383275
				p03= 26.66123598
				p31= -19.51088658
				p22= 26.97497354
				p13= -14.74772823
				p04= 1.319488384

				d00= 0.263683349
				d10= -0.077937841
				d01= 0.235224651
				d20= 0.021982476
				d11= -0.053772169
				d02= 9.08244E-05
				d30=-0.001022048
				d21= 0.009510245
				d12= 0.02069519
				d03= -0.006329513
				d31= 0.002925762
				d22= -0.010441952
				d13= 0.001629727
				d04= 0.0000253044

				#### pressure calculation
				pressure1 = (p00*composition_CO2_normalized_1**0*FDS_normalized_1**0 
				+ p10*composition_CO2_normalized_1**1*FDS_normalized_1**0 
				+ p01*composition_CO2_normalized_1**0*FDS_normalized_1**1 
				+ p20*composition_CO2_normalized_1**2*FDS_normalized_1**0 
				+ p11*composition_CO2_normalized_1**1*FDS_normalized_1**1 
				+ p02*composition_CO2_normalized_1**0*FDS_normalized_1**2 
				+ p30*composition_CO2_normalized_1**3*FDS_normalized_1**0 
				+ p21*composition_CO2_normalized_1**2*FDS_normalized_1**1
				+ p12*composition_CO2_normalized_1**1*FDS_normalized_1**2 
				+ p03*composition_CO2_normalized_1**0*FDS_normalized_1**3 
				+ p31*composition_CO2_normalized_1**3*FDS_normalized_1**1 
				+ p22*composition_CO2_normalized_1**2*FDS_normalized_1**2
				+ p13*composition_CO2_normalized_1**1*FDS_normalized_1**3 
				+ p04*composition_CO2_normalized_1**0*FDS_normalized_1**4)

				pressure2 = (p00*composition_CO2_normalized_2**0*FDS_normalized_2**0 
				+ p10*composition_CO2_normalized_2**1*FDS_normalized_2**0 
				+ p01*composition_CO2_normalized_2**0*FDS_normalized_2**1 
				+ p20*composition_CO2_normalized_2**2*FDS_normalized_2**0
				+ p11*composition_CO2_normalized_2**1*FDS_normalized_2**1 
				+ p02*composition_CO2_normalized_2**0*FDS_normalized_2**2
				+ p30*composition_CO2_normalized_2**3*FDS_normalized_2**0 
				+ p21*composition_CO2_normalized_2**2*FDS_normalized_2**1
				+ p12*composition_CO2_normalized_2**1*FDS_normalized_2**2 
				+ p03*composition_CO2_normalized_2**0*FDS_normalized_2**3 
				+ p31*composition_CO2_normalized_2**3*FDS_normalized_2**1 
				+ p22*composition_CO2_normalized_2**2*FDS_normalized_2**2
				+ p13*composition_CO2_normalized_2**1*FDS_normalized_2**3 
				+ p04*composition_CO2_normalized_2**0*FDS_normalized_2**4)

				pressure3 = (p00*composition_CO2_normalized_1**0*FDS_normalized_2**0 
				+ p10*composition_CO2_normalized_1**1*FDS_normalized_2**0 
				+ p01*composition_CO2_normalized_1**0*FDS_normalized_2**1 
				+ p20*composition_CO2_normalized_1**2*FDS_normalized_2**0
				+ p11*composition_CO2_normalized_1**1*FDS_normalized_2**1 
				+ p02*composition_CO2_normalized_1**0*FDS_normalized_2**2 
				+ p30*composition_CO2_normalized_1**3*FDS_normalized_2**0 
				+ p21*composition_CO2_normalized_1**2*FDS_normalized_2**1
				+ p12*composition_CO2_normalized_1**1*FDS_normalized_2**2 
				+ p03*composition_CO2_normalized_1**0*FDS_normalized_2**3 
				+ p31*composition_CO2_normalized_1**3*FDS_normalized_2**1 
				+ p22*composition_CO2_normalized_1**2*FDS_normalized_2**2
				+ p13*composition_CO2_normalized_1**1*FDS_normalized_2**3 
				+ p04*composition_CO2_normalized_1**0*FDS_normalized_2**4)

				pressure4 = (p00*composition_CO2_normalized_2**0*FDS_normalized_1**0 
				+ p10*composition_CO2_normalized_2**1*FDS_normalized_1**0 
				+ p01*composition_CO2_normalized_2**0*FDS_normalized_1**1 
				+ p20*composition_CO2_normalized_2**2*FDS_normalized_1**0
				+ p11*composition_CO2_normalized_2**1*FDS_normalized_1**1 
				+ p02*composition_CO2_normalized_2**0*FDS_normalized_1**2 
				+ p30*composition_CO2_normalized_2**3*FDS_normalized_1**0 
				+ p21*composition_CO2_normalized_2**2*FDS_normalized_1**1
				+ p12*composition_CO2_normalized_2**1*FDS_normalized_1**2 
				+ p03*composition_CO2_normalized_2**0*FDS_normalized_1**3 
				+ p31*composition_CO2_normalized_2**3*FDS_normalized_1**1 
				+ p22*composition_CO2_normalized_2**2*FDS_normalized_1**2
				+ p13*composition_CO2_normalized_2**1*FDS_normalized_1**3 
				+ p04*composition_CO2_normalized_2**0*FDS_normalized_1**4)

				########################
				#### density calculation

				density1 = (d00*composition_CO2_normalized_1**0*FDS_normalized_1**0 
				+ d10*composition_CO2_normalized_1**1*FDS_normalized_1**0 
				+ d01*composition_CO2_normalized_1**0*FDS_normalized_1**1 
				+ d20*composition_CO2_normalized_1**2*FDS_normalized_1**0 
				+ d11*composition_CO2_normalized_1**1*FDS_normalized_1**1 
				+ d02*composition_CO2_normalized_1**0*FDS_normalized_1**2 
				+ d30*composition_CO2_normalized_1**3*FDS_normalized_1**0 
				+ d21*composition_CO2_normalized_1**2*FDS_normalized_1**1
				+ d12*composition_CO2_normalized_1**1*FDS_normalized_1**2 
				+ d03*composition_CO2_normalized_1**0*FDS_normalized_1**3 
				+ d31*composition_CO2_normalized_1**3*FDS_normalized_1**1 
				+ d22*composition_CO2_normalized_1**2*FDS_normalized_1**2
				+ d13*composition_CO2_normalized_1**1*FDS_normalized_1**3 
				+ d04*composition_CO2_normalized_1**0*FDS_normalized_1**4)

				density2 = (d00*composition_CO2_normalized_2**0*FDS_normalized_2**0 
				+ d10*composition_CO2_normalized_2**1*FDS_normalized_2**0 
				+ d01*composition_CO2_normalized_2**0*FDS_normalized_2**1 
				+ d20*composition_CO2_normalized_2**2*FDS_normalized_2**0
				+ d11*composition_CO2_normalized_2**1*FDS_normalized_2**1 
				+ d02*composition_CO2_normalized_2**0*FDS_normalized_2**2
				+ d30*composition_CO2_normalized_2**3*FDS_normalized_2**0 
				+ d21*composition_CO2_normalized_2**2*FDS_normalized_2**1
				+ d12*composition_CO2_normalized_2**1*FDS_normalized_2**2 
				+ d03*composition_CO2_normalized_2**0*FDS_normalized_2**3 
				+ d31*composition_CO2_normalized_2**3*FDS_normalized_2**1 
				+ d22*composition_CO2_normalized_2**2*FDS_normalized_2**2
				+ d13*composition_CO2_normalized_2**1*FDS_normalized_2**3 
				+ d04*composition_CO2_normalized_2**0*FDS_normalized_2**4)

				density3 = (d00*composition_CO2_normalized_1**0*FDS_normalized_2**0 
				+ d10*composition_CO2_normalized_1**1*FDS_normalized_2**0 
				+ d01*composition_CO2_normalized_1**0*FDS_normalized_2**1 
				+ d20*composition_CO2_normalized_1**2*FDS_normalized_2**0
				+ d11*composition_CO2_normalized_1**1*FDS_normalized_2**1 
				+ d02*composition_CO2_normalized_1**0*FDS_normalized_2**2 
				+ d30*composition_CO2_normalized_1**3*FDS_normalized_2**0 
				+ d21*composition_CO2_normalized_1**2*FDS_normalized_2**1
				+ d12*composition_CO2_normalized_1**1*FDS_normalized_2**2 
				+ d03*composition_CO2_normalized_1**0*FDS_normalized_2**3 
				+ d31*composition_CO2_normalized_1**3*FDS_normalized_2**1 
				+ d22*composition_CO2_normalized_1**2*FDS_normalized_2**2
				+ d13*composition_CO2_normalized_1**1*FDS_normalized_2**3 
				+ d04*composition_CO2_normalized_1**0*FDS_normalized_2**4)

				density4 = (d00*composition_CO2_normalized_2**0*FDS_normalized_1**0 
				+ d10*composition_CO2_normalized_2**1*FDS_normalized_1**0 
				+ d01*composition_CO2_normalized_2**0*FDS_normalized_1**1 
				+ d20*composition_CO2_normalized_2**2*FDS_normalized_1**0
				+ d11*composition_CO2_normalized_2**1*FDS_normalized_1**1 
				+ d02*composition_CO2_normalized_2**0*FDS_normalized_1**2 
				+ d30*composition_CO2_normalized_2**3*FDS_normalized_1**0 
				+ d21*composition_CO2_normalized_2**2*FDS_normalized_1**1
				+ d12*composition_CO2_normalized_2**1*FDS_normalized_1**2 
				+ d03*composition_CO2_normalized_2**0*FDS_normalized_1**3 
				+ d31*composition_CO2_normalized_2**3*FDS_normalized_1**1 
				+ d22*composition_CO2_normalized_2**2*FDS_normalized_1**2
				+ d13*composition_CO2_normalized_2**1*FDS_normalized_1**3 
				+ d04*composition_CO2_normalized_2**0*FDS_normalized_1**4)              

				pressure_final = (max(pressure1, pressure2, pressure3, pressure4) + min(pressure1, pressure2, pressure3, pressure4))/2 #pressure max - pressure min
				uncer_pressure_final = 7.1 + (max(pressure1, pressure2, pressure3, pressure4) - min(pressure1, pressure2, pressure3, pressure4))/(2*np.sqrt(3))

				density_final = (max(density1, density2, density3, density4) + min(density1, density2, density3, density4))/2 #density max - density min
				uncer_density_final = 0.005 + (max(density1, density2, density3, density4) - min(density1, density2, density3, density4))/(2*np.sqrt(3))

				molarvolume1 = 1/(max(density1, density2, density3, density4)/(44*composition_CO2 + 28*composition_N2))
				molarvolume2 = 1/(min(density1, density2, density3, density4)/(44*composition_CO2 + 28*composition_N2))
				
				molarvolume_final = (molarvolume1 + molarvolume2) / 2
				uncer_molarvolume_final = (molarvolume2 - molarvolume1) / (2*np.sqrt(3))


				##### verify if measured pressure < 160 bar, if it is, re-recalculte using calibration data for 5-160 bar range.
				if pressure_final <= 150: 

					## Calibration equation's coeff of CO2-N2 at 22 °C over 5-160 bars
					# normalisation of concentration and of Fermi diad splitting
					
					composition_CO2_normalized_1 = (composition_CO2 + 0.005 - 0.30339)/0.14138
					composition_CO2_normalized_2 = (composition_CO2 - 0.005 - 0.30339)/0.14138
					FDS_normalized_1 = (FDS + unc_FDS - 102.88)/0.10219
					FDS_normalized_2 = (FDS - unc_FDS - 102.88)/0.10219
										
					p00= 70.4346
					p10= -26.55884
					p01= 49.81154
					p20= 11.3654
					p11= -23.07226
					p02= -2.14405
					p30= -4.37936
					p21= 12.94687
					p12= -2.63117
					p03= 2.28548
					p31= -3.46204
					p22= 2.30673
					p13= -1.50217
					p04= -0.01577

					d00= 0.102872156
					d10= -0.02999631
					d01= 0.078010885
					d20= 0.010556929
					d11= -0.024748763
					d02= -0.000407494
					d30= -0.003873141
					d21= 0.012345104
					d12= -0.001058896
					d03= 0.002185839
					d31= -0.002665506
					d22= 0.002099481
					d13= -0.001615525
					d04= -0.0000273713

					#### pressure calculation
					pressure1 = (p00*composition_CO2_normalized_1**0*FDS_normalized_1**0 
					+ p10*composition_CO2_normalized_1**1*FDS_normalized_1**0 
					+ p01*composition_CO2_normalized_1**0*FDS_normalized_1**1 
					+ p20*composition_CO2_normalized_1**2*FDS_normalized_1**0 
					+ p11*composition_CO2_normalized_1**1*FDS_normalized_1**1 
					+ p02*composition_CO2_normalized_1**0*FDS_normalized_1**2 
					+ p30*composition_CO2_normalized_1**3*FDS_normalized_1**0 
					+ p21*composition_CO2_normalized_1**2*FDS_normalized_1**1
					+ p12*composition_CO2_normalized_1**1*FDS_normalized_1**2 
					+ p03*composition_CO2_normalized_1**0*FDS_normalized_1**3 
					+ p31*composition_CO2_normalized_1**3*FDS_normalized_1**1 
					+ p22*composition_CO2_normalized_1**2*FDS_normalized_1**2
					+ p13*composition_CO2_normalized_1**1*FDS_normalized_1**3 
					+ p04*composition_CO2_normalized_1**0*FDS_normalized_1**4)

					pressure2 = (p00*composition_CO2_normalized_2**0*FDS_normalized_2**0 
					+ p10*composition_CO2_normalized_2**1*FDS_normalized_2**0 
					+ p01*composition_CO2_normalized_2**0*FDS_normalized_2**1 
					+ p20*composition_CO2_normalized_2**2*FDS_normalized_2**0
					+ p11*composition_CO2_normalized_2**1*FDS_normalized_2**1 
					+ p02*composition_CO2_normalized_2**0*FDS_normalized_2**2
					+ p30*composition_CO2_normalized_2**3*FDS_normalized_2**0 
					+ p21*composition_CO2_normalized_2**2*FDS_normalized_2**1
					+ p12*composition_CO2_normalized_2**1*FDS_normalized_2**2 
					+ p03*composition_CO2_normalized_2**0*FDS_normalized_2**3 
					+ p31*composition_CO2_normalized_2**3*FDS_normalized_2**1 
					+ p22*composition_CO2_normalized_2**2*FDS_normalized_2**2
					+ p13*composition_CO2_normalized_2**1*FDS_normalized_2**3 
					+ p04*composition_CO2_normalized_2**0*FDS_normalized_2**4)

					pressure3 = (p00*composition_CO2_normalized_1**0*FDS_normalized_2**0 
					+ p10*composition_CO2_normalized_1**1*FDS_normalized_2**0 
					+ p01*composition_CO2_normalized_1**0*FDS_normalized_2**1 
					+ p20*composition_CO2_normalized_1**2*FDS_normalized_2**0
					+ p11*composition_CO2_normalized_1**1*FDS_normalized_2**1 
					+ p02*composition_CO2_normalized_1**0*FDS_normalized_2**2 
					+ p30*composition_CO2_normalized_1**3*FDS_normalized_2**0 
					+ p21*composition_CO2_normalized_1**2*FDS_normalized_2**1
					+ p12*composition_CO2_normalized_1**1*FDS_normalized_2**2 
					+ p03*composition_CO2_normalized_1**0*FDS_normalized_2**3 
					+ p31*composition_CO2_normalized_1**3*FDS_normalized_2**1 
					+ p22*composition_CO2_normalized_1**2*FDS_normalized_2**2
					+ p13*composition_CO2_normalized_1**1*FDS_normalized_2**3 
					+ p04*composition_CO2_normalized_1**0*FDS_normalized_2**4)

					pressure4 = (p00*composition_CO2_normalized_2**0*FDS_normalized_1**0 
					+ p10*composition_CO2_normalized_2**1*FDS_normalized_1**0 
					+ p01*composition_CO2_normalized_2**0*FDS_normalized_1**1 
					+ p20*composition_CO2_normalized_2**2*FDS_normalized_1**0
					+ p11*composition_CO2_normalized_2**1*FDS_normalized_1**1 
					+ p02*composition_CO2_normalized_2**0*FDS_normalized_1**2 
					+ p30*composition_CO2_normalized_2**3*FDS_normalized_1**0 
					+ p21*composition_CO2_normalized_2**2*FDS_normalized_1**1
					+ p12*composition_CO2_normalized_2**1*FDS_normalized_1**2 
					+ p03*composition_CO2_normalized_2**0*FDS_normalized_1**3 
					+ p31*composition_CO2_normalized_2**3*FDS_normalized_1**1 
					+ p22*composition_CO2_normalized_2**2*FDS_normalized_1**2
					+ p13*composition_CO2_normalized_2**1*FDS_normalized_1**3 
					+ p04*composition_CO2_normalized_2**0*FDS_normalized_1**4)

					########################
					#### density calculation

					density1 = (d00*composition_CO2_normalized_1**0*FDS_normalized_1**0 
					+ d10*composition_CO2_normalized_1**1*FDS_normalized_1**0 
					+ d01*composition_CO2_normalized_1**0*FDS_normalized_1**1 
					+ d20*composition_CO2_normalized_1**2*FDS_normalized_1**0 
					+ d11*composition_CO2_normalized_1**1*FDS_normalized_1**1 
					+ d02*composition_CO2_normalized_1**0*FDS_normalized_1**2 
					+ d30*composition_CO2_normalized_1**3*FDS_normalized_1**0 
					+ d21*composition_CO2_normalized_1**2*FDS_normalized_1**1
					+ d12*composition_CO2_normalized_1**1*FDS_normalized_1**2 
					+ d03*composition_CO2_normalized_1**0*FDS_normalized_1**3 
					+ d31*composition_CO2_normalized_1**3*FDS_normalized_1**1 
					+ d22*composition_CO2_normalized_1**2*FDS_normalized_1**2
					+ d13*composition_CO2_normalized_1**1*FDS_normalized_1**3 
					+ d04*composition_CO2_normalized_1**0*FDS_normalized_1**4)

					density2 = (d00*composition_CO2_normalized_2**0*FDS_normalized_2**0 
					+ d10*composition_CO2_normalized_2**1*FDS_normalized_2**0 
					+ d01*composition_CO2_normalized_2**0*FDS_normalized_2**1 
					+ d20*composition_CO2_normalized_2**2*FDS_normalized_2**0
					+ d11*composition_CO2_normalized_2**1*FDS_normalized_2**1 
					+ d02*composition_CO2_normalized_2**0*FDS_normalized_2**2
					+ d30*composition_CO2_normalized_2**3*FDS_normalized_2**0 
					+ d21*composition_CO2_normalized_2**2*FDS_normalized_2**1
					+ d12*composition_CO2_normalized_2**1*FDS_normalized_2**2 
					+ d03*composition_CO2_normalized_2**0*FDS_normalized_2**3 
					+ d31*composition_CO2_normalized_2**3*FDS_normalized_2**1 
					+ d22*composition_CO2_normalized_2**2*FDS_normalized_2**2
					+ d13*composition_CO2_normalized_2**1*FDS_normalized_2**3 
					+ d04*composition_CO2_normalized_2**0*FDS_normalized_2**4)

					density3 = (d00*composition_CO2_normalized_1**0*FDS_normalized_2**0 
					+ d10*composition_CO2_normalized_1**1*FDS_normalized_2**0 
					+ d01*composition_CO2_normalized_1**0*FDS_normalized_2**1 
					+ d20*composition_CO2_normalized_1**2*FDS_normalized_2**0
					+ d11*composition_CO2_normalized_1**1*FDS_normalized_2**1 
					+ d02*composition_CO2_normalized_1**0*FDS_normalized_2**2 
					+ d30*composition_CO2_normalized_1**3*FDS_normalized_2**0 
					+ d21*composition_CO2_normalized_1**2*FDS_normalized_2**1
					+ d12*composition_CO2_normalized_1**1*FDS_normalized_2**2 
					+ d03*composition_CO2_normalized_1**0*FDS_normalized_2**3 
					+ d31*composition_CO2_normalized_1**3*FDS_normalized_2**1 
					+ d22*composition_CO2_normalized_1**2*FDS_normalized_2**2
					+ d13*composition_CO2_normalized_1**1*FDS_normalized_2**3 
					+ d04*composition_CO2_normalized_1**0*FDS_normalized_2**4)

					density4 = (d00*composition_CO2_normalized_2**0*FDS_normalized_1**0 
					+ d10*composition_CO2_normalized_2**1*FDS_normalized_1**0 
					+ d01*composition_CO2_normalized_2**0*FDS_normalized_1**1 
					+ d20*composition_CO2_normalized_2**2*FDS_normalized_1**0
					+ d11*composition_CO2_normalized_2**1*FDS_normalized_1**1 
					+ d02*composition_CO2_normalized_2**0*FDS_normalized_1**2 
					+ d30*composition_CO2_normalized_2**3*FDS_normalized_1**0 
					+ d21*composition_CO2_normalized_2**2*FDS_normalized_1**1
					+ d12*composition_CO2_normalized_2**1*FDS_normalized_1**2 
					+ d03*composition_CO2_normalized_2**0*FDS_normalized_1**3 
					+ d31*composition_CO2_normalized_2**3*FDS_normalized_1**1 
					+ d22*composition_CO2_normalized_2**2*FDS_normalized_1**2
					+ d13*composition_CO2_normalized_2**1*FDS_normalized_1**3 
					+ d04*composition_CO2_normalized_2**0*FDS_normalized_1**4)              

					pressure_final = (max(pressure1, pressure2, pressure3, pressure4) + min(pressure1, pressure2, pressure3, pressure4))/2 #pressure max - pressure min
					uncer_pressure_final = 2.83 + (max(pressure1, pressure2, pressure3, pressure4) - min(pressure1, pressure2, pressure3, pressure4))/(2*np.sqrt(3)) #uncertain 4

					density_final = (max(density1, density2, density3, density4) + min(density1, density2, density3, density4))/2 #density max - density min
					uncer_density_final = 0.0035 + (max(density1, density2, density3, density4) - min(density1, density2, density3, density4))/(2*np.sqrt(3)) #uncertainty 0.005

					molarvolume1 = 1/(max(density1, density2, density3, density4)/(44*composition_CO2 + 28*composition_N2))
					molarvolume2 = 1/(min(density1, density2, density3, density4)/(44*composition_CO2 + 28*composition_N2))		
					molarvolume_final = (molarvolume1 + molarvolume2) / 2
					uncer_molarvolume_final = (molarvolume2 - molarvolume1) / (2*np.sqrt(3))
				print('composition normalized', composition_CO2_normalized_1)

				print('pressure1', pressure1)
				print('pressure2', pressure2)
				print('pressure3', pressure3)
				print('pressure4', pressure4)

				print('density 1=', density1)
				print('density 2=', density2)
				print('density 3=', density3)
				print('density 4=', density4)
				
				print("molarvolume1", molarvolume1)
				print("molarvolume2", molarvolume2)
				if pressure_final > 650 or pressure1 >650 or pressure2 >650 or pressure_final < -20 or pressure1 <-20 or pressure2 <-20 or density2<0 or density1 <0 or density3<0 or density4<0 or density_final<0 :
					popupmsg_OCR()


			## Calibration equation's coeff of CO2-N2 at 32 °C over 5-500 bars
			if temperature.get() == 32 and composition_CO2 >= 0.5 and instrument.get() ==1: 

				
				# normalisation of concentration and of Fermi diad splitting
				composition_CO2_normalized_1 = (composition_CO2 + 0.005 - 0.79427 )/0.17942
				composition_CO2_normalized_2 = (composition_CO2 - 0.005 - 0.79427 )/0.17942
				FDS_normalized_1 = (FDS + unc_FDS - 103.74)/0.72596
				FDS_normalized_2 = (FDS - unc_FDS - 103.74)/0.72596
				

				
				p00= 134.8531425
				p10= -62.13942807
				p01= 95.32309211
				p20= 37.55699011
				p11= -144.1206532
				p02= 87.60480426
				p30= -27.52349216
				p21= 74.61281782
				p12= -131.2875059
				p03= 81.04989487
				p31= -23.38347901
				p22= 38.11772739
				p13= -40.14928604
				p04= 9.504943027

				d00= 0.468548895
				d10= -0.051703845
				d01= 0.385401403
				d20= 0.008264594
				d11= -0.022559707
				d02= -0.009187601
				d30= -0.013416864
				d21= -0.003756692
				d12= 0.024487064
				d03= -0.029123696
				d31= -0.008426964
				d22= -0.007617716
				d13= 0.008890962
				d04= 0.001795057


				#### pressure calculation
				pressure1 = (p00*composition_CO2_normalized_1**0*FDS_normalized_1**0 
				+ p10*composition_CO2_normalized_1**1*FDS_normalized_1**0 
				+ p01*composition_CO2_normalized_1**0*FDS_normalized_1**1 
				+ p20*composition_CO2_normalized_1**2*FDS_normalized_1**0 
				+ p11*composition_CO2_normalized_1**1*FDS_normalized_1**1 
				+ p02*composition_CO2_normalized_1**0*FDS_normalized_1**2 
				+ p30*composition_CO2_normalized_1**3*FDS_normalized_1**0 
				+ p21*composition_CO2_normalized_1**2*FDS_normalized_1**1
				+ p12*composition_CO2_normalized_1**1*FDS_normalized_1**2 
				+ p03*composition_CO2_normalized_1**0*FDS_normalized_1**3 
				+ p31*composition_CO2_normalized_1**3*FDS_normalized_1**1 
				+ p22*composition_CO2_normalized_1**2*FDS_normalized_1**2
				+ p13*composition_CO2_normalized_1**1*FDS_normalized_1**3 
				+ p04*composition_CO2_normalized_1**0*FDS_normalized_1**4)

				pressure2 = (p00*composition_CO2_normalized_2**0*FDS_normalized_2**0 
				+ p10*composition_CO2_normalized_2**1*FDS_normalized_2**0 
				+ p01*composition_CO2_normalized_2**0*FDS_normalized_2**1 
				+ p20*composition_CO2_normalized_2**2*FDS_normalized_2**0
				+ p11*composition_CO2_normalized_2**1*FDS_normalized_2**1 
				+ p02*composition_CO2_normalized_2**0*FDS_normalized_2**2
				+ p30*composition_CO2_normalized_2**3*FDS_normalized_2**0 
				+ p21*composition_CO2_normalized_2**2*FDS_normalized_2**1
				+ p12*composition_CO2_normalized_2**1*FDS_normalized_2**2 
				+ p03*composition_CO2_normalized_2**0*FDS_normalized_2**3 
				+ p31*composition_CO2_normalized_2**3*FDS_normalized_2**1 
				+ p22*composition_CO2_normalized_2**2*FDS_normalized_2**2
				+ p13*composition_CO2_normalized_2**1*FDS_normalized_2**3 
				+ p04*composition_CO2_normalized_2**0*FDS_normalized_2**4)

				pressure3 = (p00*composition_CO2_normalized_1**0*FDS_normalized_2**0 
				+ p10*composition_CO2_normalized_1**1*FDS_normalized_2**0 
				+ p01*composition_CO2_normalized_1**0*FDS_normalized_2**1 
				+ p20*composition_CO2_normalized_1**2*FDS_normalized_2**0
				+ p11*composition_CO2_normalized_1**1*FDS_normalized_2**1 
				+ p02*composition_CO2_normalized_1**0*FDS_normalized_2**2 
				+ p30*composition_CO2_normalized_1**3*FDS_normalized_2**0 
				+ p21*composition_CO2_normalized_1**2*FDS_normalized_2**1
				+ p12*composition_CO2_normalized_1**1*FDS_normalized_2**2 
				+ p03*composition_CO2_normalized_1**0*FDS_normalized_2**3 
				+ p31*composition_CO2_normalized_1**3*FDS_normalized_2**1 
				+ p22*composition_CO2_normalized_1**2*FDS_normalized_2**2
				+ p13*composition_CO2_normalized_1**1*FDS_normalized_2**3 
				+ p04*composition_CO2_normalized_1**0*FDS_normalized_2**4)

				pressure4 = (p00*composition_CO2_normalized_2**0*FDS_normalized_1**0 
				+ p10*composition_CO2_normalized_2**1*FDS_normalized_1**0 
				+ p01*composition_CO2_normalized_2**0*FDS_normalized_1**1 
				+ p20*composition_CO2_normalized_2**2*FDS_normalized_1**0
				+ p11*composition_CO2_normalized_2**1*FDS_normalized_1**1 
				+ p02*composition_CO2_normalized_2**0*FDS_normalized_1**2 
				+ p30*composition_CO2_normalized_2**3*FDS_normalized_1**0 
				+ p21*composition_CO2_normalized_2**2*FDS_normalized_1**1
				+ p12*composition_CO2_normalized_2**1*FDS_normalized_1**2 
				+ p03*composition_CO2_normalized_2**0*FDS_normalized_1**3 
				+ p31*composition_CO2_normalized_2**3*FDS_normalized_1**1 
				+ p22*composition_CO2_normalized_2**2*FDS_normalized_1**2
				+ p13*composition_CO2_normalized_2**1*FDS_normalized_1**3 
				+ p04*composition_CO2_normalized_2**0*FDS_normalized_1**4)

				########################
				#### density calculation

				density1 = (d00*composition_CO2_normalized_1**0*FDS_normalized_1**0 
				+ d10*composition_CO2_normalized_1**1*FDS_normalized_1**0 
				+ d01*composition_CO2_normalized_1**0*FDS_normalized_1**1 
				+ d20*composition_CO2_normalized_1**2*FDS_normalized_1**0 
				+ d11*composition_CO2_normalized_1**1*FDS_normalized_1**1 
				+ d02*composition_CO2_normalized_1**0*FDS_normalized_1**2 
				+ d30*composition_CO2_normalized_1**3*FDS_normalized_1**0 
				+ d21*composition_CO2_normalized_1**2*FDS_normalized_1**1
				+ d12*composition_CO2_normalized_1**1*FDS_normalized_1**2 
				+ d03*composition_CO2_normalized_1**0*FDS_normalized_1**3 
				+ d31*composition_CO2_normalized_1**3*FDS_normalized_1**1 
				+ d22*composition_CO2_normalized_1**2*FDS_normalized_1**2
				+ d13*composition_CO2_normalized_1**1*FDS_normalized_1**3 
				+ d04*composition_CO2_normalized_1**0*FDS_normalized_1**4)

				density2 = (d00*composition_CO2_normalized_2**0*FDS_normalized_2**0 
				+ d10*composition_CO2_normalized_2**1*FDS_normalized_2**0 
				+ d01*composition_CO2_normalized_2**0*FDS_normalized_2**1 
				+ d20*composition_CO2_normalized_2**2*FDS_normalized_2**0
				+ d11*composition_CO2_normalized_2**1*FDS_normalized_2**1 
				+ d02*composition_CO2_normalized_2**0*FDS_normalized_2**2
				+ d30*composition_CO2_normalized_2**3*FDS_normalized_2**0 
				+ d21*composition_CO2_normalized_2**2*FDS_normalized_2**1
				+ d12*composition_CO2_normalized_2**1*FDS_normalized_2**2 
				+ d03*composition_CO2_normalized_2**0*FDS_normalized_2**3 
				+ d31*composition_CO2_normalized_2**3*FDS_normalized_2**1 
				+ d22*composition_CO2_normalized_2**2*FDS_normalized_2**2
				+ d13*composition_CO2_normalized_2**1*FDS_normalized_2**3 
				+ d04*composition_CO2_normalized_2**0*FDS_normalized_2**4)

				density3 = (d00*composition_CO2_normalized_1**0*FDS_normalized_2**0 
				+ d10*composition_CO2_normalized_1**1*FDS_normalized_2**0 
				+ d01*composition_CO2_normalized_1**0*FDS_normalized_2**1 
				+ d20*composition_CO2_normalized_1**2*FDS_normalized_2**0
				+ d11*composition_CO2_normalized_1**1*FDS_normalized_2**1 
				+ d02*composition_CO2_normalized_1**0*FDS_normalized_2**2 
				+ d30*composition_CO2_normalized_1**3*FDS_normalized_2**0 
				+ d21*composition_CO2_normalized_1**2*FDS_normalized_2**1
				+ d12*composition_CO2_normalized_1**1*FDS_normalized_2**2 
				+ d03*composition_CO2_normalized_1**0*FDS_normalized_2**3 
				+ d31*composition_CO2_normalized_1**3*FDS_normalized_2**1 
				+ d22*composition_CO2_normalized_1**2*FDS_normalized_2**2
				+ d13*composition_CO2_normalized_1**1*FDS_normalized_2**3 
				+ d04*composition_CO2_normalized_1**0*FDS_normalized_2**4)

				density4 = (d00*composition_CO2_normalized_2**0*FDS_normalized_1**0 
				+ d10*composition_CO2_normalized_2**1*FDS_normalized_1**0 
				+ d01*composition_CO2_normalized_2**0*FDS_normalized_1**1 
				+ d20*composition_CO2_normalized_2**2*FDS_normalized_1**0
				+ d11*composition_CO2_normalized_2**1*FDS_normalized_1**1 
				+ d02*composition_CO2_normalized_2**0*FDS_normalized_1**2 
				+ d30*composition_CO2_normalized_2**3*FDS_normalized_1**0 
				+ d21*composition_CO2_normalized_2**2*FDS_normalized_1**1
				+ d12*composition_CO2_normalized_2**1*FDS_normalized_1**2 
				+ d03*composition_CO2_normalized_2**0*FDS_normalized_1**3 
				+ d31*composition_CO2_normalized_2**3*FDS_normalized_1**1 
				+ d22*composition_CO2_normalized_2**2*FDS_normalized_1**2
				+ d13*composition_CO2_normalized_2**1*FDS_normalized_1**3 
				+ d04*composition_CO2_normalized_2**0*FDS_normalized_1**4)              

				pressure_final = (max(pressure1, pressure2, pressure3, pressure4) + min(pressure1, pressure2, pressure3, pressure4))/2 #pressure max - pressure min
				uncer_pressure_final = 7.78 + (max(pressure1, pressure2, pressure3, pressure4) - min(pressure1, pressure2, pressure3, pressure4))/(2*np.sqrt(3))

				density_final = (max(density1, density2, density3, density4) + min(density1, density2, density3, density4))/2 #density max - density min
				uncer_density_final = 0.0057 + (max(density1, density2, density3, density4) - min(density1, density2, density3, density4))/(2*np.sqrt(3))

				molarvolume1 = 1/(max(density1, density2, density3, density4)/(44*composition_CO2 + 28*composition_N2))
				molarvolume2 = 1/(min(density1, density2, density3, density4)/(44*composition_CO2 + 28*composition_N2))		
				molarvolume_final = (molarvolume1 + molarvolume2 )/ 2
				uncer_molarvolume_final = (molarvolume2 - molarvolume1) / (2*np.sqrt(3))
				
				print('composition normalized', composition_CO2_normalized_1)


				##### verify if measured pressure < 160 bar, if it is, re-recalculte using calibration data for 5-160 bar range.
				if pressure_final <= 150: 

					## Calibration equation's coeff of CO2-N2 at 22 °C over 5-160 bars
					# normalisation of concentration and of Fermi diad splitting
					
					composition_CO2_normalized_1 = (composition_CO2 + 0.005 - 0.81495)/0.17944
					composition_CO2_normalized_2 = (composition_CO2 - 0.005 - 0.81495)/0.17944
					FDS_normalized_1 = (FDS + unc_FDS - 103.4)/0.6067
					FDS_normalized_2 = (FDS - unc_FDS - 103.4)/0.6067
										
					p00= 98.21110543
					p10= -31.34816997
					p01= 56.75173572
					p20= 10.95811653
					p11= -43.16424504
					p02= -11.6093266
					p30= -6.147600675
					p21= 18.06447122
					p12= -32.38414044
					p03= 24.72823226
					p31= -6.83208386
					p22= 9.44984861
					p13= -16.59404
					p04= 5.204939143

					d00= 0.285936962
					d10= -0.033443766
					d01= 0.307097935
					d20= 0.003508055
					d11= -0.019168559
					d02= 0.021840571
					d30= -0.00931312
					d21= -0.006126292
					d12= 0.010636527
					d03= -0.016469702
					d31= -0.011071135
					d22= -0.006032022
					d13= 0.001693598
					d04= 0.001601038

					#### pressure calculation
					pressure1 = (p00*composition_CO2_normalized_1**0*FDS_normalized_1**0 
					+ p10*composition_CO2_normalized_1**1*FDS_normalized_1**0 
					+ p01*composition_CO2_normalized_1**0*FDS_normalized_1**1 
					+ p20*composition_CO2_normalized_1**2*FDS_normalized_1**0 
					+ p11*composition_CO2_normalized_1**1*FDS_normalized_1**1 
					+ p02*composition_CO2_normalized_1**0*FDS_normalized_1**2 
					+ p30*composition_CO2_normalized_1**3*FDS_normalized_1**0 
					+ p21*composition_CO2_normalized_1**2*FDS_normalized_1**1
					+ p12*composition_CO2_normalized_1**1*FDS_normalized_1**2 
					+ p03*composition_CO2_normalized_1**0*FDS_normalized_1**3 
					+ p31*composition_CO2_normalized_1**3*FDS_normalized_1**1 
					+ p22*composition_CO2_normalized_1**2*FDS_normalized_1**2
					+ p13*composition_CO2_normalized_1**1*FDS_normalized_1**3 
					+ p04*composition_CO2_normalized_1**0*FDS_normalized_1**4)

					pressure2 = (p00*composition_CO2_normalized_2**0*FDS_normalized_2**0 
					+ p10*composition_CO2_normalized_2**1*FDS_normalized_2**0 
					+ p01*composition_CO2_normalized_2**0*FDS_normalized_2**1 
					+ p20*composition_CO2_normalized_2**2*FDS_normalized_2**0
					+ p11*composition_CO2_normalized_2**1*FDS_normalized_2**1 
					+ p02*composition_CO2_normalized_2**0*FDS_normalized_2**2
					+ p30*composition_CO2_normalized_2**3*FDS_normalized_2**0 
					+ p21*composition_CO2_normalized_2**2*FDS_normalized_2**1
					+ p12*composition_CO2_normalized_2**1*FDS_normalized_2**2 
					+ p03*composition_CO2_normalized_2**0*FDS_normalized_2**3 
					+ p31*composition_CO2_normalized_2**3*FDS_normalized_2**1 
					+ p22*composition_CO2_normalized_2**2*FDS_normalized_2**2
					+ p13*composition_CO2_normalized_2**1*FDS_normalized_2**3 
					+ p04*composition_CO2_normalized_2**0*FDS_normalized_2**4)

					pressure3 = (p00*composition_CO2_normalized_1**0*FDS_normalized_2**0 
					+ p10*composition_CO2_normalized_1**1*FDS_normalized_2**0 
					+ p01*composition_CO2_normalized_1**0*FDS_normalized_2**1 
					+ p20*composition_CO2_normalized_1**2*FDS_normalized_2**0
					+ p11*composition_CO2_normalized_1**1*FDS_normalized_2**1 
					+ p02*composition_CO2_normalized_1**0*FDS_normalized_2**2 
					+ p30*composition_CO2_normalized_1**3*FDS_normalized_2**0 
					+ p21*composition_CO2_normalized_1**2*FDS_normalized_2**1
					+ p12*composition_CO2_normalized_1**1*FDS_normalized_2**2 
					+ p03*composition_CO2_normalized_1**0*FDS_normalized_2**3 
					+ p31*composition_CO2_normalized_1**3*FDS_normalized_2**1 
					+ p22*composition_CO2_normalized_1**2*FDS_normalized_2**2
					+ p13*composition_CO2_normalized_1**1*FDS_normalized_2**3 
					+ p04*composition_CO2_normalized_1**0*FDS_normalized_2**4)

					pressure4 = (p00*composition_CO2_normalized_2**0*FDS_normalized_1**0 
					+ p10*composition_CO2_normalized_2**1*FDS_normalized_1**0 
					+ p01*composition_CO2_normalized_2**0*FDS_normalized_1**1 
					+ p20*composition_CO2_normalized_2**2*FDS_normalized_1**0
					+ p11*composition_CO2_normalized_2**1*FDS_normalized_1**1 
					+ p02*composition_CO2_normalized_2**0*FDS_normalized_1**2 
					+ p30*composition_CO2_normalized_2**3*FDS_normalized_1**0 
					+ p21*composition_CO2_normalized_2**2*FDS_normalized_1**1
					+ p12*composition_CO2_normalized_2**1*FDS_normalized_1**2 
					+ p03*composition_CO2_normalized_2**0*FDS_normalized_1**3 
					+ p31*composition_CO2_normalized_2**3*FDS_normalized_1**1 
					+ p22*composition_CO2_normalized_2**2*FDS_normalized_1**2
					+ p13*composition_CO2_normalized_2**1*FDS_normalized_1**3 
					+ p04*composition_CO2_normalized_2**0*FDS_normalized_1**4)

					########################
					#### density calculation

					density1 = (d00*composition_CO2_normalized_1**0*FDS_normalized_1**0 
					+ d10*composition_CO2_normalized_1**1*FDS_normalized_1**0 
					+ d01*composition_CO2_normalized_1**0*FDS_normalized_1**1 
					+ d20*composition_CO2_normalized_1**2*FDS_normalized_1**0 
					+ d11*composition_CO2_normalized_1**1*FDS_normalized_1**1 
					+ d02*composition_CO2_normalized_1**0*FDS_normalized_1**2 
					+ d30*composition_CO2_normalized_1**3*FDS_normalized_1**0 
					+ d21*composition_CO2_normalized_1**2*FDS_normalized_1**1
					+ d12*composition_CO2_normalized_1**1*FDS_normalized_1**2 
					+ d03*composition_CO2_normalized_1**0*FDS_normalized_1**3 
					+ d31*composition_CO2_normalized_1**3*FDS_normalized_1**1 
					+ d22*composition_CO2_normalized_1**2*FDS_normalized_1**2
					+ d13*composition_CO2_normalized_1**1*FDS_normalized_1**3 
					+ d04*composition_CO2_normalized_1**0*FDS_normalized_1**4)

					density2 = (d00*composition_CO2_normalized_2**0*FDS_normalized_2**0 
					+ d10*composition_CO2_normalized_2**1*FDS_normalized_2**0 
					+ d01*composition_CO2_normalized_2**0*FDS_normalized_2**1 
					+ d20*composition_CO2_normalized_2**2*FDS_normalized_2**0
					+ d11*composition_CO2_normalized_2**1*FDS_normalized_2**1 
					+ d02*composition_CO2_normalized_2**0*FDS_normalized_2**2
					+ d30*composition_CO2_normalized_2**3*FDS_normalized_2**0 
					+ d21*composition_CO2_normalized_2**2*FDS_normalized_2**1
					+ d12*composition_CO2_normalized_2**1*FDS_normalized_2**2 
					+ d03*composition_CO2_normalized_2**0*FDS_normalized_2**3 
					+ d31*composition_CO2_normalized_2**3*FDS_normalized_2**1 
					+ d22*composition_CO2_normalized_2**2*FDS_normalized_2**2
					+ d13*composition_CO2_normalized_2**1*FDS_normalized_2**3 
					+ d04*composition_CO2_normalized_2**0*FDS_normalized_2**4)

					density3 = (d00*composition_CO2_normalized_1**0*FDS_normalized_2**0 
					+ d10*composition_CO2_normalized_1**1*FDS_normalized_2**0 
					+ d01*composition_CO2_normalized_1**0*FDS_normalized_2**1 
					+ d20*composition_CO2_normalized_1**2*FDS_normalized_2**0
					+ d11*composition_CO2_normalized_1**1*FDS_normalized_2**1 
					+ d02*composition_CO2_normalized_1**0*FDS_normalized_2**2 
					+ d30*composition_CO2_normalized_1**3*FDS_normalized_2**0 
					+ d21*composition_CO2_normalized_1**2*FDS_normalized_2**1
					+ d12*composition_CO2_normalized_1**1*FDS_normalized_2**2 
					+ d03*composition_CO2_normalized_1**0*FDS_normalized_2**3 
					+ d31*composition_CO2_normalized_1**3*FDS_normalized_2**1 
					+ d22*composition_CO2_normalized_1**2*FDS_normalized_2**2
					+ d13*composition_CO2_normalized_1**1*FDS_normalized_2**3 
					+ d04*composition_CO2_normalized_1**0*FDS_normalized_2**4)

					density4 = (d00*composition_CO2_normalized_2**0*FDS_normalized_1**0 
					+ d10*composition_CO2_normalized_2**1*FDS_normalized_1**0 
					+ d01*composition_CO2_normalized_2**0*FDS_normalized_1**1 
					+ d20*composition_CO2_normalized_2**2*FDS_normalized_1**0
					+ d11*composition_CO2_normalized_2**1*FDS_normalized_1**1 
					+ d02*composition_CO2_normalized_2**0*FDS_normalized_1**2 
					+ d30*composition_CO2_normalized_2**3*FDS_normalized_1**0 
					+ d21*composition_CO2_normalized_2**2*FDS_normalized_1**1
					+ d12*composition_CO2_normalized_2**1*FDS_normalized_1**2 
					+ d03*composition_CO2_normalized_2**0*FDS_normalized_1**3 
					+ d31*composition_CO2_normalized_2**3*FDS_normalized_1**1 
					+ d22*composition_CO2_normalized_2**2*FDS_normalized_1**2
					+ d13*composition_CO2_normalized_2**1*FDS_normalized_1**3 
					+ d04*composition_CO2_normalized_2**0*FDS_normalized_1**4)              

					pressure_final = (max(pressure1, pressure2, pressure3, pressure4) + min(pressure1, pressure2, pressure3, pressure4))/2 #pressure max - pressure min
					uncer_pressure_final = 3 + (max(pressure1, pressure2, pressure3, pressure4) - min(pressure1, pressure2, pressure3, pressure4))/(2*np.sqrt(3)) #unce = 4

					density_final = (max(density1, density2, density3, density4) + min(density1, density2, density3, density4))/2 #density max - density min
					uncer_density_final = 0.0049 + (max(density1, density2, density3, density4) - min(density1, density2, density3, density4))/(2*np.sqrt(3)) #uncer= 0.007

					molarvolume1 = 1/(max(density1, density2, density3, density4)/(44*composition_CO2 + 28*composition_N2))
					molarvolume2 = 1/(min(density1, density2, density3, density4)/(44*composition_CO2 + 28*composition_N2))		
					molarvolume_final = (molarvolume1 + molarvolume2 )/ 2
					uncer_molarvolume_final = (molarvolume2 - molarvolume1) / (2*np.sqrt(3))

				print('pressure1', pressure1)
				print('pressure2', pressure2)
				print('pressure3', pressure3)
				print('pressure4', pressure4)

				print('density 1=', density1)
				print('density 2=', density2)
				print('density 3=', density3)
				print('density 4=', density4)

				print("molarvolume1", molarvolume1)
				print("molarvolume2", molarvolume2)
				
				
				if pressure_final > 650 or pressure1 >650 or pressure2 >650 or pressure_final < -20 or pressure1 <-20 or pressure2 <-20 or density2<0 or density1 <0 or density3<0 or density4<0 or density_final <0:
					popupmsg_OCR()	
			

			if temperature.get() == 32 and composition_CO2 < 0.5 and instrument.get() ==1: 

				## Calibration equation's coeff of CO2-N2 at 22 °C over 5-500 bars


				# normalisation of concentration and of Fermi diad splitting
				composition_CO2_normalized_1 = (composition_CO2 + 0.005 - 0.3)/0.14207
				composition_CO2_normalized_2 = (composition_CO2 - 0.005 - 0.3)/0.14207
				FDS_normalized_1 = (FDS + unc_FDS - 103.05)/0.26608
				FDS_normalized_2 = (FDS - unc_FDS - 103.05)/0.26608
				
				p00= 164.7455598
				p10= -72.94354971
				p01= 154.866058
				p20= 64.06681929
				p11= -115.9406874
				p02= 35.45935724
				p30= -30.25168791
				p21= 91.38437433
				p12= -60.58208945
				p03= 21.3175346
				p31= -32.48590355
				p22= 25.9500595
				p13= -10.27134275
				p04= 0.589452279


				d00= 0.245281521
				d10= -0.075498903
				d01= 0.220264697
				d20=0.032838431
				d11= -0.05963449
				d02= 0.001909669
				d30=-0.006300402
				d21= 0.02148613
				d12= 0.022501574
				d03= -0.005150028
				d31= -0.002762027
				d22= -0.012487804
				d13= 0.002949011
				d04= -0.000699892


				#### pressure calculation
				pressure1 = (p00*composition_CO2_normalized_1**0*FDS_normalized_1**0 
				+ p10*composition_CO2_normalized_1**1*FDS_normalized_1**0 
				+ p01*composition_CO2_normalized_1**0*FDS_normalized_1**1 
				+ p20*composition_CO2_normalized_1**2*FDS_normalized_1**0 
				+ p11*composition_CO2_normalized_1**1*FDS_normalized_1**1 
				+ p02*composition_CO2_normalized_1**0*FDS_normalized_1**2 
				+ p30*composition_CO2_normalized_1**3*FDS_normalized_1**0 
				+ p21*composition_CO2_normalized_1**2*FDS_normalized_1**1
				+ p12*composition_CO2_normalized_1**1*FDS_normalized_1**2 
				+ p03*composition_CO2_normalized_1**0*FDS_normalized_1**3 
				+ p31*composition_CO2_normalized_1**3*FDS_normalized_1**1 
				+ p22*composition_CO2_normalized_1**2*FDS_normalized_1**2
				+ p13*composition_CO2_normalized_1**1*FDS_normalized_1**3 
				+ p04*composition_CO2_normalized_1**0*FDS_normalized_1**4)

				pressure2 = (p00*composition_CO2_normalized_2**0*FDS_normalized_2**0 
				+ p10*composition_CO2_normalized_2**1*FDS_normalized_2**0 
				+ p01*composition_CO2_normalized_2**0*FDS_normalized_2**1 
				+ p20*composition_CO2_normalized_2**2*FDS_normalized_2**0
				+ p11*composition_CO2_normalized_2**1*FDS_normalized_2**1 
				+ p02*composition_CO2_normalized_2**0*FDS_normalized_2**2
				+ p30*composition_CO2_normalized_2**3*FDS_normalized_2**0 
				+ p21*composition_CO2_normalized_2**2*FDS_normalized_2**1
				+ p12*composition_CO2_normalized_2**1*FDS_normalized_2**2 
				+ p03*composition_CO2_normalized_2**0*FDS_normalized_2**3 
				+ p31*composition_CO2_normalized_2**3*FDS_normalized_2**1 
				+ p22*composition_CO2_normalized_2**2*FDS_normalized_2**2
				+ p13*composition_CO2_normalized_2**1*FDS_normalized_2**3 
				+ p04*composition_CO2_normalized_2**0*FDS_normalized_2**4)

				pressure3 = (p00*composition_CO2_normalized_1**0*FDS_normalized_2**0 
				+ p10*composition_CO2_normalized_1**1*FDS_normalized_2**0 
				+ p01*composition_CO2_normalized_1**0*FDS_normalized_2**1 
				+ p20*composition_CO2_normalized_1**2*FDS_normalized_2**0
				+ p11*composition_CO2_normalized_1**1*FDS_normalized_2**1 
				+ p02*composition_CO2_normalized_1**0*FDS_normalized_2**2 
				+ p30*composition_CO2_normalized_1**3*FDS_normalized_2**0 
				+ p21*composition_CO2_normalized_1**2*FDS_normalized_2**1
				+ p12*composition_CO2_normalized_1**1*FDS_normalized_2**2 
				+ p03*composition_CO2_normalized_1**0*FDS_normalized_2**3 
				+ p31*composition_CO2_normalized_1**3*FDS_normalized_2**1 
				+ p22*composition_CO2_normalized_1**2*FDS_normalized_2**2
				+ p13*composition_CO2_normalized_1**1*FDS_normalized_2**3 
				+ p04*composition_CO2_normalized_1**0*FDS_normalized_2**4)

				pressure4 = (p00*composition_CO2_normalized_2**0*FDS_normalized_1**0 
				+ p10*composition_CO2_normalized_2**1*FDS_normalized_1**0 
				+ p01*composition_CO2_normalized_2**0*FDS_normalized_1**1 
				+ p20*composition_CO2_normalized_2**2*FDS_normalized_1**0
				+ p11*composition_CO2_normalized_2**1*FDS_normalized_1**1 
				+ p02*composition_CO2_normalized_2**0*FDS_normalized_1**2 
				+ p30*composition_CO2_normalized_2**3*FDS_normalized_1**0 
				+ p21*composition_CO2_normalized_2**2*FDS_normalized_1**1
				+ p12*composition_CO2_normalized_2**1*FDS_normalized_1**2 
				+ p03*composition_CO2_normalized_2**0*FDS_normalized_1**3 
				+ p31*composition_CO2_normalized_2**3*FDS_normalized_1**1 
				+ p22*composition_CO2_normalized_2**2*FDS_normalized_1**2
				+ p13*composition_CO2_normalized_2**1*FDS_normalized_1**3 
				+ p04*composition_CO2_normalized_2**0*FDS_normalized_1**4)

				########################
				#### density calculation

				density1 = (d00*composition_CO2_normalized_1**0*FDS_normalized_1**0 
				+ d10*composition_CO2_normalized_1**1*FDS_normalized_1**0 
				+ d01*composition_CO2_normalized_1**0*FDS_normalized_1**1 
				+ d20*composition_CO2_normalized_1**2*FDS_normalized_1**0 
				+ d11*composition_CO2_normalized_1**1*FDS_normalized_1**1 
				+ d02*composition_CO2_normalized_1**0*FDS_normalized_1**2 
				+ d30*composition_CO2_normalized_1**3*FDS_normalized_1**0 
				+ d21*composition_CO2_normalized_1**2*FDS_normalized_1**1
				+ d12*composition_CO2_normalized_1**1*FDS_normalized_1**2 
				+ d03*composition_CO2_normalized_1**0*FDS_normalized_1**3 
				+ d31*composition_CO2_normalized_1**3*FDS_normalized_1**1 
				+ d22*composition_CO2_normalized_1**2*FDS_normalized_1**2
				+ d13*composition_CO2_normalized_1**1*FDS_normalized_1**3 
				+ d04*composition_CO2_normalized_1**0*FDS_normalized_1**4)

				density2 = (d00*composition_CO2_normalized_2**0*FDS_normalized_2**0 
				+ d10*composition_CO2_normalized_2**1*FDS_normalized_2**0 
				+ d01*composition_CO2_normalized_2**0*FDS_normalized_2**1 
				+ d20*composition_CO2_normalized_2**2*FDS_normalized_2**0
				+ d11*composition_CO2_normalized_2**1*FDS_normalized_2**1 
				+ d02*composition_CO2_normalized_2**0*FDS_normalized_2**2
				+ d30*composition_CO2_normalized_2**3*FDS_normalized_2**0 
				+ d21*composition_CO2_normalized_2**2*FDS_normalized_2**1
				+ d12*composition_CO2_normalized_2**1*FDS_normalized_2**2 
				+ d03*composition_CO2_normalized_2**0*FDS_normalized_2**3 
				+ d31*composition_CO2_normalized_2**3*FDS_normalized_2**1 
				+ d22*composition_CO2_normalized_2**2*FDS_normalized_2**2
				+ d13*composition_CO2_normalized_2**1*FDS_normalized_2**3 
				+ d04*composition_CO2_normalized_2**0*FDS_normalized_2**4)

				density3 = (d00*composition_CO2_normalized_1**0*FDS_normalized_2**0 
				+ d10*composition_CO2_normalized_1**1*FDS_normalized_2**0 
				+ d01*composition_CO2_normalized_1**0*FDS_normalized_2**1 
				+ d20*composition_CO2_normalized_1**2*FDS_normalized_2**0
				+ d11*composition_CO2_normalized_1**1*FDS_normalized_2**1 
				+ d02*composition_CO2_normalized_1**0*FDS_normalized_2**2 
				+ d30*composition_CO2_normalized_1**3*FDS_normalized_2**0 
				+ d21*composition_CO2_normalized_1**2*FDS_normalized_2**1
				+ d12*composition_CO2_normalized_1**1*FDS_normalized_2**2 
				+ d03*composition_CO2_normalized_1**0*FDS_normalized_2**3 
				+ d31*composition_CO2_normalized_1**3*FDS_normalized_2**1 
				+ d22*composition_CO2_normalized_1**2*FDS_normalized_2**2
				+ d13*composition_CO2_normalized_1**1*FDS_normalized_2**3 
				+ d04*composition_CO2_normalized_1**0*FDS_normalized_2**4)

				density4 = (d00*composition_CO2_normalized_2**0*FDS_normalized_1**0 
				+ d10*composition_CO2_normalized_2**1*FDS_normalized_1**0 
				+ d01*composition_CO2_normalized_2**0*FDS_normalized_1**1 
				+ d20*composition_CO2_normalized_2**2*FDS_normalized_1**0
				+ d11*composition_CO2_normalized_2**1*FDS_normalized_1**1 
				+ d02*composition_CO2_normalized_2**0*FDS_normalized_1**2 
				+ d30*composition_CO2_normalized_2**3*FDS_normalized_1**0 
				+ d21*composition_CO2_normalized_2**2*FDS_normalized_1**1
				+ d12*composition_CO2_normalized_2**1*FDS_normalized_1**2 
				+ d03*composition_CO2_normalized_2**0*FDS_normalized_1**3 
				+ d31*composition_CO2_normalized_2**3*FDS_normalized_1**1 
				+ d22*composition_CO2_normalized_2**2*FDS_normalized_1**2
				+ d13*composition_CO2_normalized_2**1*FDS_normalized_1**3 
				+ d04*composition_CO2_normalized_2**0*FDS_normalized_1**4)              

				pressure_final = (max(pressure1, pressure2, pressure3, pressure4) + min(pressure1, pressure2, pressure3, pressure4))/2 #pressure max - pressure min
				uncer_pressure_final = 8.5 + (max(pressure1, pressure2, pressure3, pressure4) - min(pressure1, pressure2, pressure3, pressure4))/(2*np.sqrt(3)) #uncer = 12

				density_final = (max(density1, density2, density3, density4) + min(density1, density2, density3, density4))/2 #density max - density min
				uncer_density_final = 0.0042  + (max(density1, density2, density3, density4) - min(density1, density2, density3, density4))/(2*np.sqrt(3)) #uncer=0.006

				molarvolume1 = 1/(max(density1, density2, density3, density4)/(44*composition_CO2 + 28*composition_N2))
				molarvolume2 = 1/(min(density1, density2, density3, density4)/(44*composition_CO2 + 28*composition_N2))		
				molarvolume_final = (molarvolume1 + molarvolume2) / 2
				uncer_molarvolume_final = (molarvolume2 - molarvolume1) / (2*np.sqrt(3))


				##### verify if measured pressure < 160 bar, if it is, re-recalculte using calibration data for 5-160 bar range.
				if pressure_final <= 150: 

					## Calibration equation's coeff of CO2-N2 at 22 °C over 5-160 bars
					# normalisation of concentration and of Fermi diad splitting
					
					composition_CO2_normalized_1 = (composition_CO2 + 0.005 - 0.30339)/0.14138
					composition_CO2_normalized_2 = (composition_CO2 - 0.005 - 0.30339)/0.14138
					FDS_normalized_1 = (FDS + unc_FDS - 102.87)/0.093082
					FDS_normalized_2 = (FDS - unc_FDS - 102.87)/0.093082
										
					p00= 69.13911052
					p10= -26.1138853
					p01= 51.15493952
					p20= 12.433977
					p11= -24.97362963
					p02= -0.61042483
					p30= -3.525410343
					p21= 12.07944049
					p12= 3.668211303
					p03= -0.998272689
					p31= -2.992344667
					p22= -3.140109598
					p13= 1.096062354
					p04= -0.061661634
					
					d00= 0.096377933					
					d10= -0.027517465
					d01= 0.075132864
					d20= 0.012065717
					d11= -0.026418972
					d02= 0.001098315
					d30= -0.002806359
					d21= 0.010828952
					d12= 0.00658279
					d03= -0.002021765
					d31= -0.001975997
					d22= -0.004846773
					d13= 0.001993775
					d04= -0.000167776


					#### pressure calculation
					pressure1 = (p00*composition_CO2_normalized_1**0*FDS_normalized_1**0 
					+ p10*composition_CO2_normalized_1**1*FDS_normalized_1**0 
					+ p01*composition_CO2_normalized_1**0*FDS_normalized_1**1 
					+ p20*composition_CO2_normalized_1**2*FDS_normalized_1**0 
					+ p11*composition_CO2_normalized_1**1*FDS_normalized_1**1 
					+ p02*composition_CO2_normalized_1**0*FDS_normalized_1**2 
					+ p30*composition_CO2_normalized_1**3*FDS_normalized_1**0 
					+ p21*composition_CO2_normalized_1**2*FDS_normalized_1**1
					+ p12*composition_CO2_normalized_1**1*FDS_normalized_1**2 
					+ p03*composition_CO2_normalized_1**0*FDS_normalized_1**3 
					+ p31*composition_CO2_normalized_1**3*FDS_normalized_1**1 
					+ p22*composition_CO2_normalized_1**2*FDS_normalized_1**2
					+ p13*composition_CO2_normalized_1**1*FDS_normalized_1**3 
					+ p04*composition_CO2_normalized_1**0*FDS_normalized_1**4)

					pressure2 = (p00*composition_CO2_normalized_2**0*FDS_normalized_2**0 
					+ p10*composition_CO2_normalized_2**1*FDS_normalized_2**0 
					+ p01*composition_CO2_normalized_2**0*FDS_normalized_2**1 
					+ p20*composition_CO2_normalized_2**2*FDS_normalized_2**0
					+ p11*composition_CO2_normalized_2**1*FDS_normalized_2**1 
					+ p02*composition_CO2_normalized_2**0*FDS_normalized_2**2
					+ p30*composition_CO2_normalized_2**3*FDS_normalized_2**0 
					+ p21*composition_CO2_normalized_2**2*FDS_normalized_2**1
					+ p12*composition_CO2_normalized_2**1*FDS_normalized_2**2 
					+ p03*composition_CO2_normalized_2**0*FDS_normalized_2**3 
					+ p31*composition_CO2_normalized_2**3*FDS_normalized_2**1 
					+ p22*composition_CO2_normalized_2**2*FDS_normalized_2**2
					+ p13*composition_CO2_normalized_2**1*FDS_normalized_2**3 
					+ p04*composition_CO2_normalized_2**0*FDS_normalized_2**4)

					pressure3 = (p00*composition_CO2_normalized_1**0*FDS_normalized_2**0 
					+ p10*composition_CO2_normalized_1**1*FDS_normalized_2**0 
					+ p01*composition_CO2_normalized_1**0*FDS_normalized_2**1 
					+ p20*composition_CO2_normalized_1**2*FDS_normalized_2**0
					+ p11*composition_CO2_normalized_1**1*FDS_normalized_2**1 
					+ p02*composition_CO2_normalized_1**0*FDS_normalized_2**2 
					+ p30*composition_CO2_normalized_1**3*FDS_normalized_2**0 
					+ p21*composition_CO2_normalized_1**2*FDS_normalized_2**1
					+ p12*composition_CO2_normalized_1**1*FDS_normalized_2**2 
					+ p03*composition_CO2_normalized_1**0*FDS_normalized_2**3 
					+ p31*composition_CO2_normalized_1**3*FDS_normalized_2**1 
					+ p22*composition_CO2_normalized_1**2*FDS_normalized_2**2
					+ p13*composition_CO2_normalized_1**1*FDS_normalized_2**3 
					+ p04*composition_CO2_normalized_1**0*FDS_normalized_2**4)

					pressure4 = (p00*composition_CO2_normalized_2**0*FDS_normalized_1**0 
					+ p10*composition_CO2_normalized_2**1*FDS_normalized_1**0 
					+ p01*composition_CO2_normalized_2**0*FDS_normalized_1**1 
					+ p20*composition_CO2_normalized_2**2*FDS_normalized_1**0
					+ p11*composition_CO2_normalized_2**1*FDS_normalized_1**1 
					+ p02*composition_CO2_normalized_2**0*FDS_normalized_1**2 
					+ p30*composition_CO2_normalized_2**3*FDS_normalized_1**0 
					+ p21*composition_CO2_normalized_2**2*FDS_normalized_1**1
					+ p12*composition_CO2_normalized_2**1*FDS_normalized_1**2 
					+ p03*composition_CO2_normalized_2**0*FDS_normalized_1**3 
					+ p31*composition_CO2_normalized_2**3*FDS_normalized_1**1 
					+ p22*composition_CO2_normalized_2**2*FDS_normalized_1**2
					+ p13*composition_CO2_normalized_2**1*FDS_normalized_1**3 
					+ p04*composition_CO2_normalized_2**0*FDS_normalized_1**4)

					########################
					#### density calculation

					density1 = (d00*composition_CO2_normalized_1**0*FDS_normalized_1**0 
					+ d10*composition_CO2_normalized_1**1*FDS_normalized_1**0 
					+ d01*composition_CO2_normalized_1**0*FDS_normalized_1**1 
					+ d20*composition_CO2_normalized_1**2*FDS_normalized_1**0 
					+ d11*composition_CO2_normalized_1**1*FDS_normalized_1**1 
					+ d02*composition_CO2_normalized_1**0*FDS_normalized_1**2 
					+ d30*composition_CO2_normalized_1**3*FDS_normalized_1**0 
					+ d21*composition_CO2_normalized_1**2*FDS_normalized_1**1
					+ d12*composition_CO2_normalized_1**1*FDS_normalized_1**2 
					+ d03*composition_CO2_normalized_1**0*FDS_normalized_1**3 
					+ d31*composition_CO2_normalized_1**3*FDS_normalized_1**1 
					+ d22*composition_CO2_normalized_1**2*FDS_normalized_1**2
					+ d13*composition_CO2_normalized_1**1*FDS_normalized_1**3 
					+ d04*composition_CO2_normalized_1**0*FDS_normalized_1**4)

					density2 = (d00*composition_CO2_normalized_2**0*FDS_normalized_2**0 
					+ d10*composition_CO2_normalized_2**1*FDS_normalized_2**0 
					+ d01*composition_CO2_normalized_2**0*FDS_normalized_2**1 
					+ d20*composition_CO2_normalized_2**2*FDS_normalized_2**0
					+ d11*composition_CO2_normalized_2**1*FDS_normalized_2**1 
					+ d02*composition_CO2_normalized_2**0*FDS_normalized_2**2
					+ d30*composition_CO2_normalized_2**3*FDS_normalized_2**0 
					+ d21*composition_CO2_normalized_2**2*FDS_normalized_2**1
					+ d12*composition_CO2_normalized_2**1*FDS_normalized_2**2 
					+ d03*composition_CO2_normalized_2**0*FDS_normalized_2**3 
					+ d31*composition_CO2_normalized_2**3*FDS_normalized_2**1 
					+ d22*composition_CO2_normalized_2**2*FDS_normalized_2**2
					+ d13*composition_CO2_normalized_2**1*FDS_normalized_2**3 
					+ d04*composition_CO2_normalized_2**0*FDS_normalized_2**4)

					density3 = (d00*composition_CO2_normalized_1**0*FDS_normalized_2**0 
					+ d10*composition_CO2_normalized_1**1*FDS_normalized_2**0 
					+ d01*composition_CO2_normalized_1**0*FDS_normalized_2**1 
					+ d20*composition_CO2_normalized_1**2*FDS_normalized_2**0
					+ d11*composition_CO2_normalized_1**1*FDS_normalized_2**1 
					+ d02*composition_CO2_normalized_1**0*FDS_normalized_2**2 
					+ d30*composition_CO2_normalized_1**3*FDS_normalized_2**0 
					+ d21*composition_CO2_normalized_1**2*FDS_normalized_2**1
					+ d12*composition_CO2_normalized_1**1*FDS_normalized_2**2 
					+ d03*composition_CO2_normalized_1**0*FDS_normalized_2**3 
					+ d31*composition_CO2_normalized_1**3*FDS_normalized_2**1 
					+ d22*composition_CO2_normalized_1**2*FDS_normalized_2**2
					+ d13*composition_CO2_normalized_1**1*FDS_normalized_2**3 
					+ d04*composition_CO2_normalized_1**0*FDS_normalized_2**4)

					density4 = (d00*composition_CO2_normalized_2**0*FDS_normalized_1**0 
					+ d10*composition_CO2_normalized_2**1*FDS_normalized_1**0 
					+ d01*composition_CO2_normalized_2**0*FDS_normalized_1**1 
					+ d20*composition_CO2_normalized_2**2*FDS_normalized_1**0
					+ d11*composition_CO2_normalized_2**1*FDS_normalized_1**1 
					+ d02*composition_CO2_normalized_2**0*FDS_normalized_1**2 
					+ d30*composition_CO2_normalized_2**3*FDS_normalized_1**0 
					+ d21*composition_CO2_normalized_2**2*FDS_normalized_1**1
					+ d12*composition_CO2_normalized_2**1*FDS_normalized_1**2 
					+ d03*composition_CO2_normalized_2**0*FDS_normalized_1**3 
					+ d31*composition_CO2_normalized_2**3*FDS_normalized_1**1 
					+ d22*composition_CO2_normalized_2**2*FDS_normalized_1**2
					+ d13*composition_CO2_normalized_2**1*FDS_normalized_1**3 
					+ d04*composition_CO2_normalized_2**0*FDS_normalized_1**4)              

					pressure_final = (max(pressure1, pressure2, pressure3, pressure4) + min(pressure1, pressure2, pressure3, pressure4))/2 #pressure max - pressure min
					uncer_pressure_final = 3.6 + (max(pressure1, pressure2, pressure3, pressure4) - min(pressure1, pressure2, pressure3, pressure4))/(2*np.sqrt(3)) # uncer = 5

					density_final = (max(density1, density2, density3, density4) + min(density1, density2, density3, density4))/2 #density max - density min
					uncer_density_final = 0.0035 + (max(density1, density2, density3, density4) - min(density1, density2, density3, density4))/(2*np.sqrt(3)) #uncer = 0.005

					molarvolume1 = 1/(max(density1, density2, density3, density4)/(44*composition_CO2 + 28*composition_N2))
					molarvolume2 = 1/(min(density1, density2, density3, density4)/(44*composition_CO2 + 28*composition_N2))		
					molarvolume_final = (molarvolume1 + molarvolume2) / 2
					uncer_molarvolume_final = (molarvolume2 - molarvolume1) / (2*np.sqrt(3))
				
				print('composition normalized', composition_CO2_normalized_1)

				print('pressure1', pressure1)
				print('pressure2', pressure2)
				print('pressure3', pressure3)
				print('pressure4', pressure4)

				print('density 1=', density1)
				print('density 2=', density2)
				print('density 3=', density3)
				print('density 4=', density4)
				
				print("molarvolume1", molarvolume1)
				print("molarvolume2", molarvolume2)

				####DISPLAY POP UP IF OUT OF RANGE	
				if pressure_final > 650 or pressure1 >650 or pressure2 >650 or pressure_final < -20 or pressure1 <-20 or pressure2 <-20 or density2<0 or density1 <0 or density3<0 or density4<0 or density_final <0 :
					popupmsg_OCR()
			

			################################
			######## OTHERS spectrometers ####		
			####################################

			if temperature.get() == 22 and composition_CO2 >= 0.5 and instrument.get() ==2: 

				## Calibration equation's coeff of CO2-N2 at 22 °C over 5-500 bars


				# normalisation of concentration and of Fermi diad splitting
				composition_CO2_normalized_1 = (composition_CO2 + 0.005)
				composition_CO2_normalized_2 = (composition_CO2 - 0.005)
				FDS_normalized_1 = (FDS + unc_FDS - FDS_std)
				FDS_normalized_2 = (FDS - unc_FDS - FDS_std)
				
				p00= -137.742
				p10= 683.702
				p01= 1930.147
				p20= -1089.503
				p11= -6950.3423975
				p02= 865.541991687
				p30= 547.846364803
				p21= 10147.692301
				p12= -3537.18972718
				p03= 600.00211371
				p31= -4980.75130798
				p22= 2557.164940876
				p13= -624.1478910201
				p04= 28.64423299

				d00= 0.376215798
				d10= -1.7408682287
				d01= 1.4904360684
				d20= 2.5618214746
				d11= -2.248784203
				d02= -0.234697082
				d30= -1.200925618
				d21= 0.665529057
				d12= 1.2015088
				d03= -0.169712
				d31= 0.4053960
				d22= -0.8846674
				d13= 0.17174924
				d04= -0.007822093

				#### pressure calculation
				pressure1 = (p00*composition_CO2_normalized_1**0*FDS_normalized_1**0 
				+ p10*composition_CO2_normalized_1**1*FDS_normalized_1**0 
				+ p01*composition_CO2_normalized_1**0*FDS_normalized_1**1 
				+ p20*composition_CO2_normalized_1**2*FDS_normalized_1**0 
				+ p11*composition_CO2_normalized_1**1*FDS_normalized_1**1 
				+ p02*composition_CO2_normalized_1**0*FDS_normalized_1**2 
				+ p30*composition_CO2_normalized_1**3*FDS_normalized_1**0 
				+ p21*composition_CO2_normalized_1**2*FDS_normalized_1**1
				+ p12*composition_CO2_normalized_1**1*FDS_normalized_1**2 
				+ p03*composition_CO2_normalized_1**0*FDS_normalized_1**3 
				+ p31*composition_CO2_normalized_1**3*FDS_normalized_1**1 
				+ p22*composition_CO2_normalized_1**2*FDS_normalized_1**2
				+ p13*composition_CO2_normalized_1**1*FDS_normalized_1**3 
				+ p04*composition_CO2_normalized_1**0*FDS_normalized_1**4)

				pressure2 = (p00*composition_CO2_normalized_2**0*FDS_normalized_2**0 
				+ p10*composition_CO2_normalized_2**1*FDS_normalized_2**0 
				+ p01*composition_CO2_normalized_2**0*FDS_normalized_2**1 
				+ p20*composition_CO2_normalized_2**2*FDS_normalized_2**0
				+ p11*composition_CO2_normalized_2**1*FDS_normalized_2**1 
				+ p02*composition_CO2_normalized_2**0*FDS_normalized_2**2
				+ p30*composition_CO2_normalized_2**3*FDS_normalized_2**0 
				+ p21*composition_CO2_normalized_2**2*FDS_normalized_2**1
				+ p12*composition_CO2_normalized_2**1*FDS_normalized_2**2 
				+ p03*composition_CO2_normalized_2**0*FDS_normalized_2**3 
				+ p31*composition_CO2_normalized_2**3*FDS_normalized_2**1 
				+ p22*composition_CO2_normalized_2**2*FDS_normalized_2**2
				+ p13*composition_CO2_normalized_2**1*FDS_normalized_2**3 
				+ p04*composition_CO2_normalized_2**0*FDS_normalized_2**4)

				pressure3 = (p00*composition_CO2_normalized_1**0*FDS_normalized_2**0 
				+ p10*composition_CO2_normalized_1**1*FDS_normalized_2**0 
				+ p01*composition_CO2_normalized_1**0*FDS_normalized_2**1 
				+ p20*composition_CO2_normalized_1**2*FDS_normalized_2**0
				+ p11*composition_CO2_normalized_1**1*FDS_normalized_2**1 
				+ p02*composition_CO2_normalized_1**0*FDS_normalized_2**2 
				+ p30*composition_CO2_normalized_1**3*FDS_normalized_2**0 
				+ p21*composition_CO2_normalized_1**2*FDS_normalized_2**1
				+ p12*composition_CO2_normalized_1**1*FDS_normalized_2**2 
				+ p03*composition_CO2_normalized_1**0*FDS_normalized_2**3 
				+ p31*composition_CO2_normalized_1**3*FDS_normalized_2**1 
				+ p22*composition_CO2_normalized_1**2*FDS_normalized_2**2
				+ p13*composition_CO2_normalized_1**1*FDS_normalized_2**3 
				+ p04*composition_CO2_normalized_1**0*FDS_normalized_2**4)

				pressure4 = (p00*composition_CO2_normalized_2**0*FDS_normalized_1**0 
				+ p10*composition_CO2_normalized_2**1*FDS_normalized_1**0 
				+ p01*composition_CO2_normalized_2**0*FDS_normalized_1**1 
				+ p20*composition_CO2_normalized_2**2*FDS_normalized_1**0
				+ p11*composition_CO2_normalized_2**1*FDS_normalized_1**1 
				+ p02*composition_CO2_normalized_2**0*FDS_normalized_1**2 
				+ p30*composition_CO2_normalized_2**3*FDS_normalized_1**0 
				+ p21*composition_CO2_normalized_2**2*FDS_normalized_1**1
				+ p12*composition_CO2_normalized_2**1*FDS_normalized_1**2 
				+ p03*composition_CO2_normalized_2**0*FDS_normalized_1**3 
				+ p31*composition_CO2_normalized_2**3*FDS_normalized_1**1 
				+ p22*composition_CO2_normalized_2**2*FDS_normalized_1**2
				+ p13*composition_CO2_normalized_2**1*FDS_normalized_1**3 
				+ p04*composition_CO2_normalized_2**0*FDS_normalized_1**4)

				########################
				#### density calculation

				density1 = (d00*composition_CO2_normalized_1**0*FDS_normalized_1**0 
				+ d10*composition_CO2_normalized_1**1*FDS_normalized_1**0 
				+ d01*composition_CO2_normalized_1**0*FDS_normalized_1**1 
				+ d20*composition_CO2_normalized_1**2*FDS_normalized_1**0 
				+ d11*composition_CO2_normalized_1**1*FDS_normalized_1**1 
				+ d02*composition_CO2_normalized_1**0*FDS_normalized_1**2 
				+ d30*composition_CO2_normalized_1**3*FDS_normalized_1**0 
				+ d21*composition_CO2_normalized_1**2*FDS_normalized_1**1
				+ d12*composition_CO2_normalized_1**1*FDS_normalized_1**2 
				+ d03*composition_CO2_normalized_1**0*FDS_normalized_1**3 
				+ d31*composition_CO2_normalized_1**3*FDS_normalized_1**1 
				+ d22*composition_CO2_normalized_1**2*FDS_normalized_1**2
				+ d13*composition_CO2_normalized_1**1*FDS_normalized_1**3 
				+ d04*composition_CO2_normalized_1**0*FDS_normalized_1**4)

				density2 = (d00*composition_CO2_normalized_2**0*FDS_normalized_2**0 
				+ d10*composition_CO2_normalized_2**1*FDS_normalized_2**0 
				+ d01*composition_CO2_normalized_2**0*FDS_normalized_2**1 
				+ d20*composition_CO2_normalized_2**2*FDS_normalized_2**0
				+ d11*composition_CO2_normalized_2**1*FDS_normalized_2**1 
				+ d02*composition_CO2_normalized_2**0*FDS_normalized_2**2
				+ d30*composition_CO2_normalized_2**3*FDS_normalized_2**0 
				+ d21*composition_CO2_normalized_2**2*FDS_normalized_2**1
				+ d12*composition_CO2_normalized_2**1*FDS_normalized_2**2 
				+ d03*composition_CO2_normalized_2**0*FDS_normalized_2**3 
				+ d31*composition_CO2_normalized_2**3*FDS_normalized_2**1 
				+ d22*composition_CO2_normalized_2**2*FDS_normalized_2**2
				+ d13*composition_CO2_normalized_2**1*FDS_normalized_2**3 
				+ d04*composition_CO2_normalized_2**0*FDS_normalized_2**4)

				density3 = (d00*composition_CO2_normalized_1**0*FDS_normalized_2**0 
				+ d10*composition_CO2_normalized_1**1*FDS_normalized_2**0 
				+ d01*composition_CO2_normalized_1**0*FDS_normalized_2**1 
				+ d20*composition_CO2_normalized_1**2*FDS_normalized_2**0
				+ d11*composition_CO2_normalized_1**1*FDS_normalized_2**1 
				+ d02*composition_CO2_normalized_1**0*FDS_normalized_2**2 
				+ d30*composition_CO2_normalized_1**3*FDS_normalized_2**0 
				+ d21*composition_CO2_normalized_1**2*FDS_normalized_2**1
				+ d12*composition_CO2_normalized_1**1*FDS_normalized_2**2 
				+ d03*composition_CO2_normalized_1**0*FDS_normalized_2**3 
				+ d31*composition_CO2_normalized_1**3*FDS_normalized_2**1 
				+ d22*composition_CO2_normalized_1**2*FDS_normalized_2**2
				+ d13*composition_CO2_normalized_1**1*FDS_normalized_2**3 
				+ d04*composition_CO2_normalized_1**0*FDS_normalized_2**4)

				density4 = (d00*composition_CO2_normalized_2**0*FDS_normalized_1**0 
				+ d10*composition_CO2_normalized_2**1*FDS_normalized_1**0 
				+ d01*composition_CO2_normalized_2**0*FDS_normalized_1**1 
				+ d20*composition_CO2_normalized_2**2*FDS_normalized_1**0
				+ d11*composition_CO2_normalized_2**1*FDS_normalized_1**1 
				+ d02*composition_CO2_normalized_2**0*FDS_normalized_1**2 
				+ d30*composition_CO2_normalized_2**3*FDS_normalized_1**0 
				+ d21*composition_CO2_normalized_2**2*FDS_normalized_1**1
				+ d12*composition_CO2_normalized_2**1*FDS_normalized_1**2 
				+ d03*composition_CO2_normalized_2**0*FDS_normalized_1**3 
				+ d31*composition_CO2_normalized_2**3*FDS_normalized_1**1 
				+ d22*composition_CO2_normalized_2**2*FDS_normalized_1**2
				+ d13*composition_CO2_normalized_2**1*FDS_normalized_1**3 
				+ d04*composition_CO2_normalized_2**0*FDS_normalized_1**4)              

				pressure_final = (max(pressure1, pressure2, pressure3, pressure4) + min(pressure1, pressure2, pressure3, pressure4))/2 #pressure max - pressure min
				uncer_pressure_final = 7.1 + (max(pressure1, pressure2, pressure3, pressure4) - min(pressure1, pressure2, pressure3, pressure4))/(2*np.sqrt(3)) #uncer = 10

				density_final = (max(density1, density2, density3, density4) + min(density1, density2, density3, density4))/2 #density max - density min
				uncer_density_final = 0.0042 + (max(density1, density2, density3, density4) - min(density1, density2, density3, density4))/(2*np.sqrt(3)) #uncer = 0.006

				molarvolume1 = 1/(max(density1, density2, density3, density4)/(44*composition_CO2 + 28*composition_N2))
				molarvolume2 = 1/(min(density1, density2, density3, density4)/(44*composition_CO2 + 28*composition_N2))
				
				molarvolume_final = (molarvolume1 + molarvolume2)/2

				uncer_molarvolume_final = (molarvolume2 - molarvolume1)/(2*np.sqrt(3))

				##### verify if measured pressure < 160 bar, if it is, re-recalculte using calibration data for 5-160 bar range.
				if pressure_final <= 150: 

					## Calibration equation's coeff of CO2-N2 at 22 °C over 5-160 bars
					# normalisation of concentration and of Fermi diad splitting
					
					composition_CO2_normalized_1 = (composition_CO2 + 0.005)
					composition_CO2_normalized_2 = (composition_CO2 - 0.005)
					FDS_normalized_1 = (FDS + unc_FDS - FDS_std)
					FDS_normalized_2 = (FDS - unc_FDS - FDS_std)
										
					p00= 88.96684561519
					p10= -377.3106013
					p01= 1118.9425823
					p20= 522.271667687
					p11= -2680.49311862
					p02= 121.15547879
					p30= -233.62694978
					p21= 2796.36506233
					p12= -757.07376958
					p03= 204.248700297
					p31= -1072.48729259
					p22= 552.45615399
					p13= -267.4897263
					p04= 38.66589267

					d00= 0.0102799391
					d10= -0.064067719
					d01= 2.6269288670
					d20= 0.12703282401
					d11= -8.142852753
					d02= 0.523088736
					d30= -0.074232412
					d21= 9.8392907602
					d12= -0.36717960071
					d03= -0.348974162
					d31= -3.9912606484
					d22= -0.209186635
					d13= 0.4692333253
					d04= -0.03545150

					#### pressure calculation
					pressure1 = (p00*composition_CO2_normalized_1**0*FDS_normalized_1**0 
					+ p10*composition_CO2_normalized_1**1*FDS_normalized_1**0 
					+ p01*composition_CO2_normalized_1**0*FDS_normalized_1**1 
					+ p20*composition_CO2_normalized_1**2*FDS_normalized_1**0 
					+ p11*composition_CO2_normalized_1**1*FDS_normalized_1**1 
					+ p02*composition_CO2_normalized_1**0*FDS_normalized_1**2 
					+ p30*composition_CO2_normalized_1**3*FDS_normalized_1**0 
					+ p21*composition_CO2_normalized_1**2*FDS_normalized_1**1
					+ p12*composition_CO2_normalized_1**1*FDS_normalized_1**2 
					+ p03*composition_CO2_normalized_1**0*FDS_normalized_1**3 
					+ p31*composition_CO2_normalized_1**3*FDS_normalized_1**1 
					+ p22*composition_CO2_normalized_1**2*FDS_normalized_1**2
					+ p13*composition_CO2_normalized_1**1*FDS_normalized_1**3 
					+ p04*composition_CO2_normalized_1**0*FDS_normalized_1**4)

					pressure2 = (p00*composition_CO2_normalized_2**0*FDS_normalized_2**0 
					+ p10*composition_CO2_normalized_2**1*FDS_normalized_2**0 
					+ p01*composition_CO2_normalized_2**0*FDS_normalized_2**1 
					+ p20*composition_CO2_normalized_2**2*FDS_normalized_2**0
					+ p11*composition_CO2_normalized_2**1*FDS_normalized_2**1 
					+ p02*composition_CO2_normalized_2**0*FDS_normalized_2**2
					+ p30*composition_CO2_normalized_2**3*FDS_normalized_2**0 
					+ p21*composition_CO2_normalized_2**2*FDS_normalized_2**1
					+ p12*composition_CO2_normalized_2**1*FDS_normalized_2**2 
					+ p03*composition_CO2_normalized_2**0*FDS_normalized_2**3 
					+ p31*composition_CO2_normalized_2**3*FDS_normalized_2**1 
					+ p22*composition_CO2_normalized_2**2*FDS_normalized_2**2
					+ p13*composition_CO2_normalized_2**1*FDS_normalized_2**3 
					+ p04*composition_CO2_normalized_2**0*FDS_normalized_2**4)

					pressure3 = (p00*composition_CO2_normalized_1**0*FDS_normalized_2**0 
					+ p10*composition_CO2_normalized_1**1*FDS_normalized_2**0 
					+ p01*composition_CO2_normalized_1**0*FDS_normalized_2**1 
					+ p20*composition_CO2_normalized_1**2*FDS_normalized_2**0
					+ p11*composition_CO2_normalized_1**1*FDS_normalized_2**1 
					+ p02*composition_CO2_normalized_1**0*FDS_normalized_2**2 
					+ p30*composition_CO2_normalized_1**3*FDS_normalized_2**0 
					+ p21*composition_CO2_normalized_1**2*FDS_normalized_2**1
					+ p12*composition_CO2_normalized_1**1*FDS_normalized_2**2 
					+ p03*composition_CO2_normalized_1**0*FDS_normalized_2**3 
					+ p31*composition_CO2_normalized_1**3*FDS_normalized_2**1 
					+ p22*composition_CO2_normalized_1**2*FDS_normalized_2**2
					+ p13*composition_CO2_normalized_1**1*FDS_normalized_2**3 
					+ p04*composition_CO2_normalized_1**0*FDS_normalized_2**4)

					pressure4 = (p00*composition_CO2_normalized_2**0*FDS_normalized_1**0 
					+ p10*composition_CO2_normalized_2**1*FDS_normalized_1**0 
					+ p01*composition_CO2_normalized_2**0*FDS_normalized_1**1 
					+ p20*composition_CO2_normalized_2**2*FDS_normalized_1**0
					+ p11*composition_CO2_normalized_2**1*FDS_normalized_1**1 
					+ p02*composition_CO2_normalized_2**0*FDS_normalized_1**2 
					+ p30*composition_CO2_normalized_2**3*FDS_normalized_1**0 
					+ p21*composition_CO2_normalized_2**2*FDS_normalized_1**1
					+ p12*composition_CO2_normalized_2**1*FDS_normalized_1**2 
					+ p03*composition_CO2_normalized_2**0*FDS_normalized_1**3 
					+ p31*composition_CO2_normalized_2**3*FDS_normalized_1**1 
					+ p22*composition_CO2_normalized_2**2*FDS_normalized_1**2
					+ p13*composition_CO2_normalized_2**1*FDS_normalized_1**3 
					+ p04*composition_CO2_normalized_2**0*FDS_normalized_1**4)

					########################
					#### density calculation

					density1 = (d00*composition_CO2_normalized_1**0*FDS_normalized_1**0 
					+ d10*composition_CO2_normalized_1**1*FDS_normalized_1**0 
					+ d01*composition_CO2_normalized_1**0*FDS_normalized_1**1 
					+ d20*composition_CO2_normalized_1**2*FDS_normalized_1**0 
					+ d11*composition_CO2_normalized_1**1*FDS_normalized_1**1 
					+ d02*composition_CO2_normalized_1**0*FDS_normalized_1**2 
					+ d30*composition_CO2_normalized_1**3*FDS_normalized_1**0 
					+ d21*composition_CO2_normalized_1**2*FDS_normalized_1**1
					+ d12*composition_CO2_normalized_1**1*FDS_normalized_1**2 
					+ d03*composition_CO2_normalized_1**0*FDS_normalized_1**3 
					+ d31*composition_CO2_normalized_1**3*FDS_normalized_1**1 
					+ d22*composition_CO2_normalized_1**2*FDS_normalized_1**2
					+ d13*composition_CO2_normalized_1**1*FDS_normalized_1**3 
					+ d04*composition_CO2_normalized_1**0*FDS_normalized_1**4)

					density2 = (d00*composition_CO2_normalized_2**0*FDS_normalized_2**0 
					+ d10*composition_CO2_normalized_2**1*FDS_normalized_2**0 
					+ d01*composition_CO2_normalized_2**0*FDS_normalized_2**1 
					+ d20*composition_CO2_normalized_2**2*FDS_normalized_2**0
					+ d11*composition_CO2_normalized_2**1*FDS_normalized_2**1 
					+ d02*composition_CO2_normalized_2**0*FDS_normalized_2**2
					+ d30*composition_CO2_normalized_2**3*FDS_normalized_2**0 
					+ d21*composition_CO2_normalized_2**2*FDS_normalized_2**1
					+ d12*composition_CO2_normalized_2**1*FDS_normalized_2**2 
					+ d03*composition_CO2_normalized_2**0*FDS_normalized_2**3 
					+ d31*composition_CO2_normalized_2**3*FDS_normalized_2**1 
					+ d22*composition_CO2_normalized_2**2*FDS_normalized_2**2
					+ d13*composition_CO2_normalized_2**1*FDS_normalized_2**3 
					+ d04*composition_CO2_normalized_2**0*FDS_normalized_2**4)

					density3 = (d00*composition_CO2_normalized_1**0*FDS_normalized_2**0 
					+ d10*composition_CO2_normalized_1**1*FDS_normalized_2**0 
					+ d01*composition_CO2_normalized_1**0*FDS_normalized_2**1 
					+ d20*composition_CO2_normalized_1**2*FDS_normalized_2**0
					+ d11*composition_CO2_normalized_1**1*FDS_normalized_2**1 
					+ d02*composition_CO2_normalized_1**0*FDS_normalized_2**2 
					+ d30*composition_CO2_normalized_1**3*FDS_normalized_2**0 
					+ d21*composition_CO2_normalized_1**2*FDS_normalized_2**1
					+ d12*composition_CO2_normalized_1**1*FDS_normalized_2**2 
					+ d03*composition_CO2_normalized_1**0*FDS_normalized_2**3 
					+ d31*composition_CO2_normalized_1**3*FDS_normalized_2**1 
					+ d22*composition_CO2_normalized_1**2*FDS_normalized_2**2
					+ d13*composition_CO2_normalized_1**1*FDS_normalized_2**3 
					+ d04*composition_CO2_normalized_1**0*FDS_normalized_2**4)

					density4 = (d00*composition_CO2_normalized_2**0*FDS_normalized_1**0 
					+ d10*composition_CO2_normalized_2**1*FDS_normalized_1**0 
					+ d01*composition_CO2_normalized_2**0*FDS_normalized_1**1 
					+ d20*composition_CO2_normalized_2**2*FDS_normalized_1**0
					+ d11*composition_CO2_normalized_2**1*FDS_normalized_1**1 
					+ d02*composition_CO2_normalized_2**0*FDS_normalized_1**2 
					+ d30*composition_CO2_normalized_2**3*FDS_normalized_1**0 
					+ d21*composition_CO2_normalized_2**2*FDS_normalized_1**1
					+ d12*composition_CO2_normalized_2**1*FDS_normalized_1**2 
					+ d03*composition_CO2_normalized_2**0*FDS_normalized_1**3 
					+ d31*composition_CO2_normalized_2**3*FDS_normalized_1**1 
					+ d22*composition_CO2_normalized_2**2*FDS_normalized_1**2
					+ d13*composition_CO2_normalized_2**1*FDS_normalized_1**3 
					+ d04*composition_CO2_normalized_2**0*FDS_normalized_1**4)              

					pressure_final = (max(pressure1, pressure2, pressure3, pressure4) + min(pressure1, pressure2, pressure3, pressure4))/2 #pressure max - pressure min
					uncer_pressure_final = 2.12 + (max(pressure1, pressure2, pressure3, pressure4) - min(pressure1, pressure2, pressure3, pressure4))/(2*np.sqrt(3))

					density_final = (max(density1, density2, density3, density4) + min(density1, density2, density3, density4))/2 #density max - density min
					uncer_density_final = 0.002 + (max(density1, density2, density3, density4) - min(density1, density2, density3, density4))/(2*np.sqrt(3))

					molarvolume1 = 1/(max(density1, density2, density3, density4)/(44*composition_CO2 + 28*composition_N2))
					molarvolume2 = 1/(min(density1, density2, density3, density4)/(44*composition_CO2 + 28*composition_N2))
				
					molarvolume_final = (molarvolume1 + molarvolume2 )/ 2
					uncer_molarvolume_final = (molarvolume2 - molarvolume1) / (2*np.sqrt(3))

				print('pressure1', pressure1)
				print('pressure2', pressure2)
				print('pressure3', pressure3)
				print('pressure4', pressure4)

				print('density 1=', density1)
				print('density 2=', density2)
				print('density 3=', density3)
				print('density 4=', density4)

				print("molarvolume1", molarvolume1)
				print("molarvolume2", molarvolume2)

				if pressure_final > 650 or pressure1 >650 or pressure2 >650 or pressure_final < -20 or pressure1 <-20 or pressure2 <-20 or density2<0 or density1 <0 or density3<0 or density4<0 or density_final <0:
					popupmsg_OCR()
			

			if temperature.get() == 22 and composition_CO2 < 0.5 and instrument.get() ==2: 

				## Calibration equation's coeff of CO2-N2 at 22 °C over 5-500 bars


				# normalisation of concentration and of Fermi diad splitting
				composition_CO2_normalized_1 = (composition_CO2 + 0.005)
				composition_CO2_normalized_2 = (composition_CO2 - 0.005)
				FDS_normalized_1 = (FDS + unc_FDS - FDS_std)
				FDS_normalized_2 = (FDS - unc_FDS - FDS_std)
				
				p00= 1.955338137
				p10= 147.81110470
				p01= 1682.40450049
				p20= -844.98493789
				p11= -9024.0468789
				p02= 1402.17034315
				p30= 1091.81592545
				p21= 26032.6843096
				p12= -11773.205714
				p03= 2319.004383
				p31= -26651.65784
				p22= 17438.3863376
				p13= -4651.094825
				p04= 205.72105645

				d00= 0.035844475
				d10= -0.39708584
				d01= 1.877266252
				d20= 1.39869742
				d11= -4.921545610
				d02= -0.713234801
				d30= -1.50524627
				d21= 2.879115414
				d12= 5.144878468
				d03= -0.40585842
				d31= 3.153925271
				d22= -6.2767562596
				d13= 0.431299266
				d04= 0.0059271219

				#### pressure calculation
				pressure1 = (p00*composition_CO2_normalized_1**0*FDS_normalized_1**0 
				+ p10*composition_CO2_normalized_1**1*FDS_normalized_1**0 
				+ p01*composition_CO2_normalized_1**0*FDS_normalized_1**1 
				+ p20*composition_CO2_normalized_1**2*FDS_normalized_1**0 
				+ p11*composition_CO2_normalized_1**1*FDS_normalized_1**1 
				+ p02*composition_CO2_normalized_1**0*FDS_normalized_1**2 
				+ p30*composition_CO2_normalized_1**3*FDS_normalized_1**0 
				+ p21*composition_CO2_normalized_1**2*FDS_normalized_1**1
				+ p12*composition_CO2_normalized_1**1*FDS_normalized_1**2 
				+ p03*composition_CO2_normalized_1**0*FDS_normalized_1**3 
				+ p31*composition_CO2_normalized_1**3*FDS_normalized_1**1 
				+ p22*composition_CO2_normalized_1**2*FDS_normalized_1**2
				+ p13*composition_CO2_normalized_1**1*FDS_normalized_1**3 
				+ p04*composition_CO2_normalized_1**0*FDS_normalized_1**4)

				pressure2 = (p00*composition_CO2_normalized_2**0*FDS_normalized_2**0 
				+ p10*composition_CO2_normalized_2**1*FDS_normalized_2**0 
				+ p01*composition_CO2_normalized_2**0*FDS_normalized_2**1 
				+ p20*composition_CO2_normalized_2**2*FDS_normalized_2**0
				+ p11*composition_CO2_normalized_2**1*FDS_normalized_2**1 
				+ p02*composition_CO2_normalized_2**0*FDS_normalized_2**2
				+ p30*composition_CO2_normalized_2**3*FDS_normalized_2**0 
				+ p21*composition_CO2_normalized_2**2*FDS_normalized_2**1
				+ p12*composition_CO2_normalized_2**1*FDS_normalized_2**2 
				+ p03*composition_CO2_normalized_2**0*FDS_normalized_2**3 
				+ p31*composition_CO2_normalized_2**3*FDS_normalized_2**1 
				+ p22*composition_CO2_normalized_2**2*FDS_normalized_2**2
				+ p13*composition_CO2_normalized_2**1*FDS_normalized_2**3 
				+ p04*composition_CO2_normalized_2**0*FDS_normalized_2**4)

				pressure3 = (p00*composition_CO2_normalized_1**0*FDS_normalized_2**0 
				+ p10*composition_CO2_normalized_1**1*FDS_normalized_2**0 
				+ p01*composition_CO2_normalized_1**0*FDS_normalized_2**1 
				+ p20*composition_CO2_normalized_1**2*FDS_normalized_2**0
				+ p11*composition_CO2_normalized_1**1*FDS_normalized_2**1 
				+ p02*composition_CO2_normalized_1**0*FDS_normalized_2**2 
				+ p30*composition_CO2_normalized_1**3*FDS_normalized_2**0 
				+ p21*composition_CO2_normalized_1**2*FDS_normalized_2**1
				+ p12*composition_CO2_normalized_1**1*FDS_normalized_2**2 
				+ p03*composition_CO2_normalized_1**0*FDS_normalized_2**3 
				+ p31*composition_CO2_normalized_1**3*FDS_normalized_2**1 
				+ p22*composition_CO2_normalized_1**2*FDS_normalized_2**2
				+ p13*composition_CO2_normalized_1**1*FDS_normalized_2**3 
				+ p04*composition_CO2_normalized_1**0*FDS_normalized_2**4)

				pressure4 = (p00*composition_CO2_normalized_2**0*FDS_normalized_1**0 
				+ p10*composition_CO2_normalized_2**1*FDS_normalized_1**0 
				+ p01*composition_CO2_normalized_2**0*FDS_normalized_1**1 
				+ p20*composition_CO2_normalized_2**2*FDS_normalized_1**0
				+ p11*composition_CO2_normalized_2**1*FDS_normalized_1**1 
				+ p02*composition_CO2_normalized_2**0*FDS_normalized_1**2 
				+ p30*composition_CO2_normalized_2**3*FDS_normalized_1**0 
				+ p21*composition_CO2_normalized_2**2*FDS_normalized_1**1
				+ p12*composition_CO2_normalized_2**1*FDS_normalized_1**2 
				+ p03*composition_CO2_normalized_2**0*FDS_normalized_1**3 
				+ p31*composition_CO2_normalized_2**3*FDS_normalized_1**1 
				+ p22*composition_CO2_normalized_2**2*FDS_normalized_1**2
				+ p13*composition_CO2_normalized_2**1*FDS_normalized_1**3 
				+ p04*composition_CO2_normalized_2**0*FDS_normalized_1**4)

				########################
				#### density calculation

				density1 = (d00*composition_CO2_normalized_1**0*FDS_normalized_1**0 
				+ d10*composition_CO2_normalized_1**1*FDS_normalized_1**0 
				+ d01*composition_CO2_normalized_1**0*FDS_normalized_1**1 
				+ d20*composition_CO2_normalized_1**2*FDS_normalized_1**0 
				+ d11*composition_CO2_normalized_1**1*FDS_normalized_1**1 
				+ d02*composition_CO2_normalized_1**0*FDS_normalized_1**2 
				+ d30*composition_CO2_normalized_1**3*FDS_normalized_1**0 
				+ d21*composition_CO2_normalized_1**2*FDS_normalized_1**1
				+ d12*composition_CO2_normalized_1**1*FDS_normalized_1**2 
				+ d03*composition_CO2_normalized_1**0*FDS_normalized_1**3 
				+ d31*composition_CO2_normalized_1**3*FDS_normalized_1**1 
				+ d22*composition_CO2_normalized_1**2*FDS_normalized_1**2
				+ d13*composition_CO2_normalized_1**1*FDS_normalized_1**3 
				+ d04*composition_CO2_normalized_1**0*FDS_normalized_1**4)

				density2 = (d00*composition_CO2_normalized_2**0*FDS_normalized_2**0 
				+ d10*composition_CO2_normalized_2**1*FDS_normalized_2**0 
				+ d01*composition_CO2_normalized_2**0*FDS_normalized_2**1 
				+ d20*composition_CO2_normalized_2**2*FDS_normalized_2**0
				+ d11*composition_CO2_normalized_2**1*FDS_normalized_2**1 
				+ d02*composition_CO2_normalized_2**0*FDS_normalized_2**2
				+ d30*composition_CO2_normalized_2**3*FDS_normalized_2**0 
				+ d21*composition_CO2_normalized_2**2*FDS_normalized_2**1
				+ d12*composition_CO2_normalized_2**1*FDS_normalized_2**2 
				+ d03*composition_CO2_normalized_2**0*FDS_normalized_2**3 
				+ d31*composition_CO2_normalized_2**3*FDS_normalized_2**1 
				+ d22*composition_CO2_normalized_2**2*FDS_normalized_2**2
				+ d13*composition_CO2_normalized_2**1*FDS_normalized_2**3 
				+ d04*composition_CO2_normalized_2**0*FDS_normalized_2**4)

				density3 = (d00*composition_CO2_normalized_1**0*FDS_normalized_2**0 
				+ d10*composition_CO2_normalized_1**1*FDS_normalized_2**0 
				+ d01*composition_CO2_normalized_1**0*FDS_normalized_2**1 
				+ d20*composition_CO2_normalized_1**2*FDS_normalized_2**0
				+ d11*composition_CO2_normalized_1**1*FDS_normalized_2**1 
				+ d02*composition_CO2_normalized_1**0*FDS_normalized_2**2 
				+ d30*composition_CO2_normalized_1**3*FDS_normalized_2**0 
				+ d21*composition_CO2_normalized_1**2*FDS_normalized_2**1
				+ d12*composition_CO2_normalized_1**1*FDS_normalized_2**2 
				+ d03*composition_CO2_normalized_1**0*FDS_normalized_2**3 
				+ d31*composition_CO2_normalized_1**3*FDS_normalized_2**1 
				+ d22*composition_CO2_normalized_1**2*FDS_normalized_2**2
				+ d13*composition_CO2_normalized_1**1*FDS_normalized_2**3 
				+ d04*composition_CO2_normalized_1**0*FDS_normalized_2**4)

				density4 = (d00*composition_CO2_normalized_2**0*FDS_normalized_1**0 
				+ d10*composition_CO2_normalized_2**1*FDS_normalized_1**0 
				+ d01*composition_CO2_normalized_2**0*FDS_normalized_1**1 
				+ d20*composition_CO2_normalized_2**2*FDS_normalized_1**0
				+ d11*composition_CO2_normalized_2**1*FDS_normalized_1**1 
				+ d02*composition_CO2_normalized_2**0*FDS_normalized_1**2 
				+ d30*composition_CO2_normalized_2**3*FDS_normalized_1**0 
				+ d21*composition_CO2_normalized_2**2*FDS_normalized_1**1
				+ d12*composition_CO2_normalized_2**1*FDS_normalized_1**2 
				+ d03*composition_CO2_normalized_2**0*FDS_normalized_1**3 
				+ d31*composition_CO2_normalized_2**3*FDS_normalized_1**1 
				+ d22*composition_CO2_normalized_2**2*FDS_normalized_1**2
				+ d13*composition_CO2_normalized_2**1*FDS_normalized_1**3 
				+ d04*composition_CO2_normalized_2**0*FDS_normalized_1**4)              

				pressure_final = (max(pressure1, pressure2, pressure3, pressure4) + min(pressure1, pressure2, pressure3, pressure4))/2 #pressure max - pressure min
				uncer_pressure_final = 7.1 + (max(pressure1, pressure2, pressure3, pressure4) - min(pressure1, pressure2, pressure3, pressure4))/(2*np.sqrt(3))

				density_final = (max(density1, density2, density3, density4) + min(density1, density2, density3, density4))/2 #density max - density min
				uncer_density_final = 0.005 + (max(density1, density2, density3, density4) - min(density1, density2, density3, density4))/(2*np.sqrt(3))

				molarvolume1 = 1/(max(density1, density2, density3, density4)/(44*composition_CO2 + 28*composition_N2))
				molarvolume2 = 1/(min(density1, density2, density3, density4)/(44*composition_CO2 + 28*composition_N2))
				
				molarvolume_final = (molarvolume1 + molarvolume2) / 2
				uncer_molarvolume_final = (molarvolume2 - molarvolume1) / (2*np.sqrt(3))


				##### verify if measured pressure < 160 bar, if it is, re-recalculte using calibration data for 5-160 bar range.
				if pressure_final <= 150: 

					## Calibration equation's coeff of CO2-N2 at 22 °C over 5-160 bars
					# normalisation of concentration and of Fermi diad splitting
					
					composition_CO2_normalized_1 = (composition_CO2 + 0.005)
					composition_CO2_normalized_2 = (composition_CO2 - 0.005)
					FDS_normalized_1 = (FDS + unc_FDS - FDS_std)
					FDS_normalized_2 = (FDS - unc_FDS - FDS_std)
										
					p00= 8.93137439510
					p10= -50.3006836
					p01= 1814.66658242
					p20= 29.398135320
					p11= -7550.765206
					p02= -406.4094371
					p30= 70.929005595
					p21= 17082.171328
					p12= -6973.1727710
					p03= 5905.0985154
					p31= -15617.520181
					p22= 15041.744214
					p13= -11712.85260
					p04= 44.60796474

					d00= 0.011259825
					d10= -0.07029199
					d01= 2.10776069
					d20= 0.06570404
					d11= -7.48047611
					d02= -0.62185552
					d30= 0.06163883
					d21= 15.9382494
					d12=-6.10767931
					d03= 6.501686977
					d31= -14.6979892
					d22= 16.0662993
					d13= -13.5700840
					d04= 0.0729528

					#### pressure calculation
					pressure1 = (p00*composition_CO2_normalized_1**0*FDS_normalized_1**0 
					+ p10*composition_CO2_normalized_1**1*FDS_normalized_1**0 
					+ p01*composition_CO2_normalized_1**0*FDS_normalized_1**1 
					+ p20*composition_CO2_normalized_1**2*FDS_normalized_1**0 
					+ p11*composition_CO2_normalized_1**1*FDS_normalized_1**1 
					+ p02*composition_CO2_normalized_1**0*FDS_normalized_1**2 
					+ p30*composition_CO2_normalized_1**3*FDS_normalized_1**0 
					+ p21*composition_CO2_normalized_1**2*FDS_normalized_1**1
					+ p12*composition_CO2_normalized_1**1*FDS_normalized_1**2 
					+ p03*composition_CO2_normalized_1**0*FDS_normalized_1**3 
					+ p31*composition_CO2_normalized_1**3*FDS_normalized_1**1 
					+ p22*composition_CO2_normalized_1**2*FDS_normalized_1**2
					+ p13*composition_CO2_normalized_1**1*FDS_normalized_1**3 
					+ p04*composition_CO2_normalized_1**0*FDS_normalized_1**4)

					pressure2 = (p00*composition_CO2_normalized_2**0*FDS_normalized_2**0 
					+ p10*composition_CO2_normalized_2**1*FDS_normalized_2**0 
					+ p01*composition_CO2_normalized_2**0*FDS_normalized_2**1 
					+ p20*composition_CO2_normalized_2**2*FDS_normalized_2**0
					+ p11*composition_CO2_normalized_2**1*FDS_normalized_2**1 
					+ p02*composition_CO2_normalized_2**0*FDS_normalized_2**2
					+ p30*composition_CO2_normalized_2**3*FDS_normalized_2**0 
					+ p21*composition_CO2_normalized_2**2*FDS_normalized_2**1
					+ p12*composition_CO2_normalized_2**1*FDS_normalized_2**2 
					+ p03*composition_CO2_normalized_2**0*FDS_normalized_2**3 
					+ p31*composition_CO2_normalized_2**3*FDS_normalized_2**1 
					+ p22*composition_CO2_normalized_2**2*FDS_normalized_2**2
					+ p13*composition_CO2_normalized_2**1*FDS_normalized_2**3 
					+ p04*composition_CO2_normalized_2**0*FDS_normalized_2**4)

					pressure3 = (p00*composition_CO2_normalized_1**0*FDS_normalized_2**0 
					+ p10*composition_CO2_normalized_1**1*FDS_normalized_2**0 
					+ p01*composition_CO2_normalized_1**0*FDS_normalized_2**1 
					+ p20*composition_CO2_normalized_1**2*FDS_normalized_2**0
					+ p11*composition_CO2_normalized_1**1*FDS_normalized_2**1 
					+ p02*composition_CO2_normalized_1**0*FDS_normalized_2**2 
					+ p30*composition_CO2_normalized_1**3*FDS_normalized_2**0 
					+ p21*composition_CO2_normalized_1**2*FDS_normalized_2**1
					+ p12*composition_CO2_normalized_1**1*FDS_normalized_2**2 
					+ p03*composition_CO2_normalized_1**0*FDS_normalized_2**3 
					+ p31*composition_CO2_normalized_1**3*FDS_normalized_2**1 
					+ p22*composition_CO2_normalized_1**2*FDS_normalized_2**2
					+ p13*composition_CO2_normalized_1**1*FDS_normalized_2**3 
					+ p04*composition_CO2_normalized_1**0*FDS_normalized_2**4)

					pressure4 = (p00*composition_CO2_normalized_2**0*FDS_normalized_1**0 
					+ p10*composition_CO2_normalized_2**1*FDS_normalized_1**0 
					+ p01*composition_CO2_normalized_2**0*FDS_normalized_1**1 
					+ p20*composition_CO2_normalized_2**2*FDS_normalized_1**0
					+ p11*composition_CO2_normalized_2**1*FDS_normalized_1**1 
					+ p02*composition_CO2_normalized_2**0*FDS_normalized_1**2 
					+ p30*composition_CO2_normalized_2**3*FDS_normalized_1**0 
					+ p21*composition_CO2_normalized_2**2*FDS_normalized_1**1
					+ p12*composition_CO2_normalized_2**1*FDS_normalized_1**2 
					+ p03*composition_CO2_normalized_2**0*FDS_normalized_1**3 
					+ p31*composition_CO2_normalized_2**3*FDS_normalized_1**1 
					+ p22*composition_CO2_normalized_2**2*FDS_normalized_1**2
					+ p13*composition_CO2_normalized_2**1*FDS_normalized_1**3 
					+ p04*composition_CO2_normalized_2**0*FDS_normalized_1**4)

					########################
					#### density calculation

					density1 = (d00*composition_CO2_normalized_1**0*FDS_normalized_1**0 
					+ d10*composition_CO2_normalized_1**1*FDS_normalized_1**0 
					+ d01*composition_CO2_normalized_1**0*FDS_normalized_1**1 
					+ d20*composition_CO2_normalized_1**2*FDS_normalized_1**0 
					+ d11*composition_CO2_normalized_1**1*FDS_normalized_1**1 
					+ d02*composition_CO2_normalized_1**0*FDS_normalized_1**2 
					+ d30*composition_CO2_normalized_1**3*FDS_normalized_1**0 
					+ d21*composition_CO2_normalized_1**2*FDS_normalized_1**1
					+ d12*composition_CO2_normalized_1**1*FDS_normalized_1**2 
					+ d03*composition_CO2_normalized_1**0*FDS_normalized_1**3 
					+ d31*composition_CO2_normalized_1**3*FDS_normalized_1**1 
					+ d22*composition_CO2_normalized_1**2*FDS_normalized_1**2
					+ d13*composition_CO2_normalized_1**1*FDS_normalized_1**3 
					+ d04*composition_CO2_normalized_1**0*FDS_normalized_1**4)

					density2 = (d00*composition_CO2_normalized_2**0*FDS_normalized_2**0 
					+ d10*composition_CO2_normalized_2**1*FDS_normalized_2**0 
					+ d01*composition_CO2_normalized_2**0*FDS_normalized_2**1 
					+ d20*composition_CO2_normalized_2**2*FDS_normalized_2**0
					+ d11*composition_CO2_normalized_2**1*FDS_normalized_2**1 
					+ d02*composition_CO2_normalized_2**0*FDS_normalized_2**2
					+ d30*composition_CO2_normalized_2**3*FDS_normalized_2**0 
					+ d21*composition_CO2_normalized_2**2*FDS_normalized_2**1
					+ d12*composition_CO2_normalized_2**1*FDS_normalized_2**2 
					+ d03*composition_CO2_normalized_2**0*FDS_normalized_2**3 
					+ d31*composition_CO2_normalized_2**3*FDS_normalized_2**1 
					+ d22*composition_CO2_normalized_2**2*FDS_normalized_2**2
					+ d13*composition_CO2_normalized_2**1*FDS_normalized_2**3 
					+ d04*composition_CO2_normalized_2**0*FDS_normalized_2**4)

					density3 = (d00*composition_CO2_normalized_1**0*FDS_normalized_2**0 
					+ d10*composition_CO2_normalized_1**1*FDS_normalized_2**0 
					+ d01*composition_CO2_normalized_1**0*FDS_normalized_2**1 
					+ d20*composition_CO2_normalized_1**2*FDS_normalized_2**0
					+ d11*composition_CO2_normalized_1**1*FDS_normalized_2**1 
					+ d02*composition_CO2_normalized_1**0*FDS_normalized_2**2 
					+ d30*composition_CO2_normalized_1**3*FDS_normalized_2**0 
					+ d21*composition_CO2_normalized_1**2*FDS_normalized_2**1
					+ d12*composition_CO2_normalized_1**1*FDS_normalized_2**2 
					+ d03*composition_CO2_normalized_1**0*FDS_normalized_2**3 
					+ d31*composition_CO2_normalized_1**3*FDS_normalized_2**1 
					+ d22*composition_CO2_normalized_1**2*FDS_normalized_2**2
					+ d13*composition_CO2_normalized_1**1*FDS_normalized_2**3 
					+ d04*composition_CO2_normalized_1**0*FDS_normalized_2**4)

					density4 = (d00*composition_CO2_normalized_2**0*FDS_normalized_1**0 
					+ d10*composition_CO2_normalized_2**1*FDS_normalized_1**0 
					+ d01*composition_CO2_normalized_2**0*FDS_normalized_1**1 
					+ d20*composition_CO2_normalized_2**2*FDS_normalized_1**0
					+ d11*composition_CO2_normalized_2**1*FDS_normalized_1**1 
					+ d02*composition_CO2_normalized_2**0*FDS_normalized_1**2 
					+ d30*composition_CO2_normalized_2**3*FDS_normalized_1**0 
					+ d21*composition_CO2_normalized_2**2*FDS_normalized_1**1
					+ d12*composition_CO2_normalized_2**1*FDS_normalized_1**2 
					+ d03*composition_CO2_normalized_2**0*FDS_normalized_1**3 
					+ d31*composition_CO2_normalized_2**3*FDS_normalized_1**1 
					+ d22*composition_CO2_normalized_2**2*FDS_normalized_1**2
					+ d13*composition_CO2_normalized_2**1*FDS_normalized_1**3 
					+ d04*composition_CO2_normalized_2**0*FDS_normalized_1**4)              

					pressure_final = (max(pressure1, pressure2, pressure3, pressure4) + min(pressure1, pressure2, pressure3, pressure4))/2 #pressure max - pressure min
					uncer_pressure_final = 2.83 + (max(pressure1, pressure2, pressure3, pressure4) - min(pressure1, pressure2, pressure3, pressure4))/(2*np.sqrt(3)) #uncertain 4

					density_final = (max(density1, density2, density3, density4) + min(density1, density2, density3, density4))/2 #density max - density min
					uncer_density_final = 0.0035 + (max(density1, density2, density3, density4) - min(density1, density2, density3, density4))/(2*np.sqrt(3)) #uncertainty 0.005

					molarvolume1 = 1/(max(density1, density2, density3, density4)/(44*composition_CO2 + 28*composition_N2))
					molarvolume2 = 1/(min(density1, density2, density3, density4)/(44*composition_CO2 + 28*composition_N2))		
					molarvolume_final = (molarvolume1 + molarvolume2) / 2
					uncer_molarvolume_final = (molarvolume2 - molarvolume1) / (2*np.sqrt(3))
				print('composition normalized', composition_CO2_normalized_1)

				print('pressure1', pressure1)
				print('pressure2', pressure2)
				print('pressure3', pressure3)
				print('pressure4', pressure4)

				print('density 1=', density1)
				print('density 2=', density2)
				print('density 3=', density3)
				print('density 4=', density4)
				
				print("molarvolume1", molarvolume1)
				print("molarvolume2", molarvolume2)
				if pressure_final > 650 or pressure1 >650 or pressure2 >650 or pressure_final < -20 or pressure1 <-20 or pressure2 <-20 or density2<0 or density1 <0 or density3<0 or density4<0 or density_final<0 :
					popupmsg_OCR()


			## Calibration equation's coeff of CO2-N2 at 32 °C over 5-500 bars
			if temperature.get() == 32 and composition_CO2 >= 0.5 and instrument.get() ==2: 

				
				# normalisation of concentration and of Fermi diad splitting
				composition_CO2_normalized_1 = (composition_CO2 + 0.005)
				composition_CO2_normalized_2 = (composition_CO2 - 0.005)
				FDS_normalized_1 = (FDS + unc_FDS - FDS_std)
				FDS_normalized_2 = (FDS - unc_FDS - FDS_std)
				
				
				p00= -141.2216310
				p10= 682.70990875
				p01= 2377.95903301
				p20= -1033.8019225
				p11= -8587.5470205
				p02= 782.69624327
				p30= 492.546066759
				p21= 11797.1779749
				p12= -2971.8183285
				p03= 533.51023525
				p31= -5410.4571648
				p22= 2092.09932387
				p13= -576.57314702
				p04= 33.947851705

				d00= 0.32255666
				d10= -1.373203489
				d01= 1.9821200969
				d20= 1.9015046299
				d11= -5.11373286
				d02= 0.0731842214
				d30= -0.84812812923
				d21= 5.30758829
				d12= 0.58991498
				d03= -0.20996789289
				d31= -1.9094265678
				d22= -0.46202084155
				d13= 0.1357534039
				d04= 0.006276158

				#### pressure calculation
				pressure1 = (p00*composition_CO2_normalized_1**0*FDS_normalized_1**0 
				+ p10*composition_CO2_normalized_1**1*FDS_normalized_1**0 
				+ p01*composition_CO2_normalized_1**0*FDS_normalized_1**1 
				+ p20*composition_CO2_normalized_1**2*FDS_normalized_1**0 
				+ p11*composition_CO2_normalized_1**1*FDS_normalized_1**1 
				+ p02*composition_CO2_normalized_1**0*FDS_normalized_1**2 
				+ p30*composition_CO2_normalized_1**3*FDS_normalized_1**0 
				+ p21*composition_CO2_normalized_1**2*FDS_normalized_1**1
				+ p12*composition_CO2_normalized_1**1*FDS_normalized_1**2 
				+ p03*composition_CO2_normalized_1**0*FDS_normalized_1**3 
				+ p31*composition_CO2_normalized_1**3*FDS_normalized_1**1 
				+ p22*composition_CO2_normalized_1**2*FDS_normalized_1**2
				+ p13*composition_CO2_normalized_1**1*FDS_normalized_1**3 
				+ p04*composition_CO2_normalized_1**0*FDS_normalized_1**4)

				pressure2 = (p00*composition_CO2_normalized_2**0*FDS_normalized_2**0 
				+ p10*composition_CO2_normalized_2**1*FDS_normalized_2**0 
				+ p01*composition_CO2_normalized_2**0*FDS_normalized_2**1 
				+ p20*composition_CO2_normalized_2**2*FDS_normalized_2**0
				+ p11*composition_CO2_normalized_2**1*FDS_normalized_2**1 
				+ p02*composition_CO2_normalized_2**0*FDS_normalized_2**2
				+ p30*composition_CO2_normalized_2**3*FDS_normalized_2**0 
				+ p21*composition_CO2_normalized_2**2*FDS_normalized_2**1
				+ p12*composition_CO2_normalized_2**1*FDS_normalized_2**2 
				+ p03*composition_CO2_normalized_2**0*FDS_normalized_2**3 
				+ p31*composition_CO2_normalized_2**3*FDS_normalized_2**1 
				+ p22*composition_CO2_normalized_2**2*FDS_normalized_2**2
				+ p13*composition_CO2_normalized_2**1*FDS_normalized_2**3 
				+ p04*composition_CO2_normalized_2**0*FDS_normalized_2**4)

				pressure3 = (p00*composition_CO2_normalized_1**0*FDS_normalized_2**0 
				+ p10*composition_CO2_normalized_1**1*FDS_normalized_2**0 
				+ p01*composition_CO2_normalized_1**0*FDS_normalized_2**1 
				+ p20*composition_CO2_normalized_1**2*FDS_normalized_2**0
				+ p11*composition_CO2_normalized_1**1*FDS_normalized_2**1 
				+ p02*composition_CO2_normalized_1**0*FDS_normalized_2**2 
				+ p30*composition_CO2_normalized_1**3*FDS_normalized_2**0 
				+ p21*composition_CO2_normalized_1**2*FDS_normalized_2**1
				+ p12*composition_CO2_normalized_1**1*FDS_normalized_2**2 
				+ p03*composition_CO2_normalized_1**0*FDS_normalized_2**3 
				+ p31*composition_CO2_normalized_1**3*FDS_normalized_2**1 
				+ p22*composition_CO2_normalized_1**2*FDS_normalized_2**2
				+ p13*composition_CO2_normalized_1**1*FDS_normalized_2**3 
				+ p04*composition_CO2_normalized_1**0*FDS_normalized_2**4)

				pressure4 = (p00*composition_CO2_normalized_2**0*FDS_normalized_1**0 
				+ p10*composition_CO2_normalized_2**1*FDS_normalized_1**0 
				+ p01*composition_CO2_normalized_2**0*FDS_normalized_1**1 
				+ p20*composition_CO2_normalized_2**2*FDS_normalized_1**0
				+ p11*composition_CO2_normalized_2**1*FDS_normalized_1**1 
				+ p02*composition_CO2_normalized_2**0*FDS_normalized_1**2 
				+ p30*composition_CO2_normalized_2**3*FDS_normalized_1**0 
				+ p21*composition_CO2_normalized_2**2*FDS_normalized_1**1
				+ p12*composition_CO2_normalized_2**1*FDS_normalized_1**2 
				+ p03*composition_CO2_normalized_2**0*FDS_normalized_1**3 
				+ p31*composition_CO2_normalized_2**3*FDS_normalized_1**1 
				+ p22*composition_CO2_normalized_2**2*FDS_normalized_1**2
				+ p13*composition_CO2_normalized_2**1*FDS_normalized_1**3 
				+ p04*composition_CO2_normalized_2**0*FDS_normalized_1**4)

				########################
				#### density calculation

				density1 = (d00*composition_CO2_normalized_1**0*FDS_normalized_1**0 
				+ d10*composition_CO2_normalized_1**1*FDS_normalized_1**0 
				+ d01*composition_CO2_normalized_1**0*FDS_normalized_1**1 
				+ d20*composition_CO2_normalized_1**2*FDS_normalized_1**0 
				+ d11*composition_CO2_normalized_1**1*FDS_normalized_1**1 
				+ d02*composition_CO2_normalized_1**0*FDS_normalized_1**2 
				+ d30*composition_CO2_normalized_1**3*FDS_normalized_1**0 
				+ d21*composition_CO2_normalized_1**2*FDS_normalized_1**1
				+ d12*composition_CO2_normalized_1**1*FDS_normalized_1**2 
				+ d03*composition_CO2_normalized_1**0*FDS_normalized_1**3 
				+ d31*composition_CO2_normalized_1**3*FDS_normalized_1**1 
				+ d22*composition_CO2_normalized_1**2*FDS_normalized_1**2
				+ d13*composition_CO2_normalized_1**1*FDS_normalized_1**3 
				+ d04*composition_CO2_normalized_1**0*FDS_normalized_1**4)

				density2 = (d00*composition_CO2_normalized_2**0*FDS_normalized_2**0 
				+ d10*composition_CO2_normalized_2**1*FDS_normalized_2**0 
				+ d01*composition_CO2_normalized_2**0*FDS_normalized_2**1 
				+ d20*composition_CO2_normalized_2**2*FDS_normalized_2**0
				+ d11*composition_CO2_normalized_2**1*FDS_normalized_2**1 
				+ d02*composition_CO2_normalized_2**0*FDS_normalized_2**2
				+ d30*composition_CO2_normalized_2**3*FDS_normalized_2**0 
				+ d21*composition_CO2_normalized_2**2*FDS_normalized_2**1
				+ d12*composition_CO2_normalized_2**1*FDS_normalized_2**2 
				+ d03*composition_CO2_normalized_2**0*FDS_normalized_2**3 
				+ d31*composition_CO2_normalized_2**3*FDS_normalized_2**1 
				+ d22*composition_CO2_normalized_2**2*FDS_normalized_2**2
				+ d13*composition_CO2_normalized_2**1*FDS_normalized_2**3 
				+ d04*composition_CO2_normalized_2**0*FDS_normalized_2**4)

				density3 = (d00*composition_CO2_normalized_1**0*FDS_normalized_2**0 
				+ d10*composition_CO2_normalized_1**1*FDS_normalized_2**0 
				+ d01*composition_CO2_normalized_1**0*FDS_normalized_2**1 
				+ d20*composition_CO2_normalized_1**2*FDS_normalized_2**0
				+ d11*composition_CO2_normalized_1**1*FDS_normalized_2**1 
				+ d02*composition_CO2_normalized_1**0*FDS_normalized_2**2 
				+ d30*composition_CO2_normalized_1**3*FDS_normalized_2**0 
				+ d21*composition_CO2_normalized_1**2*FDS_normalized_2**1
				+ d12*composition_CO2_normalized_1**1*FDS_normalized_2**2 
				+ d03*composition_CO2_normalized_1**0*FDS_normalized_2**3 
				+ d31*composition_CO2_normalized_1**3*FDS_normalized_2**1 
				+ d22*composition_CO2_normalized_1**2*FDS_normalized_2**2
				+ d13*composition_CO2_normalized_1**1*FDS_normalized_2**3 
				+ d04*composition_CO2_normalized_1**0*FDS_normalized_2**4)

				density4 = (d00*composition_CO2_normalized_2**0*FDS_normalized_1**0 
				+ d10*composition_CO2_normalized_2**1*FDS_normalized_1**0 
				+ d01*composition_CO2_normalized_2**0*FDS_normalized_1**1 
				+ d20*composition_CO2_normalized_2**2*FDS_normalized_1**0
				+ d11*composition_CO2_normalized_2**1*FDS_normalized_1**1 
				+ d02*composition_CO2_normalized_2**0*FDS_normalized_1**2 
				+ d30*composition_CO2_normalized_2**3*FDS_normalized_1**0 
				+ d21*composition_CO2_normalized_2**2*FDS_normalized_1**1
				+ d12*composition_CO2_normalized_2**1*FDS_normalized_1**2 
				+ d03*composition_CO2_normalized_2**0*FDS_normalized_1**3 
				+ d31*composition_CO2_normalized_2**3*FDS_normalized_1**1 
				+ d22*composition_CO2_normalized_2**2*FDS_normalized_1**2
				+ d13*composition_CO2_normalized_2**1*FDS_normalized_1**3 
				+ d04*composition_CO2_normalized_2**0*FDS_normalized_1**4)              

				pressure_final = (max(pressure1, pressure2, pressure3, pressure4) + min(pressure1, pressure2, pressure3, pressure4))/2 #pressure max - pressure min
				uncer_pressure_final = 7.78 + (max(pressure1, pressure2, pressure3, pressure4) - min(pressure1, pressure2, pressure3, pressure4))/(2*np.sqrt(3))

				density_final = (max(density1, density2, density3, density4) + min(density1, density2, density3, density4))/2 #density max - density min
				uncer_density_final = 0.0057 + (max(density1, density2, density3, density4) - min(density1, density2, density3, density4))/(2*np.sqrt(3))

				molarvolume1 = 1/(max(density1, density2, density3, density4)/(44*composition_CO2 + 28*composition_N2))
				molarvolume2 = 1/(min(density1, density2, density3, density4)/(44*composition_CO2 + 28*composition_N2))		
				molarvolume_final = (molarvolume1 + molarvolume2 )/ 2
				uncer_molarvolume_final = (molarvolume2 - molarvolume1) / (2*np.sqrt(3))
				
				print('composition normalized', composition_CO2_normalized_1)


				##### verify if measured pressure < 160 bar, if it is, re-recalculte using calibration data for 5-160 bar range.
				if pressure_final <= 150: 

					## Calibration equation's coeff of CO2-N2 at 22 °C over 5-160 bars
					# normalisation of concentration and of Fermi diad splitting
					
					composition_CO2_normalized_1 = (composition_CO2 + 0.005)
					composition_CO2_normalized_2 = (composition_CO2 - 0.005)
					FDS_normalized_1 = (FDS + unc_FDS - FDS_std)
					FDS_normalized_2 = (FDS - unc_FDS - FDS_std)
										
					p00= 44.65265878
					p10= -178.2175349
					p01= 1317.0235799
					p20= 228.7643461
					p11= -3376.4771457
					p02= 63.581160796
					p30= -94.0700019
					p21= 3759.5782522
					p12= -848.4445978
					p03= 348.836492741
					p31= -1534.819959
					p22= 721.8
					p13= -415.54978249
					p04= 38.400904198

					d00= 0.014507725
					d10= -0.086463979
					d01= 2.4096559176
					d20= 0.152268386
					d11= -6.7341099
					d02= -0.11631383
					d30= -0.0749366306
					d21= 7.4777100327
					d12= 0.8075136733
					d03= -0.136942356
					d31= -2.902051419
					d22= -0.4606424387
					d13= 0.04095626079
					d04= 0.01160591898

					#### pressure calculation
					pressure1 = (p00*composition_CO2_normalized_1**0*FDS_normalized_1**0 
					+ p10*composition_CO2_normalized_1**1*FDS_normalized_1**0 
					+ p01*composition_CO2_normalized_1**0*FDS_normalized_1**1 
					+ p20*composition_CO2_normalized_1**2*FDS_normalized_1**0 
					+ p11*composition_CO2_normalized_1**1*FDS_normalized_1**1 
					+ p02*composition_CO2_normalized_1**0*FDS_normalized_1**2 
					+ p30*composition_CO2_normalized_1**3*FDS_normalized_1**0 
					+ p21*composition_CO2_normalized_1**2*FDS_normalized_1**1
					+ p12*composition_CO2_normalized_1**1*FDS_normalized_1**2 
					+ p03*composition_CO2_normalized_1**0*FDS_normalized_1**3 
					+ p31*composition_CO2_normalized_1**3*FDS_normalized_1**1 
					+ p22*composition_CO2_normalized_1**2*FDS_normalized_1**2
					+ p13*composition_CO2_normalized_1**1*FDS_normalized_1**3 
					+ p04*composition_CO2_normalized_1**0*FDS_normalized_1**4)

					pressure2 = (p00*composition_CO2_normalized_2**0*FDS_normalized_2**0 
					+ p10*composition_CO2_normalized_2**1*FDS_normalized_2**0 
					+ p01*composition_CO2_normalized_2**0*FDS_normalized_2**1 
					+ p20*composition_CO2_normalized_2**2*FDS_normalized_2**0
					+ p11*composition_CO2_normalized_2**1*FDS_normalized_2**1 
					+ p02*composition_CO2_normalized_2**0*FDS_normalized_2**2
					+ p30*composition_CO2_normalized_2**3*FDS_normalized_2**0 
					+ p21*composition_CO2_normalized_2**2*FDS_normalized_2**1
					+ p12*composition_CO2_normalized_2**1*FDS_normalized_2**2 
					+ p03*composition_CO2_normalized_2**0*FDS_normalized_2**3 
					+ p31*composition_CO2_normalized_2**3*FDS_normalized_2**1 
					+ p22*composition_CO2_normalized_2**2*FDS_normalized_2**2
					+ p13*composition_CO2_normalized_2**1*FDS_normalized_2**3 
					+ p04*composition_CO2_normalized_2**0*FDS_normalized_2**4)

					pressure3 = (p00*composition_CO2_normalized_1**0*FDS_normalized_2**0 
					+ p10*composition_CO2_normalized_1**1*FDS_normalized_2**0 
					+ p01*composition_CO2_normalized_1**0*FDS_normalized_2**1 
					+ p20*composition_CO2_normalized_1**2*FDS_normalized_2**0
					+ p11*composition_CO2_normalized_1**1*FDS_normalized_2**1 
					+ p02*composition_CO2_normalized_1**0*FDS_normalized_2**2 
					+ p30*composition_CO2_normalized_1**3*FDS_normalized_2**0 
					+ p21*composition_CO2_normalized_1**2*FDS_normalized_2**1
					+ p12*composition_CO2_normalized_1**1*FDS_normalized_2**2 
					+ p03*composition_CO2_normalized_1**0*FDS_normalized_2**3 
					+ p31*composition_CO2_normalized_1**3*FDS_normalized_2**1 
					+ p22*composition_CO2_normalized_1**2*FDS_normalized_2**2
					+ p13*composition_CO2_normalized_1**1*FDS_normalized_2**3 
					+ p04*composition_CO2_normalized_1**0*FDS_normalized_2**4)

					pressure4 = (p00*composition_CO2_normalized_2**0*FDS_normalized_1**0 
					+ p10*composition_CO2_normalized_2**1*FDS_normalized_1**0 
					+ p01*composition_CO2_normalized_2**0*FDS_normalized_1**1 
					+ p20*composition_CO2_normalized_2**2*FDS_normalized_1**0
					+ p11*composition_CO2_normalized_2**1*FDS_normalized_1**1 
					+ p02*composition_CO2_normalized_2**0*FDS_normalized_1**2 
					+ p30*composition_CO2_normalized_2**3*FDS_normalized_1**0 
					+ p21*composition_CO2_normalized_2**2*FDS_normalized_1**1
					+ p12*composition_CO2_normalized_2**1*FDS_normalized_1**2 
					+ p03*composition_CO2_normalized_2**0*FDS_normalized_1**3 
					+ p31*composition_CO2_normalized_2**3*FDS_normalized_1**1 
					+ p22*composition_CO2_normalized_2**2*FDS_normalized_1**2
					+ p13*composition_CO2_normalized_2**1*FDS_normalized_1**3 
					+ p04*composition_CO2_normalized_2**0*FDS_normalized_1**4)

					########################
					#### density calculation

					density1 = (d00*composition_CO2_normalized_1**0*FDS_normalized_1**0 
					+ d10*composition_CO2_normalized_1**1*FDS_normalized_1**0 
					+ d01*composition_CO2_normalized_1**0*FDS_normalized_1**1 
					+ d20*composition_CO2_normalized_1**2*FDS_normalized_1**0 
					+ d11*composition_CO2_normalized_1**1*FDS_normalized_1**1 
					+ d02*composition_CO2_normalized_1**0*FDS_normalized_1**2 
					+ d30*composition_CO2_normalized_1**3*FDS_normalized_1**0 
					+ d21*composition_CO2_normalized_1**2*FDS_normalized_1**1
					+ d12*composition_CO2_normalized_1**1*FDS_normalized_1**2 
					+ d03*composition_CO2_normalized_1**0*FDS_normalized_1**3 
					+ d31*composition_CO2_normalized_1**3*FDS_normalized_1**1 
					+ d22*composition_CO2_normalized_1**2*FDS_normalized_1**2
					+ d13*composition_CO2_normalized_1**1*FDS_normalized_1**3 
					+ d04*composition_CO2_normalized_1**0*FDS_normalized_1**4)

					density2 = (d00*composition_CO2_normalized_2**0*FDS_normalized_2**0 
					+ d10*composition_CO2_normalized_2**1*FDS_normalized_2**0 
					+ d01*composition_CO2_normalized_2**0*FDS_normalized_2**1 
					+ d20*composition_CO2_normalized_2**2*FDS_normalized_2**0
					+ d11*composition_CO2_normalized_2**1*FDS_normalized_2**1 
					+ d02*composition_CO2_normalized_2**0*FDS_normalized_2**2
					+ d30*composition_CO2_normalized_2**3*FDS_normalized_2**0 
					+ d21*composition_CO2_normalized_2**2*FDS_normalized_2**1
					+ d12*composition_CO2_normalized_2**1*FDS_normalized_2**2 
					+ d03*composition_CO2_normalized_2**0*FDS_normalized_2**3 
					+ d31*composition_CO2_normalized_2**3*FDS_normalized_2**1 
					+ d22*composition_CO2_normalized_2**2*FDS_normalized_2**2
					+ d13*composition_CO2_normalized_2**1*FDS_normalized_2**3 
					+ d04*composition_CO2_normalized_2**0*FDS_normalized_2**4)

					density3 = (d00*composition_CO2_normalized_1**0*FDS_normalized_2**0 
					+ d10*composition_CO2_normalized_1**1*FDS_normalized_2**0 
					+ d01*composition_CO2_normalized_1**0*FDS_normalized_2**1 
					+ d20*composition_CO2_normalized_1**2*FDS_normalized_2**0
					+ d11*composition_CO2_normalized_1**1*FDS_normalized_2**1 
					+ d02*composition_CO2_normalized_1**0*FDS_normalized_2**2 
					+ d30*composition_CO2_normalized_1**3*FDS_normalized_2**0 
					+ d21*composition_CO2_normalized_1**2*FDS_normalized_2**1
					+ d12*composition_CO2_normalized_1**1*FDS_normalized_2**2 
					+ d03*composition_CO2_normalized_1**0*FDS_normalized_2**3 
					+ d31*composition_CO2_normalized_1**3*FDS_normalized_2**1 
					+ d22*composition_CO2_normalized_1**2*FDS_normalized_2**2
					+ d13*composition_CO2_normalized_1**1*FDS_normalized_2**3 
					+ d04*composition_CO2_normalized_1**0*FDS_normalized_2**4)

					density4 = (d00*composition_CO2_normalized_2**0*FDS_normalized_1**0 
					+ d10*composition_CO2_normalized_2**1*FDS_normalized_1**0 
					+ d01*composition_CO2_normalized_2**0*FDS_normalized_1**1 
					+ d20*composition_CO2_normalized_2**2*FDS_normalized_1**0
					+ d11*composition_CO2_normalized_2**1*FDS_normalized_1**1 
					+ d02*composition_CO2_normalized_2**0*FDS_normalized_1**2 
					+ d30*composition_CO2_normalized_2**3*FDS_normalized_1**0 
					+ d21*composition_CO2_normalized_2**2*FDS_normalized_1**1
					+ d12*composition_CO2_normalized_2**1*FDS_normalized_1**2 
					+ d03*composition_CO2_normalized_2**0*FDS_normalized_1**3 
					+ d31*composition_CO2_normalized_2**3*FDS_normalized_1**1 
					+ d22*composition_CO2_normalized_2**2*FDS_normalized_1**2
					+ d13*composition_CO2_normalized_2**1*FDS_normalized_1**3 
					+ d04*composition_CO2_normalized_2**0*FDS_normalized_1**4)              

					pressure_final = (max(pressure1, pressure2, pressure3, pressure4) + min(pressure1, pressure2, pressure3, pressure4))/2 #pressure max - pressure min
					uncer_pressure_final = 3 + (max(pressure1, pressure2, pressure3, pressure4) - min(pressure1, pressure2, pressure3, pressure4))/(2*np.sqrt(3)) #unce = 4

					density_final = (max(density1, density2, density3, density4) + min(density1, density2, density3, density4))/2 #density max - density min
					uncer_density_final = 0.0049 + (max(density1, density2, density3, density4) - min(density1, density2, density3, density4))/(2*np.sqrt(3)) #uncer= 0.007

					molarvolume1 = 1/(max(density1, density2, density3, density4)/(44*composition_CO2 + 28*composition_N2))
					molarvolume2 = 1/(min(density1, density2, density3, density4)/(44*composition_CO2 + 28*composition_N2))		
					molarvolume_final = (molarvolume1 + molarvolume2 )/ 2
					uncer_molarvolume_final = (molarvolume2 - molarvolume1) / (2*np.sqrt(3))

				print('pressure1', pressure1)
				print('pressure2', pressure2)
				print('pressure3', pressure3)
				print('pressure4', pressure4)

				print('density 1=', density1)
				print('density 2=', density2)
				print('density 3=', density3)
				print('density 4=', density4)

				print("molarvolume1", molarvolume1)
				print("molarvolume2", molarvolume2)
				
				
				if pressure_final > 650 or pressure1 >650 or pressure2 >650 or pressure_final < -20 or pressure1 <-20 or pressure2 <-20 or density2<0 or density1 <0 or density3<0 or density4<0 or density_final <0:
					popupmsg_OCR()	
			

			if temperature.get() == 32 and composition_CO2 < 0.5 and instrument.get() ==2: 

				## Calibration equation's coeff of CO2-N2 at 22 °C over 5-500 bars


				# normalisation of concentration and of Fermi diad splitting
				composition_CO2_normalized_1 = (composition_CO2 + 0.005)
				composition_CO2_normalized_2 = (composition_CO2 - 0.005)
				FDS_normalized_1 = (FDS + unc_FDS - FDS_std)
				FDS_normalized_2 = (FDS - unc_FDS - FDS_std)
				
				p00= -7.979799119
				p10= 269.90342983
				p01= 2587.5257747
				p20= -1224.7853215
				p11= -17336.25670
				p02= 2115.1665818
				p30= 1435.628346
				p21= 49648.79375388
				p12= -14261.990084
				p03= 2095.48960586
				p31= -47522.1569306
				p22= 18998.615306
				p13= -3716.868971
				p04= 110.044323282


				d00= 0.05296942474
				d10= -0.5914567883
				d01= 2.4186760261
				d20= 2.02181586877
				d11= -8.67656548427
				d02= -0.9986211405
				d30= -2.1120038819
				d21= 11.215350233
				d12= 6.5395043947
				d03= -0.3927794555
				d31= -2.564151083
				d22= -8.68563282
				d13= 1.0174667869
				d04= -0.13850001


				#### pressure calculation
				pressure1 = (p00*composition_CO2_normalized_1**0*FDS_normalized_1**0 
				+ p10*composition_CO2_normalized_1**1*FDS_normalized_1**0 
				+ p01*composition_CO2_normalized_1**0*FDS_normalized_1**1 
				+ p20*composition_CO2_normalized_1**2*FDS_normalized_1**0 
				+ p11*composition_CO2_normalized_1**1*FDS_normalized_1**1 
				+ p02*composition_CO2_normalized_1**0*FDS_normalized_1**2 
				+ p30*composition_CO2_normalized_1**3*FDS_normalized_1**0 
				+ p21*composition_CO2_normalized_1**2*FDS_normalized_1**1
				+ p12*composition_CO2_normalized_1**1*FDS_normalized_1**2 
				+ p03*composition_CO2_normalized_1**0*FDS_normalized_1**3 
				+ p31*composition_CO2_normalized_1**3*FDS_normalized_1**1 
				+ p22*composition_CO2_normalized_1**2*FDS_normalized_1**2
				+ p13*composition_CO2_normalized_1**1*FDS_normalized_1**3 
				+ p04*composition_CO2_normalized_1**0*FDS_normalized_1**4)

				pressure2 = (p00*composition_CO2_normalized_2**0*FDS_normalized_2**0 
				+ p10*composition_CO2_normalized_2**1*FDS_normalized_2**0 
				+ p01*composition_CO2_normalized_2**0*FDS_normalized_2**1 
				+ p20*composition_CO2_normalized_2**2*FDS_normalized_2**0
				+ p11*composition_CO2_normalized_2**1*FDS_normalized_2**1 
				+ p02*composition_CO2_normalized_2**0*FDS_normalized_2**2
				+ p30*composition_CO2_normalized_2**3*FDS_normalized_2**0 
				+ p21*composition_CO2_normalized_2**2*FDS_normalized_2**1
				+ p12*composition_CO2_normalized_2**1*FDS_normalized_2**2 
				+ p03*composition_CO2_normalized_2**0*FDS_normalized_2**3 
				+ p31*composition_CO2_normalized_2**3*FDS_normalized_2**1 
				+ p22*composition_CO2_normalized_2**2*FDS_normalized_2**2
				+ p13*composition_CO2_normalized_2**1*FDS_normalized_2**3 
				+ p04*composition_CO2_normalized_2**0*FDS_normalized_2**4)

				pressure3 = (p00*composition_CO2_normalized_1**0*FDS_normalized_2**0 
				+ p10*composition_CO2_normalized_1**1*FDS_normalized_2**0 
				+ p01*composition_CO2_normalized_1**0*FDS_normalized_2**1 
				+ p20*composition_CO2_normalized_1**2*FDS_normalized_2**0
				+ p11*composition_CO2_normalized_1**1*FDS_normalized_2**1 
				+ p02*composition_CO2_normalized_1**0*FDS_normalized_2**2 
				+ p30*composition_CO2_normalized_1**3*FDS_normalized_2**0 
				+ p21*composition_CO2_normalized_1**2*FDS_normalized_2**1
				+ p12*composition_CO2_normalized_1**1*FDS_normalized_2**2 
				+ p03*composition_CO2_normalized_1**0*FDS_normalized_2**3 
				+ p31*composition_CO2_normalized_1**3*FDS_normalized_2**1 
				+ p22*composition_CO2_normalized_1**2*FDS_normalized_2**2
				+ p13*composition_CO2_normalized_1**1*FDS_normalized_2**3 
				+ p04*composition_CO2_normalized_1**0*FDS_normalized_2**4)

				pressure4 = (p00*composition_CO2_normalized_2**0*FDS_normalized_1**0 
				+ p10*composition_CO2_normalized_2**1*FDS_normalized_1**0 
				+ p01*composition_CO2_normalized_2**0*FDS_normalized_1**1 
				+ p20*composition_CO2_normalized_2**2*FDS_normalized_1**0
				+ p11*composition_CO2_normalized_2**1*FDS_normalized_1**1 
				+ p02*composition_CO2_normalized_2**0*FDS_normalized_1**2 
				+ p30*composition_CO2_normalized_2**3*FDS_normalized_1**0 
				+ p21*composition_CO2_normalized_2**2*FDS_normalized_1**1
				+ p12*composition_CO2_normalized_2**1*FDS_normalized_1**2 
				+ p03*composition_CO2_normalized_2**0*FDS_normalized_1**3 
				+ p31*composition_CO2_normalized_2**3*FDS_normalized_1**1 
				+ p22*composition_CO2_normalized_2**2*FDS_normalized_1**2
				+ p13*composition_CO2_normalized_2**1*FDS_normalized_1**3 
				+ p04*composition_CO2_normalized_2**0*FDS_normalized_1**4)

				########################
				#### density calculation

				density1 = (d00*composition_CO2_normalized_1**0*FDS_normalized_1**0 
				+ d10*composition_CO2_normalized_1**1*FDS_normalized_1**0 
				+ d01*composition_CO2_normalized_1**0*FDS_normalized_1**1 
				+ d20*composition_CO2_normalized_1**2*FDS_normalized_1**0 
				+ d11*composition_CO2_normalized_1**1*FDS_normalized_1**1 
				+ d02*composition_CO2_normalized_1**0*FDS_normalized_1**2 
				+ d30*composition_CO2_normalized_1**3*FDS_normalized_1**0 
				+ d21*composition_CO2_normalized_1**2*FDS_normalized_1**1
				+ d12*composition_CO2_normalized_1**1*FDS_normalized_1**2 
				+ d03*composition_CO2_normalized_1**0*FDS_normalized_1**3 
				+ d31*composition_CO2_normalized_1**3*FDS_normalized_1**1 
				+ d22*composition_CO2_normalized_1**2*FDS_normalized_1**2
				+ d13*composition_CO2_normalized_1**1*FDS_normalized_1**3 
				+ d04*composition_CO2_normalized_1**0*FDS_normalized_1**4)

				density2 = (d00*composition_CO2_normalized_2**0*FDS_normalized_2**0 
				+ d10*composition_CO2_normalized_2**1*FDS_normalized_2**0 
				+ d01*composition_CO2_normalized_2**0*FDS_normalized_2**1 
				+ d20*composition_CO2_normalized_2**2*FDS_normalized_2**0
				+ d11*composition_CO2_normalized_2**1*FDS_normalized_2**1 
				+ d02*composition_CO2_normalized_2**0*FDS_normalized_2**2
				+ d30*composition_CO2_normalized_2**3*FDS_normalized_2**0 
				+ d21*composition_CO2_normalized_2**2*FDS_normalized_2**1
				+ d12*composition_CO2_normalized_2**1*FDS_normalized_2**2 
				+ d03*composition_CO2_normalized_2**0*FDS_normalized_2**3 
				+ d31*composition_CO2_normalized_2**3*FDS_normalized_2**1 
				+ d22*composition_CO2_normalized_2**2*FDS_normalized_2**2
				+ d13*composition_CO2_normalized_2**1*FDS_normalized_2**3 
				+ d04*composition_CO2_normalized_2**0*FDS_normalized_2**4)

				density3 = (d00*composition_CO2_normalized_1**0*FDS_normalized_2**0 
				+ d10*composition_CO2_normalized_1**1*FDS_normalized_2**0 
				+ d01*composition_CO2_normalized_1**0*FDS_normalized_2**1 
				+ d20*composition_CO2_normalized_1**2*FDS_normalized_2**0
				+ d11*composition_CO2_normalized_1**1*FDS_normalized_2**1 
				+ d02*composition_CO2_normalized_1**0*FDS_normalized_2**2 
				+ d30*composition_CO2_normalized_1**3*FDS_normalized_2**0 
				+ d21*composition_CO2_normalized_1**2*FDS_normalized_2**1
				+ d12*composition_CO2_normalized_1**1*FDS_normalized_2**2 
				+ d03*composition_CO2_normalized_1**0*FDS_normalized_2**3 
				+ d31*composition_CO2_normalized_1**3*FDS_normalized_2**1 
				+ d22*composition_CO2_normalized_1**2*FDS_normalized_2**2
				+ d13*composition_CO2_normalized_1**1*FDS_normalized_2**3 
				+ d04*composition_CO2_normalized_1**0*FDS_normalized_2**4)

				density4 = (d00*composition_CO2_normalized_2**0*FDS_normalized_1**0 
				+ d10*composition_CO2_normalized_2**1*FDS_normalized_1**0 
				+ d01*composition_CO2_normalized_2**0*FDS_normalized_1**1 
				+ d20*composition_CO2_normalized_2**2*FDS_normalized_1**0
				+ d11*composition_CO2_normalized_2**1*FDS_normalized_1**1 
				+ d02*composition_CO2_normalized_2**0*FDS_normalized_1**2 
				+ d30*composition_CO2_normalized_2**3*FDS_normalized_1**0 
				+ d21*composition_CO2_normalized_2**2*FDS_normalized_1**1
				+ d12*composition_CO2_normalized_2**1*FDS_normalized_1**2 
				+ d03*composition_CO2_normalized_2**0*FDS_normalized_1**3 
				+ d31*composition_CO2_normalized_2**3*FDS_normalized_1**1 
				+ d22*composition_CO2_normalized_2**2*FDS_normalized_1**2
				+ d13*composition_CO2_normalized_2**1*FDS_normalized_1**3 
				+ d04*composition_CO2_normalized_2**0*FDS_normalized_1**4)              

				pressure_final = (max(pressure1, pressure2, pressure3, pressure4) + min(pressure1, pressure2, pressure3, pressure4))/2 #pressure max - pressure min
				uncer_pressure_final = 8.5 + (max(pressure1, pressure2, pressure3, pressure4) - min(pressure1, pressure2, pressure3, pressure4))/(2*np.sqrt(3)) #uncer = 12

				density_final = (max(density1, density2, density3, density4) + min(density1, density2, density3, density4))/2 #density max - density min
				uncer_density_final = 0.0042  + (max(density1, density2, density3, density4) - min(density1, density2, density3, density4))/(2*np.sqrt(3)) #uncer=0.006

				molarvolume1 = 1/(max(density1, density2, density3, density4)/(44*composition_CO2 + 28*composition_N2))
				molarvolume2 = 1/(min(density1, density2, density3, density4)/(44*composition_CO2 + 28*composition_N2))		
				molarvolume_final = (molarvolume1 + molarvolume2) / 2
				uncer_molarvolume_final = (molarvolume2 - molarvolume1) / (2*np.sqrt(3))


				##### verify if measured pressure < 160 bar, if it is, re-recalculte using calibration data for 5-160 bar range.
				if pressure_final <= 150: 

					## Calibration equation's coeff of CO2-N2 at 22 °C over 5-160 bars
					# normalisation of concentration and of Fermi diad splitting
					
					composition_CO2_normalized_1 = (composition_CO2 + 0.005)
					composition_CO2_normalized_2 = (composition_CO2 - 0.005)
					FDS_normalized_1 = (FDS + unc_FDS - FDS_std)
					FDS_normalized_2 = (FDS - unc_FDS - FDS_std)
										
					p00= 27.87861899
					p10= -309.3407794
					p01= 2420.4319208
					p20= 1080.8824672
					p11= -11059.84037
					p02= -1531.374273
					p30= -1154.705888
					p21= 18759.02191
					p12= 11079.4201898
					p03= -2896.323979
					p31= -9353.915401
					p22= -17517.27349
					p13= 7020.0215142
					p04= -346.21689848
					
					d00= 0.032500069				
					d10= -0.361537166
					d01= 2.73893987
					d20= 1.26788623
					d11= -11.352660536
					d02= -1.873394675
					d30= -1.35961062
					d21= 17.034456813
					d12= 16.50044087
					d03= -5.356779412
					d31= -5.8185516987
					d22= -26.58492039
					d13= 13.5670353724
					d04= -1.565369608


					#### pressure calculation
					pressure1 = (p00*composition_CO2_normalized_1**0*FDS_normalized_1**0 
					+ p10*composition_CO2_normalized_1**1*FDS_normalized_1**0 
					+ p01*composition_CO2_normalized_1**0*FDS_normalized_1**1 
					+ p20*composition_CO2_normalized_1**2*FDS_normalized_1**0 
					+ p11*composition_CO2_normalized_1**1*FDS_normalized_1**1 
					+ p02*composition_CO2_normalized_1**0*FDS_normalized_1**2 
					+ p30*composition_CO2_normalized_1**3*FDS_normalized_1**0 
					+ p21*composition_CO2_normalized_1**2*FDS_normalized_1**1
					+ p12*composition_CO2_normalized_1**1*FDS_normalized_1**2 
					+ p03*composition_CO2_normalized_1**0*FDS_normalized_1**3 
					+ p31*composition_CO2_normalized_1**3*FDS_normalized_1**1 
					+ p22*composition_CO2_normalized_1**2*FDS_normalized_1**2
					+ p13*composition_CO2_normalized_1**1*FDS_normalized_1**3 
					+ p04*composition_CO2_normalized_1**0*FDS_normalized_1**4)

					pressure2 = (p00*composition_CO2_normalized_2**0*FDS_normalized_2**0 
					+ p10*composition_CO2_normalized_2**1*FDS_normalized_2**0 
					+ p01*composition_CO2_normalized_2**0*FDS_normalized_2**1 
					+ p20*composition_CO2_normalized_2**2*FDS_normalized_2**0
					+ p11*composition_CO2_normalized_2**1*FDS_normalized_2**1 
					+ p02*composition_CO2_normalized_2**0*FDS_normalized_2**2
					+ p30*composition_CO2_normalized_2**3*FDS_normalized_2**0 
					+ p21*composition_CO2_normalized_2**2*FDS_normalized_2**1
					+ p12*composition_CO2_normalized_2**1*FDS_normalized_2**2 
					+ p03*composition_CO2_normalized_2**0*FDS_normalized_2**3 
					+ p31*composition_CO2_normalized_2**3*FDS_normalized_2**1 
					+ p22*composition_CO2_normalized_2**2*FDS_normalized_2**2
					+ p13*composition_CO2_normalized_2**1*FDS_normalized_2**3 
					+ p04*composition_CO2_normalized_2**0*FDS_normalized_2**4)

					pressure3 = (p00*composition_CO2_normalized_1**0*FDS_normalized_2**0 
					+ p10*composition_CO2_normalized_1**1*FDS_normalized_2**0 
					+ p01*composition_CO2_normalized_1**0*FDS_normalized_2**1 
					+ p20*composition_CO2_normalized_1**2*FDS_normalized_2**0
					+ p11*composition_CO2_normalized_1**1*FDS_normalized_2**1 
					+ p02*composition_CO2_normalized_1**0*FDS_normalized_2**2 
					+ p30*composition_CO2_normalized_1**3*FDS_normalized_2**0 
					+ p21*composition_CO2_normalized_1**2*FDS_normalized_2**1
					+ p12*composition_CO2_normalized_1**1*FDS_normalized_2**2 
					+ p03*composition_CO2_normalized_1**0*FDS_normalized_2**3 
					+ p31*composition_CO2_normalized_1**3*FDS_normalized_2**1 
					+ p22*composition_CO2_normalized_1**2*FDS_normalized_2**2
					+ p13*composition_CO2_normalized_1**1*FDS_normalized_2**3 
					+ p04*composition_CO2_normalized_1**0*FDS_normalized_2**4)

					pressure4 = (p00*composition_CO2_normalized_2**0*FDS_normalized_1**0 
					+ p10*composition_CO2_normalized_2**1*FDS_normalized_1**0 
					+ p01*composition_CO2_normalized_2**0*FDS_normalized_1**1 
					+ p20*composition_CO2_normalized_2**2*FDS_normalized_1**0
					+ p11*composition_CO2_normalized_2**1*FDS_normalized_1**1 
					+ p02*composition_CO2_normalized_2**0*FDS_normalized_1**2 
					+ p30*composition_CO2_normalized_2**3*FDS_normalized_1**0 
					+ p21*composition_CO2_normalized_2**2*FDS_normalized_1**1
					+ p12*composition_CO2_normalized_2**1*FDS_normalized_1**2 
					+ p03*composition_CO2_normalized_2**0*FDS_normalized_1**3 
					+ p31*composition_CO2_normalized_2**3*FDS_normalized_1**1 
					+ p22*composition_CO2_normalized_2**2*FDS_normalized_1**2
					+ p13*composition_CO2_normalized_2**1*FDS_normalized_1**3 
					+ p04*composition_CO2_normalized_2**0*FDS_normalized_1**4)

					########################
					#### density calculation

					density1 = (d00*composition_CO2_normalized_1**0*FDS_normalized_1**0 
					+ d10*composition_CO2_normalized_1**1*FDS_normalized_1**0 
					+ d01*composition_CO2_normalized_1**0*FDS_normalized_1**1 
					+ d20*composition_CO2_normalized_1**2*FDS_normalized_1**0 
					+ d11*composition_CO2_normalized_1**1*FDS_normalized_1**1 
					+ d02*composition_CO2_normalized_1**0*FDS_normalized_1**2 
					+ d30*composition_CO2_normalized_1**3*FDS_normalized_1**0 
					+ d21*composition_CO2_normalized_1**2*FDS_normalized_1**1
					+ d12*composition_CO2_normalized_1**1*FDS_normalized_1**2 
					+ d03*composition_CO2_normalized_1**0*FDS_normalized_1**3 
					+ d31*composition_CO2_normalized_1**3*FDS_normalized_1**1 
					+ d22*composition_CO2_normalized_1**2*FDS_normalized_1**2
					+ d13*composition_CO2_normalized_1**1*FDS_normalized_1**3 
					+ d04*composition_CO2_normalized_1**0*FDS_normalized_1**4)

					density2 = (d00*composition_CO2_normalized_2**0*FDS_normalized_2**0 
					+ d10*composition_CO2_normalized_2**1*FDS_normalized_2**0 
					+ d01*composition_CO2_normalized_2**0*FDS_normalized_2**1 
					+ d20*composition_CO2_normalized_2**2*FDS_normalized_2**0
					+ d11*composition_CO2_normalized_2**1*FDS_normalized_2**1 
					+ d02*composition_CO2_normalized_2**0*FDS_normalized_2**2
					+ d30*composition_CO2_normalized_2**3*FDS_normalized_2**0 
					+ d21*composition_CO2_normalized_2**2*FDS_normalized_2**1
					+ d12*composition_CO2_normalized_2**1*FDS_normalized_2**2 
					+ d03*composition_CO2_normalized_2**0*FDS_normalized_2**3 
					+ d31*composition_CO2_normalized_2**3*FDS_normalized_2**1 
					+ d22*composition_CO2_normalized_2**2*FDS_normalized_2**2
					+ d13*composition_CO2_normalized_2**1*FDS_normalized_2**3 
					+ d04*composition_CO2_normalized_2**0*FDS_normalized_2**4)

					density3 = (d00*composition_CO2_normalized_1**0*FDS_normalized_2**0 
					+ d10*composition_CO2_normalized_1**1*FDS_normalized_2**0 
					+ d01*composition_CO2_normalized_1**0*FDS_normalized_2**1 
					+ d20*composition_CO2_normalized_1**2*FDS_normalized_2**0
					+ d11*composition_CO2_normalized_1**1*FDS_normalized_2**1 
					+ d02*composition_CO2_normalized_1**0*FDS_normalized_2**2 
					+ d30*composition_CO2_normalized_1**3*FDS_normalized_2**0 
					+ d21*composition_CO2_normalized_1**2*FDS_normalized_2**1
					+ d12*composition_CO2_normalized_1**1*FDS_normalized_2**2 
					+ d03*composition_CO2_normalized_1**0*FDS_normalized_2**3 
					+ d31*composition_CO2_normalized_1**3*FDS_normalized_2**1 
					+ d22*composition_CO2_normalized_1**2*FDS_normalized_2**2
					+ d13*composition_CO2_normalized_1**1*FDS_normalized_2**3 
					+ d04*composition_CO2_normalized_1**0*FDS_normalized_2**4)

					density4 = (d00*composition_CO2_normalized_2**0*FDS_normalized_1**0 
					+ d10*composition_CO2_normalized_2**1*FDS_normalized_1**0 
					+ d01*composition_CO2_normalized_2**0*FDS_normalized_1**1 
					+ d20*composition_CO2_normalized_2**2*FDS_normalized_1**0
					+ d11*composition_CO2_normalized_2**1*FDS_normalized_1**1 
					+ d02*composition_CO2_normalized_2**0*FDS_normalized_1**2 
					+ d30*composition_CO2_normalized_2**3*FDS_normalized_1**0 
					+ d21*composition_CO2_normalized_2**2*FDS_normalized_1**1
					+ d12*composition_CO2_normalized_2**1*FDS_normalized_1**2 
					+ d03*composition_CO2_normalized_2**0*FDS_normalized_1**3 
					+ d31*composition_CO2_normalized_2**3*FDS_normalized_1**1 
					+ d22*composition_CO2_normalized_2**2*FDS_normalized_1**2
					+ d13*composition_CO2_normalized_2**1*FDS_normalized_1**3 
					+ d04*composition_CO2_normalized_2**0*FDS_normalized_1**4)              

					pressure_final = (max(pressure1, pressure2, pressure3, pressure4) + min(pressure1, pressure2, pressure3, pressure4))/2 #pressure max - pressure min
					uncer_pressure_final = 3.6 + (max(pressure1, pressure2, pressure3, pressure4) - min(pressure1, pressure2, pressure3, pressure4))/(2*np.sqrt(3)) # uncer = 5

					density_final = (max(density1, density2, density3, density4) + min(density1, density2, density3, density4))/2 #density max - density min
					uncer_density_final = 0.0035 + (max(density1, density2, density3, density4) - min(density1, density2, density3, density4))/(2*np.sqrt(3)) #uncer = 0.005

					molarvolume1 = 1/(max(density1, density2, density3, density4)/(44*composition_CO2 + 28*composition_N2))
					molarvolume2 = 1/(min(density1, density2, density3, density4)/(44*composition_CO2 + 28*composition_N2))		
					molarvolume_final = (molarvolume1 + molarvolume2) / 2
					uncer_molarvolume_final = (molarvolume2 - molarvolume1) / (2*np.sqrt(3))
				
				print('composition normalized', composition_CO2_normalized_1)

				print('pressure1', pressure1)
				print('pressure2', pressure2)
				print('pressure3', pressure3)
				print('pressure4', pressure4)

				print('density 1=', density1)
				print('density 2=', density2)
				print('density 3=', density3)
				print('density 4=', density4)
				
				print("molarvolume1", molarvolume1)
				print("molarvolume2", molarvolume2)

				####DISPLAY POP UP IF OUT OF RANGE	
				if pressure_final > 650 or pressure1 >650 or pressure2 >650 or pressure_final < -20 or pressure1 <-20 or pressure2 <-20 or density2<0 or density1 <0 or density3<0 or density4<0 or density_final <0 :
					popupmsg_OCR()

			####### GET RESULTS AND BUT ON THE OUT PUT FEILD (out put field just be created below) ################       
			composition_CO2_display.insert(tk.END, "%.3f" % composition_CO2)
			composition_N2_display.insert(tk.END, "%.3f" % composition_N2)
			pressure.insert(tk.END, "%.1f" % pressure_final)
			density.insert(tk.END, "%.3f" % density_final)
			molarvolume.insert(tk.END, "%.3f" % molarvolume_final)

			uncer_pressure.insert(tk.END, "%.1f" % uncer_pressure_final)
			uncer_density.insert(tk.END, "%.3f" % uncer_density_final)
			uncer_molarvolume.insert(tk.END, "%.3f" % uncer_molarvolume_final)

		# ################################    
		# ########  display results ######
		# ################################ 
		composition_CO2_display= tk.Entry(self.frame, width = 20) #, state='disabled'
		composition_CO2_display.grid(row=35, column=1)        
		composition_N2_display= tk.Entry(self.frame, width = 20) #, state='disabled'
		composition_N2_display.grid(row=35, column=3)
		

		pressure= tk.Entry(self.frame, width = 20) #, state='disabled'
		pressure.grid(row=39, column=1)
		density = tk.Entry(self.frame, width = 20) 
		density.grid(row=40, column=1)
		molarvolume = tk.Entry(self.frame,  width = 20)
		molarvolume.grid(row=41, column=1)

		######## display uncertainty ########
		uncer_pressure = tk.Entry(self.frame,  width = 20) #, state='disabled'
		uncer_pressure.grid(row=39, column=3)
		uncer_density = tk.Entry(self.frame,  width = 20) 
		uncer_density.grid(row=40, column=3)
		uncer_molarvolume = tk.Entry(self.frame,  width = 20) 
		uncer_molarvolume.grid(row=41, column=3)


		#############################
		######### Buttons ###########
		#############################

		self.button1_1 = tk.Button(self.frame, text="Clear Input", command=clear_field_inputs)
		self.button1_1.grid(row=16, column=1, padx=10)
		self.button1_2 = tk.Button(self.frame, text="Calculate", bg="green", width=10, command=calculCO2N2)
		self.button1_2.grid(row=33, column=1, padx=20, pady=10, sticky="W")        
		self.button1_3 = tk.Button(self.frame, text="Clear Results", width=10, command=clear_field_results)
		self.button1_3.grid(row=42, column=1, padx=20)

		
		# def OpenSuppDoc_CO2N2():
		# 	os.startfile(resource_path('SuppDoc_CO2N2.pdf'))

		# self.button1_4 = tk.Button(self.frame, text="Supplement document", bg="orange", command=OpenSuppDoc_CO2N2)
		# self.button1_4.grid(row=42, column=0, padx=10, pady=10, sticky="W")

						
		self.quit = tk.Button(self.frame, text="Close", width=10, command=self.close_window)	
		self.quit.grid(row=42, column=3, padx=10)

	def close_window(self):
		self.master.destroy()




#########################################
########### Module CH4 - N2  ############
#########################################
class module4: 
	def __init__(self, master, number):
		self.master = master
		self.master.title("FRAnCIs v.1.0.1 - (CH₄-N₂ mixtures)")
		self.master.geometry("700x660")
		self.master.resizable(width=False, height=False)
		self.master.iconbitmap(resource_path("logo.ico"))
		self.frame=tk.Frame(self.master)
		self.frame.grid()

		### Create the UI of windows of module 4 
		self.label = tk.Label(self.frame, text="Calculation for CH₄-N₂ mixtures", font=('bold', 18))
		self.label.grid(row=0, column=1, columnspan=6, padx=10, pady=10, sticky="W") #remove (side="top", fill="x",)        

		self.label = tk.Label(self.frame, text="- The area of N₂ (area_N2) and CH₄ \u03BD₁ (area_CH4) bands are needed for determination of composition.")
		self.label.grid(row=1, column=0, columnspan=6, padx=10, sticky="W") #remove (side="top", fill="x",)   

		self.label = tk.Label(self.frame, text="- The CH₄ \u03BD₁ band position of the sample (\u03BD₁_sample) and of the standard containing ~5 bars of pure CH₄ (\u03BD₁_std), their")
		self.label.grid(row=2, column=0, columnspan=6,padx=10, sticky="W") #remove (side="top", fill="x",)
		
		self.label = tk.Label(self.frame, text="      uncertainty and measured composition are then used for determination of pressure and density")
		self.label.grid(row=3, column=0, columnspan=6, padx=10, sticky="W") #remove (side="top", fill="x",)
		#self.label = tk.Label(self.frame,text="______________________________________________________________________________________________________________________________________")
		#self.label.grid(row=4, column=0, padx=10, columnspan=6, sticky="E")



		self.label_remark = tk.Label(self.frame, text="Remarks:", font=('bold', 12))
		self.label_remark.grid(row=7, column=0, columnspan=8, padx=10,  sticky="W")

		self.label = tk.Label(self.frame, text="   - The area of the atmospheric N₂ band (area_N2_atm) must be excluded from that of N₂ within the sample (area_N2_sample)")
		self.label.grid(row=8, column=0, columnspan=8, sticky="W")

		self.label = tk.Label(self.frame, text="   - The fitted peak position of CH₄ should be corrected by two neon emission lines at ~2851.38 and ~2972.44 cm\u207b\u00B9 (relative to ")
		self.label.grid(row=9, column=0, columnspan=8, sticky="W")
		self.label = tk.Label(self.frame, text="       514.53 nm) to minimize the error.")
		self.label.grid(row=10, column=0, columnspan=8, sticky="W")

		self.label = tk.Label(self.frame, text="   - The calibrations were made over 5-600 bars, out of this range may cause larger errors or aberrant values.")
		self.label.grid(row=11, column=0, columnspan=8, sticky="W")
		self.label = tk.Label(self.frame, text="   - The uncertainty (1\u03C3) of the measured composition is ~ ±0.5 mol%")
		self.label.grid(row=12, column=0, columnspan=8, sticky="W")  
		#self.label = tk.Label(self.frame, text="       composition (~ ±0.5 mol%) and the uncertainty of the fitted peak position of CH₄.")
		#self.label.grid(row=13, column=0, columnspan=8, sticky="W")

		# self.label = tk.Label(self.frame, text="   - Click 'Supplement document' button below for more detail.")
		# self.label.grid(row=14, column=0, columnspan=8, sticky="W")		

		###############################
		##### INPUT section #####
		###############################

		self.label_input = tk.Label(self.frame, text="___________     INPUT:", font=('bold', 10))
		self.label_input.grid(row=16, column=0, pady=10, sticky="E")
		#self.label = tk.Label(self.frame,text="____________________________________________________________________________")
		#self.label.grid(row=16, column=2, columnspan=6,padx=10, sticky="E")

		###############################
		##### Select Température #####
		###############################
		self.label = tk.Label(self.frame, text="Select temperature:")
		self.label.grid(row=25, column=0, columnspan=1, padx=10, sticky="W") #remove (side="top", fill="x",)

		temperature = tk.IntVar()
		temperature.set(22)

		def selected_temperature():
			print(temperature.get())

		self.Rbtn1=tk.Radiobutton(self.frame, text="22 °C", variable=temperature, value=22, padx = 20,  command=selected_temperature).grid(row=25, column=1,  padx=10, pady=10)
		self.Rbtn1=tk.Radiobutton(self.frame, text="32 °C", variable=temperature, value=32, padx = 20,  command=selected_temperature).grid(row=25, column=2,  padx=10)

		####################################
		##### Select Laser wavelength #####
		####################################

		self.label = tk.Label(self.frame, text="Laser wavelength (nm):")
		self.label.grid(row=25, column=3, columnspan=2, padx=30, stick="W") #remove (side="top", fill="x",)

		# options = {"488 nm": 488, "514 nm": 514, "532 nm": 532, "633 nm": 633, "785 nm": 785}
		options=[488, 514, 532, 633, 785]
		laser_wavelength = tk.IntVar()
		laser_wavelength.set(514)
		
		# self.menu = OptionMenu(self.frame, laser_wavelength, *options.keys()).grid(row=26, column=4, stick="W")
		self.menu = OptionMenu(self.frame, laser_wavelength, *options).grid(row=25, column=4)


		######### ENTRY ##########
		######### ENTRY ##########

		##entry N2 spectroscopic data 
		self.label = tk.Label(self.frame, text="area_N2_sample")
		self.label.grid(row=27, column=1, padx=10)
		self.label = tk.Label(self.frame, text="area_N2_atm")
		self.label.grid(row=27, column=2, padx=10)
		self.label = tk.Label(self.frame, text="Spectroscopic data of N₂ :")
		self.label.grid(row=28, column=0, padx=10, sticky="W")
		
		self.area_N2_entry_sample = tk.Entry(self.frame, width = 15)
		self.area_N2_entry_sample.grid(row=28, column=1)
		self.area_N2_entry_atm = tk.Entry(self.frame, width = 15)
		self.area_N2_entry_atm.grid(row=28, column=2)

		##entry CH4 spectroscopic data 

		self.label = tk.Label(self.frame, text="area_CH4")
		self.label.grid(row=29, column=1, padx=10)
		self.label = tk.Label(self.frame, text="\u03BD₁_sample (cm\u207b\u00B9)")
		self.label.grid(row=29, column=2, padx=10)
		self.label = tk.Label(self.frame, text="\u03BD₁_std (cm\u207b\u00B9)")
		self.label.grid(row=29, column=3, padx=10)
		self.label = tk.Label(self.frame, text="\u03BD₁_Uncertainty (cm\u207b\u00B9)")
		self.label.grid(row=29, column=4, padx=10)

		self.label = tk.Label(self.frame, text="Spectroscopic data of CH₄ :")
		self.label.grid(row=30, column=0, padx=10, sticky="W")
		
		self.area_CH4_entry = tk.Entry(self.frame, width = 15)
		self.area_CH4_entry.grid(row=30, column=1)

		self.nuCH4_sample_entry = tk.Entry(self.frame, width = 15)
		self.nuCH4_sample_entry.grid(row=30, column=2)
		self.nuCH4_std_entry = tk.Entry(self.frame, width = 15)
		self.nuCH4_std_entry.grid(row=30, column=3)
		self.unc_nuCH4_entry = tk.Entry(self.frame, width = 15)
		self.unc_nuCH4_entry.grid(row=30, column=4)


		######### OUTPUT ##########
		######### OUTPUT ##########

		self.label = tk.Label(self.frame, text="____________  OUTPUT:", font=('bold', 10))
		self.label.grid(row=34, column=0,  sticky="E")
		self.label = tk.Label(self.frame, text="________________________________________________________________________")
		self.label.grid(row=34, column=2, columnspan=6, padx=10, sticky="E")        

		self.label = tk.Label(self.frame, text="(mol% CH₄)")
		self.label.grid(row=35, column=1, padx=10)
		self.label = tk.Label(self.frame, text="(mol% N₂)")
		self.label.grid(row=35, column=3, padx=10)

		self.label = tk.Label(self.frame, text="Composition")
		self.label.grid(row=36, column=0, padx=10, sticky="W")
		self.label = tk.Label(self.frame, text="(±0.5 mol%)")
		self.label.grid(row=36, column=4, padx=10, sticky="W")
		self.label = tk.Label(self.frame, text="--------------------------------------------------------------")
		self.label.grid(row=37, column=1, columnspan=3, padx=5)
		
		self.label = tk.Label(self.frame, text="Pressure")
		self.label.grid(row=39, column=0, padx=10, pady=5, sticky="W")
		self.label = tk.Label(self.frame, text="Density")
		self.label.grid(row=40, column=0, padx=10, pady=5, sticky="W")
		self.label = tk.Label(self.frame, text="Molar Volume")
		self.label.grid(row=41, column=0, padx=10, pady=5, sticky="W")

		
		self.label = tk.Label(self.frame, text="±")
		self.label.grid(row=39, column=2, padx=10, pady=5)
		self.label = tk.Label(self.frame, text="±")
		self.label.grid(row=40, column=2, padx=10, pady=5)
		self.label = tk.Label(self.frame, text="±")
		self.label.grid(row=41, column=2, padx=10, pady=5)

		
		
		self.label = tk.Label(self.frame, text="(bar)")
		self.label.grid(row=39, column=4, padx=10, pady=5, sticky="W")
		self.label = tk.Label(self.frame, text="(g.cm\u207b\u00B3)")
		self.label.grid(row=40, column=4, padx=10, pady=5, sticky="W")
		self.label = tk.Label(self.frame, text="(cm\u00B3.mol\u207b\u00B9)")
		self.label.grid(row=41, column=4, padx=10, pady=5, sticky="W")


		###############################
		##### Caculation ##############
		###############################

		#### Make a clear-button for input field
		def clear_field_inputs(): 
			
			self.area_N2_entry_sample.delete(0, tk.END)
			self.area_N2_entry_atm.delete(0, tk.END)
			self.area_CH4_entry.delete(0, tk.END)
			self.nuCH4_sample_entry.delete(0, tk.END)
			self.nuCH4_std_entry.delete(0, tk.END)
			self.unc_nuCH4_entry.delete(0, tk.END)
			
		#### Make a clear-button for output field
		def clear_field_results():
			composition_CH4_display.delete(0, tk.END)
			composition_N2_display.delete(0, tk.END)
			pressure.delete(0, tk.END)
			density.delete(0, tk.END)
			molarvolume.delete(0, tk.END)
			uncer_pressure.delete(0, tk.END)
			uncer_density.delete(0, tk.END)
			uncer_molarvolume.delete(0, tk.END)


		def calculCH4pure():
			clear_field_results()
			area_N2_sample  = float(self.area_N2_entry_sample.get())
			area_N2_atm     = float(self.area_N2_entry_atm.get())
			area_CH4        = float(self.area_CH4_entry.get())
			nuCH4_sample    = float(self.nuCH4_sample_entry.get())
			nuCH4_std       = float(self.nuCH4_std_entry.get())
			unc_nuCH4       = float(self.unc_nuCH4_entry.get())

			#Composition calculation

			if laser_wavelength.get() == 488:
				RRSCS_CO2 = 2.30
				RRSCS_CH4 = 7.80
			if laser_wavelength.get() == 514:
				RRSCS_CO2 = 2.29
				RRSCS_CH4 = 7.73
			if laser_wavelength.get() == 532:
				RRSCS_CO2 = 2.27
				RRSCS_CH4 = 7.69
			if laser_wavelength.get() == 633:
				RRSCS_CO2 = 2.20
				RRSCS_CH4 = 7.44
			if laser_wavelength.get() == 785:
				RRSCS_CO2 = 2.09
				RRSCS_CH4 = 7.05
			
			print('the wavelength of the selected laser is', laser_wavelength.get(), 'nm')
			print('RRSCS_CH4=', RRSCS_CH4)		
			print('RRSCS_C02=', RRSCS_CO2)
			         
			composition_CH4 = ((area_CH4/RRSCS_CH4)/((area_CH4/RRSCS_CH4) + ((area_N2_sample - area_N2_atm)/1)))
			composition_N2 = 1 - composition_CH4

			composition_CH4_1 = composition_CH4 + 0.005
			composition_CH4_2 = composition_CH4 - 0.005
			print('composition CH4 = ', composition_CH4)
			print('composition CH4 2 = ', composition_CH4_2)
			print('unc_nuCH4', unc_nuCH4)

			if temperature.get() == 22 and composition_CH4 >= 0.5: 

				## Calibration equation's coeff of CH4 pur at 22C

				DeltaPCH4= nuCH4_sample - nuCH4_std
				DeltaPCH4_1 = DeltaPCH4 + unc_nuCH4
				DeltaPCH4_2 = DeltaPCH4 - unc_nuCH4
				                         
				## Calibration equation's coeff of CH4-N2 at 32 °C
				p00= -100.09603
				p10= 552.9168
				p01= -170.13906
				p20= -935.499438
				p11= 483.37485
				p02= 37.74878
				p30= 503.67728
				p21= -966.93864
				p12= -217.7605215
				p03= -16.79599681
				p31= 665.3106743
				p22= 226.0929471
				p13= 29.68771314
				p04= 1.205984

				d00= -0.042772564
				d10= 0.231555
				d01= -0.181355015
				d20= -0.357587953
				d11= 0.4090893
				d02= 0.0176838
				d30= 0.17502987
				d21= -0.489589303
				d12= -0.05750992
				d03= -0.0028039
				d31= 0.233560193
				d22= 0.044569611
				d13= 0.003779058
				d04= 0.00008597

				#### pressure calculation
				pressure1 = (p00*composition_CH4_1**0*DeltaPCH4_1**0 
				+ p10*composition_CH4_1**1*DeltaPCH4_1**0 
				+ p01*composition_CH4_1**0*DeltaPCH4_1**1 
				+ p20*composition_CH4_1**2*DeltaPCH4_1**0 
				+ p11*composition_CH4_1**1*DeltaPCH4_1**1 
				+ p02*composition_CH4_1**0*DeltaPCH4_1**2 
				+ p30*composition_CH4_1**3*DeltaPCH4_1**0 
				+ p21*composition_CH4_1**2*DeltaPCH4_1**1
				+ p12*composition_CH4_1**1*DeltaPCH4_1**2 
				+ p03*composition_CH4_1**0*DeltaPCH4_1**3 
				+ p31*composition_CH4_1**3*DeltaPCH4_1**1 
				+ p22*composition_CH4_1**2*DeltaPCH4_1**2
				+ p13*composition_CH4_1**1*DeltaPCH4_1**3 
				+ p04*composition_CH4_1**0*DeltaPCH4_1**4)

				pressure2 = (p00*composition_CH4_2**0*DeltaPCH4_2**0 
				+ p10*composition_CH4_2**1*DeltaPCH4_2**0 
				+ p01*composition_CH4_2**0*DeltaPCH4_2**1 
				+ p20*composition_CH4_2**2*DeltaPCH4_2**0
				+ p11*composition_CH4_2**1*DeltaPCH4_2**1 
				+ p02*composition_CH4_2**0*DeltaPCH4_2**2 
				+ p30*composition_CH4_2**3*DeltaPCH4_2**0 
				+ p21*composition_CH4_2**2*DeltaPCH4_2**1
				+ p12*composition_CH4_2**1*DeltaPCH4_2**2 
				+ p03*composition_CH4_2**0*DeltaPCH4_2**3 
				+ p31*composition_CH4_2**3*DeltaPCH4_2**1 
				+ p22*composition_CH4_2**2*DeltaPCH4_2**2
				+ p13*composition_CH4_2**1*DeltaPCH4_2**3 
				+ p04*composition_CH4_2**0*DeltaPCH4_2**4)

				pressure3 = (p00*composition_CH4_1**0*DeltaPCH4_2**0 
				+ p10*composition_CH4_1**1*DeltaPCH4_2**0 
				+ p01*composition_CH4_1**0*DeltaPCH4_2**1 
				+ p20*composition_CH4_1**2*DeltaPCH4_2**0
				+ p11*composition_CH4_1**1*DeltaPCH4_2**1 
				+ p02*composition_CH4_1**0*DeltaPCH4_2**2 
				+ p30*composition_CH4_1**3*DeltaPCH4_2**0 
				+ p21*composition_CH4_1**2*DeltaPCH4_2**1
				+ p12*composition_CH4_1**1*DeltaPCH4_2**2 
				+ p03*composition_CH4_1**0*DeltaPCH4_2**3 
				+ p31*composition_CH4_1**3*DeltaPCH4_2**1 
				+ p22*composition_CH4_1**2*DeltaPCH4_2**2
				+ p13*composition_CH4_1**1*DeltaPCH4_2**3 
				+ p04*composition_CH4_1**0*DeltaPCH4_2**4)

				pressure4 = (p00*composition_CH4_2**0*DeltaPCH4_1**0 
				+ p10*composition_CH4_2**1*DeltaPCH4_1**0 
				+ p01*composition_CH4_2**0*DeltaPCH4_1**1 
				+ p20*composition_CH4_2**2*DeltaPCH4_1**0
				+ p11*composition_CH4_2**1*DeltaPCH4_1**1 
				+ p02*composition_CH4_2**0*DeltaPCH4_1**2 
				+ p30*composition_CH4_2**3*DeltaPCH4_1**0 
				+ p21*composition_CH4_2**2*DeltaPCH4_1**1
				+ p12*composition_CH4_2**1*DeltaPCH4_1**2 
				+ p03*composition_CH4_2**0*DeltaPCH4_1**3 
				+ p31*composition_CH4_2**3*DeltaPCH4_1**1 
				+ p22*composition_CH4_2**2*DeltaPCH4_1**2
				+ p13*composition_CH4_2**1*DeltaPCH4_1**3 
				+ p04*composition_CH4_2**0*DeltaPCH4_1**4)

				########################
				#### density calculation

				density1 = (d00*composition_CH4_1**0*DeltaPCH4_1**0 
				+ d10*composition_CH4_1**1*DeltaPCH4_1**0 
				+ d01*composition_CH4_1**0*DeltaPCH4_1**1 
				+ d20*composition_CH4_1**2*DeltaPCH4_1**0 
				+ d11*composition_CH4_1**1*DeltaPCH4_1**1 
				+ d02*composition_CH4_1**0*DeltaPCH4_1**2 
				+ d30*composition_CH4_1**3*DeltaPCH4_1**0 
				+ d21*composition_CH4_1**2*DeltaPCH4_1**1
				+ d12*composition_CH4_1**1*DeltaPCH4_1**2 
				+ d03*composition_CH4_1**0*DeltaPCH4_1**3 
				+ d31*composition_CH4_1**3*DeltaPCH4_1**1 
				+ d22*composition_CH4_1**2*DeltaPCH4_1**2
				+ d13*composition_CH4_1**1*DeltaPCH4_1**3 
				+ d04*composition_CH4_1**0*DeltaPCH4_1**4)

				density2 = (d00*composition_CH4_2**0*DeltaPCH4_2**0 
				+ d10*composition_CH4_2**1*DeltaPCH4_2**0 
				+ d01*composition_CH4_2**0*DeltaPCH4_2**1 
				+ d20*composition_CH4_2**2*DeltaPCH4_2**0
				+ d11*composition_CH4_2**1*DeltaPCH4_2**1 
				+ d02*composition_CH4_2**0*DeltaPCH4_2**2 
				+ d30*composition_CH4_2**3*DeltaPCH4_2**0 
				+ d21*composition_CH4_2**2*DeltaPCH4_2**1
				+ d12*composition_CH4_2**1*DeltaPCH4_2**2 
				+ d03*composition_CH4_2**0*DeltaPCH4_2**3 
				+ d31*composition_CH4_2**3*DeltaPCH4_2**1 
				+ d22*composition_CH4_2**2*DeltaPCH4_2**2
				+ d13*composition_CH4_2**1*DeltaPCH4_2**3 
				+ d04*composition_CH4_2**0*DeltaPCH4_2**4)


				density3 = (d00*composition_CH4_1**0*DeltaPCH4_2**0 
				+ d10*composition_CH4_1**1*DeltaPCH4_2**0 
				+ d01*composition_CH4_1**0*DeltaPCH4_2**1 
				+ d20*composition_CH4_1**2*DeltaPCH4_2**0
				+ d11*composition_CH4_1**1*DeltaPCH4_2**1 
				+ d02*composition_CH4_1**0*DeltaPCH4_2**2 
				+ d30*composition_CH4_1**3*DeltaPCH4_2**0 
				+ d21*composition_CH4_1**2*DeltaPCH4_2**1
				+ d12*composition_CH4_1**1*DeltaPCH4_2**2 
				+ d03*composition_CH4_1**0*DeltaPCH4_2**3 
				+ d31*composition_CH4_1**3*DeltaPCH4_2**1 
				+ d22*composition_CH4_1**2*DeltaPCH4_2**2
				+ d13*composition_CH4_1**1*DeltaPCH4_2**3 
				+ d04*composition_CH4_1**0*DeltaPCH4_2**4)

				density4 = (d00*composition_CH4_2**0*DeltaPCH4_1**0 
				+ d10*composition_CH4_2**1*DeltaPCH4_1**0 
				+ d01*composition_CH4_2**0*DeltaPCH4_1**1 
				+ d20*composition_CH4_2**2*DeltaPCH4_1**0
				+ d11*composition_CH4_2**1*DeltaPCH4_1**1 
				+ d02*composition_CH4_2**0*DeltaPCH4_1**2 
				+ d30*composition_CH4_2**3*DeltaPCH4_1**0 
				+ d21*composition_CH4_2**2*DeltaPCH4_1**1
				+ d12*composition_CH4_2**1*DeltaPCH4_1**2 
				+ d03*composition_CH4_2**0*DeltaPCH4_1**3 
				+ d31*composition_CH4_2**3*DeltaPCH4_1**1 
				+ d22*composition_CH4_2**2*DeltaPCH4_1**2
				+ d13*composition_CH4_2**1*DeltaPCH4_1**3 
				+ d04*composition_CH4_2**0*DeltaPCH4_1**4)              

				pressure_final = (max(pressure1, pressure2, pressure3, pressure4) + min(pressure1, pressure2, pressure3, pressure4))/2
				uncer_pressure_final = 7 + (max(pressure1, pressure2, pressure3, pressure4) - min(pressure1, pressure2, pressure3, pressure4))/(2*np.sqrt(3)) #uncer= 10

				density_final = (max(density1, density2, density3, density4) + min(density1, density2, density3, density4))/2
				uncer_density_final = 0.002 + (max(density1, density2, density3, density4) - min(density1, density2, density3, density4))/(2*np.sqrt(3)) #uncer = 0.003

				molarvolume1 = 1/(max(density1, density2, density3, density4)/(16*composition_CH4 + 28*composition_N2))
				molarvolume2 = 1/(min(density1, density2, density3, density4)/(16*composition_CH4 + 28*composition_N2))
				molarvolume_final = (molarvolume1 + molarvolume2) / 2
				uncer_molarvolume_final = (molarvolume2 - molarvolume1) / (2*np.sqrt(3))

				print('pressure1', pressure1)
				print('pressure2', pressure2)
				print('pressure3', pressure3)
				print('pressure4', pressure4)

				print('density 1=', density1)
				print('density 2=', density2)
				print('density 3=', density3)
				print('density 4=', density4)

				print("molarvolume1", molarvolume1)
				print("molarvolume2", molarvolume2)
				

				if pressure_final > 650 or pressure1 >650 or pressure2 >650 or pressure_final < -20 or pressure1 <-20 or pressure2 <-20 or density2<0 or density1 <0 or density3<0 or density4<0 or density_final <0:
					popupmsg_OCR()


			if temperature.get() == 22 and composition_CH4 < 0.5: 

				## Calibration equation's coeff of CH4 pur at 22C

				DeltaPCH4= nuCH4_sample - nuCH4_std
				DeltaPCH4_1 = DeltaPCH4 + unc_nuCH4
				DeltaPCH4_2 = DeltaPCH4 - unc_nuCH4
				                         
				## Calibration equation's coeff of CH4-N2 at 22 °C
				p00= 11.54025947
				p10= 50.50169078
				p01= -111.886253
				p20= -779.1830706
				p11= -267.8559604
				p02= -21.843384
				p30= 1444.471381
				p21= -1074.532832
				p12= -741.7473624
				p03= -78.24352803
				p31= 4440.574266
				p22= 2152.94195
				p13= 281.608841
				p04= 9.316994899

				d00= 0.002613123
				d10= 0.107929303
				d01= -0.16185595
				d20= -0.6038034
				d11= 0.26227716
				d02= 0.01568382
				d30= 0.83295667
				d21= -1.20386522
				d12= -0.3627664
				d03= -0.0270527
				d31= 2.314188306
				d22= 0.790609518
				d13= 0.07701417
				d04= 0.001612831


				#### pressure calculation
				pressure1 = (p00*composition_CH4_1**0*DeltaPCH4_1**0 
				+ p10*composition_CH4_1**1*DeltaPCH4_1**0 
				+ p01*composition_CH4_1**0*DeltaPCH4_1**1 
				+ p20*composition_CH4_1**2*DeltaPCH4_1**0 
				+ p11*composition_CH4_1**1*DeltaPCH4_1**1 
				+ p02*composition_CH4_1**0*DeltaPCH4_1**2 
				+ p30*composition_CH4_1**3*DeltaPCH4_1**0 
				+ p21*composition_CH4_1**2*DeltaPCH4_1**1
				+ p12*composition_CH4_1**1*DeltaPCH4_1**2 
				+ p03*composition_CH4_1**0*DeltaPCH4_1**3 
				+ p31*composition_CH4_1**3*DeltaPCH4_1**1 
				+ p22*composition_CH4_1**2*DeltaPCH4_1**2
				+ p13*composition_CH4_1**1*DeltaPCH4_1**3 
				+ p04*composition_CH4_1**0*DeltaPCH4_1**4)

				pressure2 = (p00*composition_CH4_2**0*DeltaPCH4_2**0 
				+ p10*composition_CH4_2**1*DeltaPCH4_2**0 
				+ p01*composition_CH4_2**0*DeltaPCH4_2**1 
				+ p20*composition_CH4_2**2*DeltaPCH4_2**0
				+ p11*composition_CH4_2**1*DeltaPCH4_2**1 
				+ p02*composition_CH4_2**0*DeltaPCH4_2**2 
				+ p30*composition_CH4_2**3*DeltaPCH4_2**0 
				+ p21*composition_CH4_2**2*DeltaPCH4_2**1
				+ p12*composition_CH4_2**1*DeltaPCH4_2**2 
				+ p03*composition_CH4_2**0*DeltaPCH4_2**3 
				+ p31*composition_CH4_2**3*DeltaPCH4_2**1 
				+ p22*composition_CH4_2**2*DeltaPCH4_2**2
				+ p13*composition_CH4_2**1*DeltaPCH4_2**3 
				+ p04*composition_CH4_2**0*DeltaPCH4_2**4)

				pressure3 = (p00*composition_CH4_1**0*DeltaPCH4_2**0 
				+ p10*composition_CH4_1**1*DeltaPCH4_2**0 
				+ p01*composition_CH4_1**0*DeltaPCH4_2**1 
				+ p20*composition_CH4_1**2*DeltaPCH4_2**0
				+ p11*composition_CH4_1**1*DeltaPCH4_2**1 
				+ p02*composition_CH4_1**0*DeltaPCH4_2**2 
				+ p30*composition_CH4_1**3*DeltaPCH4_2**0 
				+ p21*composition_CH4_1**2*DeltaPCH4_2**1
				+ p12*composition_CH4_1**1*DeltaPCH4_2**2 
				+ p03*composition_CH4_1**0*DeltaPCH4_2**3 
				+ p31*composition_CH4_1**3*DeltaPCH4_2**1 
				+ p22*composition_CH4_1**2*DeltaPCH4_2**2
				+ p13*composition_CH4_1**1*DeltaPCH4_2**3 
				+ p04*composition_CH4_1**0*DeltaPCH4_2**4)

				pressure4 = (p00*composition_CH4_2**0*DeltaPCH4_1**0 
				+ p10*composition_CH4_2**1*DeltaPCH4_1**0 
				+ p01*composition_CH4_2**0*DeltaPCH4_1**1 
				+ p20*composition_CH4_2**2*DeltaPCH4_1**0
				+ p11*composition_CH4_2**1*DeltaPCH4_1**1 
				+ p02*composition_CH4_2**0*DeltaPCH4_1**2 
				+ p30*composition_CH4_2**3*DeltaPCH4_1**0 
				+ p21*composition_CH4_2**2*DeltaPCH4_1**1
				+ p12*composition_CH4_2**1*DeltaPCH4_1**2 
				+ p03*composition_CH4_2**0*DeltaPCH4_1**3 
				+ p31*composition_CH4_2**3*DeltaPCH4_1**1 
				+ p22*composition_CH4_2**2*DeltaPCH4_1**2
				+ p13*composition_CH4_2**1*DeltaPCH4_1**3 
				+ p04*composition_CH4_2**0*DeltaPCH4_1**4)

				########################
				#### density calculation

				density1 = (d00*composition_CH4_1**0*DeltaPCH4_1**0 
				+ d10*composition_CH4_1**1*DeltaPCH4_1**0 
				+ d01*composition_CH4_1**0*DeltaPCH4_1**1 
				+ d20*composition_CH4_1**2*DeltaPCH4_1**0 
				+ d11*composition_CH4_1**1*DeltaPCH4_1**1 
				+ d02*composition_CH4_1**0*DeltaPCH4_1**2 
				+ d30*composition_CH4_1**3*DeltaPCH4_1**0 
				+ d21*composition_CH4_1**2*DeltaPCH4_1**1
				+ d12*composition_CH4_1**1*DeltaPCH4_1**2 
				+ d03*composition_CH4_1**0*DeltaPCH4_1**3 
				+ d31*composition_CH4_1**3*DeltaPCH4_1**1 
				+ d22*composition_CH4_1**2*DeltaPCH4_1**2
				+ d13*composition_CH4_1**1*DeltaPCH4_1**3 
				+ d04*composition_CH4_1**0*DeltaPCH4_1**4)

				density2 = (d00*composition_CH4_2**0*DeltaPCH4_2**0 
				+ d10*composition_CH4_2**1*DeltaPCH4_2**0 
				+ d01*composition_CH4_2**0*DeltaPCH4_2**1 
				+ d20*composition_CH4_2**2*DeltaPCH4_2**0
				+ d11*composition_CH4_2**1*DeltaPCH4_2**1 
				+ d02*composition_CH4_2**0*DeltaPCH4_2**2 
				+ d30*composition_CH4_2**3*DeltaPCH4_2**0 
				+ d21*composition_CH4_2**2*DeltaPCH4_2**1
				+ d12*composition_CH4_2**1*DeltaPCH4_2**2 
				+ d03*composition_CH4_2**0*DeltaPCH4_2**3 
				+ d31*composition_CH4_2**3*DeltaPCH4_2**1 
				+ d22*composition_CH4_2**2*DeltaPCH4_2**2
				+ d13*composition_CH4_2**1*DeltaPCH4_2**3 
				+ d04*composition_CH4_2**0*DeltaPCH4_2**4)


				density3 = (d00*composition_CH4_1**0*DeltaPCH4_2**0 
				+ d10*composition_CH4_1**1*DeltaPCH4_2**0 
				+ d01*composition_CH4_1**0*DeltaPCH4_2**1 
				+ d20*composition_CH4_1**2*DeltaPCH4_2**0
				+ d11*composition_CH4_1**1*DeltaPCH4_2**1 
				+ d02*composition_CH4_1**0*DeltaPCH4_2**2 
				+ d30*composition_CH4_1**3*DeltaPCH4_2**0 
				+ d21*composition_CH4_1**2*DeltaPCH4_2**1
				+ d12*composition_CH4_1**1*DeltaPCH4_2**2 
				+ d03*composition_CH4_1**0*DeltaPCH4_2**3 
				+ d31*composition_CH4_1**3*DeltaPCH4_2**1 
				+ d22*composition_CH4_1**2*DeltaPCH4_2**2
				+ d13*composition_CH4_1**1*DeltaPCH4_2**3 
				+ d04*composition_CH4_1**0*DeltaPCH4_2**4)

				density4 = (d00*composition_CH4_2**0*DeltaPCH4_1**0 
				+ d10*composition_CH4_2**1*DeltaPCH4_1**0 
				+ d01*composition_CH4_2**0*DeltaPCH4_1**1 
				+ d20*composition_CH4_2**2*DeltaPCH4_1**0
				+ d11*composition_CH4_2**1*DeltaPCH4_1**1 
				+ d02*composition_CH4_2**0*DeltaPCH4_1**2 
				+ d30*composition_CH4_2**3*DeltaPCH4_1**0 
				+ d21*composition_CH4_2**2*DeltaPCH4_1**1
				+ d12*composition_CH4_2**1*DeltaPCH4_1**2 
				+ d03*composition_CH4_2**0*DeltaPCH4_1**3 
				+ d31*composition_CH4_2**3*DeltaPCH4_1**1 
				+ d22*composition_CH4_2**2*DeltaPCH4_1**2
				+ d13*composition_CH4_2**1*DeltaPCH4_1**3 
				+ d04*composition_CH4_2**0*DeltaPCH4_1**4)              

				pressure_final = (max(pressure1, pressure2, pressure3, pressure4) + min(pressure1, pressure2, pressure3, pressure4))/2
				uncer_pressure_final = 13.4 + (max(pressure1, pressure2, pressure3, pressure4) - min(pressure1, pressure2, pressure3, pressure4))/(2*np.sqrt(3))  #uncer= 19

				density_final = (max(density1, density2, density3, density4) + min(density1, density2, density3, density4))/2
				uncer_density_final = 0.0056 + (max(density1, density2, density3, density4) - min(density1, density2, density3, density4))/(2*np.sqrt(3)) #uncer 0.0056

				molarvolume1 = 1/(max(density1, density2, density3, density4)/(16*composition_CH4 + 28*composition_N2))
				molarvolume2 = 1/(min(density1, density2, density3, density4)/(16*composition_CH4 + 28*composition_N2))
				molarvolume_final = (molarvolume1 + molarvolume2) / 2
				uncer_molarvolume_final = (molarvolume2 - molarvolume1) / (2*np.sqrt(3))

				print('pressure1', pressure1)
				print('pressure2', pressure2)
				print('pressure3', pressure3)
				print('pressure4', pressure4)

				print('density 1=', density1)
				print('density 2=', density2)
				print('density 3=', density3)
				print('density 4=', density4)

				print("molarvolume1", molarvolume1)
				print("molarvolume2", molarvolume2)
				

				if pressure_final > 650 or pressure1 >650 or pressure2 >650 or pressure_final < -20 or pressure1 <-20 or pressure2 <-20 or density2<0 or density1 <0 or density3<0 or density4<0 or density_final <0:
					popupmsg_OCR()

			
			if temperature.get() == 32 and composition_CH4 >= 0.5: 

				## Calibration equation's coeff of CH4 pur at 32C

				DeltaPCH4= nuCH4_sample - nuCH4_std
				DeltaPCH4_1 = DeltaPCH4 + unc_nuCH4
				DeltaPCH4_2 = DeltaPCH4 - unc_nuCH4
				                         
				## Calibration equation's coeff of CH4-N2 at 32 °C
				p00= -172.82
				p10= 862.35
				p01= -188.59
				p20= -1346.66
				p11= 644.02
				p02= 68.58
				p30= 678.52
				p21= -1217.18
				p12= -272.09
				p03= -16.01
				p31= 767.45
				p22= 248.60
				p13= 29.09
				p04= 1.279

				d00= -0.06753
				d10= 0.3112
				d01= -0.2024
				d20= -0.4362
				d11= 0.5052
				d02= 0.02588
				d30= 0.1984
				d21= -0.5917
				d12= -0.06615
				d03= -0.00212
				d31= 0.2576
				d22= 0.04373
				d13= 0.00294
				d04= 0.00008673

				#### pressure calculation
				pressure1 = (p00*composition_CH4_1**0*DeltaPCH4_1**0 
				+ p10*composition_CH4_1**1*DeltaPCH4_1**0 
				+ p01*composition_CH4_1**0*DeltaPCH4_1**1 
				+ p20*composition_CH4_1**2*DeltaPCH4_1**0 
				+ p11*composition_CH4_1**1*DeltaPCH4_1**1 
				+ p02*composition_CH4_1**0*DeltaPCH4_1**2 
				+ p30*composition_CH4_1**3*DeltaPCH4_1**0 
				+ p21*composition_CH4_1**2*DeltaPCH4_1**1
				+ p12*composition_CH4_1**1*DeltaPCH4_1**2 
				+ p03*composition_CH4_1**0*DeltaPCH4_1**3 
				+ p31*composition_CH4_1**3*DeltaPCH4_1**1 
				+ p22*composition_CH4_1**2*DeltaPCH4_1**2
				+ p13*composition_CH4_1**1*DeltaPCH4_1**3 
				+ p04*composition_CH4_1**0*DeltaPCH4_1**4)

				pressure2 = (p00*composition_CH4_2**0*DeltaPCH4_2**0 
				+ p10*composition_CH4_2**1*DeltaPCH4_2**0 
				+ p01*composition_CH4_2**0*DeltaPCH4_2**1 
				+ p20*composition_CH4_2**2*DeltaPCH4_2**0
				+ p11*composition_CH4_2**1*DeltaPCH4_2**1 
				+ p02*composition_CH4_2**0*DeltaPCH4_2**2 
				+ p30*composition_CH4_2**3*DeltaPCH4_2**0 
				+ p21*composition_CH4_2**2*DeltaPCH4_2**1
				+ p12*composition_CH4_2**1*DeltaPCH4_2**2 
				+ p03*composition_CH4_2**0*DeltaPCH4_2**3 
				+ p31*composition_CH4_2**3*DeltaPCH4_2**1 
				+ p22*composition_CH4_2**2*DeltaPCH4_2**2
				+ p13*composition_CH4_2**1*DeltaPCH4_2**3 
				+ p04*composition_CH4_2**0*DeltaPCH4_2**4)

				pressure3 = (p00*composition_CH4_1**0*DeltaPCH4_2**0 
				+ p10*composition_CH4_1**1*DeltaPCH4_2**0 
				+ p01*composition_CH4_1**0*DeltaPCH4_2**1 
				+ p20*composition_CH4_1**2*DeltaPCH4_2**0
				+ p11*composition_CH4_1**1*DeltaPCH4_2**1 
				+ p02*composition_CH4_1**0*DeltaPCH4_2**2 
				+ p30*composition_CH4_1**3*DeltaPCH4_2**0 
				+ p21*composition_CH4_1**2*DeltaPCH4_2**1
				+ p12*composition_CH4_1**1*DeltaPCH4_2**2 
				+ p03*composition_CH4_1**0*DeltaPCH4_2**3 
				+ p31*composition_CH4_1**3*DeltaPCH4_2**1 
				+ p22*composition_CH4_1**2*DeltaPCH4_2**2
				+ p13*composition_CH4_1**1*DeltaPCH4_2**3 
				+ p04*composition_CH4_1**0*DeltaPCH4_2**4)

				pressure4 = (p00*composition_CH4_2**0*DeltaPCH4_1**0 
				+ p10*composition_CH4_2**1*DeltaPCH4_1**0 
				+ p01*composition_CH4_2**0*DeltaPCH4_1**1 
				+ p20*composition_CH4_2**2*DeltaPCH4_1**0
				+ p11*composition_CH4_2**1*DeltaPCH4_1**1 
				+ p02*composition_CH4_2**0*DeltaPCH4_1**2 
				+ p30*composition_CH4_2**3*DeltaPCH4_1**0 
				+ p21*composition_CH4_2**2*DeltaPCH4_1**1
				+ p12*composition_CH4_2**1*DeltaPCH4_1**2 
				+ p03*composition_CH4_2**0*DeltaPCH4_1**3 
				+ p31*composition_CH4_2**3*DeltaPCH4_1**1 
				+ p22*composition_CH4_2**2*DeltaPCH4_1**2
				+ p13*composition_CH4_2**1*DeltaPCH4_1**3 
				+ p04*composition_CH4_2**0*DeltaPCH4_1**4)

				########################
				#### density calculation

				density1 = (d00*composition_CH4_1**0*DeltaPCH4_1**0 
				+ d10*composition_CH4_1**1*DeltaPCH4_1**0 
				+ d01*composition_CH4_1**0*DeltaPCH4_1**1 
				+ d20*composition_CH4_1**2*DeltaPCH4_1**0 
				+ d11*composition_CH4_1**1*DeltaPCH4_1**1 
				+ d02*composition_CH4_1**0*DeltaPCH4_1**2 
				+ d30*composition_CH4_1**3*DeltaPCH4_1**0 
				+ d21*composition_CH4_1**2*DeltaPCH4_1**1
				+ d12*composition_CH4_1**1*DeltaPCH4_1**2 
				+ d03*composition_CH4_1**0*DeltaPCH4_1**3 
				+ d31*composition_CH4_1**3*DeltaPCH4_1**1 
				+ d22*composition_CH4_1**2*DeltaPCH4_1**2
				+ d13*composition_CH4_1**1*DeltaPCH4_1**3 
				+ d04*composition_CH4_1**0*DeltaPCH4_1**4)

				density2 = (d00*composition_CH4_2**0*DeltaPCH4_2**0 
				+ d10*composition_CH4_2**1*DeltaPCH4_2**0 
				+ d01*composition_CH4_2**0*DeltaPCH4_2**1 
				+ d20*composition_CH4_2**2*DeltaPCH4_2**0
				+ d11*composition_CH4_2**1*DeltaPCH4_2**1 
				+ d02*composition_CH4_2**0*DeltaPCH4_2**2 
				+ d30*composition_CH4_2**3*DeltaPCH4_2**0 
				+ d21*composition_CH4_2**2*DeltaPCH4_2**1
				+ d12*composition_CH4_2**1*DeltaPCH4_2**2 
				+ d03*composition_CH4_2**0*DeltaPCH4_2**3 
				+ d31*composition_CH4_2**3*DeltaPCH4_2**1 
				+ d22*composition_CH4_2**2*DeltaPCH4_2**2
				+ d13*composition_CH4_2**1*DeltaPCH4_2**3 
				+ d04*composition_CH4_2**0*DeltaPCH4_2**4)


				density3 = (d00*composition_CH4_1**0*DeltaPCH4_2**0 
				+ d10*composition_CH4_1**1*DeltaPCH4_2**0 
				+ d01*composition_CH4_1**0*DeltaPCH4_2**1 
				+ d20*composition_CH4_1**2*DeltaPCH4_2**0
				+ d11*composition_CH4_1**1*DeltaPCH4_2**1 
				+ d02*composition_CH4_1**0*DeltaPCH4_2**2 
				+ d30*composition_CH4_1**3*DeltaPCH4_2**0 
				+ d21*composition_CH4_1**2*DeltaPCH4_2**1
				+ d12*composition_CH4_1**1*DeltaPCH4_2**2 
				+ d03*composition_CH4_1**0*DeltaPCH4_2**3 
				+ d31*composition_CH4_1**3*DeltaPCH4_2**1 
				+ d22*composition_CH4_1**2*DeltaPCH4_2**2
				+ d13*composition_CH4_1**1*DeltaPCH4_2**3 
				+ d04*composition_CH4_1**0*DeltaPCH4_2**4)

				density4 = (d00*composition_CH4_2**0*DeltaPCH4_1**0 
				+ d10*composition_CH4_2**1*DeltaPCH4_1**0 
				+ d01*composition_CH4_2**0*DeltaPCH4_1**1 
				+ d20*composition_CH4_2**2*DeltaPCH4_1**0
				+ d11*composition_CH4_2**1*DeltaPCH4_1**1 
				+ d02*composition_CH4_2**0*DeltaPCH4_1**2 
				+ d30*composition_CH4_2**3*DeltaPCH4_1**0 
				+ d21*composition_CH4_2**2*DeltaPCH4_1**1
				+ d12*composition_CH4_2**1*DeltaPCH4_1**2 
				+ d03*composition_CH4_2**0*DeltaPCH4_1**3 
				+ d31*composition_CH4_2**3*DeltaPCH4_1**1 
				+ d22*composition_CH4_2**2*DeltaPCH4_1**2
				+ d13*composition_CH4_2**1*DeltaPCH4_1**3 
				+ d04*composition_CH4_2**0*DeltaPCH4_1**4)              

				pressure_final = (max(pressure1, pressure2, pressure3, pressure4) + min(pressure1, pressure2, pressure3, pressure4))/2
				uncer_pressure_final = 7.78 + (max(pressure1, pressure2, pressure3, pressure4) - min(pressure1, pressure2, pressure3, pressure4))/(2*np.sqrt(3)) #uncer = 11

				density_final = (max(density1, density2, density3, density4) + min(density1, density2, density3, density4))/2
				uncer_density_final = 0.002 + (max(density1, density2, density3, density4) - min(density1, density2, density3, density4))/(2*np.sqrt(3)) #uncer = 0.002

				molarvolume1 = 1/(max(density1, density2, density3, density4)/(16*composition_CH4 + 28*composition_N2))
				molarvolume2 = 1/(min(density1, density2, density3, density4)/(16*composition_CH4 + 28*composition_N2))
				molarvolume_final = (molarvolume1 + molarvolume2) / 2
				uncer_molarvolume_final = (molarvolume2 - molarvolume1) / (2*np.sqrt(3))

				print('pressure1', pressure1)
				print('pressure2', pressure2)
				print('pressure3', pressure3)
				print('pressure4', pressure4)

				print('density 1=', density1)
				print('density 2=', density2)
				print('density 3=', density3)
				print('density 4=', density4)

				print("molarvolume1", molarvolume1)
				print("molarvolume2", molarvolume2)
				

				if pressure_final > 650 or pressure1 >650 or pressure2 >650 or pressure_final < -20 or pressure1 <-20 or pressure2 <-20 or density2<0 or density1 <0 or density3<0 or density4<0 or density_final <0:
					popupmsg_OCR()


			if temperature.get() == 32 and composition_CH4 < 0.5: 

				## Calibration equation's coeff of CH4 pur at 32C

				DeltaPCH4= nuCH4_sample - nuCH4_std
				DeltaPCH4_1 = DeltaPCH4 + unc_nuCH4
				DeltaPCH4_2 = DeltaPCH4 - unc_nuCH4
				                     
				## Calibration equation's coeff of CH4-N2 at 32 °C
				p00= -37.14
				p10= 746.68
				p01= -197.31
				p20= -3310.32 
				p11= 1388.21
				p02= 97.16
				p30= 4097.22
				p21= -6921.35
				p12= -1024.40
				p03= -48.88
				p31= 10121.08
				p22= 2221.96
				p13= 223.16
				p04= 10.04

				d00= 0.01993
				d10= -0.08883
				d01= -0.1465
				d20= 0.02792
				d11= 0.1963
				d02= 0.06475
				d30= 0.2052
				d21= -0.7082
				d12= -0.5293
				d03= -0.01924
				d31= 1.559
				d22= 0.9825
				d13= 0.07004
				d04= 0.002134

				#### pressure calculation
				pressure1 = (p00*composition_CH4_1**0*DeltaPCH4_1**0 
				+ p10*composition_CH4_1**1*DeltaPCH4_1**0 
				+ p01*composition_CH4_1**0*DeltaPCH4_1**1 
				+ p20*composition_CH4_1**2*DeltaPCH4_1**0 
				+ p11*composition_CH4_1**1*DeltaPCH4_1**1 
				+ p02*composition_CH4_1**0*DeltaPCH4_1**2 
				+ p30*composition_CH4_1**3*DeltaPCH4_1**0 
				+ p21*composition_CH4_1**2*DeltaPCH4_1**1
				+ p12*composition_CH4_1**1*DeltaPCH4_1**2 
				+ p03*composition_CH4_1**0*DeltaPCH4_1**3 
				+ p31*composition_CH4_1**3*DeltaPCH4_1**1 
				+ p22*composition_CH4_1**2*DeltaPCH4_1**2
				+ p13*composition_CH4_1**1*DeltaPCH4_1**3 
				+ p04*composition_CH4_1**0*DeltaPCH4_1**4)

				pressure2 = (p00*composition_CH4_2**0*DeltaPCH4_2**0 
				+ p10*composition_CH4_2**1*DeltaPCH4_2**0 
				+ p01*composition_CH4_2**0*DeltaPCH4_2**1 
				+ p20*composition_CH4_2**2*DeltaPCH4_2**0
				+ p11*composition_CH4_2**1*DeltaPCH4_2**1 
				+ p02*composition_CH4_2**0*DeltaPCH4_2**2 
				+ p30*composition_CH4_2**3*DeltaPCH4_2**0 
				+ p21*composition_CH4_2**2*DeltaPCH4_2**1
				+ p12*composition_CH4_2**1*DeltaPCH4_2**2 
				+ p03*composition_CH4_2**0*DeltaPCH4_2**3 
				+ p31*composition_CH4_2**3*DeltaPCH4_2**1 
				+ p22*composition_CH4_2**2*DeltaPCH4_2**2
				+ p13*composition_CH4_2**1*DeltaPCH4_2**3 
				+ p04*composition_CH4_2**0*DeltaPCH4_2**4)

				pressure3 = (p00*composition_CH4_1**0*DeltaPCH4_2**0 
				+ p10*composition_CH4_1**1*DeltaPCH4_2**0 
				+ p01*composition_CH4_1**0*DeltaPCH4_2**1 
				+ p20*composition_CH4_1**2*DeltaPCH4_2**0
				+ p11*composition_CH4_1**1*DeltaPCH4_2**1 
				+ p02*composition_CH4_1**0*DeltaPCH4_2**2 
				+ p30*composition_CH4_1**3*DeltaPCH4_2**0 
				+ p21*composition_CH4_1**2*DeltaPCH4_2**1
				+ p12*composition_CH4_1**1*DeltaPCH4_2**2 
				+ p03*composition_CH4_1**0*DeltaPCH4_2**3 
				+ p31*composition_CH4_1**3*DeltaPCH4_2**1 
				+ p22*composition_CH4_1**2*DeltaPCH4_2**2
				+ p13*composition_CH4_1**1*DeltaPCH4_2**3 
				+ p04*composition_CH4_1**0*DeltaPCH4_2**4)

				pressure4 = (p00*composition_CH4_2**0*DeltaPCH4_1**0 
				+ p10*composition_CH4_2**1*DeltaPCH4_1**0 
				+ p01*composition_CH4_2**0*DeltaPCH4_1**1 
				+ p20*composition_CH4_2**2*DeltaPCH4_1**0
				+ p11*composition_CH4_2**1*DeltaPCH4_1**1 
				+ p02*composition_CH4_2**0*DeltaPCH4_1**2 
				+ p30*composition_CH4_2**3*DeltaPCH4_1**0 
				+ p21*composition_CH4_2**2*DeltaPCH4_1**1
				+ p12*composition_CH4_2**1*DeltaPCH4_1**2 
				+ p03*composition_CH4_2**0*DeltaPCH4_1**3 
				+ p31*composition_CH4_2**3*DeltaPCH4_1**1 
				+ p22*composition_CH4_2**2*DeltaPCH4_1**2
				+ p13*composition_CH4_2**1*DeltaPCH4_1**3 
				+ p04*composition_CH4_2**0*DeltaPCH4_1**4)

				########################
				#### density calculation

				density1 = (d00*composition_CH4_1**0*DeltaPCH4_1**0 
				+ d10*composition_CH4_1**1*DeltaPCH4_1**0 
				+ d01*composition_CH4_1**0*DeltaPCH4_1**1 
				+ d20*composition_CH4_1**2*DeltaPCH4_1**0 
				+ d11*composition_CH4_1**1*DeltaPCH4_1**1 
				+ d02*composition_CH4_1**0*DeltaPCH4_1**2 
				+ d30*composition_CH4_1**3*DeltaPCH4_1**0 
				+ d21*composition_CH4_1**2*DeltaPCH4_1**1
				+ d12*composition_CH4_1**1*DeltaPCH4_1**2 
				+ d03*composition_CH4_1**0*DeltaPCH4_1**3 
				+ d31*composition_CH4_1**3*DeltaPCH4_1**1 
				+ d22*composition_CH4_1**2*DeltaPCH4_1**2
				+ d13*composition_CH4_1**1*DeltaPCH4_1**3 
				+ d04*composition_CH4_1**0*DeltaPCH4_1**4)

				density2 = (d00*composition_CH4_2**0*DeltaPCH4_2**0 
				+ d10*composition_CH4_2**1*DeltaPCH4_2**0 
				+ d01*composition_CH4_2**0*DeltaPCH4_2**1 
				+ d20*composition_CH4_2**2*DeltaPCH4_2**0
				+ d11*composition_CH4_2**1*DeltaPCH4_2**1 
				+ d02*composition_CH4_2**0*DeltaPCH4_2**2 
				+ d30*composition_CH4_2**3*DeltaPCH4_2**0 
				+ d21*composition_CH4_2**2*DeltaPCH4_2**1
				+ d12*composition_CH4_2**1*DeltaPCH4_2**2 
				+ d03*composition_CH4_2**0*DeltaPCH4_2**3 
				+ d31*composition_CH4_2**3*DeltaPCH4_2**1 
				+ d22*composition_CH4_2**2*DeltaPCH4_2**2
				+ d13*composition_CH4_2**1*DeltaPCH4_2**3 
				+ d04*composition_CH4_2**0*DeltaPCH4_2**4)


				density3 = (d00*composition_CH4_1**0*DeltaPCH4_2**0 
				+ d10*composition_CH4_1**1*DeltaPCH4_2**0 
				+ d01*composition_CH4_1**0*DeltaPCH4_2**1 
				+ d20*composition_CH4_1**2*DeltaPCH4_2**0
				+ d11*composition_CH4_1**1*DeltaPCH4_2**1 
				+ d02*composition_CH4_1**0*DeltaPCH4_2**2 
				+ d30*composition_CH4_1**3*DeltaPCH4_2**0 
				+ d21*composition_CH4_1**2*DeltaPCH4_2**1
				+ d12*composition_CH4_1**1*DeltaPCH4_2**2 
				+ d03*composition_CH4_1**0*DeltaPCH4_2**3 
				+ d31*composition_CH4_1**3*DeltaPCH4_2**1 
				+ d22*composition_CH4_1**2*DeltaPCH4_2**2
				+ d13*composition_CH4_1**1*DeltaPCH4_2**3 
				+ d04*composition_CH4_1**0*DeltaPCH4_2**4)

				density4 = (d00*composition_CH4_2**0*DeltaPCH4_1**0 
				+ d10*composition_CH4_2**1*DeltaPCH4_1**0 
				+ d01*composition_CH4_2**0*DeltaPCH4_1**1 
				+ d20*composition_CH4_2**2*DeltaPCH4_1**0
				+ d11*composition_CH4_2**1*DeltaPCH4_1**1 
				+ d02*composition_CH4_2**0*DeltaPCH4_1**2 
				+ d30*composition_CH4_2**3*DeltaPCH4_1**0 
				+ d21*composition_CH4_2**2*DeltaPCH4_1**1
				+ d12*composition_CH4_2**1*DeltaPCH4_1**2 
				+ d03*composition_CH4_2**0*DeltaPCH4_1**3 
				+ d31*composition_CH4_2**3*DeltaPCH4_1**1 
				+ d22*composition_CH4_2**2*DeltaPCH4_1**2
				+ d13*composition_CH4_2**1*DeltaPCH4_1**3 
				+ d04*composition_CH4_2**0*DeltaPCH4_1**4)              

				pressure_final = (max(pressure1, pressure2, pressure3, pressure4) + min(pressure1, pressure2, pressure3, pressure4))/2
				uncer_pressure_final = 12.8 + (max(pressure1, pressure2, pressure3, pressure4) - min(pressure1, pressure2, pressure3, pressure4))/(2*np.sqrt(3)) #uncer = 18

				density_final = (max(density1, density2, density3, density4) + min(density1, density2, density3, density4))/2
				uncer_density_final = 0.0042 + (max(density1, density2, density3, density4) - min(density1, density2, density3, density4))/(2*np.sqrt(3)) # uncer = 0.006

				molarvolume1 = 1/(max(density1, density2, density3, density4)/(16*composition_CH4 + 28*composition_N2))
				molarvolume2 = 1/(min(density1, density2, density3, density4)/(16*composition_CH4 + 28*composition_N2))
				molarvolume_final = (molarvolume1 + molarvolume2) / 2
				uncer_molarvolume_final = (molarvolume2 - molarvolume1) / (2*np.sqrt(3))

				print('pressure1', pressure1)
				print('pressure2', pressure2)
				print('pressure3', pressure3)
				print('pressure4', pressure4)

				print('density 1=', density1)
				print('density 2=', density2)
				print('density 3=', density3)
				print('density 4=', density4)

				print("molarvolume1", molarvolume1)
				print("molarvolume2", molarvolume2)
				

				if pressure_final > 650 or pressure1 >650 or pressure2 >650 or pressure_final < -20 or pressure1 <-20 or pressure2 <-20 or density2<0 or density1 <0 or density3<0 or density4<0 or density_final<0:
					popupmsg_OCR()

			####### GET RESULTS AND BUT ON THE OUT PUT FEILD (out put field just be created below) ################       
			composition_CH4_display.insert(tk.END, "%.3f" % composition_CH4)
			composition_N2_display.insert(tk.END, "%.3f" % composition_N2)
			pressure.insert(tk.END, "%.1f" % pressure_final)
			density.insert(tk.END, "%.3f" % density_final)
			molarvolume.insert(tk.END, "%.1f" % molarvolume_final)

			uncer_pressure.insert(tk.END, "%.1f" % uncer_pressure_final)
			uncer_density.insert(tk.END, "%.3f" % uncer_density_final)
			uncer_molarvolume.insert(tk.END, "%.3f" % uncer_molarvolume_final)

		# ################################    
		# ########  display results ######
		# ################################ 
		composition_CH4_display= tk.Entry(self.frame, width = 20) #, state='disabled'
		composition_CH4_display.grid(row=36, column=1)        
		composition_N2_display= tk.Entry(self.frame, width = 20) #, state='disabled'
		composition_N2_display.grid(row=36, column=3)

		pressure= tk.Entry(self.frame, width = 20) #, state='disabled'
		pressure.grid(row=39, column=1)
		density = tk.Entry(self.frame, width = 20) 
		density.grid(row=40, column=1)
		molarvolume = tk.Entry(self.frame,  width = 20)
		molarvolume.grid(row=41, column=1)

		######## display uncertainty ########
		
		uncer_pressure = tk.Entry(self.frame,  width = 20) #, state='disabled'
		uncer_pressure.grid(row=39, column=3)
		uncer_density = tk.Entry(self.frame,  width = 20) 
		uncer_density.grid(row=40, column=3)
		uncer_molarvolume = tk.Entry(self.frame,  width = 20) 
		uncer_molarvolume.grid(row=41, column=3)


		#############################
		######### Buttons ###########
		#############################

		self.button1_1 = tk.Button(self.frame, text="Clear Input", command=clear_field_inputs)
		self.button1_1.grid(row=16, column=1, padx=10)
		self.button1_2 = tk.Button(self.frame, text="Calculate", bg="green", width=10, command=calculCH4pure)
		self.button1_2.grid(row=34, column=1, padx=20, pady=10, sticky="W")        
		self.button1_3 = tk.Button(self.frame, text="Clear Results", width=10, command=clear_field_results)
		self.button1_3.grid(row=42, column=1, padx=20)

		
		# def OpenSuppDoc_CH4N2():
		# 	os.startfile(resource_path('SuppDoc_CH4N2.pdf'))

		# self.button1_4 = tk.Button(self.frame, text="Supplement document", bg="orange", command=OpenSuppDoc_CH4N2)
		# self.button1_4.grid(row=42, column=0, padx=20, pady=10, sticky='w')

			
		self.quit = tk.Button(self.frame, text="Close", width=13, command=self.close_window)	
		self.quit.grid(row=42, column=3, padx=10)

	def close_window(self):
		self.master.destroy()

#########################################
########### Module CO2 - CH4 #############
#########################################
class module5: 
	def __init__(self, master, number):
		self.master = master
		self.master.title("FRAnCIs v.1.0.1 - (CO₂-CH₄ mixtures)")
		self.master.geometry("750x650")
		self.master.resizable(width=False, height=False)
		self.master.iconbitmap(resource_path("logo.ico"))
		self.frame=tk.Frame(self.master)
		self.frame.grid()

		### Create the UI of windows of module 3 
		self.label = tk.Label(self.frame, text="Calculation for CO₂-CH₄ mixtures", font=('bold', 18))
		self.label.grid(row=0, column=1, columnspan=10, padx=30, pady=10, sticky="W") #remove (side="top", fill="x",)        

		self.label = tk.Label(self.frame, text="- The area of two CO₂ bands (area_CO2) and of CH₄ \u03BD₁ band (area_CH4) are used for determination of composition.")
		self.label.grid(row=1, column=0, columnspan=10, padx=10, sticky="W") #remove (side="top", fill="x",)   

		self.label = tk.Label(self.frame, text="- If the CO₂ concentration > 50 mol%, the CO₂ Fermi diad splitting (\u0394_sample and \u0394_std) are used for pressure and density determination.")
		self.label.grid(row=2, column=0, columnspan=10,padx=10, sticky="W") #remove (side="top", fill="x",)
		self.label = tk.Label(self.frame, text="- If the CH₄ concentration ≥ 50 mol%, the CH₄ \u03BD₁ band position (\u03BD₁_sample and \u03BD₁_std) are used for pressure and density determination.")
		self.label.grid(row=3, column=0, columnspan=10,padx=10, sticky="W") #remove (side="top", fill="x",)
		
		#self.label = tk.Label(self.frame,text="______________________________________________________________________________________________________________________________________________________________")
		#self.label.grid(row=5, column=0, padx=10, columnspan=10, sticky="E")


		self.label_remark = tk.Label(self.frame, text="Remarks:", font=('bold', 12))
		self.label_remark.grid(row=7, column=0, columnspan=10, padx=10,  sticky="W")

		self.label = tk.Label(self.frame, text="   - The calibrations were made over 5-600 bars, out of this range may cause larger errors or aberrant values.")
		self.label.grid(row=8, column=0, columnspan=10, sticky="W")
		self.label = tk.Label(self.frame, text="   - If the Dassin spectrometer (at GeoRessouces lab) is selected, (\u0394_std) is not required, and so type 0.")
		self.label.grid(row=9, column=0, columnspan=10, sticky="W")  
		self.label = tk.Label(self.frame, text="   - The fitted peak position of CH₄ should be corrected by two neon emission lines at ~2851.38 and ~2972.44 cm\u207b\u00B9 (relative to 514.53 nm)")
		self.label.grid(row=10, column=0, columnspan=10, sticky="W")
		self.label = tk.Label(self.frame, text="   - The uncertainty (1\u03C3) on the measured concentration is ~ ±0.5 mol%")
		self.label.grid(row=13, column=0, columnspan=10, sticky="W")
		# self.label = tk.Label(self.frame, text="   - Click 'Supplement document' button below for more detail.")
		# self.label.grid(row=14, column=0, columnspan=10, sticky="W")		

		###############################
		##### INPUT section ###########
		###############################

		self.label_input = tk.Label(self.frame, text="_____________     INPUT:", font=('bold', 10))
		self.label_input.grid(row=16, column=0, pady=10, sticky="E")
		self.label = tk.Label(self.frame,text="_____________________________________________________________________________________")
		self.label.grid(row=16, column=2, columnspan=10,padx=10, sticky="E")

		###############################
		##### Select Température #####
		###############################
		self.label = tk.Label(self.frame, text="Select temperature :")
		self.label.grid(row=20, column=0, columnspan=2, padx=10, sticky="W") #remove (side="top", fill="x",)

		temperature = tk.IntVar()
		temperature.set(22)

		def selected_temperature():
			print(temperature.get())

		self.Rbtn1=tk.Radiobutton(self.frame, text="22 °C", variable=temperature, value=22, padx = 20,  command=selected_temperature).grid(row=20, column=1,  padx=10, sticky="W")
		self.Rbtn1=tk.Radiobutton(self.frame, text="32 °C", variable=temperature, value=32, padx = 20,  command=selected_temperature).grid(row=20, column=2,  padx=10, sticky="W")

		###############################
		##### Select Instrument #####
		###############################

		self.label = tk.Label(self.frame, text="Select spectrometers :")
		self.label.grid(row=21, column=0, columnspan=2, padx=10, sticky="W") #remove (side="top", fill="x",)

		instrument = tk.IntVar()
		instrument.set(1) #Dassin = 1, other spectrometers= 2

		def selected_instrument():
			print(instrument.get())

		self.Rbtn1=tk.Radiobutton(self.frame, text="Dassin", variable=instrument, value=1, padx = 20,  command=selected_instrument).grid(row=21, column=1,  padx=10, sticky="W")
		self.Rbtn1=tk.Radiobutton(self.frame, text="Other Spectrometers", variable=instrument, value=2, padx = 20, pady = 5, command=selected_instrument).grid(row=21, column=2,  padx=10, sticky="W")


		####################################
		##### Select Laser wavelength #####
		####################################

		self.label = tk.Label(self.frame, text="Laser wavelength (nm):")
		self.label.grid(row=21, column=3, columnspan=2, padx=30, stick="W") #remove (side="top", fill="x",)

		# options = {"488 nm": 488, "514 nm": 514, "532 nm": 532, "633 nm": 633, "785 nm": 785}
		options=[488, 514, 532, 633, 785]
		laser_wavelength = tk.IntVar()
		laser_wavelength.set(514)
		
		# self.menu = OptionMenu(self.frame, laser_wavelength, *options.keys()).grid(row=26, column=4, stick="W")
		self.menu = OptionMenu(self.frame, laser_wavelength, *options).grid(row=21, column=4)


		######### ENTRY ##########
		##########################

		##entry CO2 spectroscopic data 

		self.label = tk.Label(self.frame, text="area_CO2")
		self.label.grid(row=27, column=1, padx=10)
		self.label = tk.Label(self.frame, text="\u0394_sample (cm\u207b\u00B9)")
		self.label.grid(row=27, column=2, padx=10)
		self.label = tk.Label(self.frame, text="\u0394_std (cm\u207b\u00B9)")
		self.label.grid(row=27, column=3, padx=10)
		self.label = tk.Label(self.frame, text="\u0394_uncertainty (cm\u207b\u00B9)")
		self.label.grid(row=27, column=4, padx=10)

		self.label = tk.Label(self.frame, text="Spectroscopic data of CO₂")
		self.label.grid(row=28, column=0, padx=10,  sticky="W")
		
		self.area_CO2_entry = tk.Entry(self.frame, width = 15)
		self.area_CO2_entry.grid(row=28, column=1)
		self.FDS_entry = tk.Entry(self.frame, width = 15)
		self.FDS_entry.grid(row=28, column=2)
		self.FDS_entry_std = tk.Entry(self.frame, width = 15)
		self.FDS_entry_std.grid(row=28, column=3)
		self.unc_FDS_entry = tk.Entry(self.frame, width = 15)
		self.unc_FDS_entry.grid(row=28, column=4)

		##entry CH4 spectroscopic data 

		self.label = tk.Label(self.frame, text="area_CH4")
		self.label.grid(row=29, column=1, padx=10)
		self.label = tk.Label(self.frame, text="\u03BD₁_sample (cm\u207b\u00B9)")
		self.label.grid(row=29, column=2, padx=10)
		self.label = tk.Label(self.frame, text="\u03BD₁_std (cm\u207b\u00B9)")
		self.label.grid(row=29, column=3, padx=10)
		self.label = tk.Label(self.frame, text="\u03BD₁_Uncertainty (cm\u207b\u00B9)")
		self.label.grid(row=29, column=4, padx=10)

		self.label = tk.Label(self.frame, text="Spectroscopic data of CH₄ :")
		self.label.grid(row=30, column=0, padx=10, sticky="W")
		
		self.area_CH4_entry = tk.Entry(self.frame, width = 15)
		self.area_CH4_entry.grid(row=30, column=1)

		self.nuCH4_sample_entry = tk.Entry(self.frame, width = 15)
		self.nuCH4_sample_entry.grid(row=30, column=2)
		self.nuCH4_std_entry = tk.Entry(self.frame, width = 15)
		self.nuCH4_std_entry.grid(row=30, column=3)
		self.unc_nuCH4_entry = tk.Entry(self.frame, width = 15)
		self.unc_nuCH4_entry.grid(row=30, column=4)

		######################
		### OUTPUT ###############

		self.label = tk.Label(self.frame, text="_____________  OUTPUT:", font=('bold', 10))
		self.label.grid(row=35, column=0,  sticky="E")
		self.label = tk.Label(self.frame, text="_____________________________________________________________________________________")
		self.label.grid(row=35, column=2, columnspan=10, padx=10, sticky="E")        

		self.label = tk.Label(self.frame, text="(mol% CO₂)")
		self.label.grid(row=36, column=1, padx=10)
		self.label = tk.Label(self.frame, text="(mol% CH₄)")
		self.label.grid(row=36, column=3, padx=10)

		self.label = tk.Label(self.frame, text="Composition")
		self.label.grid(row=37, column=0, padx=10,  sticky="W")
		self.label = tk.Label(self.frame, text="(±0.5 mol%)")
		self.label.grid(row=37, column=4, sticky="W")
		self.label = tk.Label(self.frame, text="-------------------------------------------------------------")
		self.label.grid(row=38, column=1, columnspan=3, padx=10)

		self.label = tk.Label(self.frame, text="Pressure")
		self.label.grid(row=39, column=0, padx=10, pady=5, sticky="W")
		self.label = tk.Label(self.frame, text="Density")
		self.label.grid(row=40, column=0, padx=10, pady=5, sticky="W")
		self.label = tk.Label(self.frame, text="Molar Volume")
		self.label.grid(row=41, column=0, padx=10, pady=5, sticky="W")

		
		self.label = tk.Label(self.frame, text="±")
		self.label.grid(row=39, column=2, padx=10, pady=5)
		self.label = tk.Label(self.frame, text="±")
		self.label.grid(row=40, column=2, padx=10, pady=5)
		self.label = tk.Label(self.frame, text="±")
		self.label.grid(row=41, column=2, padx=10, pady=5)

		
		
		self.label = tk.Label(self.frame, text="(bar)")
		self.label.grid(row=39, column=4, pady=5, sticky="W")
		self.label = tk.Label(self.frame, text="(g.cm\u207b\u00B3)")
		self.label.grid(row=40, column=4, pady=5, sticky="W")
		self.label = tk.Label(self.frame, text="(cm\u00B3.mol\u207b\u00B9)")
		self.label.grid(row=41, column=4, pady=5, sticky="W")


		###############################
		##### Caculation ##############
		###############################

		#### Make a clear-button for input field
		def clear_field_inputs(): 
			self.area_CO2_entry.delete(0, tk.END)
			self.FDS_entry.delete(0, tk.END)
			self.FDS_entry_std.delete(0, tk.END)
			self.unc_FDS_entry.delete(0, tk.END)
			
			self.area_CH4_entry.delete(0, tk.END)
			self.nuCH4_sample_entry.delete(0, tk.END)
			self.nuCH4_std_entry.delete(0, tk.END)
			self.unc_nuCH4_entry.delete(0, tk.END)
			
		#### Make a clear-button for output field
		def clear_field_results():
			composition_CO2_display.delete(0, tk.END)
			composition_CH4_display.delete(0, tk.END)
			pressure.delete(0, tk.END)
			density.delete(0, tk.END)
			molarvolume.delete(0, tk.END)
			uncer_pressure.delete(0, tk.END)
			uncer_density.delete(0, tk.END)
			uncer_molarvolume.delete(0, tk.END)


		def calculCO2CH4():
			clear_field_results()
			
			area_CO2        = float(self.area_CO2_entry.get())
			FDS    			= float(self.FDS_entry.get())
			FDS_std    		= float(self.FDS_entry_std.get())
			unc_FDS       	= float(self.unc_FDS_entry.get())

			area_CH4    	= float(self.area_CH4_entry.get())
			nuCH4_sample 	= float(self.nuCH4_sample_entry.get())
			nuCH4_std 		= float(self.nuCH4_std_entry.get())
			unc_nuCH4 		= float(self.unc_nuCH4_entry.get())


			### Composition calculation

			if laser_wavelength.get() == 488:
				RRSCS_CO2 = 2.30
				RRSCS_CH4 = 7.80
			if laser_wavelength.get() == 514:
				RRSCS_CO2 = 2.29
				RRSCS_CH4 = 7.73
			if laser_wavelength.get() == 532:
				RRSCS_CO2 = 2.27
				RRSCS_CH4 = 7.69
			if laser_wavelength.get() == 633:
				RRSCS_CO2 = 2.20
				RRSCS_CH4 = 7.44
			if laser_wavelength.get() == 785:
				RRSCS_CO2 = 2.09
				RRSCS_CH4 = 7.05
			
			print('the wavelength of the selected laser is', laser_wavelength.get(), 'nm')
			print('RRSCS_CH4=', RRSCS_CH4)		
			print('RRSCS_C02=', RRSCS_CO2)
			         
			composition_CO2 = ((area_CO2/RRSCS_CO2)/((area_CO2/RRSCS_CO2) + (area_CH4/RRSCS_CH4)))
			composition_CH4 = 1 - composition_CO2
			composition_CH4_1 = composition_CH4 + 0.005
			composition_CH4_2 = composition_CH4 - 0.005
						

			if temperature.get() == 22 and instrument.get() ==1 and composition_CO2 > 0.5: 

				## Calibration equation's coeff of CO2-CH4 at 22 °C over 5-600 bars

				# normalisation of concentration and of Fermi diad splitting ( 5-600 bars)
				composition_CO2_normalized_1 = (composition_CO2 + 0.005 - 0.7932)/0.1749
				composition_CO2_normalized_2 = (composition_CO2 - 0.005 - 0.7932)/0.1749
				FDS_normalized_1 = (FDS + unc_FDS - 103.96)/0.7906
				FDS_normalized_2 = (FDS - unc_FDS - 103.96)/0.7906
				
				p00= 112.44615
				p10= -82.57782
				p01= 113.28978
				p20= 38.5788
				p11= -206.51994
				p02= 187.13795
				p30= -23.37331
				p21= 96.30156
				p12= -191.33849
				p03= 125.1294
				p31= -16.90882
				p22= 51.29517
				p13= -59.93642
				p04= 10.40779


				d00= 0.524122882
				d10= -0.036729729
				d01= 0.395542204
				d20= -0.004702814
				d11= 0.005686733
				d02= -0.022846683
				d30= -0.002359074
				d21= -0.022675822
				d12= 0.05252559
				d03= -0.04411769
				d31= 0.001715852
				d22= -0.014560002
				d13= 0.019476762
				d04= -0.00332977

				#### pressure calculation
				pressure1 = (p00*composition_CO2_normalized_1**0*FDS_normalized_1**0 
				+ p10*composition_CO2_normalized_1**1*FDS_normalized_1**0 
				+ p01*composition_CO2_normalized_1**0*FDS_normalized_1**1 
				+ p20*composition_CO2_normalized_1**2*FDS_normalized_1**0 
				+ p11*composition_CO2_normalized_1**1*FDS_normalized_1**1 
				+ p02*composition_CO2_normalized_1**0*FDS_normalized_1**2 
				+ p30*composition_CO2_normalized_1**3*FDS_normalized_1**0 
				+ p21*composition_CO2_normalized_1**2*FDS_normalized_1**1
				+ p12*composition_CO2_normalized_1**1*FDS_normalized_1**2 
				+ p03*composition_CO2_normalized_1**0*FDS_normalized_1**3 
				+ p31*composition_CO2_normalized_1**3*FDS_normalized_1**1 
				+ p22*composition_CO2_normalized_1**2*FDS_normalized_1**2
				+ p13*composition_CO2_normalized_1**1*FDS_normalized_1**3 
				+ p04*composition_CO2_normalized_1**0*FDS_normalized_1**4)

				pressure2 = (p00*composition_CO2_normalized_2**0*FDS_normalized_2**0 
				+ p10*composition_CO2_normalized_2**1*FDS_normalized_2**0 
				+ p01*composition_CO2_normalized_2**0*FDS_normalized_2**1 
				+ p20*composition_CO2_normalized_2**2*FDS_normalized_2**0
				+ p11*composition_CO2_normalized_2**1*FDS_normalized_2**1 
				+ p02*composition_CO2_normalized_2**0*FDS_normalized_2**2
				+ p30*composition_CO2_normalized_2**3*FDS_normalized_2**0 
				+ p21*composition_CO2_normalized_2**2*FDS_normalized_2**1
				+ p12*composition_CO2_normalized_2**1*FDS_normalized_2**2 
				+ p03*composition_CO2_normalized_2**0*FDS_normalized_2**3 
				+ p31*composition_CO2_normalized_2**3*FDS_normalized_2**1 
				+ p22*composition_CO2_normalized_2**2*FDS_normalized_2**2
				+ p13*composition_CO2_normalized_2**1*FDS_normalized_2**3 
				+ p04*composition_CO2_normalized_2**0*FDS_normalized_2**4)

				pressure3 = (p00*composition_CO2_normalized_1**0*FDS_normalized_2**0 
				+ p10*composition_CO2_normalized_1**1*FDS_normalized_2**0 
				+ p01*composition_CO2_normalized_1**0*FDS_normalized_2**1 
				+ p20*composition_CO2_normalized_1**2*FDS_normalized_2**0
				+ p11*composition_CO2_normalized_1**1*FDS_normalized_2**1 
				+ p02*composition_CO2_normalized_1**0*FDS_normalized_2**2 
				+ p30*composition_CO2_normalized_1**3*FDS_normalized_2**0 
				+ p21*composition_CO2_normalized_1**2*FDS_normalized_2**1
				+ p12*composition_CO2_normalized_1**1*FDS_normalized_2**2 
				+ p03*composition_CO2_normalized_1**0*FDS_normalized_2**3 
				+ p31*composition_CO2_normalized_1**3*FDS_normalized_2**1 
				+ p22*composition_CO2_normalized_1**2*FDS_normalized_2**2
				+ p13*composition_CO2_normalized_1**1*FDS_normalized_2**3 
				+ p04*composition_CO2_normalized_1**0*FDS_normalized_2**4)

				pressure4 = (p00*composition_CO2_normalized_2**0*FDS_normalized_1**0 
				+ p10*composition_CO2_normalized_2**1*FDS_normalized_1**0 
				+ p01*composition_CO2_normalized_2**0*FDS_normalized_1**1 
				+ p20*composition_CO2_normalized_2**2*FDS_normalized_1**0
				+ p11*composition_CO2_normalized_2**1*FDS_normalized_1**1 
				+ p02*composition_CO2_normalized_2**0*FDS_normalized_1**2 
				+ p30*composition_CO2_normalized_2**3*FDS_normalized_1**0 
				+ p21*composition_CO2_normalized_2**2*FDS_normalized_1**1
				+ p12*composition_CO2_normalized_2**1*FDS_normalized_1**2 
				+ p03*composition_CO2_normalized_2**0*FDS_normalized_1**3 
				+ p31*composition_CO2_normalized_2**3*FDS_normalized_1**1 
				+ p22*composition_CO2_normalized_2**2*FDS_normalized_1**2
				+ p13*composition_CO2_normalized_2**1*FDS_normalized_1**3 
				+ p04*composition_CO2_normalized_2**0*FDS_normalized_1**4)

				########################
				#### density calculation

				density1 = (d00*composition_CO2_normalized_1**0*FDS_normalized_1**0 
				+ d10*composition_CO2_normalized_1**1*FDS_normalized_1**0 
				+ d01*composition_CO2_normalized_1**0*FDS_normalized_1**1 
				+ d20*composition_CO2_normalized_1**2*FDS_normalized_1**0 
				+ d11*composition_CO2_normalized_1**1*FDS_normalized_1**1 
				+ d02*composition_CO2_normalized_1**0*FDS_normalized_1**2 
				+ d30*composition_CO2_normalized_1**3*FDS_normalized_1**0 
				+ d21*composition_CO2_normalized_1**2*FDS_normalized_1**1
				+ d12*composition_CO2_normalized_1**1*FDS_normalized_1**2 
				+ d03*composition_CO2_normalized_1**0*FDS_normalized_1**3 
				+ d31*composition_CO2_normalized_1**3*FDS_normalized_1**1 
				+ d22*composition_CO2_normalized_1**2*FDS_normalized_1**2
				+ d13*composition_CO2_normalized_1**1*FDS_normalized_1**3 
				+ d04*composition_CO2_normalized_1**0*FDS_normalized_1**4)

				density2 = (d00*composition_CO2_normalized_2**0*FDS_normalized_2**0 
				+ d10*composition_CO2_normalized_2**1*FDS_normalized_2**0 
				+ d01*composition_CO2_normalized_2**0*FDS_normalized_2**1 
				+ d20*composition_CO2_normalized_2**2*FDS_normalized_2**0
				+ d11*composition_CO2_normalized_2**1*FDS_normalized_2**1 
				+ d02*composition_CO2_normalized_2**0*FDS_normalized_2**2
				+ d30*composition_CO2_normalized_2**3*FDS_normalized_2**0 
				+ d21*composition_CO2_normalized_2**2*FDS_normalized_2**1
				+ d12*composition_CO2_normalized_2**1*FDS_normalized_2**2 
				+ d03*composition_CO2_normalized_2**0*FDS_normalized_2**3 
				+ d31*composition_CO2_normalized_2**3*FDS_normalized_2**1 
				+ d22*composition_CO2_normalized_2**2*FDS_normalized_2**2
				+ d13*composition_CO2_normalized_2**1*FDS_normalized_2**3 
				+ d04*composition_CO2_normalized_2**0*FDS_normalized_2**4)

				density3 = (d00*composition_CO2_normalized_1**0*FDS_normalized_2**0 
				+ d10*composition_CO2_normalized_1**1*FDS_normalized_2**0 
				+ d01*composition_CO2_normalized_1**0*FDS_normalized_2**1 
				+ d20*composition_CO2_normalized_1**2*FDS_normalized_2**0
				+ d11*composition_CO2_normalized_1**1*FDS_normalized_2**1 
				+ d02*composition_CO2_normalized_1**0*FDS_normalized_2**2 
				+ d30*composition_CO2_normalized_1**3*FDS_normalized_2**0 
				+ d21*composition_CO2_normalized_1**2*FDS_normalized_2**1
				+ d12*composition_CO2_normalized_1**1*FDS_normalized_2**2 
				+ d03*composition_CO2_normalized_1**0*FDS_normalized_2**3 
				+ d31*composition_CO2_normalized_1**3*FDS_normalized_2**1 
				+ d22*composition_CO2_normalized_1**2*FDS_normalized_2**2
				+ d13*composition_CO2_normalized_1**1*FDS_normalized_2**3 
				+ d04*composition_CO2_normalized_1**0*FDS_normalized_2**4)

				density4 = (d00*composition_CO2_normalized_2**0*FDS_normalized_1**0 
				+ d10*composition_CO2_normalized_2**1*FDS_normalized_1**0 
				+ d01*composition_CO2_normalized_2**0*FDS_normalized_1**1 
				+ d20*composition_CO2_normalized_2**2*FDS_normalized_1**0
				+ d11*composition_CO2_normalized_2**1*FDS_normalized_1**1 
				+ d02*composition_CO2_normalized_2**0*FDS_normalized_1**2 
				+ d30*composition_CO2_normalized_2**3*FDS_normalized_1**0 
				+ d21*composition_CO2_normalized_2**2*FDS_normalized_1**1
				+ d12*composition_CO2_normalized_2**1*FDS_normalized_1**2 
				+ d03*composition_CO2_normalized_2**0*FDS_normalized_1**3 
				+ d31*composition_CO2_normalized_2**3*FDS_normalized_1**1 
				+ d22*composition_CO2_normalized_2**2*FDS_normalized_1**2
				+ d13*composition_CO2_normalized_2**1*FDS_normalized_1**3 
				+ d04*composition_CO2_normalized_2**0*FDS_normalized_1**4)              

				pressure_final = (max(pressure1, pressure2, pressure3, pressure4) + min(pressure1, pressure2, pressure3, pressure4))/2 #pressure max - pressure min
				uncer_pressure_final = 7 + (max(pressure1, pressure2, pressure3, pressure4) - min(pressure1, pressure2, pressure3, pressure4))/(2*np.sqrt(3)) #uncer = 10
 
				density_final = (max(density1, density2, density3, density4) + min(density1, density2, density3, density4))/2 #density max - density min
				uncer_density_final = 0.0049 + (max(density1, density2, density3, density4) - min(density1, density2, density3, density4))/(2*np.sqrt(3)) #uncer = 0.007

				molarvolume1 = 1/(max(density1, density2, density3, density4)/(44*composition_CO2 + 16*composition_CH4))
				molarvolume2 = 1/(min(density1, density2, density3, density4)/(44*composition_CO2 + 16*composition_CH4))
				molarvolume_final = (molarvolume1 + molarvolume2) / 2
				uncer_molarvolume_final = (molarvolume2 - molarvolume1) / (2*np.sqrt(3))


				##### verify if measured pressure < 160 bar, if it is, re-recalculte using calibration data for 5-160 bar range.
				if pressure_final <= 150: 

					## Calibration equation's coeff of CO2-CH4 at 22 °C over 5-160 bars
					# normalisation of concentration and of Fermi diad splitting
					
					composition_CO2_normalized_1 = (composition_CO2 + 0.005 - 0.79945)/0.17644 
					composition_CO2_normalized_2 = (composition_CO2 - 0.005 - 0.79945)/0.17644 
					FDS_normalized_1 = (FDS + unc_FDS - 103.56)/0.70116
					FDS_normalized_2 = (FDS - unc_FDS - 103.56)/0.70116
										
					p00= 87.52544861
					p10= -30.42158037
					p01= 29.11761641
					p20= 10.2290838
					p11= -52.60520058
					p02= -0.386784979
					p30= -2.196596934
					p21= 19.13204933
					p12= -49.83271376
					p03= 48.71006525
					p31= 0.679709634
					p22= 8.522626745
					p13= -27.53323027
					p04= 11.20465971


					d00= 0.317754589
					d10= -0.035146968
					d01= 0.334450048
					d20= -0.002058162
					d11= -0.042889058
					d02= 0.051564624
					d30= -0.004308855
					d21= -0.012647331
					d12= 0.022054788
					d03= -0.015355587
					d31= 0.001474274
					d22= -0.013021138
					d13= 0.023397147
					d04= -0.014013084


					#### pressure calculation
					pressure1 = (p00*composition_CO2_normalized_1**0*FDS_normalized_1**0 
					+ p10*composition_CO2_normalized_1**1*FDS_normalized_1**0 
					+ p01*composition_CO2_normalized_1**0*FDS_normalized_1**1 
					+ p20*composition_CO2_normalized_1**2*FDS_normalized_1**0 
					+ p11*composition_CO2_normalized_1**1*FDS_normalized_1**1 
					+ p02*composition_CO2_normalized_1**0*FDS_normalized_1**2 
					+ p30*composition_CO2_normalized_1**3*FDS_normalized_1**0 
					+ p21*composition_CO2_normalized_1**2*FDS_normalized_1**1
					+ p12*composition_CO2_normalized_1**1*FDS_normalized_1**2 
					+ p03*composition_CO2_normalized_1**0*FDS_normalized_1**3 
					+ p31*composition_CO2_normalized_1**3*FDS_normalized_1**1 
					+ p22*composition_CO2_normalized_1**2*FDS_normalized_1**2
					+ p13*composition_CO2_normalized_1**1*FDS_normalized_1**3 
					+ p04*composition_CO2_normalized_1**0*FDS_normalized_1**4)

					pressure2 = (p00*composition_CO2_normalized_2**0*FDS_normalized_2**0 
					+ p10*composition_CO2_normalized_2**1*FDS_normalized_2**0 
					+ p01*composition_CO2_normalized_2**0*FDS_normalized_2**1 
					+ p20*composition_CO2_normalized_2**2*FDS_normalized_2**0
					+ p11*composition_CO2_normalized_2**1*FDS_normalized_2**1 
					+ p02*composition_CO2_normalized_2**0*FDS_normalized_2**2
					+ p30*composition_CO2_normalized_2**3*FDS_normalized_2**0 
					+ p21*composition_CO2_normalized_2**2*FDS_normalized_2**1
					+ p12*composition_CO2_normalized_2**1*FDS_normalized_2**2 
					+ p03*composition_CO2_normalized_2**0*FDS_normalized_2**3 
					+ p31*composition_CO2_normalized_2**3*FDS_normalized_2**1 
					+ p22*composition_CO2_normalized_2**2*FDS_normalized_2**2
					+ p13*composition_CO2_normalized_2**1*FDS_normalized_2**3 
					+ p04*composition_CO2_normalized_2**0*FDS_normalized_2**4)

					pressure3 = (p00*composition_CO2_normalized_1**0*FDS_normalized_2**0 
					+ p10*composition_CO2_normalized_1**1*FDS_normalized_2**0 
					+ p01*composition_CO2_normalized_1**0*FDS_normalized_2**1 
					+ p20*composition_CO2_normalized_1**2*FDS_normalized_2**0
					+ p11*composition_CO2_normalized_1**1*FDS_normalized_2**1 
					+ p02*composition_CO2_normalized_1**0*FDS_normalized_2**2 
					+ p30*composition_CO2_normalized_1**3*FDS_normalized_2**0 
					+ p21*composition_CO2_normalized_1**2*FDS_normalized_2**1
					+ p12*composition_CO2_normalized_1**1*FDS_normalized_2**2 
					+ p03*composition_CO2_normalized_1**0*FDS_normalized_2**3 
					+ p31*composition_CO2_normalized_1**3*FDS_normalized_2**1 
					+ p22*composition_CO2_normalized_1**2*FDS_normalized_2**2
					+ p13*composition_CO2_normalized_1**1*FDS_normalized_2**3 
					+ p04*composition_CO2_normalized_1**0*FDS_normalized_2**4)

					pressure4 = (p00*composition_CO2_normalized_2**0*FDS_normalized_1**0 
					+ p10*composition_CO2_normalized_2**1*FDS_normalized_1**0 
					+ p01*composition_CO2_normalized_2**0*FDS_normalized_1**1 
					+ p20*composition_CO2_normalized_2**2*FDS_normalized_1**0
					+ p11*composition_CO2_normalized_2**1*FDS_normalized_1**1 
					+ p02*composition_CO2_normalized_2**0*FDS_normalized_1**2 
					+ p30*composition_CO2_normalized_2**3*FDS_normalized_1**0 
					+ p21*composition_CO2_normalized_2**2*FDS_normalized_1**1
					+ p12*composition_CO2_normalized_2**1*FDS_normalized_1**2 
					+ p03*composition_CO2_normalized_2**0*FDS_normalized_1**3 
					+ p31*composition_CO2_normalized_2**3*FDS_normalized_1**1 
					+ p22*composition_CO2_normalized_2**2*FDS_normalized_1**2
					+ p13*composition_CO2_normalized_2**1*FDS_normalized_1**3 
					+ p04*composition_CO2_normalized_2**0*FDS_normalized_1**4)

					########################
					#### density calculation

					density1 = (d00*composition_CO2_normalized_1**0*FDS_normalized_1**0 
					+ d10*composition_CO2_normalized_1**1*FDS_normalized_1**0 
					+ d01*composition_CO2_normalized_1**0*FDS_normalized_1**1 
					+ d20*composition_CO2_normalized_1**2*FDS_normalized_1**0 
					+ d11*composition_CO2_normalized_1**1*FDS_normalized_1**1 
					+ d02*composition_CO2_normalized_1**0*FDS_normalized_1**2 
					+ d30*composition_CO2_normalized_1**3*FDS_normalized_1**0 
					+ d21*composition_CO2_normalized_1**2*FDS_normalized_1**1
					+ d12*composition_CO2_normalized_1**1*FDS_normalized_1**2 
					+ d03*composition_CO2_normalized_1**0*FDS_normalized_1**3 
					+ d31*composition_CO2_normalized_1**3*FDS_normalized_1**1 
					+ d22*composition_CO2_normalized_1**2*FDS_normalized_1**2
					+ d13*composition_CO2_normalized_1**1*FDS_normalized_1**3 
					+ d04*composition_CO2_normalized_1**0*FDS_normalized_1**4)

					density2 = (d00*composition_CO2_normalized_2**0*FDS_normalized_2**0 
					+ d10*composition_CO2_normalized_2**1*FDS_normalized_2**0 
					+ d01*composition_CO2_normalized_2**0*FDS_normalized_2**1 
					+ d20*composition_CO2_normalized_2**2*FDS_normalized_2**0
					+ d11*composition_CO2_normalized_2**1*FDS_normalized_2**1 
					+ d02*composition_CO2_normalized_2**0*FDS_normalized_2**2
					+ d30*composition_CO2_normalized_2**3*FDS_normalized_2**0 
					+ d21*composition_CO2_normalized_2**2*FDS_normalized_2**1
					+ d12*composition_CO2_normalized_2**1*FDS_normalized_2**2 
					+ d03*composition_CO2_normalized_2**0*FDS_normalized_2**3 
					+ d31*composition_CO2_normalized_2**3*FDS_normalized_2**1 
					+ d22*composition_CO2_normalized_2**2*FDS_normalized_2**2
					+ d13*composition_CO2_normalized_2**1*FDS_normalized_2**3 
					+ d04*composition_CO2_normalized_2**0*FDS_normalized_2**4)

					density3 = (d00*composition_CO2_normalized_1**0*FDS_normalized_2**0 
					+ d10*composition_CO2_normalized_1**1*FDS_normalized_2**0 
					+ d01*composition_CO2_normalized_1**0*FDS_normalized_2**1 
					+ d20*composition_CO2_normalized_1**2*FDS_normalized_2**0
					+ d11*composition_CO2_normalized_1**1*FDS_normalized_2**1 
					+ d02*composition_CO2_normalized_1**0*FDS_normalized_2**2 
					+ d30*composition_CO2_normalized_1**3*FDS_normalized_2**0 
					+ d21*composition_CO2_normalized_1**2*FDS_normalized_2**1
					+ d12*composition_CO2_normalized_1**1*FDS_normalized_2**2 
					+ d03*composition_CO2_normalized_1**0*FDS_normalized_2**3 
					+ d31*composition_CO2_normalized_1**3*FDS_normalized_2**1 
					+ d22*composition_CO2_normalized_1**2*FDS_normalized_2**2
					+ d13*composition_CO2_normalized_1**1*FDS_normalized_2**3 
					+ d04*composition_CO2_normalized_1**0*FDS_normalized_2**4)

					density4 = (d00*composition_CO2_normalized_2**0*FDS_normalized_1**0 
					+ d10*composition_CO2_normalized_2**1*FDS_normalized_1**0 
					+ d01*composition_CO2_normalized_2**0*FDS_normalized_1**1 
					+ d20*composition_CO2_normalized_2**2*FDS_normalized_1**0
					+ d11*composition_CO2_normalized_2**1*FDS_normalized_1**1 
					+ d02*composition_CO2_normalized_2**0*FDS_normalized_1**2 
					+ d30*composition_CO2_normalized_2**3*FDS_normalized_1**0 
					+ d21*composition_CO2_normalized_2**2*FDS_normalized_1**1
					+ d12*composition_CO2_normalized_2**1*FDS_normalized_1**2 
					+ d03*composition_CO2_normalized_2**0*FDS_normalized_1**3 
					+ d31*composition_CO2_normalized_2**3*FDS_normalized_1**1 
					+ d22*composition_CO2_normalized_2**2*FDS_normalized_1**2
					+ d13*composition_CO2_normalized_2**1*FDS_normalized_1**3 
					+ d04*composition_CO2_normalized_2**0*FDS_normalized_1**4)              

					pressure_final = (max(pressure1, pressure2, pressure3, pressure4) + min(pressure1, pressure2, pressure3, pressure4))/2 #pressure max - pressure min
					uncer_pressure_final = 2 + (max(pressure1, pressure2, pressure3, pressure4) - min(pressure1, pressure2, pressure3, pressure4))/(2*np.sqrt(3)) #uncer = 3

					density_final = (max(density1, density2, density3, density4) + min(density1, density2, density3, density4))/2 #density max - density min
					uncer_density_final = 0.0028 + (max(density1, density2, density3, density4) - min(density1, density2, density3, density4))/(2*np.sqrt(3)) #uncer = 0.004

					molarvolume1 = 1/(max(density1, density2, density3, density4)/(44*composition_CO2 + 16*composition_CH4))
					molarvolume2 = 1/(min(density1, density2, density3, density4)/(44*composition_CO2 + 16*composition_CH4))
					molarvolume_final = (molarvolume1 + molarvolume2) / 2
					uncer_molarvolume_final = (molarvolume2 - molarvolume1) / (2*np.sqrt(3))

				print('pressure1', pressure1)
				print('pressure2', pressure2)
				print('pressure3', pressure3)
				print('pressure4', pressure4)

				print('density 1=', density1)
				print('density 2=', density2)
				print('density 3=', density3)
				print('density 4=', density4)

				print("molarvolume1", molarvolume1)
				print("molarvolume2", molarvolume2)
					
				if pressure_final > 650 or pressure1 >650 or pressure2 >650 or pressure_final < -20 or pressure1 <-20 or pressure2 <-20 or density2<0 or density1 <0 or density3<0 or density4<0 or density_final <0:
					popupmsg_OCR()
			

			if temperature.get() == 22 and instrument.get() ==1 and composition_CH4 >= 0.5: 

				
				## Calibration equation's coeff of CO2-CH4  at 22°C

				DeltaPCH4= nuCH4_sample - nuCH4_std
				DeltaPCH4_1 = DeltaPCH4 + unc_nuCH4
				DeltaPCH4_2 = DeltaPCH4 - unc_nuCH4
				                         
				
				p00= 84.97786601
				p10= -261.3506486
				p01= 67.17147457
				p20= 253.2786544
				p11= -443.9086584
				p02= 1.267945226
				p30= -55.78796878
				p21= 575.2457778
				p12= 15.72118769
				p03= 5.174034667
				p31= -192.5930176
				p22= 23.58688157
				p13= 6.205093464
				p04= 1.083685883


				d00= 0.016885078
				d10=0.0196323
				d01= -0.06771893
				d20= -0.111247509
				d11= -0.097979464
				d02= 0.002283382
				d30= 0.082873819
				d21= 0.225130412
				d12= -0.008048964
				d03= -0.000697932
				d31= -0.086836744
				d22= 0.009658324
				d13= 0.001283398
				d04= 4.88741E-05


				#### pressure calculation
				pressure1 = (p00*composition_CH4_1**0*DeltaPCH4_1**0 
				+ p10*composition_CH4_1**1*DeltaPCH4_1**0 
				+ p01*composition_CH4_1**0*DeltaPCH4_1**1 
				+ p20*composition_CH4_1**2*DeltaPCH4_1**0 
				+ p11*composition_CH4_1**1*DeltaPCH4_1**1 
				+ p02*composition_CH4_1**0*DeltaPCH4_1**2 
				+ p30*composition_CH4_1**3*DeltaPCH4_1**0 
				+ p21*composition_CH4_1**2*DeltaPCH4_1**1
				+ p12*composition_CH4_1**1*DeltaPCH4_1**2 
				+ p03*composition_CH4_1**0*DeltaPCH4_1**3 
				+ p31*composition_CH4_1**3*DeltaPCH4_1**1 
				+ p22*composition_CH4_1**2*DeltaPCH4_1**2
				+ p13*composition_CH4_1**1*DeltaPCH4_1**3 
				+ p04*composition_CH4_1**0*DeltaPCH4_1**4)

				pressure2 = (p00*composition_CH4_2**0*DeltaPCH4_2**0 
				+ p10*composition_CH4_2**1*DeltaPCH4_2**0 
				+ p01*composition_CH4_2**0*DeltaPCH4_2**1 
				+ p20*composition_CH4_2**2*DeltaPCH4_2**0
				+ p11*composition_CH4_2**1*DeltaPCH4_2**1 
				+ p02*composition_CH4_2**0*DeltaPCH4_2**2 
				+ p30*composition_CH4_2**3*DeltaPCH4_2**0 
				+ p21*composition_CH4_2**2*DeltaPCH4_2**1
				+ p12*composition_CH4_2**1*DeltaPCH4_2**2 
				+ p03*composition_CH4_2**0*DeltaPCH4_2**3 
				+ p31*composition_CH4_2**3*DeltaPCH4_2**1 
				+ p22*composition_CH4_2**2*DeltaPCH4_2**2
				+ p13*composition_CH4_2**1*DeltaPCH4_2**3 
				+ p04*composition_CH4_2**0*DeltaPCH4_2**4)

				pressure3 = (p00*composition_CH4_1**0*DeltaPCH4_2**0 
				+ p10*composition_CH4_1**1*DeltaPCH4_2**0 
				+ p01*composition_CH4_1**0*DeltaPCH4_2**1 
				+ p20*composition_CH4_1**2*DeltaPCH4_2**0
				+ p11*composition_CH4_1**1*DeltaPCH4_2**1 
				+ p02*composition_CH4_1**0*DeltaPCH4_2**2 
				+ p30*composition_CH4_1**3*DeltaPCH4_2**0 
				+ p21*composition_CH4_1**2*DeltaPCH4_2**1
				+ p12*composition_CH4_1**1*DeltaPCH4_2**2 
				+ p03*composition_CH4_1**0*DeltaPCH4_2**3 
				+ p31*composition_CH4_1**3*DeltaPCH4_2**1 
				+ p22*composition_CH4_1**2*DeltaPCH4_2**2
				+ p13*composition_CH4_1**1*DeltaPCH4_2**3 
				+ p04*composition_CH4_1**0*DeltaPCH4_2**4)

				pressure4 = (p00*composition_CH4_2**0*DeltaPCH4_1**0 
				+ p10*composition_CH4_2**1*DeltaPCH4_1**0 
				+ p01*composition_CH4_2**0*DeltaPCH4_1**1 
				+ p20*composition_CH4_2**2*DeltaPCH4_1**0
				+ p11*composition_CH4_2**1*DeltaPCH4_1**1 
				+ p02*composition_CH4_2**0*DeltaPCH4_1**2 
				+ p30*composition_CH4_2**3*DeltaPCH4_1**0 
				+ p21*composition_CH4_2**2*DeltaPCH4_1**1
				+ p12*composition_CH4_2**1*DeltaPCH4_1**2 
				+ p03*composition_CH4_2**0*DeltaPCH4_1**3 
				+ p31*composition_CH4_2**3*DeltaPCH4_1**1 
				+ p22*composition_CH4_2**2*DeltaPCH4_1**2
				+ p13*composition_CH4_2**1*DeltaPCH4_1**3 
				+ p04*composition_CH4_2**0*DeltaPCH4_1**4)

				########################
				#### density calculation

				density1 = (d00*composition_CH4_1**0*DeltaPCH4_1**0 
				+ d10*composition_CH4_1**1*DeltaPCH4_1**0 
				+ d01*composition_CH4_1**0*DeltaPCH4_1**1 
				+ d20*composition_CH4_1**2*DeltaPCH4_1**0 
				+ d11*composition_CH4_1**1*DeltaPCH4_1**1 
				+ d02*composition_CH4_1**0*DeltaPCH4_1**2 
				+ d30*composition_CH4_1**3*DeltaPCH4_1**0 
				+ d21*composition_CH4_1**2*DeltaPCH4_1**1
				+ d12*composition_CH4_1**1*DeltaPCH4_1**2 
				+ d03*composition_CH4_1**0*DeltaPCH4_1**3 
				+ d31*composition_CH4_1**3*DeltaPCH4_1**1 
				+ d22*composition_CH4_1**2*DeltaPCH4_1**2
				+ d13*composition_CH4_1**1*DeltaPCH4_1**3 
				+ d04*composition_CH4_1**0*DeltaPCH4_1**4)

				density2 = (d00*composition_CH4_2**0*DeltaPCH4_2**0 
				+ d10*composition_CH4_2**1*DeltaPCH4_2**0 
				+ d01*composition_CH4_2**0*DeltaPCH4_2**1 
				+ d20*composition_CH4_2**2*DeltaPCH4_2**0
				+ d11*composition_CH4_2**1*DeltaPCH4_2**1 
				+ d02*composition_CH4_2**0*DeltaPCH4_2**2 
				+ d30*composition_CH4_2**3*DeltaPCH4_2**0 
				+ d21*composition_CH4_2**2*DeltaPCH4_2**1
				+ d12*composition_CH4_2**1*DeltaPCH4_2**2 
				+ d03*composition_CH4_2**0*DeltaPCH4_2**3 
				+ d31*composition_CH4_2**3*DeltaPCH4_2**1 
				+ d22*composition_CH4_2**2*DeltaPCH4_2**2
				+ d13*composition_CH4_2**1*DeltaPCH4_2**3 
				+ d04*composition_CH4_2**0*DeltaPCH4_2**4)


				density3 = (d00*composition_CH4_1**0*DeltaPCH4_2**0 
				+ d10*composition_CH4_1**1*DeltaPCH4_2**0 
				+ d01*composition_CH4_1**0*DeltaPCH4_2**1 
				+ d20*composition_CH4_1**2*DeltaPCH4_2**0
				+ d11*composition_CH4_1**1*DeltaPCH4_2**1 
				+ d02*composition_CH4_1**0*DeltaPCH4_2**2 
				+ d30*composition_CH4_1**3*DeltaPCH4_2**0 
				+ d21*composition_CH4_1**2*DeltaPCH4_2**1
				+ d12*composition_CH4_1**1*DeltaPCH4_2**2 
				+ d03*composition_CH4_1**0*DeltaPCH4_2**3 
				+ d31*composition_CH4_1**3*DeltaPCH4_2**1 
				+ d22*composition_CH4_1**2*DeltaPCH4_2**2
				+ d13*composition_CH4_1**1*DeltaPCH4_2**3 
				+ d04*composition_CH4_1**0*DeltaPCH4_2**4)

				density4 = (d00*composition_CH4_2**0*DeltaPCH4_1**0 
				+ d10*composition_CH4_2**1*DeltaPCH4_1**0 
				+ d01*composition_CH4_2**0*DeltaPCH4_1**1 
				+ d20*composition_CH4_2**2*DeltaPCH4_1**0
				+ d11*composition_CH4_2**1*DeltaPCH4_1**1 
				+ d02*composition_CH4_2**0*DeltaPCH4_1**2 
				+ d30*composition_CH4_2**3*DeltaPCH4_1**0 
				+ d21*composition_CH4_2**2*DeltaPCH4_1**1
				+ d12*composition_CH4_2**1*DeltaPCH4_1**2 
				+ d03*composition_CH4_2**0*DeltaPCH4_1**3 
				+ d31*composition_CH4_2**3*DeltaPCH4_1**1 
				+ d22*composition_CH4_2**2*DeltaPCH4_1**2
				+ d13*composition_CH4_2**1*DeltaPCH4_1**3 
				+ d04*composition_CH4_2**0*DeltaPCH4_1**4)              

				pressure_final = (max(pressure1, pressure2, pressure3, pressure4) + min(pressure1, pressure2, pressure3, pressure4))/2
				uncer_pressure_final = 10.6 + (max(pressure1, pressure2, pressure3, pressure4) - min(pressure1, pressure2, pressure3, pressure4))/(2*np.sqrt(3)) #uncer 15

				density_final = (max(density1, density2, density3, density4) + min(density1, density2, density3, density4))/2
				uncer_density_final = 0.0042 + (max(density1, density2, density3, density4) - min(density1, density2, density3, density4))/(2*np.sqrt(3)) #uncer 0.006

				molarvolume1 = 1/(max(density1, density2, density3, density4)/(44*composition_CO2 + 16*composition_CH4))
				molarvolume2 = 1/(min(density1, density2, density3, density4)/(44*composition_CO2 + 16*composition_CH4))
				molarvolume_final = (molarvolume1 + molarvolume2) / 2
				uncer_molarvolume_final = (molarvolume2 - molarvolume1) / (2*np.sqrt(3))

				print('pressure1', pressure1)
				print('pressure2', pressure2)
				print('pressure3', pressure3)
				print('pressure4', pressure4)

				print('density 1=', density1)
				print('density 2=', density2)
				print('density 3=', density3)
				print('density 4=', density4)

				print("molarvolume1", molarvolume1)
				print("molarvolume2", molarvolume2)
				

				if pressure_final > 650 or pressure1 >650 or pressure2 >650 or pressure_final < -20 or pressure1 <-20 or pressure2 <-20 or density2<0 or density1 <0 or density3<0 or density4<0 or density_final <0:
					popupmsg_OCR()

			
			########################################################
			#### Caculation at temperature = 32 °C
			########################################################

			if temperature.get() == 32 and instrument.get() ==1 and composition_CO2 > 0.5: 

				## Calibration equation's coeff of CO2-CH4 at 32 °C over 5-500 bars

				# normalisation of concentration and of Fermi diad splitting ( 5-600 bars)
				composition_CO2_normalized_1 = (composition_CO2 + 0.005 - 0.82613)/0.1781
				composition_CO2_normalized_2 = (composition_CO2 - 0.005 - 0.82613)/0.1781
				FDS_normalized_1 = (FDS + unc_FDS - 103.86)/0.74857
				FDS_normalized_2 = (FDS - unc_FDS - 103.86)/0.74857
				
				p00= 117.4815787
				p10= -64.00435313
				p01= 75.90202201
				p20= 33.79624017
				p11= -153.2075523
				p02= 110.198304
				p30= -17.72552705
				p21= 81.79481677
				p12= -148.3062869
				p03= 93.93866464
				p31= -13.57700611
				p22= 43.93126678
				p13= -49.6426556
				p04= 10.75316406

				d00= 0.486313356
				d10= -0.041249121
				d01= 0.369020167
				d20= -0.001314366
				d11= -0.003487682
				d02= -0.009959664
				d30= -0.000231208
				d21= -0.013539233
				d12= 0.03746847
				d03= -0.03096695
				d31= 0.001645248
				d22= -0.01024711
				d13= 0.012428938
				d04= -0.002157202


				#### pressure calculation
				pressure1 = (p00*composition_CO2_normalized_1**0*FDS_normalized_1**0 
				+ p10*composition_CO2_normalized_1**1*FDS_normalized_1**0 
				+ p01*composition_CO2_normalized_1**0*FDS_normalized_1**1 
				+ p20*composition_CO2_normalized_1**2*FDS_normalized_1**0 
				+ p11*composition_CO2_normalized_1**1*FDS_normalized_1**1 
				+ p02*composition_CO2_normalized_1**0*FDS_normalized_1**2 
				+ p30*composition_CO2_normalized_1**3*FDS_normalized_1**0 
				+ p21*composition_CO2_normalized_1**2*FDS_normalized_1**1
				+ p12*composition_CO2_normalized_1**1*FDS_normalized_1**2 
				+ p03*composition_CO2_normalized_1**0*FDS_normalized_1**3 
				+ p31*composition_CO2_normalized_1**3*FDS_normalized_1**1 
				+ p22*composition_CO2_normalized_1**2*FDS_normalized_1**2
				+ p13*composition_CO2_normalized_1**1*FDS_normalized_1**3 
				+ p04*composition_CO2_normalized_1**0*FDS_normalized_1**4)

				pressure2 = (p00*composition_CO2_normalized_2**0*FDS_normalized_2**0 
				+ p10*composition_CO2_normalized_2**1*FDS_normalized_2**0 
				+ p01*composition_CO2_normalized_2**0*FDS_normalized_2**1 
				+ p20*composition_CO2_normalized_2**2*FDS_normalized_2**0
				+ p11*composition_CO2_normalized_2**1*FDS_normalized_2**1 
				+ p02*composition_CO2_normalized_2**0*FDS_normalized_2**2
				+ p30*composition_CO2_normalized_2**3*FDS_normalized_2**0 
				+ p21*composition_CO2_normalized_2**2*FDS_normalized_2**1
				+ p12*composition_CO2_normalized_2**1*FDS_normalized_2**2 
				+ p03*composition_CO2_normalized_2**0*FDS_normalized_2**3 
				+ p31*composition_CO2_normalized_2**3*FDS_normalized_2**1 
				+ p22*composition_CO2_normalized_2**2*FDS_normalized_2**2
				+ p13*composition_CO2_normalized_2**1*FDS_normalized_2**3 
				+ p04*composition_CO2_normalized_2**0*FDS_normalized_2**4)

				pressure3 = (p00*composition_CO2_normalized_1**0*FDS_normalized_2**0 
				+ p10*composition_CO2_normalized_1**1*FDS_normalized_2**0 
				+ p01*composition_CO2_normalized_1**0*FDS_normalized_2**1 
				+ p20*composition_CO2_normalized_1**2*FDS_normalized_2**0
				+ p11*composition_CO2_normalized_1**1*FDS_normalized_2**1 
				+ p02*composition_CO2_normalized_1**0*FDS_normalized_2**2 
				+ p30*composition_CO2_normalized_1**3*FDS_normalized_2**0 
				+ p21*composition_CO2_normalized_1**2*FDS_normalized_2**1
				+ p12*composition_CO2_normalized_1**1*FDS_normalized_2**2 
				+ p03*composition_CO2_normalized_1**0*FDS_normalized_2**3 
				+ p31*composition_CO2_normalized_1**3*FDS_normalized_2**1 
				+ p22*composition_CO2_normalized_1**2*FDS_normalized_2**2
				+ p13*composition_CO2_normalized_1**1*FDS_normalized_2**3 
				+ p04*composition_CO2_normalized_1**0*FDS_normalized_2**4)

				pressure4 = (p00*composition_CO2_normalized_2**0*FDS_normalized_1**0 
				+ p10*composition_CO2_normalized_2**1*FDS_normalized_1**0 
				+ p01*composition_CO2_normalized_2**0*FDS_normalized_1**1 
				+ p20*composition_CO2_normalized_2**2*FDS_normalized_1**0
				+ p11*composition_CO2_normalized_2**1*FDS_normalized_1**1 
				+ p02*composition_CO2_normalized_2**0*FDS_normalized_1**2 
				+ p30*composition_CO2_normalized_2**3*FDS_normalized_1**0 
				+ p21*composition_CO2_normalized_2**2*FDS_normalized_1**1
				+ p12*composition_CO2_normalized_2**1*FDS_normalized_1**2 
				+ p03*composition_CO2_normalized_2**0*FDS_normalized_1**3 
				+ p31*composition_CO2_normalized_2**3*FDS_normalized_1**1 
				+ p22*composition_CO2_normalized_2**2*FDS_normalized_1**2
				+ p13*composition_CO2_normalized_2**1*FDS_normalized_1**3 
				+ p04*composition_CO2_normalized_2**0*FDS_normalized_1**4)

				########################
				#### density calculation

				density1 = (d00*composition_CO2_normalized_1**0*FDS_normalized_1**0 
				+ d10*composition_CO2_normalized_1**1*FDS_normalized_1**0 
				+ d01*composition_CO2_normalized_1**0*FDS_normalized_1**1 
				+ d20*composition_CO2_normalized_1**2*FDS_normalized_1**0 
				+ d11*composition_CO2_normalized_1**1*FDS_normalized_1**1 
				+ d02*composition_CO2_normalized_1**0*FDS_normalized_1**2 
				+ d30*composition_CO2_normalized_1**3*FDS_normalized_1**0 
				+ d21*composition_CO2_normalized_1**2*FDS_normalized_1**1
				+ d12*composition_CO2_normalized_1**1*FDS_normalized_1**2 
				+ d03*composition_CO2_normalized_1**0*FDS_normalized_1**3 
				+ d31*composition_CO2_normalized_1**3*FDS_normalized_1**1 
				+ d22*composition_CO2_normalized_1**2*FDS_normalized_1**2
				+ d13*composition_CO2_normalized_1**1*FDS_normalized_1**3 
				+ d04*composition_CO2_normalized_1**0*FDS_normalized_1**4)

				density2 = (d00*composition_CO2_normalized_2**0*FDS_normalized_2**0 
				+ d10*composition_CO2_normalized_2**1*FDS_normalized_2**0 
				+ d01*composition_CO2_normalized_2**0*FDS_normalized_2**1 
				+ d20*composition_CO2_normalized_2**2*FDS_normalized_2**0
				+ d11*composition_CO2_normalized_2**1*FDS_normalized_2**1 
				+ d02*composition_CO2_normalized_2**0*FDS_normalized_2**2
				+ d30*composition_CO2_normalized_2**3*FDS_normalized_2**0 
				+ d21*composition_CO2_normalized_2**2*FDS_normalized_2**1
				+ d12*composition_CO2_normalized_2**1*FDS_normalized_2**2 
				+ d03*composition_CO2_normalized_2**0*FDS_normalized_2**3 
				+ d31*composition_CO2_normalized_2**3*FDS_normalized_2**1 
				+ d22*composition_CO2_normalized_2**2*FDS_normalized_2**2
				+ d13*composition_CO2_normalized_2**1*FDS_normalized_2**3 
				+ d04*composition_CO2_normalized_2**0*FDS_normalized_2**4)

				density3 = (d00*composition_CO2_normalized_1**0*FDS_normalized_2**0 
				+ d10*composition_CO2_normalized_1**1*FDS_normalized_2**0 
				+ d01*composition_CO2_normalized_1**0*FDS_normalized_2**1 
				+ d20*composition_CO2_normalized_1**2*FDS_normalized_2**0
				+ d11*composition_CO2_normalized_1**1*FDS_normalized_2**1 
				+ d02*composition_CO2_normalized_1**0*FDS_normalized_2**2 
				+ d30*composition_CO2_normalized_1**3*FDS_normalized_2**0 
				+ d21*composition_CO2_normalized_1**2*FDS_normalized_2**1
				+ d12*composition_CO2_normalized_1**1*FDS_normalized_2**2 
				+ d03*composition_CO2_normalized_1**0*FDS_normalized_2**3 
				+ d31*composition_CO2_normalized_1**3*FDS_normalized_2**1 
				+ d22*composition_CO2_normalized_1**2*FDS_normalized_2**2
				+ d13*composition_CO2_normalized_1**1*FDS_normalized_2**3 
				+ d04*composition_CO2_normalized_1**0*FDS_normalized_2**4)

				density4 = (d00*composition_CO2_normalized_2**0*FDS_normalized_1**0 
				+ d10*composition_CO2_normalized_2**1*FDS_normalized_1**0 
				+ d01*composition_CO2_normalized_2**0*FDS_normalized_1**1 
				+ d20*composition_CO2_normalized_2**2*FDS_normalized_1**0
				+ d11*composition_CO2_normalized_2**1*FDS_normalized_1**1 
				+ d02*composition_CO2_normalized_2**0*FDS_normalized_1**2 
				+ d30*composition_CO2_normalized_2**3*FDS_normalized_1**0 
				+ d21*composition_CO2_normalized_2**2*FDS_normalized_1**1
				+ d12*composition_CO2_normalized_2**1*FDS_normalized_1**2 
				+ d03*composition_CO2_normalized_2**0*FDS_normalized_1**3 
				+ d31*composition_CO2_normalized_2**3*FDS_normalized_1**1 
				+ d22*composition_CO2_normalized_2**2*FDS_normalized_1**2
				+ d13*composition_CO2_normalized_2**1*FDS_normalized_1**3 
				+ d04*composition_CO2_normalized_2**0*FDS_normalized_1**4)              

				pressure_final = (max(pressure1, pressure2, pressure3, pressure4) + min(pressure1, pressure2, pressure3, pressure4))/2 #pressure max - pressure min
				uncer_pressure_final = 7+ (max(pressure1, pressure2, pressure3, pressure4) - min(pressure1, pressure2, pressure3, pressure4))/(2*np.sqrt(3)) #10 bar

				density_final = (max(density1, density2, density3, density4) + min(density1, density2, density3, density4))/2 #density max - density min
				uncer_density_final = 5.7 + (max(density1, density2, density3, density4) - min(density1, density2, density3, density4))/(2*np.sqrt(3)) # 0.008

				molarvolume1 = 1/(max(density1, density2, density3, density4)/(44*composition_CO2 + 16*composition_CH4))
				molarvolume2 = 1/(min(density1, density2, density3, density4)/(44*composition_CO2 + 16*composition_CH4))
				molarvolume_final = (molarvolume1 + molarvolume2) / 2
				uncer_molarvolume_final = (molarvolume2 - molarvolume1) / (2*np.sqrt(3))

				##### verify if measured pressure < 160 bar, if it is, re-recalculte using calibration data for 5-160 bar range.
				if pressure_final <= 150: 

					## Calibration equation's coeff of CO2-CH4 at 32 °C over 5-160 bars
					# normalisation of concentration and of Fermi diad splitting
					
					composition_CO2_normalized_1 = (composition_CO2 + 0.005 - 0.83997)/0.17804 
					composition_CO2_normalized_2 = (composition_CO2 - 0.005 - 0.83997)/0.17804 
					FDS_normalized_1 = (FDS + unc_FDS - 103.53)/0.63658
					FDS_normalized_2 = (FDS - unc_FDS - 103.53)/0.63658
										
					p00= 94.65622893
					p10= -29.90432239
					p01= 31.9463506
					p20= 11.05019058
					p11= -41.39264514
					p02= -5.575568606
					p30= -2.412150018
					p21= 21.26972394
					p12= -39.40094963
					p03= 33.51376232
					p31= -1.313217682
					p22= 10.23037585
					p13= -22.26971706
					p04= 7.070998459

					d00= 0.318294844
					d10= -0.033717464
					d01= 0.295140901
					d20= 0.003835289
					d11= -0.034525497
					d02= 0.03615103
					d30= -0.001593066
					d21= 0.004028655
					d12= 0.006008238
					d03= -0.005570953
					d31= 0.000483165
					d22= -0.000890907
					d13= 0.008033639
					d04= -0.008589286



					#### pressure calculation
					pressure1 = (p00*composition_CO2_normalized_1**0*FDS_normalized_1**0 
					+ p10*composition_CO2_normalized_1**1*FDS_normalized_1**0 
					+ p01*composition_CO2_normalized_1**0*FDS_normalized_1**1 
					+ p20*composition_CO2_normalized_1**2*FDS_normalized_1**0 
					+ p11*composition_CO2_normalized_1**1*FDS_normalized_1**1 
					+ p02*composition_CO2_normalized_1**0*FDS_normalized_1**2 
					+ p30*composition_CO2_normalized_1**3*FDS_normalized_1**0 
					+ p21*composition_CO2_normalized_1**2*FDS_normalized_1**1
					+ p12*composition_CO2_normalized_1**1*FDS_normalized_1**2 
					+ p03*composition_CO2_normalized_1**0*FDS_normalized_1**3 
					+ p31*composition_CO2_normalized_1**3*FDS_normalized_1**1 
					+ p22*composition_CO2_normalized_1**2*FDS_normalized_1**2
					+ p13*composition_CO2_normalized_1**1*FDS_normalized_1**3 
					+ p04*composition_CO2_normalized_1**0*FDS_normalized_1**4)

					pressure2 = (p00*composition_CO2_normalized_2**0*FDS_normalized_2**0 
					+ p10*composition_CO2_normalized_2**1*FDS_normalized_2**0 
					+ p01*composition_CO2_normalized_2**0*FDS_normalized_2**1 
					+ p20*composition_CO2_normalized_2**2*FDS_normalized_2**0
					+ p11*composition_CO2_normalized_2**1*FDS_normalized_2**1 
					+ p02*composition_CO2_normalized_2**0*FDS_normalized_2**2
					+ p30*composition_CO2_normalized_2**3*FDS_normalized_2**0 
					+ p21*composition_CO2_normalized_2**2*FDS_normalized_2**1
					+ p12*composition_CO2_normalized_2**1*FDS_normalized_2**2 
					+ p03*composition_CO2_normalized_2**0*FDS_normalized_2**3 
					+ p31*composition_CO2_normalized_2**3*FDS_normalized_2**1 
					+ p22*composition_CO2_normalized_2**2*FDS_normalized_2**2
					+ p13*composition_CO2_normalized_2**1*FDS_normalized_2**3 
					+ p04*composition_CO2_normalized_2**0*FDS_normalized_2**4)

					pressure3 = (p00*composition_CO2_normalized_1**0*FDS_normalized_2**0 
					+ p10*composition_CO2_normalized_1**1*FDS_normalized_2**0 
					+ p01*composition_CO2_normalized_1**0*FDS_normalized_2**1 
					+ p20*composition_CO2_normalized_1**2*FDS_normalized_2**0
					+ p11*composition_CO2_normalized_1**1*FDS_normalized_2**1 
					+ p02*composition_CO2_normalized_1**0*FDS_normalized_2**2 
					+ p30*composition_CO2_normalized_1**3*FDS_normalized_2**0 
					+ p21*composition_CO2_normalized_1**2*FDS_normalized_2**1
					+ p12*composition_CO2_normalized_1**1*FDS_normalized_2**2 
					+ p03*composition_CO2_normalized_1**0*FDS_normalized_2**3 
					+ p31*composition_CO2_normalized_1**3*FDS_normalized_2**1 
					+ p22*composition_CO2_normalized_1**2*FDS_normalized_2**2
					+ p13*composition_CO2_normalized_1**1*FDS_normalized_2**3 
					+ p04*composition_CO2_normalized_1**0*FDS_normalized_2**4)

					pressure4 = (p00*composition_CO2_normalized_2**0*FDS_normalized_1**0 
					+ p10*composition_CO2_normalized_2**1*FDS_normalized_1**0 
					+ p01*composition_CO2_normalized_2**0*FDS_normalized_1**1 
					+ p20*composition_CO2_normalized_2**2*FDS_normalized_1**0
					+ p11*composition_CO2_normalized_2**1*FDS_normalized_1**1 
					+ p02*composition_CO2_normalized_2**0*FDS_normalized_1**2 
					+ p30*composition_CO2_normalized_2**3*FDS_normalized_1**0 
					+ p21*composition_CO2_normalized_2**2*FDS_normalized_1**1
					+ p12*composition_CO2_normalized_2**1*FDS_normalized_1**2 
					+ p03*composition_CO2_normalized_2**0*FDS_normalized_1**3 
					+ p31*composition_CO2_normalized_2**3*FDS_normalized_1**1 
					+ p22*composition_CO2_normalized_2**2*FDS_normalized_1**2
					+ p13*composition_CO2_normalized_2**1*FDS_normalized_1**3 
					+ p04*composition_CO2_normalized_2**0*FDS_normalized_1**4)

					########################
					#### density calculation

					density1 = (d00*composition_CO2_normalized_1**0*FDS_normalized_1**0 
					+ d10*composition_CO2_normalized_1**1*FDS_normalized_1**0 
					+ d01*composition_CO2_normalized_1**0*FDS_normalized_1**1 
					+ d20*composition_CO2_normalized_1**2*FDS_normalized_1**0 
					+ d11*composition_CO2_normalized_1**1*FDS_normalized_1**1 
					+ d02*composition_CO2_normalized_1**0*FDS_normalized_1**2 
					+ d30*composition_CO2_normalized_1**3*FDS_normalized_1**0 
					+ d21*composition_CO2_normalized_1**2*FDS_normalized_1**1
					+ d12*composition_CO2_normalized_1**1*FDS_normalized_1**2 
					+ d03*composition_CO2_normalized_1**0*FDS_normalized_1**3 
					+ d31*composition_CO2_normalized_1**3*FDS_normalized_1**1 
					+ d22*composition_CO2_normalized_1**2*FDS_normalized_1**2
					+ d13*composition_CO2_normalized_1**1*FDS_normalized_1**3 
					+ d04*composition_CO2_normalized_1**0*FDS_normalized_1**4)

					density2 = (d00*composition_CO2_normalized_2**0*FDS_normalized_2**0 
					+ d10*composition_CO2_normalized_2**1*FDS_normalized_2**0 
					+ d01*composition_CO2_normalized_2**0*FDS_normalized_2**1 
					+ d20*composition_CO2_normalized_2**2*FDS_normalized_2**0
					+ d11*composition_CO2_normalized_2**1*FDS_normalized_2**1 
					+ d02*composition_CO2_normalized_2**0*FDS_normalized_2**2
					+ d30*composition_CO2_normalized_2**3*FDS_normalized_2**0 
					+ d21*composition_CO2_normalized_2**2*FDS_normalized_2**1
					+ d12*composition_CO2_normalized_2**1*FDS_normalized_2**2 
					+ d03*composition_CO2_normalized_2**0*FDS_normalized_2**3 
					+ d31*composition_CO2_normalized_2**3*FDS_normalized_2**1 
					+ d22*composition_CO2_normalized_2**2*FDS_normalized_2**2
					+ d13*composition_CO2_normalized_2**1*FDS_normalized_2**3 
					+ d04*composition_CO2_normalized_2**0*FDS_normalized_2**4)

					density3 = (d00*composition_CO2_normalized_1**0*FDS_normalized_2**0 
					+ d10*composition_CO2_normalized_1**1*FDS_normalized_2**0 
					+ d01*composition_CO2_normalized_1**0*FDS_normalized_2**1 
					+ d20*composition_CO2_normalized_1**2*FDS_normalized_2**0
					+ d11*composition_CO2_normalized_1**1*FDS_normalized_2**1 
					+ d02*composition_CO2_normalized_1**0*FDS_normalized_2**2 
					+ d30*composition_CO2_normalized_1**3*FDS_normalized_2**0 
					+ d21*composition_CO2_normalized_1**2*FDS_normalized_2**1
					+ d12*composition_CO2_normalized_1**1*FDS_normalized_2**2 
					+ d03*composition_CO2_normalized_1**0*FDS_normalized_2**3 
					+ d31*composition_CO2_normalized_1**3*FDS_normalized_2**1 
					+ d22*composition_CO2_normalized_1**2*FDS_normalized_2**2
					+ d13*composition_CO2_normalized_1**1*FDS_normalized_2**3 
					+ d04*composition_CO2_normalized_1**0*FDS_normalized_2**4)

					density4 = (d00*composition_CO2_normalized_2**0*FDS_normalized_1**0 
					+ d10*composition_CO2_normalized_2**1*FDS_normalized_1**0 
					+ d01*composition_CO2_normalized_2**0*FDS_normalized_1**1 
					+ d20*composition_CO2_normalized_2**2*FDS_normalized_1**0
					+ d11*composition_CO2_normalized_2**1*FDS_normalized_1**1 
					+ d02*composition_CO2_normalized_2**0*FDS_normalized_1**2 
					+ d30*composition_CO2_normalized_2**3*FDS_normalized_1**0 
					+ d21*composition_CO2_normalized_2**2*FDS_normalized_1**1
					+ d12*composition_CO2_normalized_2**1*FDS_normalized_1**2 
					+ d03*composition_CO2_normalized_2**0*FDS_normalized_1**3 
					+ d31*composition_CO2_normalized_2**3*FDS_normalized_1**1 
					+ d22*composition_CO2_normalized_2**2*FDS_normalized_1**2
					+ d13*composition_CO2_normalized_2**1*FDS_normalized_1**3 
					+ d04*composition_CO2_normalized_2**0*FDS_normalized_1**4)              

					pressure_final = (max(pressure1, pressure2, pressure3, pressure4) + min(pressure1, pressure2, pressure3, pressure4))/2 #pressure max - pressure min
					uncer_pressure_final = 4.5 + (max(pressure1, pressure2, pressure3, pressure4) - min(pressure1, pressure2, pressure3, pressure4))/(2*np.sqrt(3)) #uncer = 6

					density_final = (max(density1, density2, density3, density4) + min(density1, density2, density3, density4))/2 #density max - density min
					uncer_density_final = 0.0057 + (max(density1, density2, density3, density4) - min(density1, density2, density3, density4))/(2*np.sqrt(3)) #uncer = 0.008

					molarvolume1 = 1/(max(density1, density2, density3, density4)/(44*composition_CO2 + 16*composition_CH4))
					molarvolume2 = 1/(min(density1, density2, density3, density4)/(44*composition_CO2 + 16*composition_CH4))
					molarvolume_final = (molarvolume1 + molarvolume2) / 2
					uncer_molarvolume_final = (molarvolume2 - molarvolume1) / (2*np.sqrt(3))

				print('pressure1', pressure1)
				print('pressure2', pressure2)
				print('pressure3', pressure3)
				print('pressure4', pressure4)

				print('density 1=', density1)
				print('density 2=', density2)
				print('density 3=', density3)
				print('density 4=', density4)

				print("molarvolume1", molarvolume1)
				print("molarvolume2", molarvolume2)
				
				if pressure_final > 650 or pressure1 >650 or pressure2 >650 or pressure_final < -20 or pressure1 <-20 or pressure2 <-20 or density2<0 or density1 <0 or density3<0 or density4<0 or density_final <0 :
					popupmsg_OCR()
					

			if temperature.get() == 32 and instrument.get() ==1 and composition_CH4 >= 0.5: 

				
				## Calibration equation's coeff of CO2CH4 at 32 °C

				DeltaPCH4= nuCH4_sample - nuCH4_std
				DeltaPCH4_1 = DeltaPCH4 + unc_nuCH4
				DeltaPCH4_2 = DeltaPCH4 - unc_nuCH4
				                         
				
				p00= 16.99348609
				p10= -75.74655975
				p01= -35.5907442
				p20= 139.4767471
				p11= -150.7113177
				p02= -20.60862944
				p30= -63.0556863
				p21= 359.9252978
				p12= 83.88300229
				p03= 6.207870544
				p31= -175.5603532
				p22= -20.17126712
				p13= 6.957810313
				p04= 1.313724336

				d00= -0.003751017
				d10=0.079358301
				d01= -0.060703048
				d20= -0.155452793
				d11= -0.106032328
				d02= 0.0036172
				d30= 0.087333073
				d21= 0.217043194
				d12= -0.005840984
				d03= -0.00024797
				d31= -0.079155646
				d22= 0.006827228
				d13= 0.001283486
				d04= 0.000100213



				#### pressure calculation
				pressure1 = (p00*composition_CH4_1**0*DeltaPCH4_1**0 
				+ p10*composition_CH4_1**1*DeltaPCH4_1**0 
				+ p01*composition_CH4_1**0*DeltaPCH4_1**1 
				+ p20*composition_CH4_1**2*DeltaPCH4_1**0 
				+ p11*composition_CH4_1**1*DeltaPCH4_1**1 
				+ p02*composition_CH4_1**0*DeltaPCH4_1**2 
				+ p30*composition_CH4_1**3*DeltaPCH4_1**0 
				+ p21*composition_CH4_1**2*DeltaPCH4_1**1
				+ p12*composition_CH4_1**1*DeltaPCH4_1**2 
				+ p03*composition_CH4_1**0*DeltaPCH4_1**3 
				+ p31*composition_CH4_1**3*DeltaPCH4_1**1 
				+ p22*composition_CH4_1**2*DeltaPCH4_1**2
				+ p13*composition_CH4_1**1*DeltaPCH4_1**3 
				+ p04*composition_CH4_1**0*DeltaPCH4_1**4)

				pressure2 = (p00*composition_CH4_2**0*DeltaPCH4_2**0 
				+ p10*composition_CH4_2**1*DeltaPCH4_2**0 
				+ p01*composition_CH4_2**0*DeltaPCH4_2**1 
				+ p20*composition_CH4_2**2*DeltaPCH4_2**0
				+ p11*composition_CH4_2**1*DeltaPCH4_2**1 
				+ p02*composition_CH4_2**0*DeltaPCH4_2**2 
				+ p30*composition_CH4_2**3*DeltaPCH4_2**0 
				+ p21*composition_CH4_2**2*DeltaPCH4_2**1
				+ p12*composition_CH4_2**1*DeltaPCH4_2**2 
				+ p03*composition_CH4_2**0*DeltaPCH4_2**3 
				+ p31*composition_CH4_2**3*DeltaPCH4_2**1 
				+ p22*composition_CH4_2**2*DeltaPCH4_2**2
				+ p13*composition_CH4_2**1*DeltaPCH4_2**3 
				+ p04*composition_CH4_2**0*DeltaPCH4_2**4)

				pressure3 = (p00*composition_CH4_1**0*DeltaPCH4_2**0 
				+ p10*composition_CH4_1**1*DeltaPCH4_2**0 
				+ p01*composition_CH4_1**0*DeltaPCH4_2**1 
				+ p20*composition_CH4_1**2*DeltaPCH4_2**0
				+ p11*composition_CH4_1**1*DeltaPCH4_2**1 
				+ p02*composition_CH4_1**0*DeltaPCH4_2**2 
				+ p30*composition_CH4_1**3*DeltaPCH4_2**0 
				+ p21*composition_CH4_1**2*DeltaPCH4_2**1
				+ p12*composition_CH4_1**1*DeltaPCH4_2**2 
				+ p03*composition_CH4_1**0*DeltaPCH4_2**3 
				+ p31*composition_CH4_1**3*DeltaPCH4_2**1 
				+ p22*composition_CH4_1**2*DeltaPCH4_2**2
				+ p13*composition_CH4_1**1*DeltaPCH4_2**3 
				+ p04*composition_CH4_1**0*DeltaPCH4_2**4)

				pressure4 = (p00*composition_CH4_2**0*DeltaPCH4_1**0 
				+ p10*composition_CH4_2**1*DeltaPCH4_1**0 
				+ p01*composition_CH4_2**0*DeltaPCH4_1**1 
				+ p20*composition_CH4_2**2*DeltaPCH4_1**0
				+ p11*composition_CH4_2**1*DeltaPCH4_1**1 
				+ p02*composition_CH4_2**0*DeltaPCH4_1**2 
				+ p30*composition_CH4_2**3*DeltaPCH4_1**0 
				+ p21*composition_CH4_2**2*DeltaPCH4_1**1
				+ p12*composition_CH4_2**1*DeltaPCH4_1**2 
				+ p03*composition_CH4_2**0*DeltaPCH4_1**3 
				+ p31*composition_CH4_2**3*DeltaPCH4_1**1 
				+ p22*composition_CH4_2**2*DeltaPCH4_1**2
				+ p13*composition_CH4_2**1*DeltaPCH4_1**3 
				+ p04*composition_CH4_2**0*DeltaPCH4_1**4)

				########################
				#### density calculation

				density1 = (d00*composition_CH4_1**0*DeltaPCH4_1**0 
				+ d10*composition_CH4_1**1*DeltaPCH4_1**0 
				+ d01*composition_CH4_1**0*DeltaPCH4_1**1 
				+ d20*composition_CH4_1**2*DeltaPCH4_1**0 
				+ d11*composition_CH4_1**1*DeltaPCH4_1**1 
				+ d02*composition_CH4_1**0*DeltaPCH4_1**2 
				+ d30*composition_CH4_1**3*DeltaPCH4_1**0 
				+ d21*composition_CH4_1**2*DeltaPCH4_1**1
				+ d12*composition_CH4_1**1*DeltaPCH4_1**2 
				+ d03*composition_CH4_1**0*DeltaPCH4_1**3 
				+ d31*composition_CH4_1**3*DeltaPCH4_1**1 
				+ d22*composition_CH4_1**2*DeltaPCH4_1**2
				+ d13*composition_CH4_1**1*DeltaPCH4_1**3 
				+ d04*composition_CH4_1**0*DeltaPCH4_1**4)

				density2 = (d00*composition_CH4_2**0*DeltaPCH4_2**0 
				+ d10*composition_CH4_2**1*DeltaPCH4_2**0 
				+ d01*composition_CH4_2**0*DeltaPCH4_2**1 
				+ d20*composition_CH4_2**2*DeltaPCH4_2**0
				+ d11*composition_CH4_2**1*DeltaPCH4_2**1 
				+ d02*composition_CH4_2**0*DeltaPCH4_2**2 
				+ d30*composition_CH4_2**3*DeltaPCH4_2**0 
				+ d21*composition_CH4_2**2*DeltaPCH4_2**1
				+ d12*composition_CH4_2**1*DeltaPCH4_2**2 
				+ d03*composition_CH4_2**0*DeltaPCH4_2**3 
				+ d31*composition_CH4_2**3*DeltaPCH4_2**1 
				+ d22*composition_CH4_2**2*DeltaPCH4_2**2
				+ d13*composition_CH4_2**1*DeltaPCH4_2**3 
				+ d04*composition_CH4_2**0*DeltaPCH4_2**4)


				density3 = (d00*composition_CH4_1**0*DeltaPCH4_2**0 
				+ d10*composition_CH4_1**1*DeltaPCH4_2**0 
				+ d01*composition_CH4_1**0*DeltaPCH4_2**1 
				+ d20*composition_CH4_1**2*DeltaPCH4_2**0
				+ d11*composition_CH4_1**1*DeltaPCH4_2**1 
				+ d02*composition_CH4_1**0*DeltaPCH4_2**2 
				+ d30*composition_CH4_1**3*DeltaPCH4_2**0 
				+ d21*composition_CH4_1**2*DeltaPCH4_2**1
				+ d12*composition_CH4_1**1*DeltaPCH4_2**2 
				+ d03*composition_CH4_1**0*DeltaPCH4_2**3 
				+ d31*composition_CH4_1**3*DeltaPCH4_2**1 
				+ d22*composition_CH4_1**2*DeltaPCH4_2**2
				+ d13*composition_CH4_1**1*DeltaPCH4_2**3 
				+ d04*composition_CH4_1**0*DeltaPCH4_2**4)

				density4 = (d00*composition_CH4_2**0*DeltaPCH4_1**0 
				+ d10*composition_CH4_2**1*DeltaPCH4_1**0 
				+ d01*composition_CH4_2**0*DeltaPCH4_1**1 
				+ d20*composition_CH4_2**2*DeltaPCH4_1**0
				+ d11*composition_CH4_2**1*DeltaPCH4_1**1 
				+ d02*composition_CH4_2**0*DeltaPCH4_1**2 
				+ d30*composition_CH4_2**3*DeltaPCH4_1**0 
				+ d21*composition_CH4_2**2*DeltaPCH4_1**1
				+ d12*composition_CH4_2**1*DeltaPCH4_1**2 
				+ d03*composition_CH4_2**0*DeltaPCH4_1**3 
				+ d31*composition_CH4_2**3*DeltaPCH4_1**1 
				+ d22*composition_CH4_2**2*DeltaPCH4_1**2
				+ d13*composition_CH4_2**1*DeltaPCH4_1**3 
				+ d04*composition_CH4_2**0*DeltaPCH4_1**4)              

				pressure_final = (max(pressure1, pressure2, pressure3, pressure4) + min(pressure1, pressure2, pressure3, pressure4))/2
				uncer_pressure_final = 10.6 + (max(pressure1, pressure2, pressure3, pressure4) - min(pressure1, pressure2, pressure3, pressure4))/(2*np.sqrt(3)) #uncer = 15

				density_final = (max(density1, density2, density3, density4) + min(density1, density2, density3, density4))/2
				uncer_density_final = 0.0035 + (max(density1, density2, density3, density4) - min(density1, density2, density3, density4))/(2*np.sqrt(3)) #uncer = 0.005

				molarvolume1 = 1/(max(density1, density2, density3, density4)/(44*composition_CO2 + 16*composition_CH4))
				molarvolume2 = 1/(min(density1, density2, density3, density4)/(44*composition_CO2 + 16*composition_CH4))
				molarvolume_final = (molarvolume1 + molarvolume2) / 2
				uncer_molarvolume_final = (molarvolume2 - molarvolume1) / (2*np.sqrt(3))

				print('pressure1', pressure1)
				print('pressure2', pressure2)
				print('pressure3', pressure3)
				print('pressure4', pressure4)

				print('density 1=', density1)
				print('density 2=', density2)
				print('density 3=', density3)
				print('density 4=', density4)

				print("molarvolume1", molarvolume1)
				print("molarvolume2", molarvolume2)
				

				if pressure_final > 650 or pressure1 >650 or pressure2 >650 or pressure_final < -20 or pressure1 <-20 or pressure2 <-20 or density2<0 or density1 <0 or density3<0 or density4<0 or density_final <0:
					popupmsg_OCR()

			######################################
			######################################
			######## OTHER SPECTROMETERS #########
			######################################
			######################################

			if temperature.get() == 22 and instrument.get() ==2 and composition_CO2 > 0.5: 

				## Calibration equation's coeff of CO2-CH4 at 22 °C over 5-600 bars

				# normalisation of concentration and of Fermi diad splitting ( 5-600 bars)
				composition_CO2_normalized_1 = (composition_CO2 + 0.005)
				composition_CO2_normalized_2 = (composition_CO2 - 0.005)
				FDS_normalized_1 = (FDS + unc_FDS - FDS_std)
				FDS_normalized_2 = (FDS - unc_FDS - FDS_std)
				
				p00= 178.11013617
				p10= -493.2755025
				p01= 174.12480428
				p20= 320.2918820
				p11= -580.958211704
				p02= 773.4627272
				p30= -1.111459845
				p21= 2655.984859119
				p12= -3584.04088023
				p03= 654.8292295398
				p31= -2100.46205349
				p22= 2686.20216700
				p13= -669.269282122
				p04= 26.174155877

				d00= -0.0951436086
				d10= 0.3881001782
				d01= 0.6273183336
				d20= -0.479419383
				d11= -0.314992616
				d02= -0.0198455367
				d30= 0.1896014963
				d21= -0.723496554
				d12= 0.8733004743
				d03= -0.216237326
				d31= 0.683057337
				d22= -0.744116947
				d13= 0.216532295
				d04= -0.009033426

				#### pressure calculation
				pressure1 = (p00*composition_CO2_normalized_1**0*FDS_normalized_1**0 
				+ p10*composition_CO2_normalized_1**1*FDS_normalized_1**0 
				+ p01*composition_CO2_normalized_1**0*FDS_normalized_1**1 
				+ p20*composition_CO2_normalized_1**2*FDS_normalized_1**0 
				+ p11*composition_CO2_normalized_1**1*FDS_normalized_1**1 
				+ p02*composition_CO2_normalized_1**0*FDS_normalized_1**2 
				+ p30*composition_CO2_normalized_1**3*FDS_normalized_1**0 
				+ p21*composition_CO2_normalized_1**2*FDS_normalized_1**1
				+ p12*composition_CO2_normalized_1**1*FDS_normalized_1**2 
				+ p03*composition_CO2_normalized_1**0*FDS_normalized_1**3 
				+ p31*composition_CO2_normalized_1**3*FDS_normalized_1**1 
				+ p22*composition_CO2_normalized_1**2*FDS_normalized_1**2
				+ p13*composition_CO2_normalized_1**1*FDS_normalized_1**3 
				+ p04*composition_CO2_normalized_1**0*FDS_normalized_1**4)

				pressure2 = (p00*composition_CO2_normalized_2**0*FDS_normalized_2**0 
				+ p10*composition_CO2_normalized_2**1*FDS_normalized_2**0 
				+ p01*composition_CO2_normalized_2**0*FDS_normalized_2**1 
				+ p20*composition_CO2_normalized_2**2*FDS_normalized_2**0
				+ p11*composition_CO2_normalized_2**1*FDS_normalized_2**1 
				+ p02*composition_CO2_normalized_2**0*FDS_normalized_2**2
				+ p30*composition_CO2_normalized_2**3*FDS_normalized_2**0 
				+ p21*composition_CO2_normalized_2**2*FDS_normalized_2**1
				+ p12*composition_CO2_normalized_2**1*FDS_normalized_2**2 
				+ p03*composition_CO2_normalized_2**0*FDS_normalized_2**3 
				+ p31*composition_CO2_normalized_2**3*FDS_normalized_2**1 
				+ p22*composition_CO2_normalized_2**2*FDS_normalized_2**2
				+ p13*composition_CO2_normalized_2**1*FDS_normalized_2**3 
				+ p04*composition_CO2_normalized_2**0*FDS_normalized_2**4)

				pressure3 = (p00*composition_CO2_normalized_1**0*FDS_normalized_2**0 
				+ p10*composition_CO2_normalized_1**1*FDS_normalized_2**0 
				+ p01*composition_CO2_normalized_1**0*FDS_normalized_2**1 
				+ p20*composition_CO2_normalized_1**2*FDS_normalized_2**0
				+ p11*composition_CO2_normalized_1**1*FDS_normalized_2**1 
				+ p02*composition_CO2_normalized_1**0*FDS_normalized_2**2 
				+ p30*composition_CO2_normalized_1**3*FDS_normalized_2**0 
				+ p21*composition_CO2_normalized_1**2*FDS_normalized_2**1
				+ p12*composition_CO2_normalized_1**1*FDS_normalized_2**2 
				+ p03*composition_CO2_normalized_1**0*FDS_normalized_2**3 
				+ p31*composition_CO2_normalized_1**3*FDS_normalized_2**1 
				+ p22*composition_CO2_normalized_1**2*FDS_normalized_2**2
				+ p13*composition_CO2_normalized_1**1*FDS_normalized_2**3 
				+ p04*composition_CO2_normalized_1**0*FDS_normalized_2**4)

				pressure4 = (p00*composition_CO2_normalized_2**0*FDS_normalized_1**0 
				+ p10*composition_CO2_normalized_2**1*FDS_normalized_1**0 
				+ p01*composition_CO2_normalized_2**0*FDS_normalized_1**1 
				+ p20*composition_CO2_normalized_2**2*FDS_normalized_1**0
				+ p11*composition_CO2_normalized_2**1*FDS_normalized_1**1 
				+ p02*composition_CO2_normalized_2**0*FDS_normalized_1**2 
				+ p30*composition_CO2_normalized_2**3*FDS_normalized_1**0 
				+ p21*composition_CO2_normalized_2**2*FDS_normalized_1**1
				+ p12*composition_CO2_normalized_2**1*FDS_normalized_1**2 
				+ p03*composition_CO2_normalized_2**0*FDS_normalized_1**3 
				+ p31*composition_CO2_normalized_2**3*FDS_normalized_1**1 
				+ p22*composition_CO2_normalized_2**2*FDS_normalized_1**2
				+ p13*composition_CO2_normalized_2**1*FDS_normalized_1**3 
				+ p04*composition_CO2_normalized_2**0*FDS_normalized_1**4)

				########################
				#### density calculation

				density1 = (d00*composition_CO2_normalized_1**0*FDS_normalized_1**0 
				+ d10*composition_CO2_normalized_1**1*FDS_normalized_1**0 
				+ d01*composition_CO2_normalized_1**0*FDS_normalized_1**1 
				+ d20*composition_CO2_normalized_1**2*FDS_normalized_1**0 
				+ d11*composition_CO2_normalized_1**1*FDS_normalized_1**1 
				+ d02*composition_CO2_normalized_1**0*FDS_normalized_1**2 
				+ d30*composition_CO2_normalized_1**3*FDS_normalized_1**0 
				+ d21*composition_CO2_normalized_1**2*FDS_normalized_1**1
				+ d12*composition_CO2_normalized_1**1*FDS_normalized_1**2 
				+ d03*composition_CO2_normalized_1**0*FDS_normalized_1**3 
				+ d31*composition_CO2_normalized_1**3*FDS_normalized_1**1 
				+ d22*composition_CO2_normalized_1**2*FDS_normalized_1**2
				+ d13*composition_CO2_normalized_1**1*FDS_normalized_1**3 
				+ d04*composition_CO2_normalized_1**0*FDS_normalized_1**4)

				density2 = (d00*composition_CO2_normalized_2**0*FDS_normalized_2**0 
				+ d10*composition_CO2_normalized_2**1*FDS_normalized_2**0 
				+ d01*composition_CO2_normalized_2**0*FDS_normalized_2**1 
				+ d20*composition_CO2_normalized_2**2*FDS_normalized_2**0
				+ d11*composition_CO2_normalized_2**1*FDS_normalized_2**1 
				+ d02*composition_CO2_normalized_2**0*FDS_normalized_2**2
				+ d30*composition_CO2_normalized_2**3*FDS_normalized_2**0 
				+ d21*composition_CO2_normalized_2**2*FDS_normalized_2**1
				+ d12*composition_CO2_normalized_2**1*FDS_normalized_2**2 
				+ d03*composition_CO2_normalized_2**0*FDS_normalized_2**3 
				+ d31*composition_CO2_normalized_2**3*FDS_normalized_2**1 
				+ d22*composition_CO2_normalized_2**2*FDS_normalized_2**2
				+ d13*composition_CO2_normalized_2**1*FDS_normalized_2**3 
				+ d04*composition_CO2_normalized_2**0*FDS_normalized_2**4)

				density3 = (d00*composition_CO2_normalized_1**0*FDS_normalized_2**0 
				+ d10*composition_CO2_normalized_1**1*FDS_normalized_2**0 
				+ d01*composition_CO2_normalized_1**0*FDS_normalized_2**1 
				+ d20*composition_CO2_normalized_1**2*FDS_normalized_2**0
				+ d11*composition_CO2_normalized_1**1*FDS_normalized_2**1 
				+ d02*composition_CO2_normalized_1**0*FDS_normalized_2**2 
				+ d30*composition_CO2_normalized_1**3*FDS_normalized_2**0 
				+ d21*composition_CO2_normalized_1**2*FDS_normalized_2**1
				+ d12*composition_CO2_normalized_1**1*FDS_normalized_2**2 
				+ d03*composition_CO2_normalized_1**0*FDS_normalized_2**3 
				+ d31*composition_CO2_normalized_1**3*FDS_normalized_2**1 
				+ d22*composition_CO2_normalized_1**2*FDS_normalized_2**2
				+ d13*composition_CO2_normalized_1**1*FDS_normalized_2**3 
				+ d04*composition_CO2_normalized_1**0*FDS_normalized_2**4)

				density4 = (d00*composition_CO2_normalized_2**0*FDS_normalized_1**0 
				+ d10*composition_CO2_normalized_2**1*FDS_normalized_1**0 
				+ d01*composition_CO2_normalized_2**0*FDS_normalized_1**1 
				+ d20*composition_CO2_normalized_2**2*FDS_normalized_1**0
				+ d11*composition_CO2_normalized_2**1*FDS_normalized_1**1 
				+ d02*composition_CO2_normalized_2**0*FDS_normalized_1**2 
				+ d30*composition_CO2_normalized_2**3*FDS_normalized_1**0 
				+ d21*composition_CO2_normalized_2**2*FDS_normalized_1**1
				+ d12*composition_CO2_normalized_2**1*FDS_normalized_1**2 
				+ d03*composition_CO2_normalized_2**0*FDS_normalized_1**3 
				+ d31*composition_CO2_normalized_2**3*FDS_normalized_1**1 
				+ d22*composition_CO2_normalized_2**2*FDS_normalized_1**2
				+ d13*composition_CO2_normalized_2**1*FDS_normalized_1**3 
				+ d04*composition_CO2_normalized_2**0*FDS_normalized_1**4)              

				pressure_final = (max(pressure1, pressure2, pressure3, pressure4) + min(pressure1, pressure2, pressure3, pressure4))/2 #pressure max - pressure min
				uncer_pressure_final = 7 + (max(pressure1, pressure2, pressure3, pressure4) - min(pressure1, pressure2, pressure3, pressure4))/(2*np.sqrt(3)) #uncer = 10
 
				density_final = (max(density1, density2, density3, density4) + min(density1, density2, density3, density4))/2 #density max - density min
				uncer_density_final = 0.0049 + (max(density1, density2, density3, density4) - min(density1, density2, density3, density4))/(2*np.sqrt(3)) #uncer = 0.007

				molarvolume1 = 1/(max(density1, density2, density3, density4)/(44*composition_CO2 + 16*composition_CH4))
				molarvolume2 = 1/(min(density1, density2, density3, density4)/(44*composition_CO2 + 16*composition_CH4))
				molarvolume_final = (molarvolume1 + molarvolume2) / 2
				uncer_molarvolume_final = (molarvolume2 - molarvolume1) / (2*np.sqrt(3))


				##### verify if measured pressure < 160 bar, if it is, re-recalculte using calibration data for 5-160 bar range.
				if pressure_final <= 150: 

					## Calibration equation's coeff of CO2-CH4 at 22 °C over 5-160 bars
					# normalisation of concentration and of Fermi diad splitting
					
					composition_CO2_normalized_1 = (composition_CO2 + 0.005)
					composition_CO2_normalized_2 = (composition_CO2 - 0.005)
					FDS_normalized_1 = (FDS + unc_FDS - FDS_std)
					FDS_normalized_2 = (FDS - unc_FDS - FDS_std)
										
					p00= 63.13772807
					p10= -229.8319644
					p01= 409.52379008
					p20= 268.95019030
					p11= -52.8224412
					p02= -154.153885
					p30= -101.4629657
					p21= -352.8545608
					p12= -417.6419021
					p03= 307.9361869
					p31= 147.0647037
					p22= 525.59937161
					p13= -400.5748251
					p04= 45.43448100


					d00= 0.042390997
					d10= -0.1635244356
					d01= 0.311038521
					d20= 0.2208505802
					d11= 0.8140677223
					d02= 0.04134989132
					d30= -0.1051469947
					d21= -1.8438145767
					d12= 0.6096230857
					d03= -0.1993785126
					d31= 1.1150645004
					d22= -0.894715470
					d13= 0.4675024479
					d04= -0.069459902


					#### pressure calculation
					pressure1 = (p00*composition_CO2_normalized_1**0*FDS_normalized_1**0 
					+ p10*composition_CO2_normalized_1**1*FDS_normalized_1**0 
					+ p01*composition_CO2_normalized_1**0*FDS_normalized_1**1 
					+ p20*composition_CO2_normalized_1**2*FDS_normalized_1**0 
					+ p11*composition_CO2_normalized_1**1*FDS_normalized_1**1 
					+ p02*composition_CO2_normalized_1**0*FDS_normalized_1**2 
					+ p30*composition_CO2_normalized_1**3*FDS_normalized_1**0 
					+ p21*composition_CO2_normalized_1**2*FDS_normalized_1**1
					+ p12*composition_CO2_normalized_1**1*FDS_normalized_1**2 
					+ p03*composition_CO2_normalized_1**0*FDS_normalized_1**3 
					+ p31*composition_CO2_normalized_1**3*FDS_normalized_1**1 
					+ p22*composition_CO2_normalized_1**2*FDS_normalized_1**2
					+ p13*composition_CO2_normalized_1**1*FDS_normalized_1**3 
					+ p04*composition_CO2_normalized_1**0*FDS_normalized_1**4)

					pressure2 = (p00*composition_CO2_normalized_2**0*FDS_normalized_2**0 
					+ p10*composition_CO2_normalized_2**1*FDS_normalized_2**0 
					+ p01*composition_CO2_normalized_2**0*FDS_normalized_2**1 
					+ p20*composition_CO2_normalized_2**2*FDS_normalized_2**0
					+ p11*composition_CO2_normalized_2**1*FDS_normalized_2**1 
					+ p02*composition_CO2_normalized_2**0*FDS_normalized_2**2
					+ p30*composition_CO2_normalized_2**3*FDS_normalized_2**0 
					+ p21*composition_CO2_normalized_2**2*FDS_normalized_2**1
					+ p12*composition_CO2_normalized_2**1*FDS_normalized_2**2 
					+ p03*composition_CO2_normalized_2**0*FDS_normalized_2**3 
					+ p31*composition_CO2_normalized_2**3*FDS_normalized_2**1 
					+ p22*composition_CO2_normalized_2**2*FDS_normalized_2**2
					+ p13*composition_CO2_normalized_2**1*FDS_normalized_2**3 
					+ p04*composition_CO2_normalized_2**0*FDS_normalized_2**4)

					pressure3 = (p00*composition_CO2_normalized_1**0*FDS_normalized_2**0 
					+ p10*composition_CO2_normalized_1**1*FDS_normalized_2**0 
					+ p01*composition_CO2_normalized_1**0*FDS_normalized_2**1 
					+ p20*composition_CO2_normalized_1**2*FDS_normalized_2**0
					+ p11*composition_CO2_normalized_1**1*FDS_normalized_2**1 
					+ p02*composition_CO2_normalized_1**0*FDS_normalized_2**2 
					+ p30*composition_CO2_normalized_1**3*FDS_normalized_2**0 
					+ p21*composition_CO2_normalized_1**2*FDS_normalized_2**1
					+ p12*composition_CO2_normalized_1**1*FDS_normalized_2**2 
					+ p03*composition_CO2_normalized_1**0*FDS_normalized_2**3 
					+ p31*composition_CO2_normalized_1**3*FDS_normalized_2**1 
					+ p22*composition_CO2_normalized_1**2*FDS_normalized_2**2
					+ p13*composition_CO2_normalized_1**1*FDS_normalized_2**3 
					+ p04*composition_CO2_normalized_1**0*FDS_normalized_2**4)

					pressure4 = (p00*composition_CO2_normalized_2**0*FDS_normalized_1**0 
					+ p10*composition_CO2_normalized_2**1*FDS_normalized_1**0 
					+ p01*composition_CO2_normalized_2**0*FDS_normalized_1**1 
					+ p20*composition_CO2_normalized_2**2*FDS_normalized_1**0
					+ p11*composition_CO2_normalized_2**1*FDS_normalized_1**1 
					+ p02*composition_CO2_normalized_2**0*FDS_normalized_1**2 
					+ p30*composition_CO2_normalized_2**3*FDS_normalized_1**0 
					+ p21*composition_CO2_normalized_2**2*FDS_normalized_1**1
					+ p12*composition_CO2_normalized_2**1*FDS_normalized_1**2 
					+ p03*composition_CO2_normalized_2**0*FDS_normalized_1**3 
					+ p31*composition_CO2_normalized_2**3*FDS_normalized_1**1 
					+ p22*composition_CO2_normalized_2**2*FDS_normalized_1**2
					+ p13*composition_CO2_normalized_2**1*FDS_normalized_1**3 
					+ p04*composition_CO2_normalized_2**0*FDS_normalized_1**4)

					########################
					#### density calculation

					density1 = (d00*composition_CO2_normalized_1**0*FDS_normalized_1**0 
					+ d10*composition_CO2_normalized_1**1*FDS_normalized_1**0 
					+ d01*composition_CO2_normalized_1**0*FDS_normalized_1**1 
					+ d20*composition_CO2_normalized_1**2*FDS_normalized_1**0 
					+ d11*composition_CO2_normalized_1**1*FDS_normalized_1**1 
					+ d02*composition_CO2_normalized_1**0*FDS_normalized_1**2 
					+ d30*composition_CO2_normalized_1**3*FDS_normalized_1**0 
					+ d21*composition_CO2_normalized_1**2*FDS_normalized_1**1
					+ d12*composition_CO2_normalized_1**1*FDS_normalized_1**2 
					+ d03*composition_CO2_normalized_1**0*FDS_normalized_1**3 
					+ d31*composition_CO2_normalized_1**3*FDS_normalized_1**1 
					+ d22*composition_CO2_normalized_1**2*FDS_normalized_1**2
					+ d13*composition_CO2_normalized_1**1*FDS_normalized_1**3 
					+ d04*composition_CO2_normalized_1**0*FDS_normalized_1**4)

					density2 = (d00*composition_CO2_normalized_2**0*FDS_normalized_2**0 
					+ d10*composition_CO2_normalized_2**1*FDS_normalized_2**0 
					+ d01*composition_CO2_normalized_2**0*FDS_normalized_2**1 
					+ d20*composition_CO2_normalized_2**2*FDS_normalized_2**0
					+ d11*composition_CO2_normalized_2**1*FDS_normalized_2**1 
					+ d02*composition_CO2_normalized_2**0*FDS_normalized_2**2
					+ d30*composition_CO2_normalized_2**3*FDS_normalized_2**0 
					+ d21*composition_CO2_normalized_2**2*FDS_normalized_2**1
					+ d12*composition_CO2_normalized_2**1*FDS_normalized_2**2 
					+ d03*composition_CO2_normalized_2**0*FDS_normalized_2**3 
					+ d31*composition_CO2_normalized_2**3*FDS_normalized_2**1 
					+ d22*composition_CO2_normalized_2**2*FDS_normalized_2**2
					+ d13*composition_CO2_normalized_2**1*FDS_normalized_2**3 
					+ d04*composition_CO2_normalized_2**0*FDS_normalized_2**4)

					density3 = (d00*composition_CO2_normalized_1**0*FDS_normalized_2**0 
					+ d10*composition_CO2_normalized_1**1*FDS_normalized_2**0 
					+ d01*composition_CO2_normalized_1**0*FDS_normalized_2**1 
					+ d20*composition_CO2_normalized_1**2*FDS_normalized_2**0
					+ d11*composition_CO2_normalized_1**1*FDS_normalized_2**1 
					+ d02*composition_CO2_normalized_1**0*FDS_normalized_2**2 
					+ d30*composition_CO2_normalized_1**3*FDS_normalized_2**0 
					+ d21*composition_CO2_normalized_1**2*FDS_normalized_2**1
					+ d12*composition_CO2_normalized_1**1*FDS_normalized_2**2 
					+ d03*composition_CO2_normalized_1**0*FDS_normalized_2**3 
					+ d31*composition_CO2_normalized_1**3*FDS_normalized_2**1 
					+ d22*composition_CO2_normalized_1**2*FDS_normalized_2**2
					+ d13*composition_CO2_normalized_1**1*FDS_normalized_2**3 
					+ d04*composition_CO2_normalized_1**0*FDS_normalized_2**4)

					density4 = (d00*composition_CO2_normalized_2**0*FDS_normalized_1**0 
					+ d10*composition_CO2_normalized_2**1*FDS_normalized_1**0 
					+ d01*composition_CO2_normalized_2**0*FDS_normalized_1**1 
					+ d20*composition_CO2_normalized_2**2*FDS_normalized_1**0
					+ d11*composition_CO2_normalized_2**1*FDS_normalized_1**1 
					+ d02*composition_CO2_normalized_2**0*FDS_normalized_1**2 
					+ d30*composition_CO2_normalized_2**3*FDS_normalized_1**0 
					+ d21*composition_CO2_normalized_2**2*FDS_normalized_1**1
					+ d12*composition_CO2_normalized_2**1*FDS_normalized_1**2 
					+ d03*composition_CO2_normalized_2**0*FDS_normalized_1**3 
					+ d31*composition_CO2_normalized_2**3*FDS_normalized_1**1 
					+ d22*composition_CO2_normalized_2**2*FDS_normalized_1**2
					+ d13*composition_CO2_normalized_2**1*FDS_normalized_1**3 
					+ d04*composition_CO2_normalized_2**0*FDS_normalized_1**4)              

					pressure_final = (max(pressure1, pressure2, pressure3, pressure4) + min(pressure1, pressure2, pressure3, pressure4))/2 #pressure max - pressure min
					uncer_pressure_final = 2 + (max(pressure1, pressure2, pressure3, pressure4) - min(pressure1, pressure2, pressure3, pressure4))/(2*np.sqrt(3)) #uncer = 3

					density_final = (max(density1, density2, density3, density4) + min(density1, density2, density3, density4))/2 #density max - density min
					uncer_density_final = 0.0028 + (max(density1, density2, density3, density4) - min(density1, density2, density3, density4))/(2*np.sqrt(3)) #uncer = 0.004

					molarvolume1 = 1/(max(density1, density2, density3, density4)/(44*composition_CO2 + 16*composition_CH4))
					molarvolume2 = 1/(min(density1, density2, density3, density4)/(44*composition_CO2 + 16*composition_CH4))
					molarvolume_final = (molarvolume1 + molarvolume2) / 2
					uncer_molarvolume_final = (molarvolume2 - molarvolume1) / (2*np.sqrt(3))

				print('pressure1', pressure1)
				print('pressure2', pressure2)
				print('pressure3', pressure3)
				print('pressure4', pressure4)

				print('density 1=', density1)
				print('density 2=', density2)
				print('density 3=', density3)
				print('density 4=', density4)

				print("molarvolume1", molarvolume1)
				print("molarvolume2", molarvolume2)
					
				if pressure_final > 650 or pressure1 >650 or pressure2 >650 or pressure_final < -20 or pressure1 <-20 or pressure2 <-20 or density2<0 or density1 <0 or density3<0 or density4<0 or density_final <0:
					popupmsg_OCR()
			

			if temperature.get() == 22 and instrument.get() ==2 and composition_CH4 >= 0.5: 

				
				## Calibration equation's coeff of CO2-CH4  at 22°C

				DeltaPCH4= nuCH4_sample - nuCH4_std
				DeltaPCH4_1 = DeltaPCH4 + unc_nuCH4
				DeltaPCH4_2 = DeltaPCH4 - unc_nuCH4
				                         
				
				p00= 84.97786601
				p10= -261.3506486
				p01= 67.17147457
				p20= 253.2786544
				p11= -443.9086584
				p02= 1.267945226
				p30= -55.78796878
				p21= 575.2457778
				p12= 15.72118769
				p03= 5.174034667
				p31= -192.5930176
				p22= 23.58688157
				p13= 6.205093464
				p04= 1.083685883


				d00= 0.016885078
				d10=0.0196323
				d01= -0.06771893
				d20= -0.111247509
				d11= -0.097979464
				d02= 0.002283382
				d30= 0.082873819
				d21= 0.225130412
				d12= -0.008048964
				d03= -0.000697932
				d31= -0.086836744
				d22= 0.009658324
				d13= 0.001283398
				d04= 4.88741E-05


				#### pressure calculation
				pressure1 = (p00*composition_CH4_1**0*DeltaPCH4_1**0 
				+ p10*composition_CH4_1**1*DeltaPCH4_1**0 
				+ p01*composition_CH4_1**0*DeltaPCH4_1**1 
				+ p20*composition_CH4_1**2*DeltaPCH4_1**0 
				+ p11*composition_CH4_1**1*DeltaPCH4_1**1 
				+ p02*composition_CH4_1**0*DeltaPCH4_1**2 
				+ p30*composition_CH4_1**3*DeltaPCH4_1**0 
				+ p21*composition_CH4_1**2*DeltaPCH4_1**1
				+ p12*composition_CH4_1**1*DeltaPCH4_1**2 
				+ p03*composition_CH4_1**0*DeltaPCH4_1**3 
				+ p31*composition_CH4_1**3*DeltaPCH4_1**1 
				+ p22*composition_CH4_1**2*DeltaPCH4_1**2
				+ p13*composition_CH4_1**1*DeltaPCH4_1**3 
				+ p04*composition_CH4_1**0*DeltaPCH4_1**4)

				pressure2 = (p00*composition_CH4_2**0*DeltaPCH4_2**0 
				+ p10*composition_CH4_2**1*DeltaPCH4_2**0 
				+ p01*composition_CH4_2**0*DeltaPCH4_2**1 
				+ p20*composition_CH4_2**2*DeltaPCH4_2**0
				+ p11*composition_CH4_2**1*DeltaPCH4_2**1 
				+ p02*composition_CH4_2**0*DeltaPCH4_2**2 
				+ p30*composition_CH4_2**3*DeltaPCH4_2**0 
				+ p21*composition_CH4_2**2*DeltaPCH4_2**1
				+ p12*composition_CH4_2**1*DeltaPCH4_2**2 
				+ p03*composition_CH4_2**0*DeltaPCH4_2**3 
				+ p31*composition_CH4_2**3*DeltaPCH4_2**1 
				+ p22*composition_CH4_2**2*DeltaPCH4_2**2
				+ p13*composition_CH4_2**1*DeltaPCH4_2**3 
				+ p04*composition_CH4_2**0*DeltaPCH4_2**4)

				pressure3 = (p00*composition_CH4_1**0*DeltaPCH4_2**0 
				+ p10*composition_CH4_1**1*DeltaPCH4_2**0 
				+ p01*composition_CH4_1**0*DeltaPCH4_2**1 
				+ p20*composition_CH4_1**2*DeltaPCH4_2**0
				+ p11*composition_CH4_1**1*DeltaPCH4_2**1 
				+ p02*composition_CH4_1**0*DeltaPCH4_2**2 
				+ p30*composition_CH4_1**3*DeltaPCH4_2**0 
				+ p21*composition_CH4_1**2*DeltaPCH4_2**1
				+ p12*composition_CH4_1**1*DeltaPCH4_2**2 
				+ p03*composition_CH4_1**0*DeltaPCH4_2**3 
				+ p31*composition_CH4_1**3*DeltaPCH4_2**1 
				+ p22*composition_CH4_1**2*DeltaPCH4_2**2
				+ p13*composition_CH4_1**1*DeltaPCH4_2**3 
				+ p04*composition_CH4_1**0*DeltaPCH4_2**4)

				pressure4 = (p00*composition_CH4_2**0*DeltaPCH4_1**0 
				+ p10*composition_CH4_2**1*DeltaPCH4_1**0 
				+ p01*composition_CH4_2**0*DeltaPCH4_1**1 
				+ p20*composition_CH4_2**2*DeltaPCH4_1**0
				+ p11*composition_CH4_2**1*DeltaPCH4_1**1 
				+ p02*composition_CH4_2**0*DeltaPCH4_1**2 
				+ p30*composition_CH4_2**3*DeltaPCH4_1**0 
				+ p21*composition_CH4_2**2*DeltaPCH4_1**1
				+ p12*composition_CH4_2**1*DeltaPCH4_1**2 
				+ p03*composition_CH4_2**0*DeltaPCH4_1**3 
				+ p31*composition_CH4_2**3*DeltaPCH4_1**1 
				+ p22*composition_CH4_2**2*DeltaPCH4_1**2
				+ p13*composition_CH4_2**1*DeltaPCH4_1**3 
				+ p04*composition_CH4_2**0*DeltaPCH4_1**4)

				########################
				#### density calculation

				density1 = (d00*composition_CH4_1**0*DeltaPCH4_1**0 
				+ d10*composition_CH4_1**1*DeltaPCH4_1**0 
				+ d01*composition_CH4_1**0*DeltaPCH4_1**1 
				+ d20*composition_CH4_1**2*DeltaPCH4_1**0 
				+ d11*composition_CH4_1**1*DeltaPCH4_1**1 
				+ d02*composition_CH4_1**0*DeltaPCH4_1**2 
				+ d30*composition_CH4_1**3*DeltaPCH4_1**0 
				+ d21*composition_CH4_1**2*DeltaPCH4_1**1
				+ d12*composition_CH4_1**1*DeltaPCH4_1**2 
				+ d03*composition_CH4_1**0*DeltaPCH4_1**3 
				+ d31*composition_CH4_1**3*DeltaPCH4_1**1 
				+ d22*composition_CH4_1**2*DeltaPCH4_1**2
				+ d13*composition_CH4_1**1*DeltaPCH4_1**3 
				+ d04*composition_CH4_1**0*DeltaPCH4_1**4)

				density2 = (d00*composition_CH4_2**0*DeltaPCH4_2**0 
				+ d10*composition_CH4_2**1*DeltaPCH4_2**0 
				+ d01*composition_CH4_2**0*DeltaPCH4_2**1 
				+ d20*composition_CH4_2**2*DeltaPCH4_2**0
				+ d11*composition_CH4_2**1*DeltaPCH4_2**1 
				+ d02*composition_CH4_2**0*DeltaPCH4_2**2 
				+ d30*composition_CH4_2**3*DeltaPCH4_2**0 
				+ d21*composition_CH4_2**2*DeltaPCH4_2**1
				+ d12*composition_CH4_2**1*DeltaPCH4_2**2 
				+ d03*composition_CH4_2**0*DeltaPCH4_2**3 
				+ d31*composition_CH4_2**3*DeltaPCH4_2**1 
				+ d22*composition_CH4_2**2*DeltaPCH4_2**2
				+ d13*composition_CH4_2**1*DeltaPCH4_2**3 
				+ d04*composition_CH4_2**0*DeltaPCH4_2**4)


				density3 = (d00*composition_CH4_1**0*DeltaPCH4_2**0 
				+ d10*composition_CH4_1**1*DeltaPCH4_2**0 
				+ d01*composition_CH4_1**0*DeltaPCH4_2**1 
				+ d20*composition_CH4_1**2*DeltaPCH4_2**0
				+ d11*composition_CH4_1**1*DeltaPCH4_2**1 
				+ d02*composition_CH4_1**0*DeltaPCH4_2**2 
				+ d30*composition_CH4_1**3*DeltaPCH4_2**0 
				+ d21*composition_CH4_1**2*DeltaPCH4_2**1
				+ d12*composition_CH4_1**1*DeltaPCH4_2**2 
				+ d03*composition_CH4_1**0*DeltaPCH4_2**3 
				+ d31*composition_CH4_1**3*DeltaPCH4_2**1 
				+ d22*composition_CH4_1**2*DeltaPCH4_2**2
				+ d13*composition_CH4_1**1*DeltaPCH4_2**3 
				+ d04*composition_CH4_1**0*DeltaPCH4_2**4)

				density4 = (d00*composition_CH4_2**0*DeltaPCH4_1**0 
				+ d10*composition_CH4_2**1*DeltaPCH4_1**0 
				+ d01*composition_CH4_2**0*DeltaPCH4_1**1 
				+ d20*composition_CH4_2**2*DeltaPCH4_1**0
				+ d11*composition_CH4_2**1*DeltaPCH4_1**1 
				+ d02*composition_CH4_2**0*DeltaPCH4_1**2 
				+ d30*composition_CH4_2**3*DeltaPCH4_1**0 
				+ d21*composition_CH4_2**2*DeltaPCH4_1**1
				+ d12*composition_CH4_2**1*DeltaPCH4_1**2 
				+ d03*composition_CH4_2**0*DeltaPCH4_1**3 
				+ d31*composition_CH4_2**3*DeltaPCH4_1**1 
				+ d22*composition_CH4_2**2*DeltaPCH4_1**2
				+ d13*composition_CH4_2**1*DeltaPCH4_1**3 
				+ d04*composition_CH4_2**0*DeltaPCH4_1**4)              

				pressure_final = (max(pressure1, pressure2, pressure3, pressure4) + min(pressure1, pressure2, pressure3, pressure4))/2
				uncer_pressure_final = 10.6 + (max(pressure1, pressure2, pressure3, pressure4) - min(pressure1, pressure2, pressure3, pressure4))/(2*np.sqrt(3)) #uncer 15

				density_final = (max(density1, density2, density3, density4) + min(density1, density2, density3, density4))/2
				uncer_density_final = 0.0042 + (max(density1, density2, density3, density4) - min(density1, density2, density3, density4))/(2*np.sqrt(3)) #uncer 0.006

				molarvolume1 = 1/(max(density1, density2, density3, density4)/(44*composition_CO2 + 16*composition_CH4))
				molarvolume2 = 1/(min(density1, density2, density3, density4)/(44*composition_CO2 + 16*composition_CH4))
				molarvolume_final = (molarvolume1 + molarvolume2) / 2
				uncer_molarvolume_final = (molarvolume2 - molarvolume1) / (2*np.sqrt(3))

				print('pressure1', pressure1)
				print('pressure2', pressure2)
				print('pressure3', pressure3)
				print('pressure4', pressure4)

				print('density 1=', density1)
				print('density 2=', density2)
				print('density 3=', density3)
				print('density 4=', density4)

				print("molarvolume1", molarvolume1)
				print("molarvolume2", molarvolume2)
				

				if pressure_final > 650 or pressure1 >650 or pressure2 >650 or pressure_final < -20 or pressure1 <-20 or pressure2 <-20 or density2<0 or density1 <0 or density3<0 or density4<0 or density_final <0:
					popupmsg_OCR()

			
			########################################################
			#### Caculation at temperature = 32 °C
			########################################################

			if temperature.get() == 32 and instrument.get() ==2 and composition_CO2 > 0.5: 

				## Calibration equation's coeff of CO2-CH4 at 32 °C over 5-500 bars

				# normalisation of concentration and of Fermi diad splitting ( 5-600 bars)
				composition_CO2_normalized_1 = (composition_CO2 + 0.005)
				composition_CO2_normalized_2 = (composition_CO2 - 0.005)
				FDS_normalized_1 = (FDS + unc_FDS - FDS_std)
				FDS_normalized_2 = (FDS - unc_FDS - FDS_std)
				
				p00= -105.913174
				p10= 631.841069
				p01= 1192.786132
				p20= -1078.549650
				p11= -4347.6194742
				p02= 758.1531764
				p30= 554.031279
				p21= 6980.102231
				p12= -3305.090080
				p03= 631.8784164
				p31= -3652.9343212
				p22= 2458.4316174
				p13= -679.75432525
				p04= 34.685553157

				d00= 0.26707535
				d10= -1.1698421
				d01= 0.81607584
				d20= 1.651564997
				d11= -0.8726431765
				d02= -0.0558924062
				d30= -0.74504069134
				d21= 0.11211555518
				d12= 0.757512216515
				d03= -0.18547039549
				d31= 0.2196811641
				d22= -0.5740298668
				d13= 0.17264413366
				d04= -0.00711231978


				#### pressure calculation
				pressure1 = (p00*composition_CO2_normalized_1**0*FDS_normalized_1**0 
				+ p10*composition_CO2_normalized_1**1*FDS_normalized_1**0 
				+ p01*composition_CO2_normalized_1**0*FDS_normalized_1**1 
				+ p20*composition_CO2_normalized_1**2*FDS_normalized_1**0 
				+ p11*composition_CO2_normalized_1**1*FDS_normalized_1**1 
				+ p02*composition_CO2_normalized_1**0*FDS_normalized_1**2 
				+ p30*composition_CO2_normalized_1**3*FDS_normalized_1**0 
				+ p21*composition_CO2_normalized_1**2*FDS_normalized_1**1
				+ p12*composition_CO2_normalized_1**1*FDS_normalized_1**2 
				+ p03*composition_CO2_normalized_1**0*FDS_normalized_1**3 
				+ p31*composition_CO2_normalized_1**3*FDS_normalized_1**1 
				+ p22*composition_CO2_normalized_1**2*FDS_normalized_1**2
				+ p13*composition_CO2_normalized_1**1*FDS_normalized_1**3 
				+ p04*composition_CO2_normalized_1**0*FDS_normalized_1**4)

				pressure2 = (p00*composition_CO2_normalized_2**0*FDS_normalized_2**0 
				+ p10*composition_CO2_normalized_2**1*FDS_normalized_2**0 
				+ p01*composition_CO2_normalized_2**0*FDS_normalized_2**1 
				+ p20*composition_CO2_normalized_2**2*FDS_normalized_2**0
				+ p11*composition_CO2_normalized_2**1*FDS_normalized_2**1 
				+ p02*composition_CO2_normalized_2**0*FDS_normalized_2**2
				+ p30*composition_CO2_normalized_2**3*FDS_normalized_2**0 
				+ p21*composition_CO2_normalized_2**2*FDS_normalized_2**1
				+ p12*composition_CO2_normalized_2**1*FDS_normalized_2**2 
				+ p03*composition_CO2_normalized_2**0*FDS_normalized_2**3 
				+ p31*composition_CO2_normalized_2**3*FDS_normalized_2**1 
				+ p22*composition_CO2_normalized_2**2*FDS_normalized_2**2
				+ p13*composition_CO2_normalized_2**1*FDS_normalized_2**3 
				+ p04*composition_CO2_normalized_2**0*FDS_normalized_2**4)

				pressure3 = (p00*composition_CO2_normalized_1**0*FDS_normalized_2**0 
				+ p10*composition_CO2_normalized_1**1*FDS_normalized_2**0 
				+ p01*composition_CO2_normalized_1**0*FDS_normalized_2**1 
				+ p20*composition_CO2_normalized_1**2*FDS_normalized_2**0
				+ p11*composition_CO2_normalized_1**1*FDS_normalized_2**1 
				+ p02*composition_CO2_normalized_1**0*FDS_normalized_2**2 
				+ p30*composition_CO2_normalized_1**3*FDS_normalized_2**0 
				+ p21*composition_CO2_normalized_1**2*FDS_normalized_2**1
				+ p12*composition_CO2_normalized_1**1*FDS_normalized_2**2 
				+ p03*composition_CO2_normalized_1**0*FDS_normalized_2**3 
				+ p31*composition_CO2_normalized_1**3*FDS_normalized_2**1 
				+ p22*composition_CO2_normalized_1**2*FDS_normalized_2**2
				+ p13*composition_CO2_normalized_1**1*FDS_normalized_2**3 
				+ p04*composition_CO2_normalized_1**0*FDS_normalized_2**4)

				pressure4 = (p00*composition_CO2_normalized_2**0*FDS_normalized_1**0 
				+ p10*composition_CO2_normalized_2**1*FDS_normalized_1**0 
				+ p01*composition_CO2_normalized_2**0*FDS_normalized_1**1 
				+ p20*composition_CO2_normalized_2**2*FDS_normalized_1**0
				+ p11*composition_CO2_normalized_2**1*FDS_normalized_1**1 
				+ p02*composition_CO2_normalized_2**0*FDS_normalized_1**2 
				+ p30*composition_CO2_normalized_2**3*FDS_normalized_1**0 
				+ p21*composition_CO2_normalized_2**2*FDS_normalized_1**1
				+ p12*composition_CO2_normalized_2**1*FDS_normalized_1**2 
				+ p03*composition_CO2_normalized_2**0*FDS_normalized_1**3 
				+ p31*composition_CO2_normalized_2**3*FDS_normalized_1**1 
				+ p22*composition_CO2_normalized_2**2*FDS_normalized_1**2
				+ p13*composition_CO2_normalized_2**1*FDS_normalized_1**3 
				+ p04*composition_CO2_normalized_2**0*FDS_normalized_1**4)

				########################
				#### density calculation

				density1 = (d00*composition_CO2_normalized_1**0*FDS_normalized_1**0 
				+ d10*composition_CO2_normalized_1**1*FDS_normalized_1**0 
				+ d01*composition_CO2_normalized_1**0*FDS_normalized_1**1 
				+ d20*composition_CO2_normalized_1**2*FDS_normalized_1**0 
				+ d11*composition_CO2_normalized_1**1*FDS_normalized_1**1 
				+ d02*composition_CO2_normalized_1**0*FDS_normalized_1**2 
				+ d30*composition_CO2_normalized_1**3*FDS_normalized_1**0 
				+ d21*composition_CO2_normalized_1**2*FDS_normalized_1**1
				+ d12*composition_CO2_normalized_1**1*FDS_normalized_1**2 
				+ d03*composition_CO2_normalized_1**0*FDS_normalized_1**3 
				+ d31*composition_CO2_normalized_1**3*FDS_normalized_1**1 
				+ d22*composition_CO2_normalized_1**2*FDS_normalized_1**2
				+ d13*composition_CO2_normalized_1**1*FDS_normalized_1**3 
				+ d04*composition_CO2_normalized_1**0*FDS_normalized_1**4)

				density2 = (d00*composition_CO2_normalized_2**0*FDS_normalized_2**0 
				+ d10*composition_CO2_normalized_2**1*FDS_normalized_2**0 
				+ d01*composition_CO2_normalized_2**0*FDS_normalized_2**1 
				+ d20*composition_CO2_normalized_2**2*FDS_normalized_2**0
				+ d11*composition_CO2_normalized_2**1*FDS_normalized_2**1 
				+ d02*composition_CO2_normalized_2**0*FDS_normalized_2**2
				+ d30*composition_CO2_normalized_2**3*FDS_normalized_2**0 
				+ d21*composition_CO2_normalized_2**2*FDS_normalized_2**1
				+ d12*composition_CO2_normalized_2**1*FDS_normalized_2**2 
				+ d03*composition_CO2_normalized_2**0*FDS_normalized_2**3 
				+ d31*composition_CO2_normalized_2**3*FDS_normalized_2**1 
				+ d22*composition_CO2_normalized_2**2*FDS_normalized_2**2
				+ d13*composition_CO2_normalized_2**1*FDS_normalized_2**3 
				+ d04*composition_CO2_normalized_2**0*FDS_normalized_2**4)

				density3 = (d00*composition_CO2_normalized_1**0*FDS_normalized_2**0 
				+ d10*composition_CO2_normalized_1**1*FDS_normalized_2**0 
				+ d01*composition_CO2_normalized_1**0*FDS_normalized_2**1 
				+ d20*composition_CO2_normalized_1**2*FDS_normalized_2**0
				+ d11*composition_CO2_normalized_1**1*FDS_normalized_2**1 
				+ d02*composition_CO2_normalized_1**0*FDS_normalized_2**2 
				+ d30*composition_CO2_normalized_1**3*FDS_normalized_2**0 
				+ d21*composition_CO2_normalized_1**2*FDS_normalized_2**1
				+ d12*composition_CO2_normalized_1**1*FDS_normalized_2**2 
				+ d03*composition_CO2_normalized_1**0*FDS_normalized_2**3 
				+ d31*composition_CO2_normalized_1**3*FDS_normalized_2**1 
				+ d22*composition_CO2_normalized_1**2*FDS_normalized_2**2
				+ d13*composition_CO2_normalized_1**1*FDS_normalized_2**3 
				+ d04*composition_CO2_normalized_1**0*FDS_normalized_2**4)

				density4 = (d00*composition_CO2_normalized_2**0*FDS_normalized_1**0 
				+ d10*composition_CO2_normalized_2**1*FDS_normalized_1**0 
				+ d01*composition_CO2_normalized_2**0*FDS_normalized_1**1 
				+ d20*composition_CO2_normalized_2**2*FDS_normalized_1**0
				+ d11*composition_CO2_normalized_2**1*FDS_normalized_1**1 
				+ d02*composition_CO2_normalized_2**0*FDS_normalized_1**2 
				+ d30*composition_CO2_normalized_2**3*FDS_normalized_1**0 
				+ d21*composition_CO2_normalized_2**2*FDS_normalized_1**1
				+ d12*composition_CO2_normalized_2**1*FDS_normalized_1**2 
				+ d03*composition_CO2_normalized_2**0*FDS_normalized_1**3 
				+ d31*composition_CO2_normalized_2**3*FDS_normalized_1**1 
				+ d22*composition_CO2_normalized_2**2*FDS_normalized_1**2
				+ d13*composition_CO2_normalized_2**1*FDS_normalized_1**3 
				+ d04*composition_CO2_normalized_2**0*FDS_normalized_1**4)              

				pressure_final = (max(pressure1, pressure2, pressure3, pressure4) + min(pressure1, pressure2, pressure3, pressure4))/2 #pressure max - pressure min
				uncer_pressure_final = 7+ (max(pressure1, pressure2, pressure3, pressure4) - min(pressure1, pressure2, pressure3, pressure4))/(2*np.sqrt(3)) #10 bar

				density_final = (max(density1, density2, density3, density4) + min(density1, density2, density3, density4))/2 #density max - density min
				uncer_density_final = 5.7 + (max(density1, density2, density3, density4) - min(density1, density2, density3, density4))/(2*np.sqrt(3)) # 0.008

				molarvolume1 = 1/(max(density1, density2, density3, density4)/(44*composition_CO2 + 16*composition_CH4))
				molarvolume2 = 1/(min(density1, density2, density3, density4)/(44*composition_CO2 + 16*composition_CH4))
				molarvolume_final = (molarvolume1 + molarvolume2) / 2
				uncer_molarvolume_final = (molarvolume2 - molarvolume1) / (2*np.sqrt(3))

				##### verify if measured pressure < 160 bar, if it is, re-recalculte using calibration data for 5-160 bar range.
				if pressure_final <= 150: 

					## Calibration equation's coeff of CO2-CH4 at 32 °C over 5-160 bars
					# normalisation of concentration and of Fermi diad splitting
					
					composition_CO2_normalized_1 = (composition_CO2 + 0.005)
					composition_CO2_normalized_2 = (composition_CO2 - 0.005)
					FDS_normalized_1 = (FDS + unc_FDS - FDS_std)
					FDS_normalized_2 = (FDS - unc_FDS - FDS_std)
										
					p00= 141.951616
					p10= -579.2394482
					p01= 614.57368028
					p20= 760.30579508
					p11= -598.0960087
					p02= -207.7329434
					p30= -322.1194760
					p21= 255.99405946
					p12= -483.56951389
					p03= 401.2795613
					p31= -109.8534278
					p22= 637.3098889
					p13= -475.6663413
					p04= 40.254842508

					d00= 0.25477220259
					d10= -1.0825921301
					d01= 0.7628970396
					d20= 1.48158046024
					d11= -0.89335476887
					d02= 0.113777445
					d30= -0.6588737729
					d21= 0.67348154411
					d12= -0.1384061389
					d03= 0.0273686878
					d31= -0.1614827445
					d22= -0.100445609
					d13= 0.15647062358
					d04= -0.055429077

					#### pressure calculation
					pressure1 = (p00*composition_CO2_normalized_1**0*FDS_normalized_1**0 
					+ p10*composition_CO2_normalized_1**1*FDS_normalized_1**0 
					+ p01*composition_CO2_normalized_1**0*FDS_normalized_1**1 
					+ p20*composition_CO2_normalized_1**2*FDS_normalized_1**0 
					+ p11*composition_CO2_normalized_1**1*FDS_normalized_1**1 
					+ p02*composition_CO2_normalized_1**0*FDS_normalized_1**2 
					+ p30*composition_CO2_normalized_1**3*FDS_normalized_1**0 
					+ p21*composition_CO2_normalized_1**2*FDS_normalized_1**1
					+ p12*composition_CO2_normalized_1**1*FDS_normalized_1**2 
					+ p03*composition_CO2_normalized_1**0*FDS_normalized_1**3 
					+ p31*composition_CO2_normalized_1**3*FDS_normalized_1**1 
					+ p22*composition_CO2_normalized_1**2*FDS_normalized_1**2
					+ p13*composition_CO2_normalized_1**1*FDS_normalized_1**3 
					+ p04*composition_CO2_normalized_1**0*FDS_normalized_1**4)

					pressure2 = (p00*composition_CO2_normalized_2**0*FDS_normalized_2**0 
					+ p10*composition_CO2_normalized_2**1*FDS_normalized_2**0 
					+ p01*composition_CO2_normalized_2**0*FDS_normalized_2**1 
					+ p20*composition_CO2_normalized_2**2*FDS_normalized_2**0
					+ p11*composition_CO2_normalized_2**1*FDS_normalized_2**1 
					+ p02*composition_CO2_normalized_2**0*FDS_normalized_2**2
					+ p30*composition_CO2_normalized_2**3*FDS_normalized_2**0 
					+ p21*composition_CO2_normalized_2**2*FDS_normalized_2**1
					+ p12*composition_CO2_normalized_2**1*FDS_normalized_2**2 
					+ p03*composition_CO2_normalized_2**0*FDS_normalized_2**3 
					+ p31*composition_CO2_normalized_2**3*FDS_normalized_2**1 
					+ p22*composition_CO2_normalized_2**2*FDS_normalized_2**2
					+ p13*composition_CO2_normalized_2**1*FDS_normalized_2**3 
					+ p04*composition_CO2_normalized_2**0*FDS_normalized_2**4)

					pressure3 = (p00*composition_CO2_normalized_1**0*FDS_normalized_2**0 
					+ p10*composition_CO2_normalized_1**1*FDS_normalized_2**0 
					+ p01*composition_CO2_normalized_1**0*FDS_normalized_2**1 
					+ p20*composition_CO2_normalized_1**2*FDS_normalized_2**0
					+ p11*composition_CO2_normalized_1**1*FDS_normalized_2**1 
					+ p02*composition_CO2_normalized_1**0*FDS_normalized_2**2 
					+ p30*composition_CO2_normalized_1**3*FDS_normalized_2**0 
					+ p21*composition_CO2_normalized_1**2*FDS_normalized_2**1
					+ p12*composition_CO2_normalized_1**1*FDS_normalized_2**2 
					+ p03*composition_CO2_normalized_1**0*FDS_normalized_2**3 
					+ p31*composition_CO2_normalized_1**3*FDS_normalized_2**1 
					+ p22*composition_CO2_normalized_1**2*FDS_normalized_2**2
					+ p13*composition_CO2_normalized_1**1*FDS_normalized_2**3 
					+ p04*composition_CO2_normalized_1**0*FDS_normalized_2**4)

					pressure4 = (p00*composition_CO2_normalized_2**0*FDS_normalized_1**0 
					+ p10*composition_CO2_normalized_2**1*FDS_normalized_1**0 
					+ p01*composition_CO2_normalized_2**0*FDS_normalized_1**1 
					+ p20*composition_CO2_normalized_2**2*FDS_normalized_1**0
					+ p11*composition_CO2_normalized_2**1*FDS_normalized_1**1 
					+ p02*composition_CO2_normalized_2**0*FDS_normalized_1**2 
					+ p30*composition_CO2_normalized_2**3*FDS_normalized_1**0 
					+ p21*composition_CO2_normalized_2**2*FDS_normalized_1**1
					+ p12*composition_CO2_normalized_2**1*FDS_normalized_1**2 
					+ p03*composition_CO2_normalized_2**0*FDS_normalized_1**3 
					+ p31*composition_CO2_normalized_2**3*FDS_normalized_1**1 
					+ p22*composition_CO2_normalized_2**2*FDS_normalized_1**2
					+ p13*composition_CO2_normalized_2**1*FDS_normalized_1**3 
					+ p04*composition_CO2_normalized_2**0*FDS_normalized_1**4)

					########################
					#### density calculation

					density1 = (d00*composition_CO2_normalized_1**0*FDS_normalized_1**0 
					+ d10*composition_CO2_normalized_1**1*FDS_normalized_1**0 
					+ d01*composition_CO2_normalized_1**0*FDS_normalized_1**1 
					+ d20*composition_CO2_normalized_1**2*FDS_normalized_1**0 
					+ d11*composition_CO2_normalized_1**1*FDS_normalized_1**1 
					+ d02*composition_CO2_normalized_1**0*FDS_normalized_1**2 
					+ d30*composition_CO2_normalized_1**3*FDS_normalized_1**0 
					+ d21*composition_CO2_normalized_1**2*FDS_normalized_1**1
					+ d12*composition_CO2_normalized_1**1*FDS_normalized_1**2 
					+ d03*composition_CO2_normalized_1**0*FDS_normalized_1**3 
					+ d31*composition_CO2_normalized_1**3*FDS_normalized_1**1 
					+ d22*composition_CO2_normalized_1**2*FDS_normalized_1**2
					+ d13*composition_CO2_normalized_1**1*FDS_normalized_1**3 
					+ d04*composition_CO2_normalized_1**0*FDS_normalized_1**4)

					density2 = (d00*composition_CO2_normalized_2**0*FDS_normalized_2**0 
					+ d10*composition_CO2_normalized_2**1*FDS_normalized_2**0 
					+ d01*composition_CO2_normalized_2**0*FDS_normalized_2**1 
					+ d20*composition_CO2_normalized_2**2*FDS_normalized_2**0
					+ d11*composition_CO2_normalized_2**1*FDS_normalized_2**1 
					+ d02*composition_CO2_normalized_2**0*FDS_normalized_2**2
					+ d30*composition_CO2_normalized_2**3*FDS_normalized_2**0 
					+ d21*composition_CO2_normalized_2**2*FDS_normalized_2**1
					+ d12*composition_CO2_normalized_2**1*FDS_normalized_2**2 
					+ d03*composition_CO2_normalized_2**0*FDS_normalized_2**3 
					+ d31*composition_CO2_normalized_2**3*FDS_normalized_2**1 
					+ d22*composition_CO2_normalized_2**2*FDS_normalized_2**2
					+ d13*composition_CO2_normalized_2**1*FDS_normalized_2**3 
					+ d04*composition_CO2_normalized_2**0*FDS_normalized_2**4)

					density3 = (d00*composition_CO2_normalized_1**0*FDS_normalized_2**0 
					+ d10*composition_CO2_normalized_1**1*FDS_normalized_2**0 
					+ d01*composition_CO2_normalized_1**0*FDS_normalized_2**1 
					+ d20*composition_CO2_normalized_1**2*FDS_normalized_2**0
					+ d11*composition_CO2_normalized_1**1*FDS_normalized_2**1 
					+ d02*composition_CO2_normalized_1**0*FDS_normalized_2**2 
					+ d30*composition_CO2_normalized_1**3*FDS_normalized_2**0 
					+ d21*composition_CO2_normalized_1**2*FDS_normalized_2**1
					+ d12*composition_CO2_normalized_1**1*FDS_normalized_2**2 
					+ d03*composition_CO2_normalized_1**0*FDS_normalized_2**3 
					+ d31*composition_CO2_normalized_1**3*FDS_normalized_2**1 
					+ d22*composition_CO2_normalized_1**2*FDS_normalized_2**2
					+ d13*composition_CO2_normalized_1**1*FDS_normalized_2**3 
					+ d04*composition_CO2_normalized_1**0*FDS_normalized_2**4)

					density4 = (d00*composition_CO2_normalized_2**0*FDS_normalized_1**0 
					+ d10*composition_CO2_normalized_2**1*FDS_normalized_1**0 
					+ d01*composition_CO2_normalized_2**0*FDS_normalized_1**1 
					+ d20*composition_CO2_normalized_2**2*FDS_normalized_1**0
					+ d11*composition_CO2_normalized_2**1*FDS_normalized_1**1 
					+ d02*composition_CO2_normalized_2**0*FDS_normalized_1**2 
					+ d30*composition_CO2_normalized_2**3*FDS_normalized_1**0 
					+ d21*composition_CO2_normalized_2**2*FDS_normalized_1**1
					+ d12*composition_CO2_normalized_2**1*FDS_normalized_1**2 
					+ d03*composition_CO2_normalized_2**0*FDS_normalized_1**3 
					+ d31*composition_CO2_normalized_2**3*FDS_normalized_1**1 
					+ d22*composition_CO2_normalized_2**2*FDS_normalized_1**2
					+ d13*composition_CO2_normalized_2**1*FDS_normalized_1**3 
					+ d04*composition_CO2_normalized_2**0*FDS_normalized_1**4)              

					pressure_final = (max(pressure1, pressure2, pressure3, pressure4) + min(pressure1, pressure2, pressure3, pressure4))/2 #pressure max - pressure min
					uncer_pressure_final = 4.5 + (max(pressure1, pressure2, pressure3, pressure4) - min(pressure1, pressure2, pressure3, pressure4))/(2*np.sqrt(3)) #uncer = 6

					density_final = (max(density1, density2, density3, density4) + min(density1, density2, density3, density4))/2 #density max - density min
					uncer_density_final = 0.0057 + (max(density1, density2, density3, density4) - min(density1, density2, density3, density4))/(2*np.sqrt(3)) #uncer = 0.008

					molarvolume1 = 1/(max(density1, density2, density3, density4)/(44*composition_CO2 + 16*composition_CH4))
					molarvolume2 = 1/(min(density1, density2, density3, density4)/(44*composition_CO2 + 16*composition_CH4))
					molarvolume_final = (molarvolume1 + molarvolume2) / 2
					uncer_molarvolume_final = (molarvolume2 - molarvolume1) / (2*np.sqrt(3))

				print('pressure1', pressure1)
				print('pressure2', pressure2)
				print('pressure3', pressure3)
				print('pressure4', pressure4)

				print('density 1=', density1)
				print('density 2=', density2)
				print('density 3=', density3)
				print('density 4=', density4)

				print("molarvolume1", molarvolume1)
				print("molarvolume2", molarvolume2)
				
				if pressure_final > 650 or pressure1 >650 or pressure2 >650 or pressure_final < -20 or pressure1 <-20 or pressure2 <-20 or density2<0 or density1 <0 or density3<0 or density4<0 or density_final <0 :
					popupmsg_OCR()
					

			if temperature.get() == 32 and instrument.get() ==2 and composition_CH4 >= 0.5: 

				
				## Calibration equation's coeff of CO2CH4 at 32 °C

				DeltaPCH4= nuCH4_sample - nuCH4_std
				DeltaPCH4_1 = DeltaPCH4 + unc_nuCH4
				DeltaPCH4_2 = DeltaPCH4 - unc_nuCH4
				                         
				
				p00= 16.99348609
				p10= -75.74655975
				p01= -35.5907442
				p20= 139.4767471
				p11= -150.7113177
				p02= -20.60862944
				p30= -63.0556863
				p21= 359.9252978
				p12= 83.88300229
				p03= 6.207870544
				p31= -175.5603532
				p22= -20.17126712
				p13= 6.957810313
				p04= 1.313724336

				d00= -0.003751017
				d10=0.079358301
				d01= -0.060703048
				d20= -0.155452793
				d11= -0.106032328
				d02= 0.0036172
				d30= 0.087333073
				d21= 0.217043194
				d12= -0.005840984
				d03= -0.00024797
				d31= -0.079155646
				d22= 0.006827228
				d13= 0.001283486
				d04= 0.000100213



				#### pressure calculation
				pressure1 = (p00*composition_CH4_1**0*DeltaPCH4_1**0 
				+ p10*composition_CH4_1**1*DeltaPCH4_1**0 
				+ p01*composition_CH4_1**0*DeltaPCH4_1**1 
				+ p20*composition_CH4_1**2*DeltaPCH4_1**0 
				+ p11*composition_CH4_1**1*DeltaPCH4_1**1 
				+ p02*composition_CH4_1**0*DeltaPCH4_1**2 
				+ p30*composition_CH4_1**3*DeltaPCH4_1**0 
				+ p21*composition_CH4_1**2*DeltaPCH4_1**1
				+ p12*composition_CH4_1**1*DeltaPCH4_1**2 
				+ p03*composition_CH4_1**0*DeltaPCH4_1**3 
				+ p31*composition_CH4_1**3*DeltaPCH4_1**1 
				+ p22*composition_CH4_1**2*DeltaPCH4_1**2
				+ p13*composition_CH4_1**1*DeltaPCH4_1**3 
				+ p04*composition_CH4_1**0*DeltaPCH4_1**4)

				pressure2 = (p00*composition_CH4_2**0*DeltaPCH4_2**0 
				+ p10*composition_CH4_2**1*DeltaPCH4_2**0 
				+ p01*composition_CH4_2**0*DeltaPCH4_2**1 
				+ p20*composition_CH4_2**2*DeltaPCH4_2**0
				+ p11*composition_CH4_2**1*DeltaPCH4_2**1 
				+ p02*composition_CH4_2**0*DeltaPCH4_2**2 
				+ p30*composition_CH4_2**3*DeltaPCH4_2**0 
				+ p21*composition_CH4_2**2*DeltaPCH4_2**1
				+ p12*composition_CH4_2**1*DeltaPCH4_2**2 
				+ p03*composition_CH4_2**0*DeltaPCH4_2**3 
				+ p31*composition_CH4_2**3*DeltaPCH4_2**1 
				+ p22*composition_CH4_2**2*DeltaPCH4_2**2
				+ p13*composition_CH4_2**1*DeltaPCH4_2**3 
				+ p04*composition_CH4_2**0*DeltaPCH4_2**4)

				pressure3 = (p00*composition_CH4_1**0*DeltaPCH4_2**0 
				+ p10*composition_CH4_1**1*DeltaPCH4_2**0 
				+ p01*composition_CH4_1**0*DeltaPCH4_2**1 
				+ p20*composition_CH4_1**2*DeltaPCH4_2**0
				+ p11*composition_CH4_1**1*DeltaPCH4_2**1 
				+ p02*composition_CH4_1**0*DeltaPCH4_2**2 
				+ p30*composition_CH4_1**3*DeltaPCH4_2**0 
				+ p21*composition_CH4_1**2*DeltaPCH4_2**1
				+ p12*composition_CH4_1**1*DeltaPCH4_2**2 
				+ p03*composition_CH4_1**0*DeltaPCH4_2**3 
				+ p31*composition_CH4_1**3*DeltaPCH4_2**1 
				+ p22*composition_CH4_1**2*DeltaPCH4_2**2
				+ p13*composition_CH4_1**1*DeltaPCH4_2**3 
				+ p04*composition_CH4_1**0*DeltaPCH4_2**4)

				pressure4 = (p00*composition_CH4_2**0*DeltaPCH4_1**0 
				+ p10*composition_CH4_2**1*DeltaPCH4_1**0 
				+ p01*composition_CH4_2**0*DeltaPCH4_1**1 
				+ p20*composition_CH4_2**2*DeltaPCH4_1**0
				+ p11*composition_CH4_2**1*DeltaPCH4_1**1 
				+ p02*composition_CH4_2**0*DeltaPCH4_1**2 
				+ p30*composition_CH4_2**3*DeltaPCH4_1**0 
				+ p21*composition_CH4_2**2*DeltaPCH4_1**1
				+ p12*composition_CH4_2**1*DeltaPCH4_1**2 
				+ p03*composition_CH4_2**0*DeltaPCH4_1**3 
				+ p31*composition_CH4_2**3*DeltaPCH4_1**1 
				+ p22*composition_CH4_2**2*DeltaPCH4_1**2
				+ p13*composition_CH4_2**1*DeltaPCH4_1**3 
				+ p04*composition_CH4_2**0*DeltaPCH4_1**4)

				########################
				#### density calculation

				density1 = (d00*composition_CH4_1**0*DeltaPCH4_1**0 
				+ d10*composition_CH4_1**1*DeltaPCH4_1**0 
				+ d01*composition_CH4_1**0*DeltaPCH4_1**1 
				+ d20*composition_CH4_1**2*DeltaPCH4_1**0 
				+ d11*composition_CH4_1**1*DeltaPCH4_1**1 
				+ d02*composition_CH4_1**0*DeltaPCH4_1**2 
				+ d30*composition_CH4_1**3*DeltaPCH4_1**0 
				+ d21*composition_CH4_1**2*DeltaPCH4_1**1
				+ d12*composition_CH4_1**1*DeltaPCH4_1**2 
				+ d03*composition_CH4_1**0*DeltaPCH4_1**3 
				+ d31*composition_CH4_1**3*DeltaPCH4_1**1 
				+ d22*composition_CH4_1**2*DeltaPCH4_1**2
				+ d13*composition_CH4_1**1*DeltaPCH4_1**3 
				+ d04*composition_CH4_1**0*DeltaPCH4_1**4)

				density2 = (d00*composition_CH4_2**0*DeltaPCH4_2**0 
				+ d10*composition_CH4_2**1*DeltaPCH4_2**0 
				+ d01*composition_CH4_2**0*DeltaPCH4_2**1 
				+ d20*composition_CH4_2**2*DeltaPCH4_2**0
				+ d11*composition_CH4_2**1*DeltaPCH4_2**1 
				+ d02*composition_CH4_2**0*DeltaPCH4_2**2 
				+ d30*composition_CH4_2**3*DeltaPCH4_2**0 
				+ d21*composition_CH4_2**2*DeltaPCH4_2**1
				+ d12*composition_CH4_2**1*DeltaPCH4_2**2 
				+ d03*composition_CH4_2**0*DeltaPCH4_2**3 
				+ d31*composition_CH4_2**3*DeltaPCH4_2**1 
				+ d22*composition_CH4_2**2*DeltaPCH4_2**2
				+ d13*composition_CH4_2**1*DeltaPCH4_2**3 
				+ d04*composition_CH4_2**0*DeltaPCH4_2**4)


				density3 = (d00*composition_CH4_1**0*DeltaPCH4_2**0 
				+ d10*composition_CH4_1**1*DeltaPCH4_2**0 
				+ d01*composition_CH4_1**0*DeltaPCH4_2**1 
				+ d20*composition_CH4_1**2*DeltaPCH4_2**0
				+ d11*composition_CH4_1**1*DeltaPCH4_2**1 
				+ d02*composition_CH4_1**0*DeltaPCH4_2**2 
				+ d30*composition_CH4_1**3*DeltaPCH4_2**0 
				+ d21*composition_CH4_1**2*DeltaPCH4_2**1
				+ d12*composition_CH4_1**1*DeltaPCH4_2**2 
				+ d03*composition_CH4_1**0*DeltaPCH4_2**3 
				+ d31*composition_CH4_1**3*DeltaPCH4_2**1 
				+ d22*composition_CH4_1**2*DeltaPCH4_2**2
				+ d13*composition_CH4_1**1*DeltaPCH4_2**3 
				+ d04*composition_CH4_1**0*DeltaPCH4_2**4)

				density4 = (d00*composition_CH4_2**0*DeltaPCH4_1**0 
				+ d10*composition_CH4_2**1*DeltaPCH4_1**0 
				+ d01*composition_CH4_2**0*DeltaPCH4_1**1 
				+ d20*composition_CH4_2**2*DeltaPCH4_1**0
				+ d11*composition_CH4_2**1*DeltaPCH4_1**1 
				+ d02*composition_CH4_2**0*DeltaPCH4_1**2 
				+ d30*composition_CH4_2**3*DeltaPCH4_1**0 
				+ d21*composition_CH4_2**2*DeltaPCH4_1**1
				+ d12*composition_CH4_2**1*DeltaPCH4_1**2 
				+ d03*composition_CH4_2**0*DeltaPCH4_1**3 
				+ d31*composition_CH4_2**3*DeltaPCH4_1**1 
				+ d22*composition_CH4_2**2*DeltaPCH4_1**2
				+ d13*composition_CH4_2**1*DeltaPCH4_1**3 
				+ d04*composition_CH4_2**0*DeltaPCH4_1**4)              

				pressure_final = (max(pressure1, pressure2, pressure3, pressure4) + min(pressure1, pressure2, pressure3, pressure4))/2
				uncer_pressure_final = 10.6 + (max(pressure1, pressure2, pressure3, pressure4) - min(pressure1, pressure2, pressure3, pressure4))/(2*np.sqrt(3)) #uncer = 15

				density_final = (max(density1, density2, density3, density4) + min(density1, density2, density3, density4))/2
				uncer_density_final = 0.0035 + (max(density1, density2, density3, density4) - min(density1, density2, density3, density4))/(2*np.sqrt(3)) #uncer = 0.005

				molarvolume1 = 1/(max(density1, density2, density3, density4)/(44*composition_CO2 + 16*composition_CH4))
				molarvolume2 = 1/(min(density1, density2, density3, density4)/(44*composition_CO2 + 16*composition_CH4))
				molarvolume_final = (molarvolume1 + molarvolume2) / 2
				uncer_molarvolume_final = (molarvolume2 - molarvolume1) / (2*np.sqrt(3))

				print('pressure1', pressure1)
				print('pressure2', pressure2)
				print('pressure3', pressure3)
				print('pressure4', pressure4)

				print('density 1=', density1)
				print('density 2=', density2)
				print('density 3=', density3)
				print('density 4=', density4)

				print("molarvolume1", molarvolume1)
				print("molarvolume2", molarvolume2)
				

				if pressure_final > 650 or pressure1 >650 or pressure2 >650 or pressure_final < -20 or pressure1 <-20 or pressure2 <-20 or density2<0 or density1 <0 or density3<0 or density4<0 or density_final <0:
					popupmsg_OCR()


			####### GET RESULTS AND BUT ON THE OUT PUT FEILD (out put field just be created below) ################       
			composition_CO2_display.insert(tk.END, "%.3f" % composition_CO2)
			composition_CH4_display.insert(tk.END, "%.3f" % composition_CH4)
			pressure.insert(tk.END, "%.1f" % pressure_final)
			density.insert(tk.END, "%.3f" % density_final)
			molarvolume.insert(tk.END, "%.3f" % molarvolume_final)

			uncer_pressure.insert(tk.END, "%.1f" % uncer_pressure_final)
			uncer_density.insert(tk.END, "%.3f" % uncer_density_final)
			uncer_molarvolume.insert(tk.END, "%.3f" % uncer_molarvolume_final)

		# ################################    
		# ########  display results ######
		# ################################ 
		composition_CO2_display= tk.Entry(self.frame, width = 20) #, state='disabled'
		composition_CO2_display.grid(row=37, column=1)        
		composition_CH4_display= tk.Entry(self.frame, width = 20) #, state='disabled'
		composition_CH4_display.grid(row=37, column=3)

		pressure= tk.Entry(self.frame, width = 20) #, state='disabled'
		pressure.grid(row=39, column=1)
		density = tk.Entry(self.frame, width = 20) 
		density.grid(row=40, column=1)
		molarvolume = tk.Entry(self.frame,  width = 20)
		molarvolume.grid(row=41, column=1)

		######## display uncertainty ########
		
		uncer_pressure = tk.Entry(self.frame,  width = 20) #, state='disabled'
		uncer_pressure.grid(row=39, column=3)
		uncer_density = tk.Entry(self.frame,  width = 20) 
		uncer_density.grid(row=40, column=3)
		uncer_molarvolume = tk.Entry(self.frame,  width = 20) 
		uncer_molarvolume.grid(row=41, column=3)


		#############################
		######### Buttons ###########
		#############################

		self.button1_1 = tk.Button(self.frame, text="Clear Input", command=clear_field_inputs)
		self.button1_1.grid(row=16, column=1, padx=10)
		self.button1_2 = tk.Button(self.frame, text="Calculate", bg="green", width=10, command=calculCO2CH4)
		self.button1_2.grid(row=35, column=1, padx=20, pady=10, sticky="W")        
		self.button1_3 = tk.Button(self.frame, text="Clear Results", width=10, command=clear_field_results)
		self.button1_3.grid(row=42, column=1, padx=20, sticky="W")

		
		# def OpenSuppDoc_CO2CH4():
		# 	os.startfile(resource_path('SuppDoc_CO2CH4.pdf'))

		# self.button1_4 = tk.Button(self.frame, text="Supplement document", bg="orange", command=OpenSuppDoc_CO2CH4)
		# self.button1_4.grid(row=42, column=0, padx=10)

						
		self.quit = tk.Button(self.frame, text="Close", width=15, command=self.close_window)	
		self.quit.grid(row=42, column=3, padx=10)

	def close_window(self):
		self.master.destroy()


###############################################
########### Module CO2 - CH4 - N2 #############
###############################################
class module6: 
	def __init__(self, master, number):
		self.master = master
		self.master.title("FRAnCIs v.1.0.1 - (CO₂-CH₄-N₂ mixtures)")
		self.master.geometry("750x650")
		self.master.resizable(width=False, height=False)
		self.master.iconbitmap(resource_path("logo.ico"))
		self.frame=tk.Frame(self.master)
		self.frame.grid()

		### Create the UI of windows of module 3 
		self.label = tk.Label(self.frame, text="Calculation for CO₂-CH₄-N₂ mixtures", font=('bold', 18))
		self.label.grid(row=0, column=1, columnspan=8, padx=10, pady=10, sticky="W") #remove (side="top", fill="x",)        

		self.label = tk.Label(self.frame, text="- The area of two CO₂ bands (area_CO2), of CH₄ \u03BD₁ band (area_CH4) and of N₂ band (area_N2) are used for composition determination.")
		self.label.grid(row=1, column=0, columnspan=8, padx=10, sticky="W") #remove (side="top", fill="x",)   
		self.label = tk.Label(self.frame, text="- The measured composition and the CO₂ Fermi diad splitting (\u0394_sample and \u0394_std) are then used for pressure and density determination.")
		self.label.grid(row=3, column=0, columnspan=8,padx=10, sticky="W") #remove (side="top", fill="x",)
		

		#self.label = tk.Label(self.frame,text="___________________________________________________________________________________________________________________________________________________________________")
		#self.label.grid(row=5, column=0, padx=10, columnspan=6, sticky="E")


		self.label_remark = tk.Label(self.frame, text="Remarks:", font=('bold', 12))
		self.label_remark.grid(row=7, column=0, columnspan=8, padx=10,  sticky="W")

		self.label = tk.Label(self.frame, text="   - The calibrations were made over 5-600 bars, out of this range may cause larger errors or aberrant values.")
		self.label.grid(row=8, column=0, columnspan=10, sticky="W")
		self.label = tk.Label(self.frame, text="   - If the Dassin spectrometer (at GeoRessouces lab) is selected, (\u0394_std) is not required, and so type 0.")
		self.label.grid(row=9, column=0, columnspan=10, sticky="W")  
		self.label = tk.Label(self.frame, text="   - The area of the atmospheric N₂ band (area_N2_atm) must be excluded from that of N₂ within the sample (area_N2_sample).")
		self.label.grid(row=10, column=0, columnspan=10, sticky="W")
		self.label = tk.Label(self.frame, text="   - The fitted peak position of CH₄ should be corrected by two neon emission lines at ~2851.38 and ~2972.44 cm\u207b\u00B9 (relative to 514.53 nm).")
		self.label.grid(row=11, column=0, columnspan=10, sticky="W")
		self.label = tk.Label(self.frame, text="   - The uncertainty (1\u03C3) on the measured concentration is ~ ±0.5 mol%.")
		self.label.grid(row=13, column=0, columnspan=10, sticky="W")
		# self.label = tk.Label(self.frame, text="   - Click 'Supplement document' button below for more detail.")
		# self.label.grid(row=14, column=0, columnspan=10, sticky="W")		

		###############################
		##### INPUT section #####
		###############################

		self.label_input = tk.Label(self.frame, text="_____________     INPUT:", font=('bold', 10))
		self.label_input.grid(row=16, column=0, pady=10, sticky="E")
		self.label = tk.Label(self.frame,text="_____________________________________________________________________________________")
		self.label.grid(row=16, column=2, columnspan=6,padx=10, sticky="W")

		###############################
		##### Select Température #####
		###############################
		self.label = tk.Label(self.frame, text="Select temperature :")
		self.label.grid(row=25, column=0, columnspan=2, padx=10, sticky="W") #remove (side="top", fill="x",)

		temperature = tk.IntVar()
		temperature.set(22)

		def selected_temperature():
			print(temperature.get())

		self.Rbtn1=tk.Radiobutton(self.frame, text="22 °C", variable=temperature, value=22, padx = 20,  command=selected_temperature).grid(row=25, column=1,  padx=10, sticky="W")
		self.Rbtn1=tk.Radiobutton(self.frame, text="32 °C", variable=temperature, value=32, padx = 20,  command=selected_temperature).grid(row=25, column=2,  padx=10, sticky="W")

		###############################
		##### Select Instrument #####
		###############################

		self.label = tk.Label(self.frame, text="Select spectrometers :")
		self.label.grid(row=26, column=0, columnspan=2, padx=10, sticky="W") #remove (side="top", fill="x",)

		instrument = tk.IntVar()
		instrument.set(1) #Dassin = 1, other spectrometers= 2

		def selected_instrument():
			print(instrument.get())

		self.Rbtn1=tk.Radiobutton(self.frame, text="Dassin", variable=instrument, value=1, padx = 20,  command=selected_instrument).grid(row=26, column=1,  padx=10, sticky="W")
		self.Rbtn1=tk.Radiobutton(self.frame, text="Other Spectrometers", variable=instrument, value=2, padx = 20,  command=selected_instrument).grid(row=26, column=2,  padx=10, sticky="W")

		####################################
		##### Select Laser wavelength #####
		####################################

		self.label = tk.Label(self.frame, text="Laser wavelength (nm):")
		self.label.grid(row=26, column=3, columnspan=2, padx=30, stick="W") #remove (side="top", fill="x",)

		# options = {"488 nm": 488, "514 nm": 514, "532 nm": 532, "633 nm": 633, "785 nm": 785}
		options=[488, 514, 532, 633, 785]
		laser_wavelength = tk.IntVar()
		laser_wavelength.set(514)
		
		# self.menu = OptionMenu(self.frame, laser_wavelength, *options.keys()).grid(row=26, column=4, stick="W")
		self.menu = OptionMenu(self.frame, laser_wavelength, *options).grid(row=26, column=4)


		######### ENTRY ##########

		##entry CO2 spectroscopic data 
		self.label = tk.Label(self.frame, text="Spectroscopic data of CO₂ :")
		self.label.grid(row=30, column=0, padx=10, sticky="W")

		self.label = tk.Label(self.frame, text="area_CO2")
		self.label.grid(row=29, column=1, padx=10)
		self.label = tk.Label(self.frame, text="\u0394_sample (cm\u207b\u00B9)")
		self.label.grid(row=29, column=2, padx=10)
		self.label = tk.Label(self.frame, text="\u0394_std (cm\u207b\u00B9)")
		self.label.grid(row=29, column=3, padx=10)
		self.label = tk.Label(self.frame, text="\u0394_uncertainty (cm\u207b\u00B9)")
		self.label.grid(row=29, column=4, padx=10)

		self.area_CO2_entry = tk.Entry(self.frame, width = 15)
		self.area_CO2_entry.grid(row=30, column=1)
		self.FDS_entry = tk.Entry(self.frame, width = 15)
		self.FDS_entry.grid(row=30, column=2)
		self.FDS_entry_std = tk.Entry(self.frame, width = 15)
		self.FDS_entry_std.grid(row=30, column=3)
		self.unc_FDS_entry = tk.Entry(self.frame, width = 15)
		self.unc_FDS_entry.grid(row=30, column=4)
		
		##entry CH4 and N2 spectroscopic data (peak area)
		self.label = tk.Label(self.frame, text="Peak area of CH₄ and N₂ :")
		self.label.grid(row=32, column=0, padx=10, sticky="W")
		self.label = tk.Label(self.frame, text="area_CH4")
		self.label.grid(row=31, column=1, padx=10)
		self.label = tk.Label(self.frame, text="area_N2_sample")
		self.label.grid(row=31, column=2, padx=10)
		self.label = tk.Label(self.frame, text="area_N2_atm")
		self.label.grid(row=31, column=3, padx=10)
		

		
		self.area_CH4_entry = tk.Entry(self.frame, width = 15)
		self.area_CH4_entry.grid(row=32, column=1)
		self.area_N2_entry_sample = tk.Entry(self.frame, width = 15)
		self.area_N2_entry_sample.grid(row=32, column=2)
		self.area_N2_entry_atm = tk.Entry(self.frame, width = 15)
		self.area_N2_entry_atm.grid(row=32, column=3)

		
	    ##########################
		### OUTPUT ###############

		self.label = tk.Label(self.frame, text="____________  OUTPUT:", font=('bold', 10))
		self.label.grid(row=37, column=0,  sticky="E")
		self.label = tk.Label(self.frame, text="_____________________________________________________________________________________")
		self.label.grid(row=37, column=2, columnspan=10, padx=10, sticky="W")        

		self.label = tk.Label(self.frame, text="(mol% CO₂)")
		self.label.grid(row=38, column=1, padx=10)
		self.label = tk.Label(self.frame, text="(mol% CH₄)")
		self.label.grid(row=38, column=2, padx=10)
		self.label = tk.Label(self.frame, text="(mol% N₂)")
		self.label.grid(row=38, column=3, padx=10)

		self.label = tk.Label(self.frame, text="Composition")
		self.label.grid(row=39, column=0, padx=10, sticky="W")
		self.label = tk.Label(self.frame, text="(±0.5 mol%)")
		self.label.grid(row=39, column=4, padx=10, sticky="W")
		
		self.label = tk.Label(self.frame, text="------------------------------------------------------------------")
		self.label.grid(row=40, column=1, columnspan=3, padx=10)

		self.label = tk.Label(self.frame, text="Pressure")
		self.label.grid(row=41, column=0, padx=10, pady=5, sticky="W")
		self.label = tk.Label(self.frame, text="Density")
		self.label.grid(row=42, column=0, padx=10, pady=5, sticky="W")
		self.label = tk.Label(self.frame, text="Molar Volume")
		self.label.grid(row=43, column=0, padx=10, pady=5, sticky="W")

		
		
		self.label = tk.Label(self.frame, text="±")
		self.label.grid(row=41, column=2, padx=10, pady=5)
		self.label = tk.Label(self.frame, text="±")
		self.label.grid(row=42, column=2, padx=10, pady=5)
		self.label = tk.Label(self.frame, text="±")
		self.label.grid(row=43, column=2, padx=10, pady=5)

		
		
		self.label = tk.Label(self.frame, text="(bar)")
		self.label.grid(row=42, column=4, padx=10, pady=5, sticky="W")
		self.label = tk.Label(self.frame, text="(g.cm\u207b\u00B3)")
		self.label.grid(row=43, column=4, padx=10, pady=5, sticky="W")
		self.label = tk.Label(self.frame, text="(cm\u00B3.mol\u207b\u00B9)")
		self.label.grid(row=41, column=4, padx=10, pady=5, sticky="W")


		###############################
		##### Caculation ##############
		###############################

		#### Make a clear-button for input field
		def clear_field_inputs(): 
			self.area_CO2_entry.delete(0, tk.END)
			self.area_CH4_entry.delete(0, tk.END)
			self.area_N2_entry_sample.delete(0, tk.END)
			self.area_N2_entry_atm.delete(0, tk.END)
			self.FDS_entry.delete(0, tk.END)
			self.FDS_entry_std.delete(0, tk.END)
			self.unc_FDS_entry.delete(0, tk.END)

			# self.nuCH4_sample_entry.delete(0, tk.END)
			# self.nuCH4_std_entry.delete(0, tk.END)
			# self.unc_nuCH4_entry.delete(0, tk.END)
			
		#### Make a clear-button for output field
		def clear_field_results():
			composition_CO2_display.delete(0, tk.END)
			composition_CH4_display.delete(0, tk.END)
			composition_N2_display.delete(0, tk.END)
			pressure.delete(0, tk.END)
			density.delete(0, tk.END)
			molarvolume.delete(0, tk.END)
			uncer_pressure.delete(0, tk.END)
			uncer_density.delete(0, tk.END)
			uncer_molarvolume.delete(0, tk.END)


		def calculCO2CH4N2():
			clear_field_results()
			area_CH4    	= float(self.area_CH4_entry.get())
			area_CO2        = float(self.area_CO2_entry.get())
			area_N2_sample  = float(self.area_N2_entry_sample.get())
			area_N2_atm  	= float(self.area_N2_entry_atm.get())
			FDS    			= float(self.FDS_entry.get())
			FDS_std    		= float(self.FDS_entry_std.get())
			unc_FDS       	= float(self.unc_FDS_entry.get())
			# nuCH4_sample 	= float(self.nuCH4_sample_entry.get())
			# nuCH4_std 		= float(self.nuCH4_std_entry.get())
			# unc_nuCH4 		= float(self.unc_nuCH4_entry.get())


			### Composition calculation

			if laser_wavelength.get() == 488:
				RRSCS_CO2 = 2.30
				RRSCS_CH4 = 7.80
			if laser_wavelength.get() == 514:
				RRSCS_CO2 = 2.29
				RRSCS_CH4 = 7.73
			if laser_wavelength.get() == 532:
				RRSCS_CO2 = 2.27
				RRSCS_CH4 = 7.69
			if laser_wavelength.get() == 633:
				RRSCS_CO2 = 2.20
				RRSCS_CH4 = 7.44
			if laser_wavelength.get() == 785:
				RRSCS_CO2 = 2.09
				RRSCS_CH4 = 7.05
			
			print('the wavelength of the selected laser is', laser_wavelength.get(), 'nm')
			print('RRSCS_CH4=', RRSCS_CH4)		
			print('RRSCS_C02=', RRSCS_CO2)
			         
			composition_CO2 = (area_CO2/RRSCS_CO2)/((area_CO2/RRSCS_CO2) + (area_CH4/RRSCS_CH4) +((area_N2_sample - area_N2_atm)/1))
			composition_CH4 = (area_CH4/RRSCS_CH4)/((area_CO2/RRSCS_CO2) + (area_CH4/RRSCS_CH4) +((area_N2_sample - area_N2_atm)/1))  # => coeff b in equation (8, article 2)
			composition_N2 	= 1 - composition_CO2 - composition_CH4   # => coeff a in equation (8, article 2)
									

			#### for the calculation of ternary mixtures. We performe the following steps:
			#### 1) calculation the P1 value from given composition and Fermi diad splittings using CO2CH4 calibration data (coeffs will be denoted with i)
			#### 2) calculation the P2 value from given composition and Fermi diad splittings using CO2N2 calibration data (coeffs will be denoted with j)
			#### 3) calucation the value P using equation 8 in article 2 (ref 2), then ultimate uncertainty 
			#### 4) repeat the step 2 if obtained P2 value < 150 bar, using, this time, calibration data for 5-150bars (for CO2N2 calibration)
			if temperature.get() == 22 and instrument.get() == 1 and composition_CO2 >= 0.5: 

				#coefficient of CO2CH4 calibration (i)
				composition_CO2_normalized_1_i = (composition_CO2 + 0.005 - 0.7932)/0.1749
				composition_CO2_normalized_2_i = (composition_CO2 - 0.005 - 0.7932)/0.1749
				FDS_normalized_1_i = (FDS + unc_FDS - 103.96)/0.7906
				FDS_normalized_2_i = (FDS - unc_FDS - 103.96)/0.7906
				
				p00_i= 112.44615
				p10_i= -82.57782
				p01_i= 113.28978
				p20_i= 38.5788
				p11_i= -206.51994
				p02_i= 187.13795
				p30_i= -23.37331
				p21_i= 96.30156
				p12_i= -191.33849
				p03_i= 125.1294
				p31_i= -16.90882
				p22_i= 51.29517
				p13_i= -59.93642
				p04_i= 10.40779


				d00_i= 0.524122882
				d10_i= -0.036729729
				d01_i= 0.395542204
				d20_i= -0.004702814
				d11_i= 0.005686733
				d02_i= -0.022846683
				d30_i= -0.002359074
				d21_i= -0.022675822
				d12_i= 0.05252559
				d03_i= -0.04411769
				d31_i= 0.001715852
				d22_i= -0.014560002
				d13_i= 0.019476762
				d04_i= -0.00332977

				#### pressure calculation using CO2CH4 calibration (i)

				pressure3_i = (p00_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**0 
				+ p10_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**0 
				+ p01_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**1 
				+ p20_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**0
				+ p11_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**1 
				+ p02_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**2 
				+ p30_i*composition_CO2_normalized_1_i**3*FDS_normalized_2_i**0 
				+ p21_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**1
				+ p12_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**2 
				+ p03_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**3 
				+ p31_i*composition_CO2_normalized_1_i**3*FDS_normalized_2_i**1 
				+ p22_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**2
				+ p13_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**3 
				+ p04_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**4)

				pressure4_i = (p00_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**0 
				+ p10_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**0 
				+ p01_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**1 
				+ p20_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**0
				+ p11_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**1 
				+ p02_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**2 
				+ p30_i*composition_CO2_normalized_2_i**3*FDS_normalized_1_i**0 
				+ p21_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**1
				+ p12_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**2 
				+ p03_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**3 
				+ p31_i*composition_CO2_normalized_2_i**3*FDS_normalized_1_i**1 
				+ p22_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**2
				+ p13_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**3 
				+ p04_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**4)

				########################
				#### density calculation  using CO2CH4 calibration (i)


				density3_i = (d00_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**0 
				+ d10_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**0 
				+ d01_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**1 
				+ d20_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**0
				+ d11_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**1 
				+ d02_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**2 
				+ d30_i*composition_CO2_normalized_1_i**3*FDS_normalized_2_i**0 
				+ d21_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**1
				+ d12_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**2 
				+ d03_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**3 
				+ d31_i*composition_CO2_normalized_1_i**3*FDS_normalized_2_i**1 
				+ d22_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**2
				+ d13_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**3 
				+ d04_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**4)

				density4_i = (d00_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**0 
				+ d10_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**0 
				+ d01_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**1 
				+ d20_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**0
				+ d11_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**1 
				+ d02_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**2 
				+ d30_i*composition_CO2_normalized_2_i**3*FDS_normalized_1_i**0 
				+ d21_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**1
				+ d12_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**2 
				+ d03_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**3 
				+ d31_i*composition_CO2_normalized_2_i**3*FDS_normalized_1_i**1 
				+ d22_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**2
				+ d13_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**3 
				+ d04_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**4)              

				pressure_final_i = (max(pressure3_i, pressure4_i) + min(pressure3_i, pressure4_i))/2 #pressure max + pressure min
				uncer_pressure_final_i = 7 + (max(pressure3_i, pressure4_i) - min(pressure3_i, pressure4_i))/(2*np.sqrt(3))

				density_final_i = (max(density3_i, density4_i) + min(density3_i, density4_i))/2 #density max - density min
				uncer_density_final_i = 0.0049 + (max(density3_i, density4_i) - min(density3_i, density4_i))/(2*np.sqrt(3))

				molarvolume3_i = 1/(max(density3_i, density4_i)/(44*composition_CO2 + 16*composition_CH4 + 28*composition_N2))
				molarvolume4_i = 1/(min(density3_i, density4_i)/(44*composition_CO2 + 16*composition_CH4 + 28*composition_N2))
				molarvolume_final_i = (molarvolume3_i + molarvolume4_i) / 2
				uncer_molarvolume_final_i = (molarvolume4_i - molarvolume3_i) / (2*np.sqrt(3))


				##### verify if measured pressure < 160 bar, if it is, re-recalculte using calibration data for 5-160 bar range.
				if pressure_final_i <= 150: 

					## Calibration equation's coeff of CO2-CH4 at 22 °C over 5-160 bars
					# normalisation of concentration and of Fermi diad splitting
					
					#coefficient of CO2CH4 calibration (i)
					composition_CO2_normalized_1_i = (composition_CO2 + 0.005 - 0.79945)/0.17644
					composition_CO2_normalized_2_i = (composition_CO2 - 0.005 - 0.79945)/0.17644
					FDS_normalized_1_i = (FDS + unc_FDS - 103.56)/0.70116
					FDS_normalized_2_i = (FDS - unc_FDS - 103.56)/0.70116
					
					p00_i= 87.52544861
					p10_i= -30.42158037
					p01_i= 29.11761641
					p20_i= 10.2290838
					p11_i= -52.60520058
					p02_i= -0.386784979
					p30_i= -2.196596934
					p21_i= 19.13204933
					p12_i= -49.83271376
					p03_i= 48.71006525
					p31_i= 0.679709634
					p22_i= 8.522626745
					p13_i= -27.53323027
					p04_i= 11.20465971


					d00_i= 0.317754589
					d10_i= -0.035146968
					d01_i= 0.334450048
					d20_i= -0.002058162
					d11_i= -0.042889058
					d02_i= 0.051564624
					d30_i= -0.004308855
					d21_i= -0.012647331
					d12_i= 0.022054788
					d03_i= -0.015355587
					d31_i= 0.001474274
					d22_i= -0.013021138
					d13_i= 0.023397147
					d04_i= -0.014013084

					#### pressure calculation using CO2CH4 calibration (i)

					pressure3_i = (p00_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**0 
					+ p10_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**0 
					+ p01_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**1 
					+ p20_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**0
					+ p11_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**1 
					+ p02_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**2 
					+ p30_i*composition_CO2_normalized_1_i**3*FDS_normalized_2_i**0 
					+ p21_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**1
					+ p12_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**2 
					+ p03_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**3 
					+ p31_i*composition_CO2_normalized_1_i**3*FDS_normalized_2_i**1 
					+ p22_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**2
					+ p13_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**3 
					+ p04_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**4)

					pressure4_i = (p00_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**0 
					+ p10_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**0 
					+ p01_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**1 
					+ p20_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**0
					+ p11_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**1 
					+ p02_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**2 
					+ p30_i*composition_CO2_normalized_2_i**3*FDS_normalized_1_i**0 
					+ p21_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**1
					+ p12_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**2 
					+ p03_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**3 
					+ p31_i*composition_CO2_normalized_2_i**3*FDS_normalized_1_i**1 
					+ p22_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**2
					+ p13_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**3 
					+ p04_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**4)

					########################
					#### density calculation  using CO2CH4 calibration (i)


					density3_i = (d00_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**0 
					+ d10_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**0 
					+ d01_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**1 
					+ d20_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**0
					+ d11_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**1 
					+ d02_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**2 
					+ d30_i*composition_CO2_normalized_1_i**3*FDS_normalized_2_i**0 
					+ d21_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**1
					+ d12_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**2 
					+ d03_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**3 
					+ d31_i*composition_CO2_normalized_1_i**3*FDS_normalized_2_i**1 
					+ d22_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**2
					+ d13_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**3 
					+ d04_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**4)

					density4_i = (d00_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**0 
					+ d10_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**0 
					+ d01_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**1 
					+ d20_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**0
					+ d11_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**1 
					+ d02_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**2 
					+ d30_i*composition_CO2_normalized_2_i**3*FDS_normalized_1_i**0 
					+ d21_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**1
					+ d12_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**2 
					+ d03_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**3 
					+ d31_i*composition_CO2_normalized_2_i**3*FDS_normalized_1_i**1 
					+ d22_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**2
					+ d13_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**3 
					+ d04_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**4)              

					pressure_final_i = (max(pressure3_i, pressure4_i) + min(pressure3_i, pressure4_i))/2 #pressure max + pressure min
					uncer_pressure_final_i = 3 + (max(pressure3_i, pressure4_i) - min(pressure3_i, pressure4_i))/(2*np.sqrt(3))

					density_final_i = (max(density3_i, density4_i) + min(density3_i, density4_i))/2 #density max - density min
					uncer_density_final_i = 0.0049 + (max(density3_i, density4_i) - min(density3_i, density4_i))/(2*np.sqrt(3))

					molarvolume3_i = 1/(max(density3_i, density4_i)/(44*composition_CO2 + 16*composition_CH4 + 28*composition_N2))
					molarvolume4_i = 1/(min(density3_i, density4_i)/(44*composition_CO2 + 16*composition_CH4 + 28*composition_N2))
					molarvolume_final_i = (molarvolume3_i + molarvolume4_i) / 2
					uncer_molarvolume_final_i = (molarvolume4_i - molarvolume3_i) / (2*np.sqrt(3))

			
				print('pressure3_i', pressure3_i)
				print('pressure4_i', pressure4_i)
				print('density 3_i=', density3_i)
				print('density 4_i=', density4_i)
				print("molarvolume3_i", molarvolume3_i)
				print("molarvolume4_i", molarvolume4_i)	
				

				#################################
				#coefficient of CO2 N2 calibration (j)
				############################"""
				composition_CO2_normalized_1_j = (composition_CO2 + 0.005 - 0.76444)/0.17554
				composition_CO2_normalized_2_j = (composition_CO2 - 0.005 - 0.76444)/0.17554
				FDS_normalized_1_j = (FDS + unc_FDS - 103.82)/0.79435
				FDS_normalized_2_j = (FDS - unc_FDS - 103.82)/0.79435
				
				p00_j= 132.737333
				p10_j= -97.87543837
				p01_j= 118.8159698
				p20_j= 52.48193614
				p11_j= -214.9144587
				p02_j= 156.1857227
				p30_j= -23.2742455
				p21_j= 101.6493196
				p12_j= -182.0409482
				p03_j= 122.9468574
				p31_j= -18.8741818
				p22_j= 48.57346341
				p13_j= -55.41887799
				p04_j= 11.58755259

				d00_j= 0.506428629
				d10_j= -0.08233871
				d01_j= 0.419517371
				d20_j= 0.01221691
				d11_j= -0.03625585
				d02_j= -0.006580948
				d30_j= -0.003308056
				d21_j= -0.007634737
				d12_j= 0.045147691
				d03_j= -0.036154129
				d31_j= 0.002204595
				d22_j= -0.01695751
				d13_j= 0.015373196
				d04_j= -0.003243828

				#### pressure calculation using CO2CH4 calibration (j)

				pressure3_j = (p00_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**0 
				+ p10_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**0 
				+ p01_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**1 
				+ p20_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**0
				+ p11_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**1 
				+ p02_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**2 
				+ p30_j*composition_CO2_normalized_1_j**3*FDS_normalized_2_j**0 
				+ p21_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**1
				+ p12_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**2 
				+ p03_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**3 
				+ p31_j*composition_CO2_normalized_1_j**3*FDS_normalized_2_j**1 
				+ p22_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**2
				+ p13_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**3 
				+ p04_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**4)

				pressure4_j = (p00_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**0 
				+ p10_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**0 
				+ p01_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**1 
				+ p20_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**0
				+ p11_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**1 
				+ p02_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**2 
				+ p30_j*composition_CO2_normalized_2_j**3*FDS_normalized_1_j**0 
				+ p21_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**1
				+ p12_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**2 
				+ p03_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**3 
				+ p31_j*composition_CO2_normalized_2_j**3*FDS_normalized_1_j**1 
				+ p22_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**2
				+ p13_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**3 
				+ p04_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**4)

				########################
				#### density calculation  using CO2CH4 calibration (i)


				density3_j = (d00_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**0 
				+ d10_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**0 
				+ d01_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**1 
				+ d20_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**0
				+ d11_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**1 
				+ d02_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**2 
				+ d30_j*composition_CO2_normalized_1_j**3*FDS_normalized_2_j**0 
				+ d21_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**1
				+ d12_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**2 
				+ d03_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**3 
				+ d31_j*composition_CO2_normalized_1_j**3*FDS_normalized_2_j**1 
				+ d22_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**2
				+ d13_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**3 
				+ d04_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**4)

				density4_j = (d00_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**0 
				+ d10_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**0 
				+ d01_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**1 
				+ d20_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**0
				+ d11_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**1 
				+ d02_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**2 
				+ d30_j*composition_CO2_normalized_2_j**3*FDS_normalized_1_j**0 
				+ d21_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**1
				+ d12_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**2 
				+ d03_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**3 
				+ d31_j*composition_CO2_normalized_2_j**3*FDS_normalized_1_j**1 
				+ d22_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**2
				+ d13_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**3 
				+ d04_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**4)              

				pressure_final_j = (max(pressure3_j, pressure4_j) + min(pressure3_j, pressure4_j))/2 #pressure max + pressure min
				uncer_pressure_final_j = 7 + (max(pressure3_j, pressure4_j) - min(pressure3_j, pressure4_j))/(2*np.sqrt(3))

				density_final_j = (max(density3_j, density4_j) + min(density3_j, density4_j))/2 #density max - density min
				uncer_density_final_j = 0.0042 + (max(density3_j, density4_j) - min(density3_j, density4_j))/(2*np.sqrt(3))

				molarvolume3_j = 1/(max(density3_j, density4_j)/(44*composition_CO2 + 16*composition_CH4 + 28*composition_N2))
				molarvolume4_j = 1/(min(density3_j, density4_j)/(44*composition_CO2 + 16*composition_CH4 + 28*composition_N2))
				molarvolume_final_j = (molarvolume3_j + molarvolume4_j) / 2
				uncer_molarvolume_final_j = (molarvolume4_j - molarvolume3_j) / (2*np.sqrt(3))


				##### verify if measured pressure < 160 bar, if it is, re-recalculte using calibration data for 5-160 bar range.
				if pressure_final_j <= 150: 

					## Calibration equation's coeff of CO2-CH4 at 22 °C over 5-160 bars
					# normalisation of concentration and of Fermi diad splitting
					
					#coefficient of CO2CH4 calibration (j)
					composition_CO2_normalized_1_j = (composition_CO2 + 0.005 - 0.77632)/0.18027
					composition_CO2_normalized_2_j = (composition_CO2 - 0.005 - 0.77632)/0.18027
					FDS_normalized_1_j = (FDS + unc_FDS - 103.4)/0.69548
					FDS_normalized_2_j = (FDS - unc_FDS - 103.4)/0.69548
					
					p00_j= 96.04521259
					p10_j= -37.64345175
					p01_j= 59.6284227
					p20_j= 13.03677947
					p11_j= -61.06487393
					p02_j= -19.9683198
					p30_j= -4.75652517
					p21_j= 23.80817957
					p12_j= -37.44444918
					p03_j= 32.33006119
					p31_j= -3.837992187
					p22_j= 8.303532695
					p13_j= -16.87991622
					p04_j= 9.516399693

					d00_j= 0.291506042
					d10_j= -0.04488858
					d01_j= 0.345009126
					d20_j= 0.003754508
					d11_j=-0.050522777
					d02_j= 0.024506871
					d30_j= -0.013553702
					d21_j= 0.002377929
					d12_j= 0.02365643
					d03_j= -0.027150512
					d31_j=-0.014003719
					d22_j= -0.006231591
					d13_j= 0.031093488
					d04_j= -0.008939409

					#### pressure calculation using CO2CH4 calibration (j)

					pressure3_j = (p00_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**0 
					+ p10_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**0 
					+ p01_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**1 
					+ p20_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**0
					+ p11_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**1 
					+ p02_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**2 
					+ p30_j*composition_CO2_normalized_1_j**3*FDS_normalized_2_j**0 
					+ p21_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**1
					+ p12_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**2 
					+ p03_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**3 
					+ p31_j*composition_CO2_normalized_1_j**3*FDS_normalized_2_j**1 
					+ p22_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**2
					+ p13_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**3 
					+ p04_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**4)

					pressure4_j = (p00_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**0 
					+ p10_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**0 
					+ p01_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**1 
					+ p20_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**0
					+ p11_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**1 
					+ p02_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**2 
					+ p30_j*composition_CO2_normalized_2_j**3*FDS_normalized_1_j**0 
					+ p21_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**1
					+ p12_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**2 
					+ p03_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**3 
					+ p31_j*composition_CO2_normalized_2_j**3*FDS_normalized_1_j**1 
					+ p22_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**2
					+ p13_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**3 
					+ p04_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**4)

					########################
					#### density calculation  using CO2CH4 calibration (i)


					density3_j = (d00_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**0 
					+ d10_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**0 
					+ d01_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**1 
					+ d20_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**0
					+ d11_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**1 
					+ d02_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**2 
					+ d30_j*composition_CO2_normalized_1_j**3*FDS_normalized_2_j**0 
					+ d21_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**1
					+ d12_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**2 
					+ d03_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**3 
					+ d31_j*composition_CO2_normalized_1_j**3*FDS_normalized_2_j**1 
					+ d22_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**2
					+ d13_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**3 
					+ d04_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**4)

					density4_j = (d00_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**0 
					+ d10_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**0 
					+ d01_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**1 
					+ d20_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**0
					+ d11_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**1 
					+ d02_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**2 
					+ d30_j*composition_CO2_normalized_2_j**3*FDS_normalized_1_j**0 
					+ d21_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**1
					+ d12_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**2 
					+ d03_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**3 
					+ d31_j*composition_CO2_normalized_2_j**3*FDS_normalized_1_j**1 
					+ d22_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**2
					+ d13_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**3 
					+ d04_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**4)              

					pressure_final_j = (max(pressure3_j, pressure4_j) + min(pressure3_j, pressure4_j))/2 #pressure max + pressure min
					uncer_pressure_final_j = 3 + (max(pressure3_j, pressure4_j) - min(pressure3_j, pressure4_j))/(2*np.sqrt(3))

					density_final_j = (max(density3_j, density4_j) + min(density3_j, density4_j))/2 #density max - density min
					uncer_density_final_j = 0.003 + (max(density3_j, density4_j) - min(density3_j, density4_j))/(2*np.sqrt(3))

					molarvolume3_j = 1/(max(density3_j, density4_j)/(44*composition_CO2 + 16*composition_CH4 + 28*composition_N2))
					molarvolume4_j = 1/(min(density3_j, density4_j)/(44*composition_CO2 + 16*composition_CH4 + 28*composition_N2))
					molarvolume_final_j = (molarvolume3_j + molarvolume4_j) / 2
					uncer_molarvolume_final_j = (molarvolume4_j - molarvolume3_j) / (2*np.sqrt(3))



			
				print('pressure3_j', pressure3_j)
				print('pressure4_j', pressure4_j)
				print('density 3_j=', density3_j)
				print('density 4_j=', density4_j)
				print("molarvolume3_j", molarvolume3_j)
				print("molarvolume4_j", molarvolume4_j)	
				if pressure_final_i > 650 or pressure3_i >650 or pressure4_i >650 or pressure_final_i < -20 or pressure3_i <-20 or pressure4_i <-20 or pressure_final_j > 650 or pressure3_j >650 or pressure4_j >650 or pressure_final_j < -20 or pressure3_j <-20 or pressure4_j <-20 or density3_i<0 or density4_i <0 or density3_j<0 or density4_j<0 or density_final_i<0 or density_final_j<0  :
					popupmsg_OCR()


				############ Calculation final pressure, density from pressure final i and j, depending on the concentration of CH4, N2 (coeff, a b within equation 8))
				############ and calculation uncertainty of FINAL RESULTS
				pressure_final = (composition_N2*pressure_final_j + composition_CH4*pressure_final_i)/(composition_N2 + composition_CH4) ## Equation 8 in the reference 2
				uncer_pressure_final = np.sqrt((composition_N2/(composition_N2+composition_CH4))**2*(uncer_pressure_final_j)**2 + (composition_CH4/(composition_N2+composition_CH4))**2*(uncer_pressure_final_i)**2)  ## base on the formule of the calulation of final_pressure above
				
				density_final = (composition_N2*density_final_j + composition_CH4*density_final_i)/(composition_N2 + composition_CH4) ## Equation 8 in the reference 2
				uncer_density_final = np.sqrt((composition_N2/(composition_N2+composition_CH4))**2*(uncer_density_final_j)**2 + (composition_CH4/(composition_N2+composition_CH4))**2*(uncer_density_final_i)**2)  ## base on the formule of the calulation of final_pressure above

				molarvolume_final = (composition_N2*molarvolume_final_j + composition_CH4*molarvolume_final_i)/(composition_N2 + composition_CH4)
				uncer_molarvolume_final = (uncer_molarvolume_final_j + uncer_molarvolume_final_i)/2

########################
########################

			if temperature.get() == 22 and instrument.get() == 1 and composition_CO2 < 0.5: 

				#coefficient of CO2CH4 calibration (i)
				composition_CO2_normalized_1_i = (composition_CO2 + 0.005 - 0.302)/0.1414
				composition_CO2_normalized_2_i = (composition_CO2 - 0.005 - 0.302)/0.1414
				FDS_normalized_1_i = (FDS + unc_FDS - 103.13)/0.32761
				FDS_normalized_2_i = (FDS - unc_FDS - 103.13)/0.32761
				
				p00_i= 156.68022
				p10_i= -75.86492
				p01_i= 143.43081
				p20_i= 64.99618
				p11_i= -130.8664
				p02_i= 57.11613
				p30_i= -30.39489
				p21_i= 100.57864
				p12_i= -104.91941
				p03_i= 48.32697
				p31_i= -36.6262
				p22_i= 43.15493
				p13_i= -25.19951
				p04_i= 1.41357


				d00_i= 0.23665
				d10_i= -0.05817
				d01_i= 0.21604
				d20_i= 0.00723
				d11_i= -0.02177
				d02_i= -0.00877
				d30_i= 0.00166
				d21_i= -0.01714
				d12_i= 0.03703
				d03_i= -0.01353
				d31_i= 0.00324
				d22_i= -0.01689
				d13_i= 0.00846
				d04_i= -0.000819

				#### pressure calculation using CO2CH4 calibration (i)

				pressure3_i = (p00_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**0 
				+ p10_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**0 
				+ p01_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**1 
				+ p20_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**0
				+ p11_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**1 
				+ p02_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**2 
				+ p30_i*composition_CO2_normalized_1_i**3*FDS_normalized_2_i**0 
				+ p21_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**1
				+ p12_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**2 
				+ p03_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**3 
				+ p31_i*composition_CO2_normalized_1_i**3*FDS_normalized_2_i**1 
				+ p22_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**2
				+ p13_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**3 
				+ p04_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**4)

				pressure4_i = (p00_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**0 
				+ p10_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**0 
				+ p01_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**1 
				+ p20_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**0
				+ p11_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**1 
				+ p02_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**2 
				+ p30_i*composition_CO2_normalized_2_i**3*FDS_normalized_1_i**0 
				+ p21_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**1
				+ p12_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**2 
				+ p03_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**3 
				+ p31_i*composition_CO2_normalized_2_i**3*FDS_normalized_1_i**1 
				+ p22_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**2
				+ p13_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**3 
				+ p04_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**4)

				########################
				#### density calculation  using CO2CH4 calibration (i)


				density3_i = (d00_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**0 
				+ d10_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**0 
				+ d01_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**1 
				+ d20_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**0
				+ d11_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**1 
				+ d02_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**2 
				+ d30_i*composition_CO2_normalized_1_i**3*FDS_normalized_2_i**0 
				+ d21_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**1
				+ d12_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**2 
				+ d03_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**3 
				+ d31_i*composition_CO2_normalized_1_i**3*FDS_normalized_2_i**1 
				+ d22_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**2
				+ d13_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**3 
				+ d04_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**4)

				density4_i = (d00_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**0 
				+ d10_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**0 
				+ d01_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**1 
				+ d20_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**0
				+ d11_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**1 
				+ d02_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**2 
				+ d30_i*composition_CO2_normalized_2_i**3*FDS_normalized_1_i**0 
				+ d21_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**1
				+ d12_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**2 
				+ d03_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**3 
				+ d31_i*composition_CO2_normalized_2_i**3*FDS_normalized_1_i**1 
				+ d22_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**2
				+ d13_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**3 
				+ d04_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**4)              

				pressure_final_i = (max(pressure3_i, pressure4_i) + min(pressure3_i, pressure4_i))/2 #pressure max + pressure min
				uncer_pressure_final_i = 11 + (max(pressure3_i, pressure4_i) - min(pressure3_i, pressure4_i))/(2*np.sqrt(3))

				density_final_i = (max(density3_i, density4_i) + min(density3_i, density4_i))/2 #density max - density min
				uncer_density_final_i = 0.0049 + (max(density3_i, density4_i) - min(density3_i, density4_i))/(2*np.sqrt(3))

				molarvolume3_i = 1/(max(density3_i, density4_i)/(44*composition_CO2 + 16*composition_CH4 + 28*composition_N2))
				molarvolume4_i = 1/(min(density3_i, density4_i)/(44*composition_CO2 + 16*composition_CH4 + 28*composition_N2))
				molarvolume_final_i = (molarvolume3_i + molarvolume4_i) / 2
				uncer_molarvolume_final_i = (molarvolume4_i - molarvolume3_i) / (2*np.sqrt(3))



				##### verify if measured pressure < 160 bar, if it is, re-recalculte using calibration data for 5-160 bar range.
				if pressure_final_i <= 150: 

					## Calibration equation's coeff of CO2-CH4 at 22 °C over 5-160 bars
					# normalisation of concentration and of Fermi diad splitting
					
					#coefficient of CO2CH4 calibration (i)
					composition_CO2_normalized_1_i = (composition_CO2 + 0.005 -  0.302)/0.14191
					composition_CO2_normalized_2_i = (composition_CO2 - 0.005 - 0.302)/0.14191
					FDS_normalized_1_i = (FDS + unc_FDS - 102.92)/0.14693
					FDS_normalized_2_i = (FDS - unc_FDS - 102.92)/0.14693
					
					
					p00_i= 78.18921
					p10_i= -34.86334
					p01_i= 59.61547
					p20_i= 19.49752
					p11_i= -20.56441
					p02_i= -6.3739
					p30_i= -5.31241
					p21_i= 10.83197
					p12_i= 5.8996
					p03_i= 0.95159
					p31_i= -5.69768
					p22_i= -3.76814
					p13_i= -0.15086
					p04_i= 0.07775


					d00_i= 0.09868
					d10_i= -0.02885
					d01_i= 0.09325
					d20_i= 0.01655
					d11_i= -0.01878
					d02_i= 0.00371
					d30_i= -0.00446
					d21_i= 0.00736
					d12_i= 0.00506
					d03_i= -0.0029
					d31_i= -0.00605
					d22_i= -0.00532
					d13_i= 0.00284
					d04_i= -1.62E-04

					#### pressure calculation using CO2CH4 calibration (i)

					pressure3_i = (p00_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**0 
					+ p10_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**0 
					+ p01_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**1 
					+ p20_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**0
					+ p11_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**1 
					+ p02_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**2 
					+ p30_i*composition_CO2_normalized_1_i**3*FDS_normalized_2_i**0 
					+ p21_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**1
					+ p12_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**2 
					+ p03_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**3 
					+ p31_i*composition_CO2_normalized_1_i**3*FDS_normalized_2_i**1 
					+ p22_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**2
					+ p13_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**3 
					+ p04_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**4)

					pressure4_i = (p00_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**0 
					+ p10_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**0 
					+ p01_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**1 
					+ p20_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**0
					+ p11_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**1 
					+ p02_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**2 
					+ p30_i*composition_CO2_normalized_2_i**3*FDS_normalized_1_i**0 
					+ p21_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**1
					+ p12_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**2 
					+ p03_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**3 
					+ p31_i*composition_CO2_normalized_2_i**3*FDS_normalized_1_i**1 
					+ p22_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**2
					+ p13_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**3 
					+ p04_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**4)

					########################
					#### density calculation  using CO2CH4 calibration (i)


					density3_i = (d00_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**0 
					+ d10_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**0 
					+ d01_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**1 
					+ d20_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**0
					+ d11_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**1 
					+ d02_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**2 
					+ d30_i*composition_CO2_normalized_1_i**3*FDS_normalized_2_i**0 
					+ d21_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**1
					+ d12_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**2 
					+ d03_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**3 
					+ d31_i*composition_CO2_normalized_1_i**3*FDS_normalized_2_i**1 
					+ d22_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**2
					+ d13_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**3 
					+ d04_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**4)

					density4_i = (d00_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**0 
					+ d10_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**0 
					+ d01_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**1 
					+ d20_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**0
					+ d11_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**1 
					+ d02_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**2 
					+ d30_i*composition_CO2_normalized_2_i**3*FDS_normalized_1_i**0 
					+ d21_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**1
					+ d12_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**2 
					+ d03_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**3 
					+ d31_i*composition_CO2_normalized_2_i**3*FDS_normalized_1_i**1 
					+ d22_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**2
					+ d13_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**3 
					+ d04_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**4)              

					pressure_final_i = (max(pressure3_i, pressure4_i) + min(pressure3_i, pressure4_i))/2 #pressure max + pressure min
					uncer_pressure_final_i = 7 + (max(pressure3_i, pressure4_i) - min(pressure3_i, pressure4_i))/(2*np.sqrt(3))

					density_final_i = (max(density3_i, density4_i) + min(density3_i, density4_i))/2 #density max - density min
					uncer_density_final_i = 0.0049 + (max(density3_i, density4_i) - min(density3_i, density4_i))/(2*np.sqrt(3))

					molarvolume3_i = 1/(max(density3_i, density4_i)/(44*composition_CO2 + 16*composition_CH4 + 28*composition_N2))
					molarvolume4_i = 1/(min(density3_i, density4_i)/(44*composition_CO2 + 16*composition_CH4 + 28*composition_N2))
					molarvolume_final_i = (molarvolume3_i + molarvolume4_i) / 2
					uncer_molarvolume_final_i = (molarvolume4_i - molarvolume3_i) / (2*np.sqrt(3))


			
				print('pressure3_i', pressure3_i)
				print('pressure4_i', pressure4_i)
				print('density 3_i=', density3_i)
				print('density 4_i=', density4_i)
				print("molarvolume3_i", molarvolume3_i)
				print("molarvolume4_i", molarvolume4_i)	
				

				#################################
				#coefficient of CO2 N2 calibration (j)
				############################"""
				composition_CO2_normalized_1_j = (composition_CO2 + 0.005 - 0.3)/0.14207
				composition_CO2_normalized_2_j = (composition_CO2 - 0.005 - 0.3)/0.14207
				FDS_normalized_1_j = (FDS + unc_FDS - 103.08)/0.28273
				FDS_normalized_2_j = (FDS - unc_FDS - 103.08)/0.28273
				
				
				p00_j= 170.1797482
				p10_j= -77.91652847
				p01_j= 157.7783087
				p20_j= 48.92637063
				p11_j= -117.851987
				p02_j= 37.8190835
				p30_j= -19.71210412
				p21_j= 73.33809699
				p12_j= -65.0383275
				p03_j= 26.66123598
				p31_j= -19.51088658
				p22_j= 26.97497354
				p13_j= -14.74772823
				p04_j= 1.319488384
				
				d00_j= 0.263683349
				d10_j= -0.077937841
				d01_j= 0.235224651
				d20_j= 0.021982476
				d11_j= -0.053772169
				d02_j= 9.08244E-05
				d30_j=-0.001022048
				d21_j= 0.009510245
				d12_j= 0.02069519
				d03_j= -0.006329513
				d31_j= 0.002925762
				d22_j= -0.010441952
				d13_j= 0.001629727
				d04_j= 0.0000253044

				#### pressure calculation using CO2CH4 calibration (j)

				pressure3_j = (p00_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**0 
				+ p10_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**0 
				+ p01_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**1 
				+ p20_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**0
				+ p11_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**1 
				+ p02_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**2 
				+ p30_j*composition_CO2_normalized_1_j**3*FDS_normalized_2_j**0 
				+ p21_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**1
				+ p12_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**2 
				+ p03_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**3 
				+ p31_j*composition_CO2_normalized_1_j**3*FDS_normalized_2_j**1 
				+ p22_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**2
				+ p13_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**3 
				+ p04_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**4)

				pressure4_j = (p00_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**0 
				+ p10_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**0 
				+ p01_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**1 
				+ p20_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**0
				+ p11_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**1 
				+ p02_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**2 
				+ p30_j*composition_CO2_normalized_2_j**3*FDS_normalized_1_j**0 
				+ p21_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**1
				+ p12_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**2 
				+ p03_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**3 
				+ p31_j*composition_CO2_normalized_2_j**3*FDS_normalized_1_j**1 
				+ p22_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**2
				+ p13_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**3 
				+ p04_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**4)

				########################
				#### density calculation  using CO2CH4 calibration (i)


				density3_j = (d00_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**0 
				+ d10_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**0 
				+ d01_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**1 
				+ d20_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**0
				+ d11_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**1 
				+ d02_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**2 
				+ d30_j*composition_CO2_normalized_1_j**3*FDS_normalized_2_j**0 
				+ d21_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**1
				+ d12_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**2 
				+ d03_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**3 
				+ d31_j*composition_CO2_normalized_1_j**3*FDS_normalized_2_j**1 
				+ d22_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**2
				+ d13_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**3 
				+ d04_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**4)

				density4_j = (d00_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**0 
				+ d10_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**0 
				+ d01_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**1 
				+ d20_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**0
				+ d11_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**1 
				+ d02_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**2 
				+ d30_j*composition_CO2_normalized_2_j**3*FDS_normalized_1_j**0 
				+ d21_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**1
				+ d12_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**2 
				+ d03_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**3 
				+ d31_j*composition_CO2_normalized_2_j**3*FDS_normalized_1_j**1 
				+ d22_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**2
				+ d13_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**3 
				+ d04_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**4)              

				pressure_final_j = (max(pressure3_j, pressure4_j) + min(pressure3_j, pressure4_j))/2 #pressure max + pressure min
				uncer_pressure_final_j = 7 + (max(pressure3_j, pressure4_j) - min(pressure3_j, pressure4_j))/(2*np.sqrt(3))

				density_final_j = (max(density3_j, density4_j) + min(density3_j, density4_j))/2 #density max - density min
				uncer_density_final_j = 0.0049 + (max(density3_j, density4_j) - min(density3_j, density4_j))/(2*np.sqrt(3))

				molarvolume3_j = 1/(max(density3_j, density4_j)/(44*composition_CO2 + 16*composition_CH4 + 28*composition_N2))
				molarvolume4_j = 1/(min(density3_j, density4_j)/(44*composition_CO2 + 16*composition_CH4 + 28*composition_N2))
				molarvolume_final_j = (molarvolume3_j + molarvolume4_j) / 2
				uncer_molarvolume_final_j = (molarvolume4_j - molarvolume3_j) / (2*np.sqrt(3))



				##### verify if measured pressure < 160 bar, if it is, re-recalculte using calibration data for 5-160 bar range.
				if pressure_final_j <= 150: 

					## Calibration equation's coeff of CO2-CH4 at 22 °C over 5-160 bars
					# normalisation of concentration and of Fermi diad splitting
					
					#coefficient of CO2CH4 calibration (j)
					composition_CO2_normalized_1_j = (composition_CO2 + 0.005 - 0.30339)/0.14138
					composition_CO2_normalized_2_j = (composition_CO2 - 0.005 - 0.30339)/0.14138
					FDS_normalized_1_j = (FDS + unc_FDS - 102.88)/0.10219
					FDS_normalized_2_j = (FDS - unc_FDS - 102.88)/0.10219
					
					p00_j= 70.4346
					p10_j= -26.55884
					p01_j= 49.81154
					p20_j= 11.3654
					p11_j= -23.07226
					p02_j= -2.14405
					p30_j= -4.37936
					p21_j= 12.94687
					p12_j= -2.63117
					p03_j= 2.28548
					p31_j= -3.46204
					p22_j= 2.30673
					p13_j= -1.50217
					p04_j= -0.01577

					d00_j= 0.102872156
					d10_j= -0.02999631
					d01_j= 0.078010885
					d20_j= 0.010556929
					d11_j= -0.024748763
					d02_j= -0.000407494
					d30_j= -0.003873141
					d21_j= 0.012345104
					d12_j= -0.001058896
					d03_j= 0.002185839
					d31_j= -0.002665506
					d22_j= 0.002099481
					d13_j= -0.001615525
					d04_j= -0.0000273713

					#### pressure calculation using CO2CH4 calibration (j)

					pressure3_j = (p00_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**0 
					+ p10_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**0 
					+ p01_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**1 
					+ p20_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**0
					+ p11_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**1 
					+ p02_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**2 
					+ p30_j*composition_CO2_normalized_1_j**3*FDS_normalized_2_j**0 
					+ p21_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**1
					+ p12_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**2 
					+ p03_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**3 
					+ p31_j*composition_CO2_normalized_1_j**3*FDS_normalized_2_j**1 
					+ p22_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**2
					+ p13_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**3 
					+ p04_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**4)

					pressure4_j = (p00_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**0 
					+ p10_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**0 
					+ p01_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**1 
					+ p20_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**0
					+ p11_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**1 
					+ p02_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**2 
					+ p30_j*composition_CO2_normalized_2_j**3*FDS_normalized_1_j**0 
					+ p21_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**1
					+ p12_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**2 
					+ p03_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**3 
					+ p31_j*composition_CO2_normalized_2_j**3*FDS_normalized_1_j**1 
					+ p22_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**2
					+ p13_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**3 
					+ p04_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**4)

					########################
					#### density calculation  using CO2CH4 calibration (i)


					density3_j = (d00_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**0 
					+ d10_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**0 
					+ d01_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**1 
					+ d20_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**0
					+ d11_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**1 
					+ d02_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**2 
					+ d30_j*composition_CO2_normalized_1_j**3*FDS_normalized_2_j**0 
					+ d21_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**1
					+ d12_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**2 
					+ d03_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**3 
					+ d31_j*composition_CO2_normalized_1_j**3*FDS_normalized_2_j**1 
					+ d22_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**2
					+ d13_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**3 
					+ d04_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**4)

					density4_j = (d00_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**0 
					+ d10_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**0 
					+ d01_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**1 
					+ d20_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**0
					+ d11_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**1 
					+ d02_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**2 
					+ d30_j*composition_CO2_normalized_2_j**3*FDS_normalized_1_j**0 
					+ d21_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**1
					+ d12_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**2 
					+ d03_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**3 
					+ d31_j*composition_CO2_normalized_2_j**3*FDS_normalized_1_j**1 
					+ d22_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**2
					+ d13_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**3 
					+ d04_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**4)              

					pressure_final_j = (max(pressure3_j, pressure4_j) + min(pressure3_j, pressure4_j))/2 #pressure max + pressure min
					uncer_pressure_final_j = 3 + (max(pressure3_j, pressure4_j) - min(pressure3_j, pressure4_j))/(2*np.sqrt(3))

					density_final_j = (max(density3_j, density4_j) + min(density3_j, density4_j))/2 #density max - density min
					uncer_density_final_j = 0.004 + (max(density3_j, density4_j) - min(density3_j, density4_j))/(2*np.sqrt(3))

					molarvolume3_j = 1/(max(density3_j, density4_j)/(44*composition_CO2 + 16*composition_CH4 + 28*composition_N2))
					molarvolume4_j = 1/(min(density3_j, density4_j)/(44*composition_CO2 + 16*composition_CH4 + 28*composition_N2))
					molarvolume_final_j = (molarvolume3_j + molarvolume4_j) / 2
					uncer_molarvolume_final_j = (molarvolume4_j - molarvolume3_j) / (2*np.sqrt(3))


			
				print('pressure3_j', pressure3_j)
				print('pressure4_j', pressure4_j)
				print('density 3_j=', density3_j)
				print('density 4_j=', density4_j)
				print("molarvolume3_i", molarvolume3_j)
				print("molarvolume4_i", molarvolume4_j)	
				if pressure_final_i > 650 or pressure3_i >650 or pressure4_i >650 or pressure_final_i < -20 or pressure3_i <-20 or pressure4_i <-20 or pressure_final_j > 650 or pressure3_j >650 or pressure4_j >650 or pressure_final_j < -20 or pressure3_j <-20 or pressure4_j <-20 or density3_i<0 or density4_i <0 or density3_j<0 or density4_j<0 or density_final_i<0 or density_final_j<0 :
					popupmsg_OCR()


				############ Calculation final pressure, density from pressure final i and j, depending on the concentration of CH4, N2 (coeff, a b within equation 8))
				############ and calculation uncertainty of FINAL RESULTS
				pressure_final = (composition_N2*pressure_final_j + composition_CH4*pressure_final_i)/(composition_N2 + composition_CH4) ## Equation 8 in the reference 2
				uncer_pressure_final = np.sqrt((composition_N2/(composition_N2+composition_CH4))**2*(uncer_pressure_final_j)**2 + (composition_CH4/(composition_N2+composition_CH4))**2*(uncer_pressure_final_i)**2)  ## base on the formule of the calulation of final_pressure above
				
				density_final = (composition_N2*density_final_j + composition_CH4*density_final_i)/(composition_N2 + composition_CH4) ## Equation 8 in the reference 2
				uncer_density_final = np.sqrt((composition_N2/(composition_N2+composition_CH4))**2*(uncer_density_final_j)**2 + (composition_CH4/(composition_N2+composition_CH4))**2*(uncer_density_final_i)**2)  ## base on the formule of the calulation of final_pressure above

				molarvolume_final = (composition_N2*molarvolume_final_j + composition_CH4*molarvolume_final_i)/(composition_N2 + composition_CH4)
				uncer_molarvolume_final = (uncer_molarvolume_final_j + uncer_molarvolume_final_i)/2

################################
####### 32 °C ##################
#################################

			if temperature.get() == 32 and instrument.get() == 1 and composition_CO2 >= 0.5: 

				#coefficient of CO2CH4 calibration (i)
				composition_CO2_normalized_1_i = (composition_CO2 + 0.005 - 0.82613)/0.1781
				composition_CO2_normalized_2_i = (composition_CO2 - 0.005 - 0.82613)/0.1781
				FDS_normalized_1_i = (FDS + unc_FDS - 103.86)/0.74857
				FDS_normalized_2_i = (FDS - unc_FDS - 103.86)/0.74857
				
				p00_i= 117.4815787
				p10_i= -64.00435313
				p01_i= 75.90202201
				p20_i= 33.79624017
				p11_i= -153.2075523
				p02_i= 110.198304
				p30_i= -17.72552705
				p21_i= 81.79481677
				p12_i= -148.3062869
				p03_i= 93.93866464
				p31_i= -13.57700611
				p22_i= 43.93126678
				p13_i= -49.6426556
				p04_i= 10.75316406
				
				d00_i= 0.486313356
				d10_i= -0.041249121
				d01_i= 0.369020167
				d20_i= -0.001314366
				d11_i= -0.003487682
				d02_i= -0.009959664
				d30_i= -0.000231208
				d21_i= -0.013539233
				d12_i= 0.03746847
				d03_i= -0.03096695
				d31_i= 0.001645248
				d22_i= -0.01024711
				d13_i= 0.012428938
				d04_i= -0.002157202

				#### pressure calculation using CO2CH4 calibration (i)

				pressure3_i = (p00_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**0 
				+ p10_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**0 
				+ p01_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**1 
				+ p20_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**0
				+ p11_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**1 
				+ p02_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**2 
				+ p30_i*composition_CO2_normalized_1_i**3*FDS_normalized_2_i**0 
				+ p21_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**1
				+ p12_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**2 
				+ p03_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**3 
				+ p31_i*composition_CO2_normalized_1_i**3*FDS_normalized_2_i**1 
				+ p22_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**2
				+ p13_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**3 
				+ p04_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**4)

				pressure4_i = (p00_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**0 
				+ p10_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**0 
				+ p01_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**1 
				+ p20_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**0
				+ p11_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**1 
				+ p02_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**2 
				+ p30_i*composition_CO2_normalized_2_i**3*FDS_normalized_1_i**0 
				+ p21_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**1
				+ p12_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**2 
				+ p03_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**3 
				+ p31_i*composition_CO2_normalized_2_i**3*FDS_normalized_1_i**1 
				+ p22_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**2
				+ p13_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**3 
				+ p04_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**4)

				########################
				#### density calculation  using CO2CH4 calibration (i)


				density3_i = (d00_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**0 
				+ d10_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**0 
				+ d01_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**1 
				+ d20_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**0
				+ d11_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**1 
				+ d02_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**2 
				+ d30_i*composition_CO2_normalized_1_i**3*FDS_normalized_2_i**0 
				+ d21_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**1
				+ d12_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**2 
				+ d03_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**3 
				+ d31_i*composition_CO2_normalized_1_i**3*FDS_normalized_2_i**1 
				+ d22_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**2
				+ d13_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**3 
				+ d04_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**4)

				density4_i = (d00_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**0 
				+ d10_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**0 
				+ d01_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**1 
				+ d20_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**0
				+ d11_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**1 
				+ d02_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**2 
				+ d30_i*composition_CO2_normalized_2_i**3*FDS_normalized_1_i**0 
				+ d21_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**1
				+ d12_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**2 
				+ d03_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**3 
				+ d31_i*composition_CO2_normalized_2_i**3*FDS_normalized_1_i**1 
				+ d22_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**2
				+ d13_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**3 
				+ d04_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**4)              

				pressure_final_i = (max(pressure3_i, pressure4_i) + min(pressure3_i, pressure4_i))/2 #pressure max + pressure min
				uncer_pressure_final_i = 7 + (max(pressure3_i, pressure4_i) - min(pressure3_i, pressure4_i))/(2*np.sqrt(3))

				density_final_i = (max(density3_i, density4_i) + min(density3_i, density4_i))/2 #density max - density min
				uncer_density_final_i = 0.0057 + (max(density3_i, density4_i) - min(density3_i, density4_i))/(2*np.sqrt(3))

				molarvolume3_i = 1/(max(density3_i, density4_i)/(44*composition_CO2 + 16*composition_CH4 + 28*composition_N2))
				molarvolume4_i = 1/(min(density3_i, density4_i)/(44*composition_CO2 + 16*composition_CH4 + 28*composition_N2))
				molarvolume_final_i = (molarvolume3_i + molarvolume4_i) / 2
				uncer_molarvolume_final_i = (molarvolume4_i - molarvolume3_i) / (2*np.sqrt(3))



				##### verify if measured pressure < 160 bar, if it is, re-recalculte using calibration data for 5-160 bar range.
				if pressure_final_i <= 150: 

					## Calibration equation's coeff of CO2-CH4 at 32 °C over 5-160 bars
					# normalisation of concentration and of Fermi diad splitting
					
					#coefficient of CO2CH4 calibration (i)
					composition_CO2_normalized_1_i = (composition_CO2 + 0.005 - 0.83997)/0.17804 
					composition_CO2_normalized_2_i = (composition_CO2 - 0.005 - 0.83997)/0.17804 
					FDS_normalized_1_i = (FDS + unc_FDS - 103.53)/0.63658
					FDS_normalized_2_i = (FDS - unc_FDS - 103.53)/0.63658
					
					p00_i= 94.65622893
					p10_i= -29.90432239
					p01_i= 31.9463506
					p20_i= 11.05019058
					p11_i= -41.39264514
					p02_i= -5.575568606
					p30_i= -2.412150018
					p21_i= 21.26972394
					p12_i= -39.40094963
					p03_i= 33.51376232
					p31_i= -1.313217682
					p22_i= 10.23037585
					p13_i= -22.26971706
					p04_i= 7.070998459

					d00_i= 0.318294844
					d10_i= -0.033717464
					d01_i= 0.295140901
					d20_i= 0.003835289
					d11_i= -0.034525497
					d02_i= 0.03615103
					d30_i= -0.001593066
					d21_i= 0.004028655
					d12_i= 0.006008238
					d03_i= -0.005570953
					d31_i= 0.000483165
					d22_i= -0.000890907
					d13_i= 0.008033639
					d04_i= -0.008589286

					#### pressure calculation using CO2CH4 calibration (i)

					pressure3_i = (p00_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**0 
					+ p10_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**0 
					+ p01_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**1 
					+ p20_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**0
					+ p11_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**1 
					+ p02_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**2 
					+ p30_i*composition_CO2_normalized_1_i**3*FDS_normalized_2_i**0 
					+ p21_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**1
					+ p12_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**2 
					+ p03_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**3 
					+ p31_i*composition_CO2_normalized_1_i**3*FDS_normalized_2_i**1 
					+ p22_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**2
					+ p13_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**3 
					+ p04_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**4)

					pressure4_i = (p00_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**0 
					+ p10_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**0 
					+ p01_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**1 
					+ p20_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**0
					+ p11_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**1 
					+ p02_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**2 
					+ p30_i*composition_CO2_normalized_2_i**3*FDS_normalized_1_i**0 
					+ p21_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**1
					+ p12_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**2 
					+ p03_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**3 
					+ p31_i*composition_CO2_normalized_2_i**3*FDS_normalized_1_i**1 
					+ p22_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**2
					+ p13_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**3 
					+ p04_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**4)

					########################
					#### density calculation  using CO2CH4 calibration (i)


					density3_i = (d00_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**0 
					+ d10_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**0 
					+ d01_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**1 
					+ d20_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**0
					+ d11_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**1 
					+ d02_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**2 
					+ d30_i*composition_CO2_normalized_1_i**3*FDS_normalized_2_i**0 
					+ d21_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**1
					+ d12_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**2 
					+ d03_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**3 
					+ d31_i*composition_CO2_normalized_1_i**3*FDS_normalized_2_i**1 
					+ d22_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**2
					+ d13_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**3 
					+ d04_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**4)

					density4_i = (d00_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**0 
					+ d10_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**0 
					+ d01_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**1 
					+ d20_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**0
					+ d11_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**1 
					+ d02_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**2 
					+ d30_i*composition_CO2_normalized_2_i**3*FDS_normalized_1_i**0 
					+ d21_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**1
					+ d12_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**2 
					+ d03_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**3 
					+ d31_i*composition_CO2_normalized_2_i**3*FDS_normalized_1_i**1 
					+ d22_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**2
					+ d13_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**3 
					+ d04_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**4)              

					pressure_final_i = (max(pressure3_i, pressure4_i) + min(pressure3_i, pressure4_i))/2 #pressure max + pressure min
					uncer_pressure_final_i = 4.2 + (max(pressure3_i, pressure4_i) - min(pressure3_i, pressure4_i))/(2*np.sqrt(3))

					density_final_i = (max(density3_i, density4_i) + min(density3_i, density4_i))/2 #density max - density min
					uncer_density_final_i = 0.0057 + (max(density3_i, density4_i) - min(density3_i, density4_i))/(2*np.sqrt(3))

					molarvolume3_i = 1/(max(density3_i, density4_i)/(44*composition_CO2 + 16*composition_CH4 + 28*composition_N2))
					molarvolume4_i = 1/(min(density3_i, density4_i)/(44*composition_CO2 + 16*composition_CH4 + 28*composition_N2))
					molarvolume_final_i = (molarvolume3_i + molarvolume4_i) / 2
					uncer_molarvolume_final_i = (molarvolume4_i - molarvolume3_i) / (2*np.sqrt(3))

			
				print('pressure3_i', pressure3_i)
				print('pressure4_i', pressure4_i)
				print('density 3_i=', density3_i)
				print('density 4_i=', density4_i)
				print("molarvolume3_i", molarvolume3_i)
				print("molarvolume4_i", molarvolume4_i)	
				

				#################################
				#coefficient of CO2 N2 calibration (j)
				############################"""
				composition_CO2_normalized_1_j = (composition_CO2 + 0.005 - 0.79427 )/0.17942
				composition_CO2_normalized_2_j = (composition_CO2 - 0.005 - 0.79427 )/0.17942
				FDS_normalized_1_j = (FDS + unc_FDS - 103.74)/0.72596
				FDS_normalized_2_j = (FDS - unc_FDS - 103.74)/0.72596
				
				p00_j= 134.8531425
				p10_j= -62.13942807
				p01_j= 95.32309211
				p20_j= 37.55699011
				p11_j= -144.1206532
				p02_j= 87.60480426
				p30_j= -27.52349216
				p21_j= 74.61281782
				p12_j= -131.2875059
				p03_j= 81.04989487
				p31_j= -23.38347901
				p22_j= 38.11772739
				p13_j= -40.14928604
				p04_j= 9.504943027

				d00_j= 0.468548895
				d10_j= -0.051703845
				d01_j= 0.385401403
				d20_j= 0.008264594
				d11_j= -0.022559707
				d02_j= -0.009187601
				d30_j= -0.013416864
				d21_j= -0.003756692
				d12_j= 0.024487064
				d03_j= -0.029123696
				d31_j= -0.008426964
				d22_j= -0.007617716
				d13_j= 0.008890962
				d04_j= 0.001795057

				#### pressure calculation using CO2 N2  calibration (j)

				pressure3_j = (p00_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**0 
				+ p10_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**0 
				+ p01_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**1 
				+ p20_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**0
				+ p11_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**1 
				+ p02_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**2 
				+ p30_j*composition_CO2_normalized_1_j**3*FDS_normalized_2_j**0 
				+ p21_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**1
				+ p12_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**2 
				+ p03_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**3 
				+ p31_j*composition_CO2_normalized_1_j**3*FDS_normalized_2_j**1 
				+ p22_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**2
				+ p13_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**3 
				+ p04_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**4)

				pressure4_j = (p00_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**0 
				+ p10_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**0 
				+ p01_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**1 
				+ p20_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**0
				+ p11_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**1 
				+ p02_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**2 
				+ p30_j*composition_CO2_normalized_2_j**3*FDS_normalized_1_j**0 
				+ p21_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**1
				+ p12_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**2 
				+ p03_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**3 
				+ p31_j*composition_CO2_normalized_2_j**3*FDS_normalized_1_j**1 
				+ p22_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**2
				+ p13_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**3 
				+ p04_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**4)

				########################
				#### density calculation  using CO2 N2  calibration (j)


				density3_j = (d00_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**0 
				+ d10_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**0 
				+ d01_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**1 
				+ d20_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**0
				+ d11_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**1 
				+ d02_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**2 
				+ d30_j*composition_CO2_normalized_1_j**3*FDS_normalized_2_j**0 
				+ d21_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**1
				+ d12_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**2 
				+ d03_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**3 
				+ d31_j*composition_CO2_normalized_1_j**3*FDS_normalized_2_j**1 
				+ d22_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**2
				+ d13_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**3 
				+ d04_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**4)

				density4_j = (d00_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**0 
				+ d10_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**0 
				+ d01_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**1 
				+ d20_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**0
				+ d11_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**1 
				+ d02_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**2 
				+ d30_j*composition_CO2_normalized_2_j**3*FDS_normalized_1_j**0 
				+ d21_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**1
				+ d12_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**2 
				+ d03_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**3 
				+ d31_j*composition_CO2_normalized_2_j**3*FDS_normalized_1_j**1 
				+ d22_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**2
				+ d13_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**3 
				+ d04_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**4)              

				pressure_final_j = (max(pressure3_j, pressure4_j) + min(pressure3_j, pressure4_j))/2 #pressure max + pressure min
				uncer_pressure_final_j = 7.8 + (max(pressure3_j, pressure4_j) - min(pressure3_j, pressure4_j))/(2*np.sqrt(3))

				density_final_j = (max(density3_j, density4_j) + min(density3_j, density4_j))/2 #density max - density min
				uncer_density_final_j = 0.0057 + (max(density3_j, density4_j) - min(density3_j, density4_j))/(2*np.sqrt(3))

				molarvolume3_j = 1/(max(density3_j, density4_j)/(44*composition_CO2 + 16*composition_CH4 + 28*composition_N2))
				molarvolume4_j = 1/(min(density3_j, density4_j)/(44*composition_CO2 + 16*composition_CH4 + 28*composition_N2))
				molarvolume_final_j = (molarvolume3_j + molarvolume4_j) / 2
				uncer_molarvolume_final_j = (molarvolume4_j - molarvolume3_j) / (2*np.sqrt(3))



				##### verify if measured pressure < 160 bar, if it is, re-recalculte using calibration data for 5-160 bar range.
				if pressure_final_j <= 150: 

					## Calibration equation's coeff of CO2-CH4 at 22 °C over 5-160 bars
					# normalisation of concentration and of Fermi diad splitting
					
					#coefficient of CO2 N2  calibration (j)
					composition_CO2_normalized_1_j = (composition_CO2 + 0.005 - 0.81495)/0.17944
					composition_CO2_normalized_2_j = (composition_CO2 - 0.005 - 0.81495)/0.17944
					FDS_normalized_1_j = (FDS + unc_FDS - 103.4)/0.6067
					FDS_normalized_2_j = (FDS - unc_FDS - 103.4)/0.6067
					
					p00_j= 98.21110543
					p10_j= -31.34816997
					p01_j= 56.75173572
					p20_j= 10.95811653
					p11_j= -43.16424504
					p02_j= -11.6093266
					p30_j= -6.147600675
					p21_j= 18.06447122
					p12_j= -32.38414044
					p03_j= 24.72823226
					p31_j= -6.83208386
					p22_j= 9.44984861
					p13_j= -16.59404
					p04_j= 5.204939143

					d00_j= 0.285936962
					d10_j= -0.033443766
					d01_j= 0.307097935
					d20_j= 0.003508055
					d11_j= -0.019168559
					d02_j= 0.021840571
					d30_j= -0.00931312
					d21_j= -0.006126292
					d12_j= 0.010636527
					d03_j= -0.016469702
					d31_j= -0.011071135
					d22_j= -0.006032022
					d13_j= 0.001693598
					d04_j= 0.001601038

					#### pressure calculation using CO2 N2  calibration (j)

					pressure3_j = (p00_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**0 
					+ p10_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**0 
					+ p01_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**1 
					+ p20_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**0
					+ p11_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**1 
					+ p02_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**2 
					+ p30_j*composition_CO2_normalized_1_j**3*FDS_normalized_2_j**0 
					+ p21_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**1
					+ p12_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**2 
					+ p03_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**3 
					+ p31_j*composition_CO2_normalized_1_j**3*FDS_normalized_2_j**1 
					+ p22_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**2
					+ p13_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**3 
					+ p04_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**4)

					pressure4_j = (p00_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**0 
					+ p10_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**0 
					+ p01_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**1 
					+ p20_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**0
					+ p11_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**1 
					+ p02_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**2 
					+ p30_j*composition_CO2_normalized_2_j**3*FDS_normalized_1_j**0 
					+ p21_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**1
					+ p12_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**2 
					+ p03_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**3 
					+ p31_j*composition_CO2_normalized_2_j**3*FDS_normalized_1_j**1 
					+ p22_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**2
					+ p13_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**3 
					+ p04_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**4)

					########################
					#### density calculation  using CO2 N2  calibration (i)


					density3_j = (d00_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**0 
					+ d10_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**0 
					+ d01_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**1 
					+ d20_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**0
					+ d11_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**1 
					+ d02_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**2 
					+ d30_j*composition_CO2_normalized_1_j**3*FDS_normalized_2_j**0 
					+ d21_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**1
					+ d12_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**2 
					+ d03_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**3 
					+ d31_j*composition_CO2_normalized_1_j**3*FDS_normalized_2_j**1 
					+ d22_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**2
					+ d13_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**3 
					+ d04_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**4)

					density4_j = (d00_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**0 
					+ d10_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**0 
					+ d01_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**1 
					+ d20_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**0
					+ d11_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**1 
					+ d02_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**2 
					+ d30_j*composition_CO2_normalized_2_j**3*FDS_normalized_1_j**0 
					+ d21_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**1
					+ d12_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**2 
					+ d03_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**3 
					+ d31_j*composition_CO2_normalized_2_j**3*FDS_normalized_1_j**1 
					+ d22_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**2
					+ d13_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**3 
					+ d04_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**4)              

					pressure_final_j = (max(pressure3_j, pressure4_j) + min(pressure3_j, pressure4_j))/2 #pressure max + pressure min
					uncer_pressure_final_j = 3 + (max(pressure3_j, pressure4_j) - min(pressure3_j, pressure4_j))/(2*np.sqrt(3))

					density_final_j = (max(density3_j, density4_j) + min(density3_j, density4_j))/2 #density max - density min
					uncer_density_final_j = 0.0042 + (max(density3_j, density4_j) - min(density3_j, density4_j))/(2*np.sqrt(3))

					molarvolume3_j = 1/(max(density3_j, density4_j)/(44*composition_CO2 + 16*composition_CH4 + 28*composition_N2))
					molarvolume4_j = 1/(min(density3_j, density4_j)/(44*composition_CO2 + 16*composition_CH4 + 28*composition_N2))
					molarvolume_final_j = (molarvolume3_j + molarvolume4_j) / 2
					uncer_molarvolume_final_j = (molarvolume4_j - molarvolume3_j) / (2*np.sqrt(3))



			
				print('pressure3_j', pressure3_j)
				print('pressure4_j', pressure4_j)
				print('density 3_j=', density3_j)
				print('density 4_j=', density4_j)
				print("molarvolume3_j", molarvolume3_j)
				print("molarvolume4_j", molarvolume4_j)	
				if pressure_final_i > 650 or pressure3_i >650 or pressure4_i >650 or pressure_final_i < -20 or pressure3_i <-20 or pressure4_i <-20 or pressure_final_j > 650 or pressure3_j >650 or pressure4_j >650 or pressure_final_j < -20 or pressure3_j <-20 or pressure4_j <-20 or density3_i<0 or density4_i <0 or density3_j<0 or density4_j<0 or density_final_i<0 or density_final_j<0 :
					popupmsg_OCR()


				############ Calculation final pressure, density from pressure final i and j, depending on the concentration of CH4, N2 (coeff, a b within equation 8))
				############ and calculation uncertainty of FINAL RESULTS
				pressure_final = (composition_N2*pressure_final_j + composition_CH4*pressure_final_i)/(composition_N2 + composition_CH4) ## Equation 8 in the reference 2
				uncer_pressure_final = np.sqrt((composition_N2/(composition_N2+composition_CH4))**2*(uncer_pressure_final_j)**2 + (composition_CH4/(composition_N2+composition_CH4))**2*(uncer_pressure_final_i)**2)  ## base on the formule of the calulation of final_pressure above
				
				density_final = (composition_N2*density_final_j + composition_CH4*density_final_i)/(composition_N2 + composition_CH4) ## Equation 8 in the reference 2
				uncer_density_final = np.sqrt((composition_N2/(composition_N2+composition_CH4))**2*(uncer_density_final_j)**2 + (composition_CH4/(composition_N2+composition_CH4))**2*(uncer_density_final_i)**2)  ## base on the formule of the calulation of final_pressure above

				molarvolume_final = (composition_N2*molarvolume_final_j + composition_CH4*molarvolume_final_i)/(composition_N2 + composition_CH4)
				uncer_molarvolume_final = (uncer_molarvolume_final_j + uncer_molarvolume_final_i)/2

########################
########################

			if temperature.get() == 32 and instrument.get() == 1 and composition_CO2 < 0.5: 

				#coefficient of CO2CH4 calibration (i)
				composition_CO2_normalized_1_i = (composition_CO2 + 0.005 - 0.3022)/0.1414
				composition_CO2_normalized_2_i = (composition_CO2 - 0.005 - 0.3022)/0.1414
				FDS_normalized_1_i = (FDS + unc_FDS - 103.09)/0.30473
				FDS_normalized_2_i = (FDS - unc_FDS - 103.09)/0.30473
				
				p00_i= 160.30964
				p10_i= -70.7304
				p01_i= 143.1939
				p20_i= 61.43567
				p11_i= -118.06532
				p02_i= 44.22433
				p30_i= -30.10597
				p21_i= 94.64936
				p12_i= -88.33662
				p03_i= 40.28167
				p31_i= -35.52924
				p22_i= 39.00078
				p13_i= -20.5409
				p04_i= 0.75141

				d00_i= 0.22219
				d10_i= -0.05087
				d01_i= 0.20111
				d20_i= 0.00975
				d11_i= -0.02361
				d02_i= -0.00858
				d30_i= -4.96E-04
				d21_i= -8.54E-03
				d12_i= 0.02996
				d03_i= -0.00905
				d31_i= 0.00217
				d22_i= -0.01292
				d13_i= 0.00529
				d04_i= -0.000725

				#### pressure calculation using CO2CH4 calibration (i)

				pressure3_i = (p00_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**0 
				+ p10_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**0 
				+ p01_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**1 
				+ p20_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**0
				+ p11_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**1 
				+ p02_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**2 
				+ p30_i*composition_CO2_normalized_1_i**3*FDS_normalized_2_i**0 
				+ p21_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**1
				+ p12_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**2 
				+ p03_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**3 
				+ p31_i*composition_CO2_normalized_1_i**3*FDS_normalized_2_i**1 
				+ p22_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**2
				+ p13_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**3 
				+ p04_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**4)

				pressure4_i = (p00_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**0 
				+ p10_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**0 
				+ p01_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**1 
				+ p20_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**0
				+ p11_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**1 
				+ p02_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**2 
				+ p30_i*composition_CO2_normalized_2_i**3*FDS_normalized_1_i**0 
				+ p21_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**1
				+ p12_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**2 
				+ p03_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**3 
				+ p31_i*composition_CO2_normalized_2_i**3*FDS_normalized_1_i**1 
				+ p22_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**2
				+ p13_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**3 
				+ p04_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**4)

				########################
				#### density calculation  using CO2CH4 calibration (i)


				density3_i = (d00_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**0 
				+ d10_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**0 
				+ d01_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**1 
				+ d20_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**0
				+ d11_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**1 
				+ d02_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**2 
				+ d30_i*composition_CO2_normalized_1_i**3*FDS_normalized_2_i**0 
				+ d21_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**1
				+ d12_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**2 
				+ d03_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**3 
				+ d31_i*composition_CO2_normalized_1_i**3*FDS_normalized_2_i**1 
				+ d22_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**2
				+ d13_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**3 
				+ d04_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**4)

				density4_i = (d00_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**0 
				+ d10_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**0 
				+ d01_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**1 
				+ d20_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**0
				+ d11_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**1 
				+ d02_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**2 
				+ d30_i*composition_CO2_normalized_2_i**3*FDS_normalized_1_i**0 
				+ d21_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**1
				+ d12_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**2 
				+ d03_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**3 
				+ d31_i*composition_CO2_normalized_2_i**3*FDS_normalized_1_i**1 
				+ d22_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**2
				+ d13_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**3 
				+ d04_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**4)              

				pressure_final_i = (max(pressure3_i, pressure4_i) + min(pressure3_i, pressure4_i))/2 #pressure max + pressure min
				uncer_pressure_final_i = 8.5 + (max(pressure3_i, pressure4_i) - min(pressure3_i, pressure4_i))/(2*np.sqrt(3))

				density_final_i = (max(density3_i, density4_i) + min(density3_i, density4_i))/2 #density max - density min
				uncer_density_final_i = 0.0049 + (max(density3_i, density4_i) - min(density3_i, density4_i))/(2*np.sqrt(3))

				molarvolume3_i = 1/(max(density3_i, density4_i)/(44*composition_CO2 + 16*composition_CH4 + 28*composition_N2))
				molarvolume4_i = 1/(min(density3_i, density4_i)/(44*composition_CO2 + 16*composition_CH4 + 28*composition_N2))
				molarvolume_final_i = (molarvolume3_i + molarvolume4_i) / 2
				uncer_molarvolume_final_i = (molarvolume4_i - molarvolume3_i) / (2*np.sqrt(3))



				##### verify if measured pressure < 160 bar, if it is, re-recalculte using calibration data for 5-160 bar range.
				if pressure_final_i <= 150: 

					## Calibration equation's coeff of CO2-CH4 at 22 °C over 5-160 bars
					# normalisation of concentration and of Fermi diad splitting
					
					#coefficient of CO2CH4 calibration (i)
					composition_CO2_normalized_1_i = (composition_CO2 + 0.005 -  0.3022)/0.14182  
					composition_CO2_normalized_2_i = (composition_CO2 - 0.005 - 0.3022)/0.14182  
					FDS_normalized_1_i = (FDS + unc_FDS - 102.92)/0.13981
					FDS_normalized_2_i = (FDS - unc_FDS - 102.92)/0.13981
					
					
					p00_i= 86.45553
					p10_i= -36.98006
					p01_i= 63.38251
					p20_i= 16.24622
					p11_i= -18.99735
					p02_i= -9.01309
					p30_i= -3.58623
					p21_i= 5.9654
					p12_i= 11.75184
					p03_i= 0.85861
					p31_i= -2.43154
					p22_i= -5.96449
					p13_i= -1.51232
					p04_i= 0.5601


					d00_i= 0.10363
					d10_i= -0.02684
					d01_i= 0.09192
					d20_i= 0.01111
					d11_i= -0.01222
					d02_i= -0.00223
					d30_i= -0.00287
					d21_i= 0.00124
					d12_i= 0.01194
					d03_i= -0.00339
					d31_i= -0.00255
					d22_i= -0.00636
					d13_i= 5.24E-04
					d04_i= 7.17E-04

					#### pressure calculation using CO2CH4 calibration (i)

					pressure3_i = (p00_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**0 
					+ p10_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**0 
					+ p01_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**1 
					+ p20_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**0
					+ p11_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**1 
					+ p02_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**2 
					+ p30_i*composition_CO2_normalized_1_i**3*FDS_normalized_2_i**0 
					+ p21_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**1
					+ p12_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**2 
					+ p03_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**3 
					+ p31_i*composition_CO2_normalized_1_i**3*FDS_normalized_2_i**1 
					+ p22_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**2
					+ p13_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**3 
					+ p04_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**4)

					pressure4_i = (p00_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**0 
					+ p10_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**0 
					+ p01_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**1 
					+ p20_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**0
					+ p11_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**1 
					+ p02_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**2 
					+ p30_i*composition_CO2_normalized_2_i**3*FDS_normalized_1_i**0 
					+ p21_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**1
					+ p12_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**2 
					+ p03_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**3 
					+ p31_i*composition_CO2_normalized_2_i**3*FDS_normalized_1_i**1 
					+ p22_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**2
					+ p13_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**3 
					+ p04_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**4)

					########################
					#### density calculation  using CO2CH4 calibration (i)


					density3_i = (d00_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**0 
					+ d10_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**0 
					+ d01_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**1 
					+ d20_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**0
					+ d11_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**1 
					+ d02_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**2 
					+ d30_i*composition_CO2_normalized_1_i**3*FDS_normalized_2_i**0 
					+ d21_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**1
					+ d12_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**2 
					+ d03_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**3 
					+ d31_i*composition_CO2_normalized_1_i**3*FDS_normalized_2_i**1 
					+ d22_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**2
					+ d13_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**3 
					+ d04_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**4)

					density4_i = (d00_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**0 
					+ d10_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**0 
					+ d01_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**1 
					+ d20_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**0
					+ d11_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**1 
					+ d02_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**2 
					+ d30_i*composition_CO2_normalized_2_i**3*FDS_normalized_1_i**0 
					+ d21_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**1
					+ d12_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**2 
					+ d03_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**3 
					+ d31_i*composition_CO2_normalized_2_i**3*FDS_normalized_1_i**1 
					+ d22_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**2
					+ d13_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**3 
					+ d04_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**4)              

					pressure_final_i = (max(pressure3_i, pressure4_i) + min(pressure3_i, pressure4_i))/2 #pressure max + pressure min
					uncer_pressure_final_i = 5 + (max(pressure3_i, pressure4_i) - min(pressure3_i, pressure4_i))/(2*np.sqrt(3))

					density_final_i = (max(density3_i, density4_i) + min(density3_i, density4_i))/2 #density max - density min
					uncer_density_final_i = 0.0049 + (max(density3_i, density4_i) - min(density3_i, density4_i))/(2*np.sqrt(3))

					molarvolume3_i = 1/(max(density3_i, density4_i)/(44*composition_CO2 + 16*composition_CH4 + 28*composition_N2))
					molarvolume4_i = 1/(min(density3_i, density4_i)/(44*composition_CO2 + 16*composition_CH4 + 28*composition_N2))
					molarvolume_final_i = (molarvolume3_i + molarvolume4_i) / 2
					uncer_molarvolume_final_i = (molarvolume4_i - molarvolume3_i) / (2*np.sqrt(3))

			
				print('pressure3_i', pressure3_i)
				print('pressure4_i', pressure4_i)
				print('density 3_i=', density3_i)
				print('density 4_i=', density4_i)
				print("molarvolume3_i", molarvolume3_i)
				print("molarvolume4_i", molarvolume4_i)	
				

				#################################
				#coefficient of CO2 N2 calibration (j)
				############################"""
				composition_CO2_normalized_1_j = (composition_CO2 + 0.005 - 0.3)/0.14207
				composition_CO2_normalized_2_j = (composition_CO2 - 0.005 - 0.3)/0.14207
				FDS_normalized_1_j = (FDS + unc_FDS - 103.05)/0.26608
				FDS_normalized_2_j = (FDS - unc_FDS - 103.05)/0.26608
				
				
				p00_j= 164.7455598
				p10_j= -72.94354971
				p01_j= 154.866058
				p20_j= 64.06681929
				p11_j= -115.9406874
				p02_j= 35.45935724
				p30_j= -30.25168791
				p21_j= 91.38437433
				p12_j= -60.58208945
				p03_j= 21.3175346
				p31_j= -32.48590355
				p22_j= 25.9500595
				p13_j= -10.27134275
				p04_j= 0.589452279


				d00_j= 0.245281521
				d10_j= -0.075498903
				d01_j= 0.220264697
				d20_j=0.032838431
				d11_j= -0.05963449
				d02_j= 0.001909669
				d30_j=-0.006300402
				d21_j= 0.02148613
				d12_j= 0.022501574
				d03_j= -0.005150028
				d31_j= -0.002762027
				d22_j= -0.012487804
				d13_j= 0.002949011
				d04_j= -0.000699892

				#### pressure calculation using CO2 N2  calibration (j)

				pressure3_j = (p00_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**0 
				+ p10_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**0 
				+ p01_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**1 
				+ p20_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**0
				+ p11_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**1 
				+ p02_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**2 
				+ p30_j*composition_CO2_normalized_1_j**3*FDS_normalized_2_j**0 
				+ p21_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**1
				+ p12_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**2 
				+ p03_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**3 
				+ p31_j*composition_CO2_normalized_1_j**3*FDS_normalized_2_j**1 
				+ p22_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**2
				+ p13_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**3 
				+ p04_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**4)

				pressure4_j = (p00_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**0 
				+ p10_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**0 
				+ p01_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**1 
				+ p20_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**0
				+ p11_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**1 
				+ p02_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**2 
				+ p30_j*composition_CO2_normalized_2_j**3*FDS_normalized_1_j**0 
				+ p21_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**1
				+ p12_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**2 
				+ p03_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**3 
				+ p31_j*composition_CO2_normalized_2_j**3*FDS_normalized_1_j**1 
				+ p22_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**2
				+ p13_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**3 
				+ p04_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**4)

				########################
				#### density calculation  using CO2 N2  calibration (i)


				density3_j = (d00_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**0 
				+ d10_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**0 
				+ d01_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**1 
				+ d20_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**0
				+ d11_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**1 
				+ d02_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**2 
				+ d30_j*composition_CO2_normalized_1_j**3*FDS_normalized_2_j**0 
				+ d21_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**1
				+ d12_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**2 
				+ d03_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**3 
				+ d31_j*composition_CO2_normalized_1_j**3*FDS_normalized_2_j**1 
				+ d22_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**2
				+ d13_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**3 
				+ d04_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**4)

				density4_j = (d00_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**0 
				+ d10_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**0 
				+ d01_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**1 
				+ d20_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**0
				+ d11_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**1 
				+ d02_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**2 
				+ d30_j*composition_CO2_normalized_2_j**3*FDS_normalized_1_j**0 
				+ d21_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**1
				+ d12_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**2 
				+ d03_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**3 
				+ d31_j*composition_CO2_normalized_2_j**3*FDS_normalized_1_j**1 
				+ d22_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**2
				+ d13_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**3 
				+ d04_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**4)              

				pressure_final_j = (max(pressure3_j, pressure4_j) + min(pressure3_j, pressure4_j))/2 #pressure max + pressure min
				uncer_pressure_final_j = 5.7 + (max(pressure3_j, pressure4_j) - min(pressure3_j, pressure4_j))/(2*np.sqrt(3))

				density_final_j = (max(density3_j, density4_j) + min(density3_j, density4_j))/2 #density max - density min
				uncer_density_final_j = 0.0042 + (max(density3_j, density4_j) - min(density3_j, density4_j))/(2*np.sqrt(3))

				molarvolume3_j = 1/(max(density3_j, density4_j)/(44*composition_CO2 + 16*composition_CH4 + 28*composition_N2))
				molarvolume4_j = 1/(min(density3_j, density4_j)/(44*composition_CO2 + 16*composition_CH4 + 28*composition_N2))
				molarvolume_final_j = (molarvolume3_j + molarvolume4_j) / 2
				uncer_molarvolume_final_j = (molarvolume4_j - molarvolume3_j) / (2*np.sqrt(3))


				##### verify if measured pressure < 160 bar, if it is, re-recalculte using calibration data for 5-160 bar range.
				if pressure_final_j <= 150: 

					## Calibration equation's coeff of CO2-CH4 at 22 °C over 5-160 bars
					# normalisation of concentration and of Fermi diad splitting
					
					#coefficient of CO2CH4 calibration (j)
					composition_CO2_normalized_1_j = (composition_CO2 + 0.005 - 0.30339)/0.14138
					composition_CO2_normalized_2_j = (composition_CO2 - 0.005 - 0.30339)/0.14138
					FDS_normalized_1_j = (FDS + unc_FDS - 102.87)/0.093082
					FDS_normalized_2_j = (FDS - unc_FDS - 102.87)/0.093082
					
					p00_j= 69.13911052
					p10_j= -26.1138853
					p01_j= 51.15493952
					p20_j= 12.433977
					p11_j= -24.97362963
					p02_j= -0.61042483
					p30_j= -3.525410343
					p21_j= 12.07944049
					p12_j= 3.668211303
					p03_j= -0.998272689
					p31_j= -2.992344667
					p22_j= -3.140109598
					p13_j= 1.096062354
					p04_j= -0.061661634
					
					d00_j= 0.096377933					
					d10_j= -0.027517465
					d01_j= 0.075132864
					d20_j= 0.012065717
					d11_j= -0.026418972
					d02_j= 0.001098315
					d30_j= -0.002806359
					d21_j= 0.010828952
					d12_j= 0.00658279
					d03_j= -0.002021765
					d31_j= -0.001975997
					d22_j= -0.004846773
					d13_j= 0.001993775
					d04_j= -0.000167776

					#### pressure calculation using CO2CH4 calibration (j)

					pressure3_j = (p00_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**0 
					+ p10_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**0 
					+ p01_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**1 
					+ p20_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**0
					+ p11_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**1 
					+ p02_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**2 
					+ p30_j*composition_CO2_normalized_1_j**3*FDS_normalized_2_j**0 
					+ p21_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**1
					+ p12_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**2 
					+ p03_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**3 
					+ p31_j*composition_CO2_normalized_1_j**3*FDS_normalized_2_j**1 
					+ p22_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**2
					+ p13_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**3 
					+ p04_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**4)

					pressure4_j = (p00_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**0 
					+ p10_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**0 
					+ p01_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**1 
					+ p20_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**0
					+ p11_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**1 
					+ p02_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**2 
					+ p30_j*composition_CO2_normalized_2_j**3*FDS_normalized_1_j**0 
					+ p21_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**1
					+ p12_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**2 
					+ p03_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**3 
					+ p31_j*composition_CO2_normalized_2_j**3*FDS_normalized_1_j**1 
					+ p22_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**2
					+ p13_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**3 
					+ p04_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**4)

					########################
					#### density calculation  using CO2CH4 calibration (i)

					density3_j = (d00_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**0 
					+ d10_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**0 
					+ d01_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**1 
					+ d20_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**0
					+ d11_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**1 
					+ d02_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**2 
					+ d30_j*composition_CO2_normalized_1_j**3*FDS_normalized_2_j**0 
					+ d21_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**1
					+ d12_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**2 
					+ d03_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**3 
					+ d31_j*composition_CO2_normalized_1_j**3*FDS_normalized_2_j**1 
					+ d22_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**2
					+ d13_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**3 
					+ d04_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**4)

					density4_j = (d00_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**0 
					+ d10_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**0 
					+ d01_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**1 
					+ d20_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**0
					+ d11_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**1 
					+ d02_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**2 
					+ d30_j*composition_CO2_normalized_2_j**3*FDS_normalized_1_j**0 
					+ d21_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**1
					+ d12_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**2 
					+ d03_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**3 
					+ d31_j*composition_CO2_normalized_2_j**3*FDS_normalized_1_j**1 
					+ d22_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**2
					+ d13_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**3 
					+ d04_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**4)              

					pressure_final_j = (max(pressure3_j, pressure4_j) + min(pressure3_j, pressure4_j))/2 #pressure max + pressure min
					uncer_pressure_final_j = 4 + (max(pressure3_j, pressure4_j) - min(pressure3_j, pressure4_j))/(2*np.sqrt(3))

					density_final_j = (max(density3_j, density4_j) + min(density3_j, density4_j))/2 #density max - density min
					uncer_density_final_j = 0.004 + (max(density3_j, density4_j) - min(density3_j, density4_j))/(2*np.sqrt(3))

					molarvolume3_j = 1/(max(density3_j, density4_j)/(44*composition_CO2 + 16*composition_CH4 + 28*composition_N2))
					molarvolume4_j = 1/(min(density3_j, density4_j)/(44*composition_CO2 + 16*composition_CH4 + 28*composition_N2))
					molarvolume_final_j = (molarvolume3_j + molarvolume4_j) / 2
					uncer_molarvolume_final_j = (molarvolume4_j - molarvolume3_j) / (2*np.sqrt(3))
		
				print('pressure3_j', pressure3_j)
				print('pressure4_j', pressure4_j)
				print('density 3_j=', density3_j)
				print('density 4_j=', density4_j)
				print("molarvolume3_i", molarvolume3_j)
				print("molarvolume4_i", molarvolume4_j)	
				if pressure_final_i > 650 or pressure3_i >650 or pressure4_i >650 or pressure_final_i < -20 or pressure3_i <-20 or pressure4_i <-20 or pressure_final_j > 650 or pressure3_j >650 or pressure4_j >650 or pressure_final_j < -20 or pressure3_j <-20 or pressure4_j <-20 or density3_i<0 or density4_i <0 or density3_j<0 or density4_j<0 or density_final_i<0 or density_final_j<0 :
					popupmsg_OCR()


				############ Calculation final pressure, density from pressure final i and j, depending on the concentration of CH4, N2 (coeff, a b within equation 8))
				############ and calculation uncertainty of FINAL RESULTS
				pressure_final = (composition_N2*pressure_final_j + composition_CH4*pressure_final_i)/(composition_N2 + composition_CH4) ## Equation 8 in the reference 2
				uncer_pressure_final = np.sqrt((composition_N2/(composition_N2+composition_CH4))**2*(uncer_pressure_final_j)**2 + (composition_CH4/(composition_N2+composition_CH4))**2*(uncer_pressure_final_i)**2)  ## base on the formule of the calulation of final_pressure above
				
				density_final = (composition_N2*density_final_j + composition_CH4*density_final_i)/(composition_N2 + composition_CH4) ## Equation 8 in the reference 2
				uncer_density_final = np.sqrt((composition_N2/(composition_N2+composition_CH4))**2*(uncer_density_final_j)**2 + (composition_CH4/(composition_N2+composition_CH4))**2*(uncer_density_final_i)**2)  ## base on the formule of the calulation of final_pressure above

				molarvolume_final = (composition_N2*molarvolume_final_j + composition_CH4*molarvolume_final_i)/(composition_N2 + composition_CH4)
				uncer_molarvolume_final = (uncer_molarvolume_final_j + uncer_molarvolume_final_i)/2

#################################
#################################
####### OTHERS instrument #######
#################################
#################################

			if temperature.get() == 22 and instrument.get() == 2 and composition_CO2 >= 0.5: 

				#coefficient of CO2CH4 calibration (i)
				composition_CO2_normalized_1_i = (composition_CO2 + 0.005)
				composition_CO2_normalized_2_i = (composition_CO2 - 0.005)
				FDS_normalized_1_i = (FDS + unc_FDS - FDS_std)
				FDS_normalized_2_i = (FDS - unc_FDS - FDS_std)
				
				p00_i= 178.110
				p10_i= -493.276
				p01_i= 174.125
				p20_i= 320.292
				p11_i= -580.958
				p02_i= 773.463
				p30_i= -1.111
				p21_i= 2655.985
				p12_i= -3584.041
				p03_i= 654.829
				p31_i= -2100.462
				p22_i= 2686.202
				p13_i= -669.269
				p04_i= 26.174


				d00_i= -0.095144
				d10_i= 0.388100
				d01_i= 0.627318
				d20_i= -0.479419
				d11_i= -0.314993
				d02_i= -0.019846
				d30_i= 0.189601
				d21_i= -0.723497
				d12_i= 0.873300
				d03_i= -0.216237
				d31_i= 0.683057
				d22_i= -0.744117
				d13_i= 0.216532
				d04_i= -0.009033

				#### pressure calculation using CO2CH4 calibration (i)

				pressure3_i = (p00_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**0 
				+ p10_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**0 
				+ p01_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**1 
				+ p20_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**0
				+ p11_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**1 
				+ p02_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**2 
				+ p30_i*composition_CO2_normalized_1_i**3*FDS_normalized_2_i**0 
				+ p21_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**1
				+ p12_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**2 
				+ p03_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**3 
				+ p31_i*composition_CO2_normalized_1_i**3*FDS_normalized_2_i**1 
				+ p22_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**2
				+ p13_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**3 
				+ p04_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**4)

				pressure4_i = (p00_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**0 
				+ p10_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**0 
				+ p01_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**1 
				+ p20_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**0
				+ p11_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**1 
				+ p02_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**2 
				+ p30_i*composition_CO2_normalized_2_i**3*FDS_normalized_1_i**0 
				+ p21_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**1
				+ p12_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**2 
				+ p03_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**3 
				+ p31_i*composition_CO2_normalized_2_i**3*FDS_normalized_1_i**1 
				+ p22_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**2
				+ p13_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**3 
				+ p04_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**4)

				########################
				#### density calculation  using CO2CH4 calibration (i)


				density3_i = (d00_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**0 
				+ d10_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**0 
				+ d01_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**1 
				+ d20_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**0
				+ d11_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**1 
				+ d02_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**2 
				+ d30_i*composition_CO2_normalized_1_i**3*FDS_normalized_2_i**0 
				+ d21_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**1
				+ d12_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**2 
				+ d03_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**3 
				+ d31_i*composition_CO2_normalized_1_i**3*FDS_normalized_2_i**1 
				+ d22_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**2
				+ d13_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**3 
				+ d04_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**4)

				density4_i = (d00_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**0 
				+ d10_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**0 
				+ d01_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**1 
				+ d20_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**0
				+ d11_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**1 
				+ d02_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**2 
				+ d30_i*composition_CO2_normalized_2_i**3*FDS_normalized_1_i**0 
				+ d21_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**1
				+ d12_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**2 
				+ d03_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**3 
				+ d31_i*composition_CO2_normalized_2_i**3*FDS_normalized_1_i**1 
				+ d22_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**2
				+ d13_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**3 
				+ d04_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**4)              

				pressure_final_i = (max(pressure3_i, pressure4_i) + min(pressure3_i, pressure4_i))/2 #pressure max + pressure min
				uncer_pressure_final_i = 7 + (max(pressure3_i, pressure4_i) - min(pressure3_i, pressure4_i))/(2*np.sqrt(3))

				density_final_i = (max(density3_i, density4_i) + min(density3_i, density4_i))/2 #density max - density min
				uncer_density_final_i = 0.0049 + (max(density3_i, density4_i) - min(density3_i, density4_i))/(2*np.sqrt(3))

				molarvolume3_i = 1/(max(density3_i, density4_i)/(44*composition_CO2 + 16*composition_CH4 + 28*composition_N2))
				molarvolume4_i = 1/(min(density3_i, density4_i)/(44*composition_CO2 + 16*composition_CH4 + 28*composition_N2))
				molarvolume_final_i = (molarvolume3_i + molarvolume4_i) / 2
				uncer_molarvolume_final_i = (molarvolume4_i - molarvolume3_i) / (2*np.sqrt(3))


				##### verify if measured pressure < 160 bar, if it is, re-recalculte using calibration data for 5-160 bar range.
				if pressure_final_i <= 150: 

					## Calibration equation's coeff of CO2-CH4 at 22 °C over 5-160 bars
					# normalisation of concentration and of Fermi diad splitting
					
					#coefficient of CO2CH4 calibration (i)
					composition_CO2_normalized_1_i = (composition_CO2 + 0.005)
					composition_CO2_normalized_2_i = (composition_CO2 - 0.005)
					FDS_normalized_1_i = (FDS + unc_FDS - FDS_std)
					FDS_normalized_2_i = (FDS - unc_FDS - FDS_std)
					
					p00_i= 63.138
					p10_i= -229.832
					p01_i= 409.524
					p20_i= 268.950
					p11_i= -52.822
					p02_i= -154.154
					p30_i= -101.463
					p21_i= -352.855
					p12_i= -417.642
					p03_i= 307.936
					p31_i= 147.065
					p22_i= 525.599
					p13_i= -400.575
					p04_i= 45.434


					d00_i= 0.042391
					d10_i= -0.163524
					d01_i= 0.311039
					d20_i= 0.220851
					d11_i= 0.814068
					d02_i= 0.041350
					d30_i= -0.105147
					d21_i= -1.843815
					d12_i= 0.609623
					d03_i= -0.199379
					d31_i= 1.115065
					d22_i= -0.894715
					d13_i= 0.467502
					d04_i= -0.069460

					#### pressure calculation using CO2CH4 calibration (i)

					pressure3_i = (p00_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**0 
					+ p10_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**0 
					+ p01_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**1 
					+ p20_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**0
					+ p11_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**1 
					+ p02_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**2 
					+ p30_i*composition_CO2_normalized_1_i**3*FDS_normalized_2_i**0 
					+ p21_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**1
					+ p12_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**2 
					+ p03_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**3 
					+ p31_i*composition_CO2_normalized_1_i**3*FDS_normalized_2_i**1 
					+ p22_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**2
					+ p13_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**3 
					+ p04_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**4)

					pressure4_i = (p00_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**0 
					+ p10_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**0 
					+ p01_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**1 
					+ p20_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**0
					+ p11_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**1 
					+ p02_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**2 
					+ p30_i*composition_CO2_normalized_2_i**3*FDS_normalized_1_i**0 
					+ p21_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**1
					+ p12_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**2 
					+ p03_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**3 
					+ p31_i*composition_CO2_normalized_2_i**3*FDS_normalized_1_i**1 
					+ p22_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**2
					+ p13_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**3 
					+ p04_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**4)

					########################
					#### density calculation  using CO2CH4 calibration (i)


					density3_i = (d00_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**0 
					+ d10_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**0 
					+ d01_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**1 
					+ d20_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**0
					+ d11_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**1 
					+ d02_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**2 
					+ d30_i*composition_CO2_normalized_1_i**3*FDS_normalized_2_i**0 
					+ d21_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**1
					+ d12_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**2 
					+ d03_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**3 
					+ d31_i*composition_CO2_normalized_1_i**3*FDS_normalized_2_i**1 
					+ d22_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**2
					+ d13_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**3 
					+ d04_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**4)

					density4_i = (d00_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**0 
					+ d10_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**0 
					+ d01_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**1 
					+ d20_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**0
					+ d11_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**1 
					+ d02_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**2 
					+ d30_i*composition_CO2_normalized_2_i**3*FDS_normalized_1_i**0 
					+ d21_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**1
					+ d12_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**2 
					+ d03_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**3 
					+ d31_i*composition_CO2_normalized_2_i**3*FDS_normalized_1_i**1 
					+ d22_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**2
					+ d13_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**3 
					+ d04_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**4)              

					pressure_final_i = (max(pressure3_i, pressure4_i) + min(pressure3_i, pressure4_i))/2 #pressure max + pressure min
					uncer_pressure_final_i = 3 + (max(pressure3_i, pressure4_i) - min(pressure3_i, pressure4_i))/(2*np.sqrt(3))

					density_final_i = (max(density3_i, density4_i) + min(density3_i, density4_i))/2 #density max - density min
					uncer_density_final_i = 0.0049 + (max(density3_i, density4_i) - min(density3_i, density4_i))/(2*np.sqrt(3))

					molarvolume3_i = 1/(max(density3_i, density4_i)/(44*composition_CO2 + 16*composition_CH4 + 28*composition_N2))
					molarvolume4_i = 1/(min(density3_i, density4_i)/(44*composition_CO2 + 16*composition_CH4 + 28*composition_N2))
					molarvolume_final_i = (molarvolume3_i + molarvolume4_i) / 2
					uncer_molarvolume_final_i = (molarvolume4_i - molarvolume3_i) / (2*np.sqrt(3))

			
				print('pressure3_i', pressure3_i)
				print('pressure4_i', pressure4_i)
				print('density 3_i=', density3_i)
				print('density 4_i=', density4_i)
				print("molarvolume3_i", molarvolume3_i)
				print("molarvolume4_i", molarvolume4_i)	
				

				#################################
				#coefficient of CO2 N2 calibration at 22 °C (j)
				############################"""
				composition_CO2_normalized_1_j = (composition_CO2 + 0.005)
				composition_CO2_normalized_2_j = (composition_CO2 - 0.005)
				FDS_normalized_1_j = (FDS + unc_FDS - FDS_std)
				FDS_normalized_2_j = (FDS - unc_FDS - FDS_std)
				
				p00_j= -137.742
				p10_j= 683.702
				p01_j= 1930.147
				p20_j= -1089.503
				p11_j= -6950.342
				p02_j= 865.542
				p30_j= 547.846
				p21_j= 10147.692
				p12_j= -3537.190
				p03_j= 600.002
				p31_j= -4980.751
				p22_j= 2557.165
				p13_j= -624.148
				p04_j= 28.644

				d00_j= 0.376216
				d10_j= -1.740868
				d01_j= 1.490436
				d20_j= 2.561821
				d11_j= -2.248784
				d02_j= -0.234697
				d30_j= -1.200926
				d21_j= 0.665529
				d12_j= 1.201509
				d03_j= -0.169712
				d31_j= 0.405396
				d22_j= -0.884667
				d13_j= 0.171749
				d04_j= -0.007822

				#### pressure calculation using CO2CH4 calibration (j)

				pressure3_j = (p00_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**0 
				+ p10_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**0 
				+ p01_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**1 
				+ p20_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**0
				+ p11_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**1 
				+ p02_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**2 
				+ p30_j*composition_CO2_normalized_1_j**3*FDS_normalized_2_j**0 
				+ p21_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**1
				+ p12_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**2 
				+ p03_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**3 
				+ p31_j*composition_CO2_normalized_1_j**3*FDS_normalized_2_j**1 
				+ p22_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**2
				+ p13_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**3 
				+ p04_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**4)

				pressure4_j = (p00_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**0 
				+ p10_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**0 
				+ p01_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**1 
				+ p20_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**0
				+ p11_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**1 
				+ p02_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**2 
				+ p30_j*composition_CO2_normalized_2_j**3*FDS_normalized_1_j**0 
				+ p21_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**1
				+ p12_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**2 
				+ p03_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**3 
				+ p31_j*composition_CO2_normalized_2_j**3*FDS_normalized_1_j**1 
				+ p22_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**2
				+ p13_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**3 
				+ p04_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**4)

				########################
				#### density calculation  using CO2CH4 calibration (i)


				density3_j = (d00_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**0 
				+ d10_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**0 
				+ d01_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**1 
				+ d20_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**0
				+ d11_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**1 
				+ d02_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**2 
				+ d30_j*composition_CO2_normalized_1_j**3*FDS_normalized_2_j**0 
				+ d21_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**1
				+ d12_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**2 
				+ d03_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**3 
				+ d31_j*composition_CO2_normalized_1_j**3*FDS_normalized_2_j**1 
				+ d22_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**2
				+ d13_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**3 
				+ d04_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**4)

				density4_j = (d00_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**0 
				+ d10_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**0 
				+ d01_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**1 
				+ d20_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**0
				+ d11_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**1 
				+ d02_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**2 
				+ d30_j*composition_CO2_normalized_2_j**3*FDS_normalized_1_j**0 
				+ d21_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**1
				+ d12_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**2 
				+ d03_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**3 
				+ d31_j*composition_CO2_normalized_2_j**3*FDS_normalized_1_j**1 
				+ d22_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**2
				+ d13_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**3 
				+ d04_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**4)              

				pressure_final_j = (max(pressure3_j, pressure4_j) + min(pressure3_j, pressure4_j))/2 #pressure max + pressure min
				uncer_pressure_final_j = 7 + (max(pressure3_j, pressure4_j) - min(pressure3_j, pressure4_j))/(2*np.sqrt(3))

				density_final_j = (max(density3_j, density4_j) + min(density3_j, density4_j))/2 #density max - density min
				uncer_density_final_j = 0.0042 + (max(density3_j, density4_j) - min(density3_j, density4_j))/(2*np.sqrt(3))

				molarvolume3_j = 1/(max(density3_j, density4_j)/(44*composition_CO2 + 16*composition_CH4 + 28*composition_N2))
				molarvolume4_j = 1/(min(density3_j, density4_j)/(44*composition_CO2 + 16*composition_CH4 + 28*composition_N2))
				molarvolume_final_j = (molarvolume3_j + molarvolume4_j) / 2
				uncer_molarvolume_final_j = (molarvolume4_j - molarvolume3_j) / (2*np.sqrt(3))


				##### verify if measured pressure < 160 bar, if it is, re-recalculte using calibration data for 5-160 bar range.
				if pressure_final_j <= 150: 

					## Calibration equation's coeff of CO2-CH4 at 22 °C over 5-160 bars
					# normalisation of concentration and of Fermi diad splitting
					
					#coefficient of CO2CH4 calibration (j)
					composition_CO2_normalized_1_j = (composition_CO2 + 0.005)
					composition_CO2_normalized_2_j = (composition_CO2 - 0.005)
					FDS_normalized_1_j = (FDS + unc_FDS - FDS_std)
					FDS_normalized_2_j = (FDS - unc_FDS - FDS_std)
					
					p00_j= 88.967
					p10_j= -377.311
					p01_j= 1118.943
					p20_j= 522.272
					p11_j= -2680.493
					p02_j= 121.155
					p30_j= -233.627
					p21_j= 2796.365
					p12_j= -757.074
					p03_j= 204.249
					p31_j= -1072.487
					p22_j= 552.456
					p13_j= -267.490
					p04_j= 38.666

					d00_j= 0.010280
					d10_j= -0.064068
					d01_j= 2.626929
					d20_j= 0.127033
					d11_j= -8.142853
					d02_j= 0.523089
					d30_j= -0.074232
					d21_j= 9.839291
					d12_j= -0.367180
					d03_j= -0.348974
					d31_j= -3.991261
					d22_j= -0.209187
					d13_j= 0.469233
					d04_j= -0.035452

					#### pressure calculation using CO2CH4 calibration (j)

					pressure3_j = (p00_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**0 
					+ p10_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**0 
					+ p01_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**1 
					+ p20_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**0
					+ p11_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**1 
					+ p02_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**2 
					+ p30_j*composition_CO2_normalized_1_j**3*FDS_normalized_2_j**0 
					+ p21_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**1
					+ p12_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**2 
					+ p03_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**3 
					+ p31_j*composition_CO2_normalized_1_j**3*FDS_normalized_2_j**1 
					+ p22_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**2
					+ p13_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**3 
					+ p04_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**4)

					pressure4_j = (p00_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**0 
					+ p10_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**0 
					+ p01_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**1 
					+ p20_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**0
					+ p11_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**1 
					+ p02_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**2 
					+ p30_j*composition_CO2_normalized_2_j**3*FDS_normalized_1_j**0 
					+ p21_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**1
					+ p12_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**2 
					+ p03_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**3 
					+ p31_j*composition_CO2_normalized_2_j**3*FDS_normalized_1_j**1 
					+ p22_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**2
					+ p13_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**3 
					+ p04_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**4)

					########################
					#### density calculation  using CO2CH4 calibration (i)


					density3_j = (d00_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**0 
					+ d10_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**0 
					+ d01_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**1 
					+ d20_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**0
					+ d11_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**1 
					+ d02_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**2 
					+ d30_j*composition_CO2_normalized_1_j**3*FDS_normalized_2_j**0 
					+ d21_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**1
					+ d12_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**2 
					+ d03_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**3 
					+ d31_j*composition_CO2_normalized_1_j**3*FDS_normalized_2_j**1 
					+ d22_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**2
					+ d13_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**3 
					+ d04_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**4)

					density4_j = (d00_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**0 
					+ d10_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**0 
					+ d01_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**1 
					+ d20_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**0
					+ d11_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**1 
					+ d02_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**2 
					+ d30_j*composition_CO2_normalized_2_j**3*FDS_normalized_1_j**0 
					+ d21_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**1
					+ d12_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**2 
					+ d03_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**3 
					+ d31_j*composition_CO2_normalized_2_j**3*FDS_normalized_1_j**1 
					+ d22_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**2
					+ d13_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**3 
					+ d04_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**4)              

					pressure_final_j = (max(pressure3_j, pressure4_j) + min(pressure3_j, pressure4_j))/2 #pressure max + pressure min
					uncer_pressure_final_j = 3 + (max(pressure3_j, pressure4_j) - min(pressure3_j, pressure4_j))/(2*np.sqrt(3))

					density_final_j = (max(density3_j, density4_j) + min(density3_j, density4_j))/2 #density max - density min
					uncer_density_final_j = 0.003 + (max(density3_j, density4_j) - min(density3_j, density4_j))/(2*np.sqrt(3))

					molarvolume3_j = 1/(max(density3_j, density4_j)/(44*composition_CO2 + 16*composition_CH4 + 28*composition_N2))
					molarvolume4_j = 1/(min(density3_j, density4_j)/(44*composition_CO2 + 16*composition_CH4 + 28*composition_N2))
					molarvolume_final_j = (molarvolume3_j + molarvolume4_j) / 2
					uncer_molarvolume_final_j = (molarvolume4_j - molarvolume3_j) / (2*np.sqrt(3))



			
				print('pressure3_j', pressure3_j)
				print('pressure4_j', pressure4_j)
				print('density 3_j=', density3_j)
				print('density 4_j=', density4_j)
				print("molarvolume3_j", molarvolume3_j)
				print("molarvolume4_j", molarvolume4_j)	
				if pressure_final_i > 650 or pressure3_i >650 or pressure4_i >650 or pressure_final_i < -20 or pressure3_i <-20 or pressure4_i <-20 or pressure_final_j > 650 or pressure3_j >650 or pressure4_j >650 or pressure_final_j < -20 or pressure3_j <-20 or pressure4_j <-20 or density3_i<0 or density4_i <0 or density3_j<0 or density4_j<0 or density_final_i<0 or density_final_j<0  :
					popupmsg_OCR()


				############ Calculation final pressure, density from pressure final i and j, depending on the concentration of CH4, N2 (coeff, a b within equation 8))
				############ and calculation uncertainty of FINAL RESULTS
				pressure_final = (composition_N2*pressure_final_j + composition_CH4*pressure_final_i)/(composition_N2 + composition_CH4) ## Equation 8 in the reference 2
				uncer_pressure_final = np.sqrt((composition_N2/(composition_N2+composition_CH4))**2*(uncer_pressure_final_j)**2 + (composition_CH4/(composition_N2+composition_CH4))**2*(uncer_pressure_final_i)**2)  ## base on the formule of the calulation of final_pressure above
				
				density_final = (composition_N2*density_final_j + composition_CH4*density_final_i)/(composition_N2 + composition_CH4) ## Equation 8 in the reference 2
				uncer_density_final = np.sqrt((composition_N2/(composition_N2+composition_CH4))**2*(uncer_density_final_j)**2 + (composition_CH4/(composition_N2+composition_CH4))**2*(uncer_density_final_i)**2)  ## base on the formule of the calulation of final_pressure above

				molarvolume_final = (composition_N2*molarvolume_final_j + composition_CH4*molarvolume_final_i)/(composition_N2 + composition_CH4)
				uncer_molarvolume_final = (uncer_molarvolume_final_j + uncer_molarvolume_final_i)/2

########################
########################

			if temperature.get() == 22 and instrument.get() == 2 and composition_CO2 < 0.5: 

				#coefficient of CO2CH4 calibration (i)
				composition_CO2_normalized_1_i = (composition_CO2 + 0.005)
				composition_CO2_normalized_2_i = (composition_CO2 - 0.005)
				FDS_normalized_1_i = (FDS + unc_FDS - FDS_std)
				FDS_normalized_2_i = (FDS - unc_FDS - FDS_std) 
				
				p00_i= 45.382
				p10_i= -437.060
				p01_i= -13.891
				p20_i= 1379.635
				p11_i= 9096.755
				p02_i= -385.162
				p30_i= -1398.590
				p21_i= -33996.147
				p12_i= -2105.436
				p03_i= 2163.473
				p31_i= 35077.079
				p22_i= 3647.292
				p13_i= -3723.511
				p04_i= 95.283


				d00_i= -0.028497
				d10_i= 0.446167
				d01_i= 0.823317
				d20_i= -1.795601
				d11_i= -0.498819
				d02_i= 0.067829
				d30_i= 2.075280
				d21_i= -0.668362
				d12_i= 0.985340
				d03_i= -0.587449
				d31_i= -0.193511
				d22_i= -1.604829
				d13_i= 1.174957
				d04_i= -0.054438

				#### pressure calculation using CO2CH4 calibration (i)

				pressure3_i = (p00_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**0 
				+ p10_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**0 
				+ p01_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**1 
				+ p20_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**0
				+ p11_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**1 
				+ p02_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**2 
				+ p30_i*composition_CO2_normalized_1_i**3*FDS_normalized_2_i**0 
				+ p21_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**1
				+ p12_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**2 
				+ p03_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**3 
				+ p31_i*composition_CO2_normalized_1_i**3*FDS_normalized_2_i**1 
				+ p22_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**2
				+ p13_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**3 
				+ p04_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**4)

				pressure4_i = (p00_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**0 
				+ p10_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**0 
				+ p01_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**1 
				+ p20_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**0
				+ p11_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**1 
				+ p02_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**2 
				+ p30_i*composition_CO2_normalized_2_i**3*FDS_normalized_1_i**0 
				+ p21_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**1
				+ p12_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**2 
				+ p03_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**3 
				+ p31_i*composition_CO2_normalized_2_i**3*FDS_normalized_1_i**1 
				+ p22_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**2
				+ p13_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**3 
				+ p04_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**4)

				########################
				#### density calculation  using CO2CH4 calibration (i)


				density3_i = (d00_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**0 
				+ d10_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**0 
				+ d01_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**1 
				+ d20_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**0
				+ d11_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**1 
				+ d02_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**2 
				+ d30_i*composition_CO2_normalized_1_i**3*FDS_normalized_2_i**0 
				+ d21_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**1
				+ d12_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**2 
				+ d03_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**3 
				+ d31_i*composition_CO2_normalized_1_i**3*FDS_normalized_2_i**1 
				+ d22_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**2
				+ d13_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**3 
				+ d04_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**4)

				density4_i = (d00_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**0 
				+ d10_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**0 
				+ d01_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**1 
				+ d20_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**0
				+ d11_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**1 
				+ d02_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**2 
				+ d30_i*composition_CO2_normalized_2_i**3*FDS_normalized_1_i**0 
				+ d21_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**1
				+ d12_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**2 
				+ d03_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**3 
				+ d31_i*composition_CO2_normalized_2_i**3*FDS_normalized_1_i**1 
				+ d22_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**2
				+ d13_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**3 
				+ d04_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**4)              

				pressure_final_i = (max(pressure3_i, pressure4_i) + min(pressure3_i, pressure4_i))/2 #pressure max + pressure min
				uncer_pressure_final_i = 11 + (max(pressure3_i, pressure4_i) - min(pressure3_i, pressure4_i))/(2*np.sqrt(3))

				density_final_i = (max(density3_i, density4_i) + min(density3_i, density4_i))/2 #density max - density min
				uncer_density_final_i = 0.0049 + (max(density3_i, density4_i) - min(density3_i, density4_i))/(2*np.sqrt(3))

				molarvolume3_i = 1/(max(density3_i, density4_i)/(44*composition_CO2 + 16*composition_CH4 + 28*composition_N2))
				molarvolume4_i = 1/(min(density3_i, density4_i)/(44*composition_CO2 + 16*composition_CH4 + 28*composition_N2))
				molarvolume_final_i = (molarvolume3_i + molarvolume4_i) / 2
				uncer_molarvolume_final_i = (molarvolume4_i - molarvolume3_i) / (2*np.sqrt(3))



				##### verify if measured pressure < 160 bar, if it is, re-recalculte using calibration data for 5-160 bar range.
				if pressure_final_i <= 150: 

					## Calibration equation's coeff of CO2-CH4 at 22 °C over 5-160 bars
					# normalisation of concentration and of Fermi diad splitting
					
					#coefficient of CO2CH4 calibration (i)
					composition_CO2_normalized_1_i = (composition_CO2 + 0.005)
					composition_CO2_normalized_2_i = (composition_CO2 - 0.005)
					FDS_normalized_1_i = (FDS + unc_FDS - FDS_std)
					FDS_normalized_2_i = (FDS - unc_FDS - FDS_std)
					
					
					p00_i= -18.197
					p10_i= 291.460
					p01_i= 853.921
					p20_i= -1096.748
					p11_i= 413.727
					p02_i= -1397.053
					p30_i= 1181.763
					p21_i= -7348.360
					p12_i= 5112.146
					p03_i= 249.588
					p31_i= 9121.890
					p22_i= -6356.070
					p13_i= 208.556
					p04_i= -35.643


					d00_i= -0.015283
					d10_i= 0.250370
					d01_i= 0.817400
					d20_i= -0.924644
					d11_i= -0.526408
					d02_i= 0.290467
					d30_i= 0.972751
					d21_i= -3.491540
					d12_i= 5.508150
					d03_i= -3.529910
					d31_i= 6.275225
					d22_i= -12.943609
					d13_i= 8.131834
					d04_i= -0.328421

					#### pressure calculation using CO2CH4 calibration (i)

					pressure3_i = (p00_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**0 
					+ p10_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**0 
					+ p01_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**1 
					+ p20_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**0
					+ p11_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**1 
					+ p02_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**2 
					+ p30_i*composition_CO2_normalized_1_i**3*FDS_normalized_2_i**0 
					+ p21_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**1
					+ p12_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**2 
					+ p03_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**3 
					+ p31_i*composition_CO2_normalized_1_i**3*FDS_normalized_2_i**1 
					+ p22_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**2
					+ p13_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**3 
					+ p04_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**4)

					pressure4_i = (p00_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**0 
					+ p10_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**0 
					+ p01_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**1 
					+ p20_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**0
					+ p11_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**1 
					+ p02_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**2 
					+ p30_i*composition_CO2_normalized_2_i**3*FDS_normalized_1_i**0 
					+ p21_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**1
					+ p12_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**2 
					+ p03_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**3 
					+ p31_i*composition_CO2_normalized_2_i**3*FDS_normalized_1_i**1 
					+ p22_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**2
					+ p13_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**3 
					+ p04_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**4)

					########################
					#### density calculation  using CO2CH4 calibration (i)


					density3_i = (d00_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**0 
					+ d10_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**0 
					+ d01_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**1 
					+ d20_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**0
					+ d11_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**1 
					+ d02_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**2 
					+ d30_i*composition_CO2_normalized_1_i**3*FDS_normalized_2_i**0 
					+ d21_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**1
					+ d12_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**2 
					+ d03_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**3 
					+ d31_i*composition_CO2_normalized_1_i**3*FDS_normalized_2_i**1 
					+ d22_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**2
					+ d13_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**3 
					+ d04_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**4)

					density4_i = (d00_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**0 
					+ d10_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**0 
					+ d01_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**1 
					+ d20_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**0
					+ d11_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**1 
					+ d02_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**2 
					+ d30_i*composition_CO2_normalized_2_i**3*FDS_normalized_1_i**0 
					+ d21_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**1
					+ d12_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**2 
					+ d03_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**3 
					+ d31_i*composition_CO2_normalized_2_i**3*FDS_normalized_1_i**1 
					+ d22_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**2
					+ d13_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**3 
					+ d04_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**4)              

					pressure_final_i = (max(pressure3_i, pressure4_i) + min(pressure3_i, pressure4_i))/2 #pressure max + pressure min
					uncer_pressure_final_i = 7 + (max(pressure3_i, pressure4_i) - min(pressure3_i, pressure4_i))/(2*np.sqrt(3))

					density_final_i = (max(density3_i, density4_i) + min(density3_i, density4_i))/2 #density max - density min
					uncer_density_final_i = 0.0049 + (max(density3_i, density4_i) - min(density3_i, density4_i))/(2*np.sqrt(3))

					molarvolume3_i = 1/(max(density3_i, density4_i)/(44*composition_CO2 + 16*composition_CH4 + 28*composition_N2))
					molarvolume4_i = 1/(min(density3_i, density4_i)/(44*composition_CO2 + 16*composition_CH4 + 28*composition_N2))
					molarvolume_final_i = (molarvolume3_i + molarvolume4_i) / 2
					uncer_molarvolume_final_i = (molarvolume4_i - molarvolume3_i) / (2*np.sqrt(3))


			
				print('pressure3_i', pressure3_i)
				print('pressure4_i', pressure4_i)
				print('density 3_i=', density3_i)
				print('density 4_i=', density4_i)
				print("molarvolume3_i", molarvolume3_i)
				print("molarvolume4_i", molarvolume4_i)	
				

				#################################
				#coefficient of CO2 N2 calibration (j)
				############################"""
				composition_CO2_normalized_1_j = (composition_CO2 + 0.005 )
				composition_CO2_normalized_2_j = (composition_CO2 - 0.005 )
				FDS_normalized_1_j = (FDS + unc_FDS - FDS_std)
				FDS_normalized_2_j = (FDS - unc_FDS - FDS_std)
				
				
				p00_j= 1.955
				p10_j= 147.811
				p01_j= 1682.405
				p20_j= -844.985
				p11_j= -9024.047
				p02_j= 1402.170
				p30_j= 1091.816
				p21_j= 26032.684
				p12_j= -11773.206
				p03_j= 2319.004
				p31_j= -26651.658
				p22_j= 17438.386
				p13_j= -4651.095
				p04_j= 205.721
				
				d00_j= 0.035844
				d10_j= -0.397086
				d01_j= 1.877266
				d20_j= 1.398697
				d11_j= -4.921546
				d02_j= -0.713235
				d30_j= -1.505246
				d21_j= 2.879115
				d12_j= 5.144878
				d03_j= -0.405858
				d31_j= 3.153925
				d22_j= -6.276756
				d13_j= 0.431299
				d04_j= 0.005927

				#### pressure calculation using CO2CH4 calibration (j)

				pressure3_j = (p00_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**0 
				+ p10_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**0 
				+ p01_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**1 
				+ p20_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**0
				+ p11_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**1 
				+ p02_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**2 
				+ p30_j*composition_CO2_normalized_1_j**3*FDS_normalized_2_j**0 
				+ p21_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**1
				+ p12_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**2 
				+ p03_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**3 
				+ p31_j*composition_CO2_normalized_1_j**3*FDS_normalized_2_j**1 
				+ p22_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**2
				+ p13_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**3 
				+ p04_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**4)

				pressure4_j = (p00_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**0 
				+ p10_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**0 
				+ p01_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**1 
				+ p20_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**0
				+ p11_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**1 
				+ p02_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**2 
				+ p30_j*composition_CO2_normalized_2_j**3*FDS_normalized_1_j**0 
				+ p21_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**1
				+ p12_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**2 
				+ p03_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**3 
				+ p31_j*composition_CO2_normalized_2_j**3*FDS_normalized_1_j**1 
				+ p22_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**2
				+ p13_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**3 
				+ p04_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**4)

				########################
				#### density calculation  using CO2CH4 calibration (i)


				density3_j = (d00_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**0 
				+ d10_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**0 
				+ d01_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**1 
				+ d20_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**0
				+ d11_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**1 
				+ d02_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**2 
				+ d30_j*composition_CO2_normalized_1_j**3*FDS_normalized_2_j**0 
				+ d21_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**1
				+ d12_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**2 
				+ d03_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**3 
				+ d31_j*composition_CO2_normalized_1_j**3*FDS_normalized_2_j**1 
				+ d22_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**2
				+ d13_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**3 
				+ d04_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**4)

				density4_j = (d00_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**0 
				+ d10_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**0 
				+ d01_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**1 
				+ d20_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**0
				+ d11_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**1 
				+ d02_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**2 
				+ d30_j*composition_CO2_normalized_2_j**3*FDS_normalized_1_j**0 
				+ d21_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**1
				+ d12_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**2 
				+ d03_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**3 
				+ d31_j*composition_CO2_normalized_2_j**3*FDS_normalized_1_j**1 
				+ d22_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**2
				+ d13_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**3 
				+ d04_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**4)              

				pressure_final_j = (max(pressure3_j, pressure4_j) + min(pressure3_j, pressure4_j))/2 #pressure max + pressure min
				uncer_pressure_final_j = 7 + (max(pressure3_j, pressure4_j) - min(pressure3_j, pressure4_j))/(2*np.sqrt(3))

				density_final_j = (max(density3_j, density4_j) + min(density3_j, density4_j))/2 #density max - density min
				uncer_density_final_j = 0.0049 + (max(density3_j, density4_j) - min(density3_j, density4_j))/(2*np.sqrt(3))

				molarvolume3_j = 1/(max(density3_j, density4_j)/(44*composition_CO2 + 16*composition_CH4 + 28*composition_N2))
				molarvolume4_j = 1/(min(density3_j, density4_j)/(44*composition_CO2 + 16*composition_CH4 + 28*composition_N2))
				molarvolume_final_j = (molarvolume3_j + molarvolume4_j) / 2
				uncer_molarvolume_final_j = (molarvolume4_j - molarvolume3_j) / (2*np.sqrt(3))



				##### verify if measured pressure < 160 bar, if it is, re-recalculte using calibration data for 5-160 bar range.
				if pressure_final_j <= 150: 

					## Calibration equation's coeff of CO2-CH4 at 22 °C over 5-160 bars
					# normalisation of concentration and of Fermi diad splitting
					
					#coefficient of CO2CH4 calibration (j)
					composition_CO2_normalized_1_j = (composition_CO2 + 0.005)
					composition_CO2_normalized_2_j = (composition_CO2 - 0.005)
					FDS_normalized_1_j = (FDS + unc_FDS - FDS_std)
					FDS_normalized_2_j = (FDS - unc_FDS - FDS_std)
					
					p00_j= 8.931
					p10_j= -50.301
					p01_j= 1814.667
					p20_j= 29.398
					p11_j= -7550.765
					p02_j= -406.409
					p30_j= 70.929
					p21_j= 17082.171
					p12_j= -6973.173
					p03_j= 5905.099
					p31_j= -15617.520
					p22_j= 15041.744
					p13_j= -11712.853
					p04_j= 44.608

					d00_j= 0.011260
					d10_j= -0.070292
					d01_j= 2.107761
					d20_j= 0.065704
					d11_j= -7.480476
					d02_j= -0.621856
					d30_j= 0.061639
					d21_j= 15.938249
					d12_j= -6.107679
					d03_j= 6.501687
					d31_j= -14.697989
					d22_j= 16.066299
					d13_j= -13.570084
					d04_j= 0.072953

					#### pressure calculation using CO2CH4 calibration (j)

					pressure3_j = (p00_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**0 
					+ p10_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**0 
					+ p01_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**1 
					+ p20_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**0
					+ p11_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**1 
					+ p02_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**2 
					+ p30_j*composition_CO2_normalized_1_j**3*FDS_normalized_2_j**0 
					+ p21_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**1
					+ p12_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**2 
					+ p03_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**3 
					+ p31_j*composition_CO2_normalized_1_j**3*FDS_normalized_2_j**1 
					+ p22_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**2
					+ p13_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**3 
					+ p04_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**4)

					pressure4_j = (p00_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**0 
					+ p10_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**0 
					+ p01_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**1 
					+ p20_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**0
					+ p11_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**1 
					+ p02_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**2 
					+ p30_j*composition_CO2_normalized_2_j**3*FDS_normalized_1_j**0 
					+ p21_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**1
					+ p12_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**2 
					+ p03_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**3 
					+ p31_j*composition_CO2_normalized_2_j**3*FDS_normalized_1_j**1 
					+ p22_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**2
					+ p13_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**3 
					+ p04_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**4)

					########################
					#### density calculation  using CO2CH4 calibration (i)


					density3_j = (d00_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**0 
					+ d10_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**0 
					+ d01_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**1 
					+ d20_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**0
					+ d11_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**1 
					+ d02_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**2 
					+ d30_j*composition_CO2_normalized_1_j**3*FDS_normalized_2_j**0 
					+ d21_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**1
					+ d12_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**2 
					+ d03_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**3 
					+ d31_j*composition_CO2_normalized_1_j**3*FDS_normalized_2_j**1 
					+ d22_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**2
					+ d13_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**3 
					+ d04_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**4)

					density4_j = (d00_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**0 
					+ d10_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**0 
					+ d01_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**1 
					+ d20_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**0
					+ d11_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**1 
					+ d02_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**2 
					+ d30_j*composition_CO2_normalized_2_j**3*FDS_normalized_1_j**0 
					+ d21_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**1
					+ d12_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**2 
					+ d03_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**3 
					+ d31_j*composition_CO2_normalized_2_j**3*FDS_normalized_1_j**1 
					+ d22_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**2
					+ d13_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**3 
					+ d04_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**4)              

					pressure_final_j = (max(pressure3_j, pressure4_j) + min(pressure3_j, pressure4_j))/2 #pressure max + pressure min
					uncer_pressure_final_j = 3 + (max(pressure3_j, pressure4_j) - min(pressure3_j, pressure4_j))/(2*np.sqrt(3))

					density_final_j = (max(density3_j, density4_j) + min(density3_j, density4_j))/2 #density max - density min
					uncer_density_final_j = 0.004 + (max(density3_j, density4_j) - min(density3_j, density4_j))/(2*np.sqrt(3))

					molarvolume3_j = 1/(max(density3_j, density4_j)/(44*composition_CO2 + 16*composition_CH4 + 28*composition_N2))
					molarvolume4_j = 1/(min(density3_j, density4_j)/(44*composition_CO2 + 16*composition_CH4 + 28*composition_N2))
					molarvolume_final_j = (molarvolume3_j + molarvolume4_j) / 2
					uncer_molarvolume_final_j = (molarvolume4_j - molarvolume3_j) / (2*np.sqrt(3))


			
				print('pressure3_j', pressure3_j)
				print('pressure4_j', pressure4_j)
				print('density 3_j=', density3_j)
				print('density 4_j=', density4_j)
				print("molarvolume3_i", molarvolume3_j)
				print("molarvolume4_i", molarvolume4_j)	
				if pressure_final_i > 650 or pressure3_i >650 or pressure4_i >650 or pressure_final_i < -20 or pressure3_i <-20 or pressure4_i <-20 or pressure_final_j > 650 or pressure3_j >650 or pressure4_j >650 or pressure_final_j < -20 or pressure3_j <-20 or pressure4_j <-20 or density3_i<0 or density4_i <0 or density3_j<0 or density4_j<0 or density_final_i<0 or density_final_j<0 :
					popupmsg_OCR()


				############ Calculation final pressure, density from pressure final i and j, depending on the concentration of CH4, N2 (coeff, a b within equation 8))
				############ and calculation uncertainty of FINAL RESULTS
				pressure_final = (composition_N2*pressure_final_j + composition_CH4*pressure_final_i)/(composition_N2 + composition_CH4) ## Equation 8 in the reference 2
				uncer_pressure_final = np.sqrt((composition_N2/(composition_N2+composition_CH4))**2*(uncer_pressure_final_j)**2 + (composition_CH4/(composition_N2+composition_CH4))**2*(uncer_pressure_final_i)**2)  ## base on the formule of the calulation of final_pressure above
				
				density_final = (composition_N2*density_final_j + composition_CH4*density_final_i)/(composition_N2 + composition_CH4) ## Equation 8 in the reference 2
				uncer_density_final = np.sqrt((composition_N2/(composition_N2+composition_CH4))**2*(uncer_density_final_j)**2 + (composition_CH4/(composition_N2+composition_CH4))**2*(uncer_density_final_i)**2)  ## base on the formule of the calulation of final_pressure above

				molarvolume_final = (composition_N2*molarvolume_final_j + composition_CH4*molarvolume_final_i)/(composition_N2 + composition_CH4)
				uncer_molarvolume_final = (uncer_molarvolume_final_j + uncer_molarvolume_final_i)/2

################################
####### 32 °C ##################
#################################

			if temperature.get() == 32 and instrument.get() == 2 and composition_CO2 >= 0.5: 

				#coefficient of CO2CH4 calibration (i)
				composition_CO2_normalized_1_i = (composition_CO2 + 0.005 )
				composition_CO2_normalized_2_i = (composition_CO2 - 0.005 )
				FDS_normalized_1_i = (FDS + unc_FDS - FDS_std)
				FDS_normalized_2_i = (FDS - unc_FDS - FDS_std)
				
				p00_i= -105.913
				p10_i= 631.841
				p01_i= 1192.786
				p20_i= -1078.549
				p11_i= -4347.619
				p02_i= 758.153
				p30_i= 554.031
				p21_i= 6980.102
				p12_i= -3305.090
				p03_i= 631.878
				p31_i= -3652.934
				p22_i= 2458.432
				p13_i= -679.754
				p04_i= 34.686
				
				d00_i= 0.267075
				d10_i= -1.169842
				d01_i= 0.816076
				d20_i= 1.651565
				d11_i= -0.872643
				d02_i= -0.055892
				d30_i= -0.745041
				d21_i= 0.1121156
				d12_i= 0.7575122
				d03_i= -0.1854704
				d31_i= 0.2196812
				d22_i= -0.5740299
				d13_i= 0.1726441
				d04_i= -0.0071123

				#### pressure calculation using CO2CH4 calibration (i)

				pressure3_i = (p00_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**0 
				+ p10_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**0 
				+ p01_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**1 
				+ p20_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**0
				+ p11_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**1 
				+ p02_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**2 
				+ p30_i*composition_CO2_normalized_1_i**3*FDS_normalized_2_i**0 
				+ p21_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**1
				+ p12_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**2 
				+ p03_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**3 
				+ p31_i*composition_CO2_normalized_1_i**3*FDS_normalized_2_i**1 
				+ p22_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**2
				+ p13_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**3 
				+ p04_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**4)

				pressure4_i = (p00_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**0 
				+ p10_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**0 
				+ p01_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**1 
				+ p20_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**0
				+ p11_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**1 
				+ p02_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**2 
				+ p30_i*composition_CO2_normalized_2_i**3*FDS_normalized_1_i**0 
				+ p21_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**1
				+ p12_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**2 
				+ p03_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**3 
				+ p31_i*composition_CO2_normalized_2_i**3*FDS_normalized_1_i**1 
				+ p22_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**2
				+ p13_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**3 
				+ p04_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**4)

				########################
				#### density calculation  using CO2CH4 calibration (i)


				density3_i = (d00_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**0 
				+ d10_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**0 
				+ d01_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**1 
				+ d20_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**0
				+ d11_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**1 
				+ d02_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**2 
				+ d30_i*composition_CO2_normalized_1_i**3*FDS_normalized_2_i**0 
				+ d21_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**1
				+ d12_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**2 
				+ d03_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**3 
				+ d31_i*composition_CO2_normalized_1_i**3*FDS_normalized_2_i**1 
				+ d22_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**2
				+ d13_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**3 
				+ d04_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**4)

				density4_i = (d00_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**0 
				+ d10_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**0 
				+ d01_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**1 
				+ d20_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**0
				+ d11_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**1 
				+ d02_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**2 
				+ d30_i*composition_CO2_normalized_2_i**3*FDS_normalized_1_i**0 
				+ d21_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**1
				+ d12_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**2 
				+ d03_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**3 
				+ d31_i*composition_CO2_normalized_2_i**3*FDS_normalized_1_i**1 
				+ d22_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**2
				+ d13_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**3 
				+ d04_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**4)              

				pressure_final_i = (max(pressure3_i, pressure4_i) + min(pressure3_i, pressure4_i))/2 #pressure max + pressure min
				uncer_pressure_final_i = 7 + (max(pressure3_i, pressure4_i) - min(pressure3_i, pressure4_i))/(2*np.sqrt(3))

				density_final_i = (max(density3_i, density4_i) + min(density3_i, density4_i))/2 #density max - density min
				uncer_density_final_i = 0.0057 + (max(density3_i, density4_i) - min(density3_i, density4_i))/(2*np.sqrt(3))

				molarvolume3_i = 1/(max(density3_i, density4_i)/(44*composition_CO2 + 16*composition_CH4 + 28*composition_N2))
				molarvolume4_i = 1/(min(density3_i, density4_i)/(44*composition_CO2 + 16*composition_CH4 + 28*composition_N2))
				molarvolume_final_i = (molarvolume3_i + molarvolume4_i) / 2
				uncer_molarvolume_final_i = (molarvolume4_i - molarvolume3_i) / (2*np.sqrt(3))



				##### verify if measured pressure < 160 bar, if it is, re-recalculte using calibration data for 5-160 bar range.
				if pressure_final_i <= 150: 

					## Calibration equation's coeff of CO2-CH4 at 32 °C over 5-160 bars
					# normalisation of concentration and of Fermi diad splitting
					
					#coefficient of CO2CH4 calibration (i)
					composition_CO2_normalized_1_i = (composition_CO2 + 0.005)
					composition_CO2_normalized_2_i = (composition_CO2 - 0.005)
					FDS_normalized_1_i = (FDS + unc_FDS - FDS_std)
					FDS_normalized_2_i = (FDS - unc_FDS - FDS_std)
					
					p00_i= 141.952
					p10_i= -579.239
					p01_i= 614.574
					p20_i= 760.306
					p11_i= -598.096
					p02_i= -207.733
					p30_i= -322.119
					p21_i= 255.994
					p12_i= -483.570
					p03_i= 401.280
					p31_i= -109.853
					p22_i= 637.310
					p13_i= -475.666
					p04_i= 40.255

					d00_i= 0.254772
					d10_i= -1.082592
					d01_i= 0.762897
					d20_i= 1.481580
					d11_i= -0.893355
					d02_i= 0.113777
					d30_i= -0.658874
					d21_i= 0.673482 
					d12_i= -0.138406
					d03_i= 0.027368
					d31_i= -0.161483
					d22_i= -0.100446
					d13_i= 0.156471
					d04_i= -0.055429

					#### pressure calculation using CO2CH4 calibration (i)

					pressure3_i = (p00_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**0 
					+ p10_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**0 
					+ p01_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**1 
					+ p20_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**0
					+ p11_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**1 
					+ p02_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**2 
					+ p30_i*composition_CO2_normalized_1_i**3*FDS_normalized_2_i**0 
					+ p21_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**1
					+ p12_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**2 
					+ p03_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**3 
					+ p31_i*composition_CO2_normalized_1_i**3*FDS_normalized_2_i**1 
					+ p22_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**2
					+ p13_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**3 
					+ p04_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**4)

					pressure4_i = (p00_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**0 
					+ p10_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**0 
					+ p01_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**1 
					+ p20_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**0
					+ p11_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**1 
					+ p02_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**2 
					+ p30_i*composition_CO2_normalized_2_i**3*FDS_normalized_1_i**0 
					+ p21_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**1
					+ p12_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**2 
					+ p03_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**3 
					+ p31_i*composition_CO2_normalized_2_i**3*FDS_normalized_1_i**1 
					+ p22_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**2
					+ p13_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**3 
					+ p04_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**4)

					########################
					#### density calculation  using CO2CH4 calibration (i)


					density3_i = (d00_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**0 
					+ d10_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**0 
					+ d01_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**1 
					+ d20_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**0
					+ d11_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**1 
					+ d02_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**2 
					+ d30_i*composition_CO2_normalized_1_i**3*FDS_normalized_2_i**0 
					+ d21_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**1
					+ d12_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**2 
					+ d03_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**3 
					+ d31_i*composition_CO2_normalized_1_i**3*FDS_normalized_2_i**1 
					+ d22_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**2
					+ d13_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**3 
					+ d04_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**4)

					density4_i = (d00_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**0 
					+ d10_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**0 
					+ d01_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**1 
					+ d20_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**0
					+ d11_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**1 
					+ d02_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**2 
					+ d30_i*composition_CO2_normalized_2_i**3*FDS_normalized_1_i**0 
					+ d21_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**1
					+ d12_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**2 
					+ d03_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**3 
					+ d31_i*composition_CO2_normalized_2_i**3*FDS_normalized_1_i**1 
					+ d22_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**2
					+ d13_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**3 
					+ d04_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**4)              

					pressure_final_i = (max(pressure3_i, pressure4_i) + min(pressure3_i, pressure4_i))/2 #pressure max + pressure min
					uncer_pressure_final_i = 4.2 + (max(pressure3_i, pressure4_i) - min(pressure3_i, pressure4_i))/(2*np.sqrt(3))

					density_final_i = (max(density3_i, density4_i) + min(density3_i, density4_i))/2 #density max - density min
					uncer_density_final_i = 0.0057 + (max(density3_i, density4_i) - min(density3_i, density4_i))/(2*np.sqrt(3))

					molarvolume3_i = 1/(max(density3_i, density4_i)/(44*composition_CO2 + 16*composition_CH4 + 28*composition_N2))
					molarvolume4_i = 1/(min(density3_i, density4_i)/(44*composition_CO2 + 16*composition_CH4 + 28*composition_N2))
					molarvolume_final_i = (molarvolume3_i + molarvolume4_i) / 2
					uncer_molarvolume_final_i = (molarvolume4_i - molarvolume3_i) / (2*np.sqrt(3))

			
				print('pressure3_i', pressure3_i)
				print('pressure4_i', pressure4_i)
				print('density 3_i=', density3_i)
				print('density 4_i=', density4_i)
				print("molarvolume3_i", molarvolume3_i)
				print("molarvolume4_i", molarvolume4_i)	
				

				#################################
				#coefficient of CO2 N2 calibration (j)
				############################"""
				composition_CO2_normalized_1_j = (composition_CO2 + 0.005)
				composition_CO2_normalized_2_j = (composition_CO2 - 0.005)
				FDS_normalized_1_j = (FDS + unc_FDS - FDS_std)
				FDS_normalized_2_j = (FDS - unc_FDS - FDS_std)
				
				p00_j= -141.222
				p10_j= 682.710
				p01_j= 2377.959
				p20_j= -1033.802
				p11_j= -8587.547
				p02_j= 782.696
				p30_j= 492.546
				p21_j= 11797.178
				p12_j= -2971.818
				p03_j= 533.510
				p31_j= -5410.457
				p22_j= 2092.099
				p13_j= -576.573
				p04_j= 33.948

				d00_j= 0.322557
				d10_j= -1.373203
				d01_j= 1.982120
				d20_j= 1.901505
				d11_j= -5.113733
				d02_j= 0.073184
				d30_j= -0.848128
				d21_j= 5.307588
				d12_j= 0.589915
				d03_j= -0.209968
				d31_j= -1.909427
				d22_j= -0.462021
				d13_j= 0.135753
				d04_j= 0.006276

				#### pressure calculation using CO2N2 calibration (j)

				pressure3_j = (p00_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**0 
				+ p10_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**0 
				+ p01_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**1 
				+ p20_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**0
				+ p11_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**1 
				+ p02_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**2 
				+ p30_j*composition_CO2_normalized_1_j**3*FDS_normalized_2_j**0 
				+ p21_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**1
				+ p12_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**2 
				+ p03_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**3 
				+ p31_j*composition_CO2_normalized_1_j**3*FDS_normalized_2_j**1 
				+ p22_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**2
				+ p13_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**3 
				+ p04_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**4)

				pressure4_j = (p00_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**0 
				+ p10_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**0 
				+ p01_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**1 
				+ p20_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**0
				+ p11_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**1 
				+ p02_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**2 
				+ p30_j*composition_CO2_normalized_2_j**3*FDS_normalized_1_j**0 
				+ p21_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**1
				+ p12_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**2 
				+ p03_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**3 
				+ p31_j*composition_CO2_normalized_2_j**3*FDS_normalized_1_j**1 
				+ p22_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**2
				+ p13_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**3 
				+ p04_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**4)

				########################
				#### density calculation  using CO2N2 calibration (j)


				density3_j = (d00_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**0 
				+ d10_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**0 
				+ d01_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**1 
				+ d20_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**0
				+ d11_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**1 
				+ d02_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**2 
				+ d30_j*composition_CO2_normalized_1_j**3*FDS_normalized_2_j**0 
				+ d21_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**1
				+ d12_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**2 
				+ d03_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**3 
				+ d31_j*composition_CO2_normalized_1_j**3*FDS_normalized_2_j**1 
				+ d22_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**2
				+ d13_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**3 
				+ d04_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**4)

				density4_j = (d00_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**0 
				+ d10_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**0 
				+ d01_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**1 
				+ d20_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**0
				+ d11_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**1 
				+ d02_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**2 
				+ d30_j*composition_CO2_normalized_2_j**3*FDS_normalized_1_j**0 
				+ d21_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**1
				+ d12_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**2 
				+ d03_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**3 
				+ d31_j*composition_CO2_normalized_2_j**3*FDS_normalized_1_j**1 
				+ d22_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**2
				+ d13_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**3 
				+ d04_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**4)              

				pressure_final_j = (max(pressure3_j, pressure4_j) + min(pressure3_j, pressure4_j))/2 #pressure max + pressure min
				uncer_pressure_final_j = 7.8 + (max(pressure3_j, pressure4_j) - min(pressure3_j, pressure4_j))/(2*np.sqrt(3))

				density_final_j = (max(density3_j, density4_j) + min(density3_j, density4_j))/2 #density max - density min
				uncer_density_final_j = 0.0057 + (max(density3_j, density4_j) - min(density3_j, density4_j))/(2*np.sqrt(3))

				molarvolume3_j = 1/(max(density3_j, density4_j)/(44*composition_CO2 + 16*composition_CH4 + 28*composition_N2))
				molarvolume4_j = 1/(min(density3_j, density4_j)/(44*composition_CO2 + 16*composition_CH4 + 28*composition_N2))
				molarvolume_final_j = (molarvolume3_j + molarvolume4_j) / 2
				uncer_molarvolume_final_j = (molarvolume4_j - molarvolume3_j) / (2*np.sqrt(3))



				##### verify if measured pressure < 160 bar, if it is, re-recalculte using calibration data for 5-160 bar range.
				if pressure_final_j <= 150: 

					## Calibration equation's coeff of CO2-CH4 at 22 °C over 5-160 bars
					# normalisation of concentration and of Fermi diad splitting
					
					#coefficient of CO2N2 calibration (j)
					composition_CO2_normalized_1_j = (composition_CO2 + 0.005 )
					composition_CO2_normalized_2_j = (composition_CO2 - 0.005 )
					FDS_normalized_1_j = (FDS + unc_FDS - FDS_std)
					FDS_normalized_2_j = (FDS - unc_FDS - FDS_std)
					
					p00_j= 44.653
					p10_j= -178.218
					p01_j= 1317.024
					p20_j= 228.764
					p11_j= -3376.477
					p02_j= 63.581
					p30_j= -94.070
					p21_j= 3759.578
					p12_j= -848.445
					p03_j= 348.836
					p31_j= -1534.820
					p22_j= 721.8
					p13_j= -415.550
					p04_j= 38.401

					d00_j= 0.014508
					d10_j= -0.086464
					d01_j= 2.409656
					d20_j= 0.152268
					d11_j= -6.734110
					d02_j= -0.116314
					d30_j= -0.074937
					d21_j= 7.477710
					d12_j= 0.807514
					d03_j= -0.136942
					d31_j= -2.902051
					d22_j= -0.460642
					d13_j= 0.040956
					d04_j= 0.011606

					#### pressure calculation using CO2CH4 calibration (j)

					pressure3_j = (p00_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**0 
					+ p10_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**0 
					+ p01_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**1 
					+ p20_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**0
					+ p11_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**1 
					+ p02_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**2 
					+ p30_j*composition_CO2_normalized_1_j**3*FDS_normalized_2_j**0 
					+ p21_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**1
					+ p12_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**2 
					+ p03_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**3 
					+ p31_j*composition_CO2_normalized_1_j**3*FDS_normalized_2_j**1 
					+ p22_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**2
					+ p13_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**3 
					+ p04_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**4)

					pressure4_j = (p00_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**0 
					+ p10_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**0 
					+ p01_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**1 
					+ p20_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**0
					+ p11_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**1 
					+ p02_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**2 
					+ p30_j*composition_CO2_normalized_2_j**3*FDS_normalized_1_j**0 
					+ p21_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**1
					+ p12_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**2 
					+ p03_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**3 
					+ p31_j*composition_CO2_normalized_2_j**3*FDS_normalized_1_j**1 
					+ p22_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**2
					+ p13_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**3 
					+ p04_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**4)

					########################
					#### density calculation  using CO2CH4 calibration (i)


					density3_j = (d00_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**0 
					+ d10_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**0 
					+ d01_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**1 
					+ d20_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**0
					+ d11_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**1 
					+ d02_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**2 
					+ d30_j*composition_CO2_normalized_1_j**3*FDS_normalized_2_j**0 
					+ d21_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**1
					+ d12_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**2 
					+ d03_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**3 
					+ d31_j*composition_CO2_normalized_1_j**3*FDS_normalized_2_j**1 
					+ d22_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**2
					+ d13_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**3 
					+ d04_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**4)

					density4_j = (d00_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**0 
					+ d10_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**0 
					+ d01_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**1 
					+ d20_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**0
					+ d11_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**1 
					+ d02_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**2 
					+ d30_j*composition_CO2_normalized_2_j**3*FDS_normalized_1_j**0 
					+ d21_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**1
					+ d12_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**2 
					+ d03_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**3 
					+ d31_j*composition_CO2_normalized_2_j**3*FDS_normalized_1_j**1 
					+ d22_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**2
					+ d13_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**3 
					+ d04_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**4)              

					pressure_final_j = (max(pressure3_j, pressure4_j) + min(pressure3_j, pressure4_j))/2 #pressure max + pressure min
					uncer_pressure_final_j = 3 + (max(pressure3_j, pressure4_j) - min(pressure3_j, pressure4_j))/(2*np.sqrt(3))

					density_final_j = (max(density3_j, density4_j) + min(density3_j, density4_j))/2 #density max - density min
					uncer_density_final_j = 0.0042 + (max(density3_j, density4_j) - min(density3_j, density4_j))/(2*np.sqrt(3))

					molarvolume3_j = 1/(max(density3_j, density4_j)/(44*composition_CO2 + 16*composition_CH4 + 28*composition_N2))
					molarvolume4_j = 1/(min(density3_j, density4_j)/(44*composition_CO2 + 16*composition_CH4 + 28*composition_N2))
					molarvolume_final_j = (molarvolume3_j + molarvolume4_j) / 2
					uncer_molarvolume_final_j = (molarvolume4_j - molarvolume3_j) / (2*np.sqrt(3))



			
				print('pressure3_j', pressure3_j)
				print('pressure4_j', pressure4_j)
				print('density 3_j=', density3_j)
				print('density 4_j=', density4_j)
				print("molarvolume3_j", molarvolume3_j)
				print("molarvolume4_j", molarvolume4_j)	
				if pressure_final_i > 650 or pressure3_i >650 or pressure4_i >650 or pressure_final_i < -20 or pressure3_i <-20 or pressure4_i <-20 or pressure_final_j > 650 or pressure3_j >650 or pressure4_j >650 or pressure_final_j < -20 or pressure3_j <-20 or pressure4_j <-20 or density3_i<0 or density4_i <0 or density3_j<0 or density4_j<0 or density_final_i<0 or density_final_j<0 :
					popupmsg_OCR()


				############ Calculation final pressure, density from pressure final i and j, depending on the concentration of CH4, N2 (coeff, a b within equation 8))
				############ and calculation uncertainty of FINAL RESULTS
				pressure_final = (composition_N2*pressure_final_j + composition_CH4*pressure_final_i)/(composition_N2 + composition_CH4) ## Equation 8 in the reference 2
				uncer_pressure_final = np.sqrt((composition_N2/(composition_N2+composition_CH4))**2*(uncer_pressure_final_j)**2 + (composition_CH4/(composition_N2+composition_CH4))**2*(uncer_pressure_final_i)**2)  ## base on the formule of the calulation of final_pressure above
				
				density_final = (composition_N2*density_final_j + composition_CH4*density_final_i)/(composition_N2 + composition_CH4) ## Equation 8 in the reference 2
				uncer_density_final = np.sqrt((composition_N2/(composition_N2+composition_CH4))**2*(uncer_density_final_j)**2 + (composition_CH4/(composition_N2+composition_CH4))**2*(uncer_density_final_i)**2)  ## base on the formule of the calulation of final_pressure above

				molarvolume_final = (composition_N2*molarvolume_final_j + composition_CH4*molarvolume_final_i)/(composition_N2 + composition_CH4)
				uncer_molarvolume_final = (uncer_molarvolume_final_j + uncer_molarvolume_final_i)/2

########################
########################

			if temperature.get() == 32 and instrument.get() == 2 and composition_CO2 < 0.5: 

				#coefficient of CO2CH4 calibration (i)
				composition_CO2_normalized_1_i = (composition_CO2 + 0.005)
				composition_CO2_normalized_2_i = (composition_CO2 - 0.005)
				FDS_normalized_1_i = (FDS + unc_FDS - FDS_std)
				FDS_normalized_2_i = (FDS - unc_FDS - FDS_std)
				
				p00_i= 20.141
				p10_i= 119.317
				p01_i= 1735.798
				p20_i= -1063.462
				p11_i= -10364.644
				p02_i= 1503.426
				p30_i= 1503.573
				p21_i= 33241.615
				p12_i= -14970.863
				p03_i= 3045.567
				p31_i= -35823.587
				p22_i= 22248.061
				p13_i= -5471.870
				p04_i= 80.945

				d00_i= 0.062867
				d10_i= -0.683745 
				d01_i= 1.281116
				d20_i= 2.274286
				d11_i= -1.634755
				d02_i= -0.901265
				d30_i= -2.317295
				d21_i= -4.154535
				d12_i= 5.889787
				d03_i= -0.595327
				d31_i= 8.311497
				d22_i= -7.983288
				d13_i= 1.397482
				d04_i= -0.102337

				#### pressure calculation using CO2CH4 calibration (i)

				pressure3_i = (p00_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**0 
				+ p10_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**0 
				+ p01_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**1 
				+ p20_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**0
				+ p11_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**1 
				+ p02_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**2 
				+ p30_i*composition_CO2_normalized_1_i**3*FDS_normalized_2_i**0 
				+ p21_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**1
				+ p12_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**2 
				+ p03_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**3 
				+ p31_i*composition_CO2_normalized_1_i**3*FDS_normalized_2_i**1 
				+ p22_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**2
				+ p13_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**3 
				+ p04_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**4)

				pressure4_i = (p00_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**0 
				+ p10_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**0 
				+ p01_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**1 
				+ p20_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**0
				+ p11_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**1 
				+ p02_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**2 
				+ p30_i*composition_CO2_normalized_2_i**3*FDS_normalized_1_i**0 
				+ p21_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**1
				+ p12_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**2 
				+ p03_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**3 
				+ p31_i*composition_CO2_normalized_2_i**3*FDS_normalized_1_i**1 
				+ p22_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**2
				+ p13_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**3 
				+ p04_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**4)

				########################
				#### density calculation  using CO2CH4 calibration (i)


				density3_i = (d00_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**0 
				+ d10_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**0 
				+ d01_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**1 
				+ d20_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**0
				+ d11_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**1 
				+ d02_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**2 
				+ d30_i*composition_CO2_normalized_1_i**3*FDS_normalized_2_i**0 
				+ d21_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**1
				+ d12_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**2 
				+ d03_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**3 
				+ d31_i*composition_CO2_normalized_1_i**3*FDS_normalized_2_i**1 
				+ d22_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**2
				+ d13_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**3 
				+ d04_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**4)

				density4_i = (d00_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**0 
				+ d10_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**0 
				+ d01_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**1 
				+ d20_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**0
				+ d11_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**1 
				+ d02_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**2 
				+ d30_i*composition_CO2_normalized_2_i**3*FDS_normalized_1_i**0 
				+ d21_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**1
				+ d12_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**2 
				+ d03_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**3 
				+ d31_i*composition_CO2_normalized_2_i**3*FDS_normalized_1_i**1 
				+ d22_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**2
				+ d13_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**3 
				+ d04_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**4)              

				pressure_final_i = (max(pressure3_i, pressure4_i) + min(pressure3_i, pressure4_i))/2 #pressure max + pressure min
				uncer_pressure_final_i = 8.5 + (max(pressure3_i, pressure4_i) - min(pressure3_i, pressure4_i))/(2*np.sqrt(3))

				density_final_i = (max(density3_i, density4_i) + min(density3_i, density4_i))/2 #density max - density min
				uncer_density_final_i = 0.0049 + (max(density3_i, density4_i) - min(density3_i, density4_i))/(2*np.sqrt(3))

				molarvolume3_i = 1/(max(density3_i, density4_i)/(44*composition_CO2 + 16*composition_CH4 + 28*composition_N2))
				molarvolume4_i = 1/(min(density3_i, density4_i)/(44*composition_CO2 + 16*composition_CH4 + 28*composition_N2))
				molarvolume_final_i = (molarvolume3_i + molarvolume4_i) / 2
				uncer_molarvolume_final_i = (molarvolume4_i - molarvolume3_i) / (2*np.sqrt(3))



				##### verify if measured pressure < 160 bar, if it is, re-recalculte using calibration data for 5-160 bar range.
				if pressure_final_i <= 150: 

					## Calibration equation's coeff of CO2-CH4 at 22 °C over 5-160 bars
					# normalisation of concentration and of Fermi diad splitting
					
					#coefficient of CO2CH4 calibration (i)
					composition_CO2_normalized_1_i = (composition_CO2 + 0.005 )
					composition_CO2_normalized_2_i = (composition_CO2 - 0.005 )
					FDS_normalized_1_i = (FDS + unc_FDS - FDS_std)
					FDS_normalized_2_i = (FDS - unc_FDS - FDS_std)
					
					
					p00_i= 54.201
					p10_i= -579.442
					p01_i= 2003.442
					p20_i= 1889.818
					p11_i= -5145.786
					p02_i= -4786.568
					p30_i= -1886.673
					p21_i= 456.077
					p12_i= 19020.925
					p03_i= 1651.598
					p31_i= 6424.637
					p22_i= -18744.547
					p13_i= -5277.348
					p04_i= 1174.052


					d00_i= 0.047241
					d10_i= -0.543798
					d01_i= 1.582450
					d20_i= 1.857576
					d11_i= -2.644046
					d02_i= -3.137805
					d30_i= -1.907131
					d21_i= -5.118171
					d12_i= 18.341107
					d03_i= -1.806949
					d31_i= 11.389876
					d22_i= -21.602594
					d13_i= 0.245593
					d04_i= 1.535738

					#### pressure calculation using CO2CH4 calibration (i)

					pressure3_i = (p00_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**0 
					+ p10_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**0 
					+ p01_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**1 
					+ p20_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**0
					+ p11_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**1 
					+ p02_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**2 
					+ p30_i*composition_CO2_normalized_1_i**3*FDS_normalized_2_i**0 
					+ p21_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**1
					+ p12_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**2 
					+ p03_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**3 
					+ p31_i*composition_CO2_normalized_1_i**3*FDS_normalized_2_i**1 
					+ p22_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**2
					+ p13_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**3 
					+ p04_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**4)

					pressure4_i = (p00_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**0 
					+ p10_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**0 
					+ p01_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**1 
					+ p20_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**0
					+ p11_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**1 
					+ p02_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**2 
					+ p30_i*composition_CO2_normalized_2_i**3*FDS_normalized_1_i**0 
					+ p21_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**1
					+ p12_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**2 
					+ p03_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**3 
					+ p31_i*composition_CO2_normalized_2_i**3*FDS_normalized_1_i**1 
					+ p22_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**2
					+ p13_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**3 
					+ p04_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**4)

					########################
					#### density calculation  using CO2CH4 calibration (i)


					density3_i = (d00_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**0 
					+ d10_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**0 
					+ d01_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**1 
					+ d20_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**0
					+ d11_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**1 
					+ d02_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**2 
					+ d30_i*composition_CO2_normalized_1_i**3*FDS_normalized_2_i**0 
					+ d21_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**1
					+ d12_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**2 
					+ d03_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**3 
					+ d31_i*composition_CO2_normalized_1_i**3*FDS_normalized_2_i**1 
					+ d22_i*composition_CO2_normalized_1_i**2*FDS_normalized_2_i**2
					+ d13_i*composition_CO2_normalized_1_i**1*FDS_normalized_2_i**3 
					+ d04_i*composition_CO2_normalized_1_i**0*FDS_normalized_2_i**4)

					density4_i = (d00_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**0 
					+ d10_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**0 
					+ d01_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**1 
					+ d20_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**0
					+ d11_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**1 
					+ d02_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**2 
					+ d30_i*composition_CO2_normalized_2_i**3*FDS_normalized_1_i**0 
					+ d21_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**1
					+ d12_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**2 
					+ d03_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**3 
					+ d31_i*composition_CO2_normalized_2_i**3*FDS_normalized_1_i**1 
					+ d22_i*composition_CO2_normalized_2_i**2*FDS_normalized_1_i**2
					+ d13_i*composition_CO2_normalized_2_i**1*FDS_normalized_1_i**3 
					+ d04_i*composition_CO2_normalized_2_i**0*FDS_normalized_1_i**4)              

					pressure_final_i = (max(pressure3_i, pressure4_i) + min(pressure3_i, pressure4_i))/2 #pressure max + pressure min
					uncer_pressure_final_i = 5 + (max(pressure3_i, pressure4_i) - min(pressure3_i, pressure4_i))/(2*np.sqrt(3))

					density_final_i = (max(density3_i, density4_i) + min(density3_i, density4_i))/2 #density max - density min
					uncer_density_final_i = 0.0049 + (max(density3_i, density4_i) - min(density3_i, density4_i))/(2*np.sqrt(3))

					molarvolume3_i = 1/(max(density3_i, density4_i)/(44*composition_CO2 + 16*composition_CH4 + 28*composition_N2))
					molarvolume4_i = 1/(min(density3_i, density4_i)/(44*composition_CO2 + 16*composition_CH4 + 28*composition_N2))
					molarvolume_final_i = (molarvolume3_i + molarvolume4_i) / 2
					uncer_molarvolume_final_i = (molarvolume4_i - molarvolume3_i) / (2*np.sqrt(3))

			
				print('pressure3_i', pressure3_i)
				print('pressure4_i', pressure4_i)
				print('density 3_i=', density3_i)
				print('density 4_i=', density4_i)
				print("molarvolume3_i", molarvolume3_i)
				print("molarvolume4_i", molarvolume4_i)	
				

				#################################
				#coefficient of CO2 N2 calibration (j)
				############################"""
				composition_CO2_normalized_1_j = (composition_CO2 + 0.005)
				composition_CO2_normalized_2_j = (composition_CO2 - 0.005 )
				FDS_normalized_1_j = (FDS + unc_FDS - FDS_std)
				FDS_normalized_2_j = (FDS - unc_FDS - FDS_std)
				
				
				p00_j= -7.980
				p10_j= 269.903
				p01_j= 2587.526
				p20_j= -1224.785
				p11_j= -17336.257
				p02_j= 2115.167
				p30_j= 1435.628
				p21_j= 49648.794
				p12_j= -14261.990
				p03_j= 2095.490
				p31_j= -47522.157
				p22_j= 18998.615
				p13_j= -3716.869
				p04_j= 110.044


				d00_j= 0.052969
				d10_j= -0.591457
				d01_j= 2.418676
				d20_j= 2.021816
				d11_j= -8.676565
				d02_j= -0.998621
				d30_j= -2.112004
				d21_j= 11.215350
				d12_j= 6.539504
				d03_j= -0.392779
				d31_j= -2.564151
				d22_j= -8.685633
				d13_j= 1.017467
				d04_j= -0.138500

				#### pressure calculation using CO2 N2 calibration (j)

				pressure3_j = (p00_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**0 
				+ p10_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**0 
				+ p01_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**1 
				+ p20_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**0
				+ p11_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**1 
				+ p02_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**2 
				+ p30_j*composition_CO2_normalized_1_j**3*FDS_normalized_2_j**0 
				+ p21_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**1
				+ p12_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**2 
				+ p03_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**3 
				+ p31_j*composition_CO2_normalized_1_j**3*FDS_normalized_2_j**1 
				+ p22_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**2
				+ p13_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**3 
				+ p04_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**4)

				pressure4_j = (p00_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**0 
				+ p10_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**0 
				+ p01_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**1 
				+ p20_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**0
				+ p11_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**1 
				+ p02_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**2 
				+ p30_j*composition_CO2_normalized_2_j**3*FDS_normalized_1_j**0 
				+ p21_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**1
				+ p12_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**2 
				+ p03_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**3 
				+ p31_j*composition_CO2_normalized_2_j**3*FDS_normalized_1_j**1 
				+ p22_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**2
				+ p13_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**3 
				+ p04_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**4)

				########################
				#### density calculation  using CO2 N2  calibration (i)


				density3_j = (d00_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**0 
				+ d10_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**0 
				+ d01_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**1 
				+ d20_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**0
				+ d11_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**1 
				+ d02_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**2 
				+ d30_j*composition_CO2_normalized_1_j**3*FDS_normalized_2_j**0 
				+ d21_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**1
				+ d12_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**2 
				+ d03_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**3 
				+ d31_j*composition_CO2_normalized_1_j**3*FDS_normalized_2_j**1 
				+ d22_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**2
				+ d13_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**3 
				+ d04_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**4)

				density4_j = (d00_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**0 
				+ d10_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**0 
				+ d01_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**1 
				+ d20_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**0
				+ d11_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**1 
				+ d02_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**2 
				+ d30_j*composition_CO2_normalized_2_j**3*FDS_normalized_1_j**0 
				+ d21_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**1
				+ d12_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**2 
				+ d03_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**3 
				+ d31_j*composition_CO2_normalized_2_j**3*FDS_normalized_1_j**1 
				+ d22_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**2
				+ d13_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**3 
				+ d04_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**4)              

				pressure_final_j = (max(pressure3_j, pressure4_j) + min(pressure3_j, pressure4_j))/2 #pressure max + pressure min
				uncer_pressure_final_j = 5.7 + (max(pressure3_j, pressure4_j) - min(pressure3_j, pressure4_j))/(2*np.sqrt(3))

				density_final_j = (max(density3_j, density4_j) + min(density3_j, density4_j))/2 #density max - density min
				uncer_density_final_j = 0.0042 + (max(density3_j, density4_j) - min(density3_j, density4_j))/(2*np.sqrt(3))

				molarvolume3_j = 1/(max(density3_j, density4_j)/(44*composition_CO2 + 16*composition_CH4 + 28*composition_N2))
				molarvolume4_j = 1/(min(density3_j, density4_j)/(44*composition_CO2 + 16*composition_CH4 + 28*composition_N2))
				molarvolume_final_j = (molarvolume3_j + molarvolume4_j) / 2
				uncer_molarvolume_final_j = (molarvolume4_j - molarvolume3_j) / (2*np.sqrt(3))


				##### verify if measured pressure < 160 bar, if it is, re-recalculte using calibration data for 5-160 bar range.
				if pressure_final_j <= 150: 

					## Calibration equation's coeff of CO2-CH4 at 22 °C over 5-160 bars
					# normalisation of concentration and of Fermi diad splitting
					
					#coefficient of CO2N2 calibration (j)
					composition_CO2_normalized_1_j = (composition_CO2 + 0.005)
					composition_CO2_normalized_2_j = (composition_CO2 - 0.005)
					FDS_normalized_1_j = (FDS + unc_FDS - FDS_std)
					FDS_normalized_2_j = (FDS - unc_FDS - FDS_std)
					
					p00_j= 27.879
					p10_j= -309.341
					p01_j= 2420.432
					p20_j= 1080.882
					p11_j= -11059.840
					p02_j= -1531.374
					p30_j= -1154.706
					p21_j= 18759.022
					p12_j= 11079.420
					p03_j= -2896.324
					p31_j= -9353.915
					p22_j= -17517.273
					p13_j= 7020.022
					p04_j= -346.217
					
					d00_j= 0.032500			
					d10_j= -0.361537
					d01_j= 2.738940
					d20_j= 1.267886
					d11_j= -11.352661
					d02_j= -1.873395
					d30_j= -1.359611
					d21_j= 17.034457
					d12_j= 16.500441
					d03_j= -5.356779
					d31_j= -5.818552
					d22_j= -26.584920
					d13_j= 13.567035
					d04_j= -1.565370

					#### pressure calculation using CO2CH4 calibration (j)

					pressure3_j = (p00_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**0 
					+ p10_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**0 
					+ p01_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**1 
					+ p20_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**0
					+ p11_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**1 
					+ p02_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**2 
					+ p30_j*composition_CO2_normalized_1_j**3*FDS_normalized_2_j**0 
					+ p21_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**1
					+ p12_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**2 
					+ p03_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**3 
					+ p31_j*composition_CO2_normalized_1_j**3*FDS_normalized_2_j**1 
					+ p22_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**2
					+ p13_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**3 
					+ p04_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**4)

					pressure4_j = (p00_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**0 
					+ p10_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**0 
					+ p01_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**1 
					+ p20_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**0
					+ p11_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**1 
					+ p02_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**2 
					+ p30_j*composition_CO2_normalized_2_j**3*FDS_normalized_1_j**0 
					+ p21_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**1
					+ p12_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**2 
					+ p03_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**3 
					+ p31_j*composition_CO2_normalized_2_j**3*FDS_normalized_1_j**1 
					+ p22_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**2
					+ p13_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**3 
					+ p04_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**4)

					########################
					#### density calculation  using CO2CH4 calibration (i)

					density3_j = (d00_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**0 
					+ d10_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**0 
					+ d01_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**1 
					+ d20_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**0
					+ d11_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**1 
					+ d02_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**2 
					+ d30_j*composition_CO2_normalized_1_j**3*FDS_normalized_2_j**0 
					+ d21_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**1
					+ d12_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**2 
					+ d03_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**3 
					+ d31_j*composition_CO2_normalized_1_j**3*FDS_normalized_2_j**1 
					+ d22_j*composition_CO2_normalized_1_j**2*FDS_normalized_2_j**2
					+ d13_j*composition_CO2_normalized_1_j**1*FDS_normalized_2_j**3 
					+ d04_j*composition_CO2_normalized_1_j**0*FDS_normalized_2_j**4)

					density4_j = (d00_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**0 
					+ d10_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**0 
					+ d01_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**1 
					+ d20_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**0
					+ d11_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**1 
					+ d02_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**2 
					+ d30_j*composition_CO2_normalized_2_j**3*FDS_normalized_1_j**0 
					+ d21_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**1
					+ d12_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**2 
					+ d03_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**3 
					+ d31_j*composition_CO2_normalized_2_j**3*FDS_normalized_1_j**1 
					+ d22_j*composition_CO2_normalized_2_j**2*FDS_normalized_1_j**2
					+ d13_j*composition_CO2_normalized_2_j**1*FDS_normalized_1_j**3 
					+ d04_j*composition_CO2_normalized_2_j**0*FDS_normalized_1_j**4)              

					pressure_final_j = (max(pressure3_j, pressure4_j) + min(pressure3_j, pressure4_j))/2 #pressure max + pressure min
					uncer_pressure_final_j = 4 + (max(pressure3_j, pressure4_j) - min(pressure3_j, pressure4_j))/(2*np.sqrt(3))

					density_final_j = (max(density3_j, density4_j) + min(density3_j, density4_j))/2 #density max - density min
					uncer_density_final_j = 0.004 + (max(density3_j, density4_j) - min(density3_j, density4_j))/(2*np.sqrt(3))

					molarvolume3_j = 1/(max(density3_j, density4_j)/(44*composition_CO2 + 16*composition_CH4 + 28*composition_N2))
					molarvolume4_j = 1/(min(density3_j, density4_j)/(44*composition_CO2 + 16*composition_CH4 + 28*composition_N2))
					molarvolume_final_j = (molarvolume3_j + molarvolume4_j) / 2
					uncer_molarvolume_final_j = (molarvolume4_j - molarvolume3_j) / (2*np.sqrt(3))
		
				print('pressure3_j', pressure3_j)
				print('pressure4_j', pressure4_j)
				print('density 3_j=', density3_j)
				print('density 4_j=', density4_j)
				print("molarvolume3_i", molarvolume3_j)
				print("molarvolume4_i", molarvolume4_j)	
				if pressure_final_i > 650 or pressure3_i >650 or pressure4_i >650 or pressure_final_i < -20 or pressure3_i <-20 or pressure4_i <-20 or pressure_final_j > 650 or pressure3_j >650 or pressure4_j >650 or pressure_final_j < -20 or pressure3_j <-20 or pressure4_j <-20 or density3_i<0 or density4_i <0 or density3_j<0 or density4_j<0 or density_final_i<0 or density_final_j<0 :
					popupmsg_OCR()
			

				############ Calculation final pressure, density from pressure final i and j, depending on the concentration of CH4, N2 (coeff, a b within equation 8))
				############ and calculation uncertainty of FINAL RESULTS
				pressure_final = (composition_N2*pressure_final_j + composition_CH4*pressure_final_i)/(composition_N2 + composition_CH4) ## Equation 8 in the reference 2
				uncer_pressure_final = np.sqrt((composition_N2/(composition_N2+composition_CH4))**2*(uncer_pressure_final_j)**2 + (composition_CH4/(composition_N2+composition_CH4))**2*(uncer_pressure_final_i)**2)  ## base on the formule of the calulation of final_pressure above
				
				density_final = (composition_N2*density_final_j + composition_CH4*density_final_i)/(composition_N2 + composition_CH4) ## Equation 8 in the reference 2
				uncer_density_final = np.sqrt((composition_N2/(composition_N2+composition_CH4))**2*(uncer_density_final_j)**2 + (composition_CH4/(composition_N2+composition_CH4))**2*(uncer_density_final_i)**2)  ## base on the formule of the calulation of final_pressure above

				molarvolume_final = (composition_N2*molarvolume_final_j + composition_CH4*molarvolume_final_i)/(composition_N2 + composition_CH4)
				uncer_molarvolume_final = (uncer_molarvolume_final_j + uncer_molarvolume_final_i)/2


#####################################
######### FIN OF CALCULATION ########
#####################################

			
			####### GET RESULTS AND BUT ON THE OUT PUT FEILD (out put field just be created below) ################       
			composition_CO2_display.insert(tk.END, "%.3f" % composition_CO2)
			composition_CH4_display.insert(tk.END, "%.3f" % composition_CH4)
			composition_N2_display.insert(tk.END, "%.3f" % composition_N2)
			
			pressure.insert(tk.END, "%.1f" % pressure_final)
			density.insert(tk.END, "%.3f" % density_final)
			molarvolume.insert(tk.END, "%.3f" % molarvolume_final)

			uncer_pressure.insert(tk.END, "%.1f" % uncer_pressure_final)
			uncer_density.insert(tk.END, "%.3f" % uncer_density_final)
			uncer_molarvolume.insert(tk.END, "%.3f" % uncer_molarvolume_final)

		# ################################    
		# ########  create a field to display results ######
		# ################################ 
		composition_CO2_display= tk.Entry(self.frame, width = 20) #, state='disabled'
		composition_CO2_display.grid(row=39, column=1)    
		composition_CH4_display= tk.Entry(self.frame, width = 20) #, state='disabled'
		composition_CH4_display.grid(row=39, column=2)
		composition_N2_display= tk.Entry(self.frame, width = 20) #, state='disabled'
		composition_N2_display.grid(row=39, column=3)

		pressure= tk.Entry(self.frame, width = 20) #, state='disabled'
		pressure.grid(row=41, column=1)
		density = tk.Entry(self.frame, width = 20) 
		density.grid(row=42, column=1)
		molarvolume = tk.Entry(self.frame,  width = 20)
		molarvolume.grid(row=43, column=1)
		
		uncer_pressure = tk.Entry(self.frame,  width = 20) #, state='disabled'
		uncer_pressure.grid(row=41, column=3)
		uncer_density = tk.Entry(self.frame,  width = 20) 
		uncer_density.grid(row=42, column=3)
		uncer_molarvolume = tk.Entry(self.frame,  width = 20) 
		uncer_molarvolume.grid(row=43, column=3)


		#############################
		######### Buttons ###########
		#############################

		self.button1_1 = tk.Button(self.frame, text="Clear Input", command=clear_field_inputs)
		self.button1_1.grid(row=16, column=1, padx=10)
		self.button1_2 = tk.Button(self.frame, text="Calculate", bg="green", width=10, command=calculCO2CH4N2)
		self.button1_2.grid(row=37, column=1, padx=20, pady=10, sticky="W")        
		self.button1_3 = tk.Button(self.frame, text="Clear Results", width=10, command=clear_field_results)
		self.button1_3.grid(row=44, column=1, padx=20, pady=10, sticky="W")

		
		# def OpenSuppDoc_CO2CH4N2():
		# 	os.startfile(resource_path('SuppDoc_CO2CH4N2.pdf'))

		# self.button1_4 = tk.Button(self.frame, text="Supplement document", bg="orange", command=OpenSuppDoc_CO2CH4N2)
		# self.button1_4.grid(row=44, column=0, padx=10,  sticky="W")

						
		self.quit = tk.Button(self.frame, text="Close", width=15, command=self.close_window)	
		self.quit.grid(row=44, column=3, padx=10,  sticky="W")

	def close_window(self):
		self.master.destroy()


########################################################################################
########### desolved and non deseolved CH4 within H2O (Caumon et al. 2014) #############
########################################################################################
class module7: 
	def __init__(self, master, number):
		self.master = master
		self.master.geometry("580x560")
		self.master.title("FRAnCIs v.1.0.1 - (CH₄ dissolved and non-dissolved in H₂O)")
		self.master.resizable(width=False, height=False)
		self.master.iconbitmap(resource_path("logo.ico"))
		self.frame=tk.Frame(self.master)
		self.frame.grid()
		
		##############################
        ##### CREATE INTERFACE #######
        ##############################
        
		self.label= tk.Label(self.frame, text="CH₄ dissolved and non-dissolved in H₂O", font=('bold', 18))
		self.label.grid(row=0, column=0, columnspan=7, padx=70, pady=10,sticky="W")
		self.label = tk.Label(self.frame, text="   Validity range : (6-180 °C) and (30-1000 bar) and (0-4 mol.kg\u207b\u00B9 NaCl)")
		self.label.grid(row=1, column=0, columnspan=7)

		self.label= tk.Label(self.frame, text="1. Measurement of dissolved CH₄ in aqueous phase" , font=('bold', 14))
		self.label.grid(row=2, column=0, columnspan=7, padx=10, pady=5, sticky="W")

		self.label = tk.Label(self.frame, text="   - Raman analysis must be performed a few Celsius degrees above the homogenation temperature.")
		self.label.grid(row=3, column=0, columnspan=7, sticky="W")
		self.label = tk.Label(self.frame, text="   - The H₂O band area (A_H2O) is measured between 2700-3950 cm\u207b\u00B9.")
		self.label.grid(row=4, column=0, columnspan=7, sticky="W")
		self.label = tk.Label(self.frame, text="   - The CH₄ band area (A_CH4) is measured from the band at about 2905 cm\u207b\u00B9.")
		self.label.grid(row=5, column=0, columnspan=7, sticky="W")
		self.label = tk.Label(self.frame, text="   - The uncertainty of the measured results is about 5-10%.")
		self.label.grid(row=6, column=0, columnspan=7, sticky="W")
		
	
		
		###############################
        ##### INPUT + OUTPUT  ######
        ###############################
		
		self.label_input = tk.Label(self.frame, text="______ INPUT:", font=('bold', 10))
		self.label_input.grid(row=8, column=0, padx=10, pady=10, sticky="E")   


		self.label = tk.Label(self.frame, text="A_H2O")
		self.label.grid(row=9, column=0,  padx=10, sticky="E") #remove (side="top", fill="x",)
		self.A_H2O_entry_1 = tk.Entry(self.frame, width = 15)
		self.A_H2O_entry_1.grid(row=9,  pady=5,column=1)

		self.A_CH4_entry_1 = tk.Entry(self.frame, width = 15)
		self.A_CH4_entry_1.grid(row=10, column=1)
		self.label = tk.Label(self.frame, text="A_CH4")
		self.label.grid(row=10, column=0, padx=10, sticky="E") #remove (side="top", fill="x",)

		self.label = tk.Label(self.frame, text="Solubility of CH₄")
		self.label.grid(row=9, column=2,  padx=10, sticky="E")
		self.label = tk.Label(self.frame, text="(mol.kg\u207b\u00B9 H₂O)")
		self.label.grid(row=9, column=4,  padx=0, sticky="W")



		self.label= tk.Label(self.frame, text="2. Measurement of H₂O molar proportion in gas phase" , font=('bold', 14))
		self.label.grid(row=12, column=0, columnspan=7, padx=10, pady=5, sticky="W")

		self.label = tk.Label(self.frame, text="   - Raman analysis of the gas bubble can be performed at room temperature.")
		self.label.grid(row=13, column=0, columnspan=7, sticky="W")
		self.label = tk.Label(self.frame, text="   - The H₂O band area (A_H2O) is measured from the band at 3655 cm\u207b\u00B9.")
		self.label.grid(row=14, column=0, columnspan=7, sticky="W")
		self.label = tk.Label(self.frame, text="   - The CH₄ band area (A_CH4) is measured between 2630-3500 cm\u207b\u00B9.")
		self.label.grid(row=15, column=0, columnspan=7, sticky="W")
		#self.label = tk.Label(self.frame, text="   - The band areas are corrected from their Raman scattering cross-section.")
		#self.label.grid(row=16, column=0, columnspan=7, sticky="W")
		self.label = tk.Label(self.frame, text="   - The uncertainty of the measured results is less than about 10%.")
		self.label.grid(row=17, column=0, columnspan=7, sticky="W")
		
		self.label_input = tk.Label(self.frame, text="______ INPUT:", font=('bold', 10))
		self.label_input.grid(row=18, column=0, padx=10, pady=10, sticky="E")   


		self.label = tk.Label(self.frame, text="A_H2O")
		self.label.grid(row=19, column=0,  padx=10, sticky="E") #remove (side="top", fill="x",)
		self.A_H2O_entry_2 = tk.Entry(self.frame, width = 15)
		self.A_H2O_entry_2.grid(row=19,  pady=5,column=1)

		self.A_CH4_entry_2 = tk.Entry(self.frame, width = 15)
		self.A_CH4_entry_2.grid(row=20, column=1)
		self.label = tk.Label(self.frame, text="A_CH4")
		self.label.grid(row=20, column=0, padx=10, sticky="E") #remove (side="top", fill="x",)

		self.label = tk.Label(self.frame, text="H₂O molar proportion")
		self.label.grid(row=19, column=2,  padx=10, sticky="E")
		self.label = tk.Label(self.frame, text="")
		self.label.grid(row=19, column=4,  padx=10, sticky="W")
		
        ###############################
        ##### Caculation #######
        ###############################

        #### Make a clear-button for input field
		def clear_field_inputs(): 
			self.A_CH4_entry_1.delete(0, tk.END)
			self.A_H2O_entry_1.delete(0, tk.END)
			self.A_CH4_entry_2.delete(0, tk.END)
			self.A_H2O_entry_2.delete(0, tk.END)


		#### Make a clear-button for output field
		def clear_field_results_1():
			solubilityCH4.delete(0, tk.END)
			
		def clear_field_results_2():
			molarproportionH2O.delete(0, tk.END)

		def calcul_1():
			clear_field_results_1()
			A_CH4_1    	=float(self.A_CH4_entry_1.get())
			A_H2O_1 	=float(self.A_H2O_entry_1.get())
			
			r=A_CH4_1/A_H2O_1			

			a= 0.008
			b= 50.2
			c= -660
			

			solubilityCH4_final = a + b*r + c*r**2

			print('solubilityCH4_final', solubilityCH4_final)
			

			solubilityCH4.insert(tk.END, "%.3f" % solubilityCH4_final)

		def calcul_2():
			clear_field_results_2()
			A_CH4_2    	=float(self.A_CH4_entry_2.get())
			A_H2O_2 	=float(self.A_H2O_entry_2.get())
			
						

			molarproportionH2O_final = 5.19*(A_H2O_2/(A_H2O_2+A_CH4_2))

			print('molarproportionH2O_final', molarproportionH2O_final)
			

			molarproportionH2O.insert(tk.END, "%.3f" % molarproportionH2O_final)
			
			
		################################    
		########  display results ######
		################################ 
		
		solubilityCH4= tk.Entry(self.frame, width = 15) #, state='disabled'
		solubilityCH4.grid(row=9, column=3, sticky="W")
		
		molarproportionH2O = tk.Entry(self.frame, width = 15) 
		molarproportionH2O.grid(row=19, column=3, sticky="W")
		#molarvolume = tk.Entry(self.frame,  width = 20)
		#molarvolume.grid(row=20, column=1)

		#############################
		######### Buttons ###########
		#############################

		self.button1_1 = tk.Button(self.frame, text="Clear Input", command=clear_field_inputs)
		self.button1_1.grid(row=8, column=1, padx=10)

		self.button1_1 = tk.Button(self.frame, text="Clear Input", command=clear_field_inputs)
		self.button1_1.grid(row=18, column=1, padx=10)

		self.button1_2 = tk.Button(self.frame, text="Calculate", bg="green", width=10, command=calcul_1)
		self.button1_2.grid(row=8, column=3, padx=10, pady=10)

		self.button1_2 = tk.Button(self.frame, text="Calculate", bg="green", width=10, command=calcul_2)
		self.button1_2.grid(row=18, column=3, padx=10, pady=10)

		
		# def OpenSuppDoc_module7():
		# 	os.startfile(resource_path('module7.pdf'))
		# self.button1_4 = tk.Button(self.frame, text="Reference", bg="orange", width=10, command=OpenSuppDoc_module7)
		# self.button1_4.grid(row=21, column=3, padx=10, sticky="W")


		self.quit = tk.Button(self.frame, text="Close", width=10, command=self.close_window)	
		self.quit.grid(row=21, column=4, padx=10)

	def close_window(self):
		self.master.destroy()


root = tk.Tk()
app = FRAnCIs(root)
root.mainloop()