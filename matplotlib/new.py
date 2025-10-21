import matplotlib.pyplot as plt
import numpy as np 

x = [2023, 2024, 2025, 2026]
y = [15, 25, 30, 20]

plt.plot(x, y, 
         marker=".", 
         #ms=15, 
         color='red',
         linestyle = '-',
         linewidth = 2,
         markerfacecolor = 'blue',
         markeredgewidth = 3,
         markeredgecolor = 'green',
         markersize = 10,
         alpha = 0.7,
         label = 'Sales Data',
         )
plt.legend(
           loc = 'upper left',
           fontsize = 12, 
           shadow = True,
           borderpad = 20,
           )
plt.title('Yearly Sales Data',
          fontsize=20,
           color='#03fcca',
          loc = 'center',
          pad = 20,

          )
plt.xlabel('Year',
           fontsize = 15,
           color = 'purple',
           labelpad = 15,

           )
plt.ylabel('Sales',
           fontsize = 15,
           color = 'purple',
           labelpad= 15,

           )

           

plt.grid(True,
         which = 'both',
         axis = 'y',
         color = 'gray',
         )
plt.show()
