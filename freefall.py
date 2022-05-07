# free fall
import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
A = []
n = int(input("Enter the no of inputs you want to give: "))

for i in range(n):
    M = []
    print("\n\t\t\t\t INPUT ",i+1)
    m = float(input("\nEnter the mass of the object in kg: "))
    M.append(m)
    h1 = int(input("\nEnter the height from which the object is dropped: "))
    M.append(h1)
    area = float(input("Enter the Cross-Sectional Area of the object: "))
    M.append(area)
    g = 9.81
    density = 1.225
    W = round((m*g),2)
    M.append(W)
    print("Density of air = ", density)
    t = float(input("Enter the time interval for which you want to print the output: "))
    M.append(t)
    
    print("\nDrag coefficient of some shapes:","\n 1. Cube = 1.05","\n 2. Sphere = 0.47",
          "\n 3. Solid Hemisphere(flow on convex face) = 0.42","\n 4. Cone= 0.50","\n 5. Angled cube = 0.80",
          "\n 6. Long cylinder = 0.82","\n 7. Short cylinder = 1.15",
          "\n 8. Streamlined body = 0.04","\n 9. Streamlined half body = 0.09")

    drag_coeffi = float(input("\nEnter the drag coefficient according to the shape of object : "))
    
    Tv = round(math.sqrt((2 * m * g)/(density * drag_coeffi * area)),2)               #Terminal velocity
    M.append(Tv)
    
    vt = round((Tv * math.tanh((g * t)/Tv)),2)                                        #velocity with respect to time
    M.append(vt)
    
    at = round((g * (1+ (math.tanh((g * t)/Tv)**2))),2)                               #acceleration
    M.append(at)
    
    h = round((h1 - (((Tv**2)/g) * math.log(math.cosh((g*t)/Tv)))),2)                 #position
    M.append(h)
    
    A.append(M)
v = Tv

#Code For Table

plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True    
fig, ax =plt.subplots(1,1)
data = A
column_labels=["Mass","Initial Height","Cross-Sectional Area","Gravitational Force \n(weight)","Time","Terminal Velocity","Velocity","Acceleration",
               "Position"]
df = pd.DataFrame(data,columns=column_labels)
ax.axis('tight')
ax.axis('off')
the_table = ax.table(cellText=df.values,colLabels=df.columns,loc="center")
the_table.auto_set_font_size(False)
the_table.set_fontsize(8)

plt.show(block=False)

#Code For Graph

T = np.linspace(0,5,100)                                    #array to pass 100 values between 0 to 5
H = h1 - (((v**2)/g) * np.log(np.cosh((g*T)/v)))            #here we have used numpy as it can recive an array of values 
V = v * np.tanh((g * T)/v)                                  #while in math it recive only one value
AC = g * (1+(np.tanh((g * T)/v)**2))
plt.figure(figsize=(7,5))
plt.xticks(np.arange(-2,5,1))                                #to put the ticks on x axis
plt.xlim(-2,5)
plt.title("Psition, Velocity and Acceleration versus Time graph")
plt.xlabel("Time (in seconds)")
plt.plot(T,H,label="Position")                              #to plot the graph
plt.plot(T,V,label="Velocity")                              #label is to label the curve what it repersent
plt.plot(T,AC,label="Acceleration")
plt.legend()                                                #legend is the function which support label or recive label as argument
plt.show()

