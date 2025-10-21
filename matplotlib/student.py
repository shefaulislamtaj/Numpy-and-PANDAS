#import matplotlib.pyplot as pltimport 
import matplotlib.pyplot as plt
import numpy as np
x = np.array([2023,2024,2025,2026])
y1 = np.array([15,25,30,20])
y2 = np.array([17,23,38,5]) 
y3 = np.array([13,15,20,30])

plt.title("Class Size", fontsize = 20,
          family = 'Arial',
          fontweight = 'bold', 
          color = '#2d4cfc',
          )
line_style = dict(marker = 'o',
         markersize = '30',
         #color = 'blue',
        markeredgecolor = 'red',
         linestyle = 'solid',
         linewidth = '2',
         #color = '#1c5bfc',
        )
plt.xlabel("year",fontsize = 20,
           family = 'Arial',
          fontweight = 'bold',
            color = 'red')

plt.ylabel("Students",fontsize = 20,family = 'Arial',
          fontweight = 'bold', color = 'red')

plt.tick_params(axis= "both", 
                colors = "#f5d902")


plt.plot(x,y1, **line_style)#color = '#48e868'

plt.plot(x,y2,**line_style)#color = '#48e868'
plt.plot(x,y3, **line_style)#color = '#48e868'
plt.xticks(x)


#plt.plot(x, y1, marker = 'o',
         #markersize = '30',
         #color = 'blue',
        #markeredgecolor = 'red',
        ##linewidth = '2',
        # color = '#1c5bfc',
        #)
#plt.plot(x,y2)

plt.show()



