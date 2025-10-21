import matplotlib.pyplot as plt
import numpy as np 

x = [2023,2024,2025,2026]
y = [15,25,30,20] 

plt.plot(x,y, marker =".",
       ms=15,color='Red',
       linestyle = '--',
       linewidth = 2,
       markerfacecolor = 'blue',
       markeredgewidth = 2,
       markeredgecolor = 'green',
       
       )
plt.title('Yearly Sales Data',
          fontsize = 20,
          color = '#03fcca',
          

          )
plt.xlabel('Year',
           fontsize = 15,
           color = "#2b7ef1",
           
           )
plt.ylabel('Sales in USD (in Thousands)',
           fontsize = 15,
           color = "#03bafc",

           )
plt.show()