import matplotlib.pyplot as plt
import numpy as np 

x = [2023, 2024, 2025, 2026]
y = [15, 25, 30, 20]

plt.bar(
    x, y,
    color='red',       # ✅ color works for bar chart
    width=0.5,         # optional: control bar width
    alpha=0.8          # optional: transparency
)

plt.title(
    'Yearly Sales Data',   # ✅ fixed typo
    fontsize=20,
    color='#03fcca'
)

plt.xlabel('Year', fontsize=15, color='blue')
plt.ylabel('Sales (in Thousands)', fontsize=15, color='blue')

plt.show()























'''
import matplotlib.pyplot as plt
import numpy as np 

x = [2023, 2024, 2025, 2026]
y = [15, 25, 30, 20]

plt.plot(
    x, y,
    marker=".",
    color='red',
    linestyle='-',
    linewidth=2,
    markerfacecolor='blue',
    markeredgewidth=3,
    markeredgecolor='green',
    markersize=10,
    alpha=0.7,
    label='Sales Data'
)

# ✅ fixed typos below
plt.legend(
    loc='upper left',
    fontsize=12,
    shadow=True,
    borderpad=1
)

plt.title(
    'Yearly Sales Data',
    fontsize=20,
    color='#03fcca',
    loc='center',
    pad=20
)

plt.xlabel(
    'Year',
    fontsize=15,
    color='purple',
    labelpad=15
)

plt.ylabel(
    'Sales',
    fontsize=15,
    color='purple',
    labelpad=15
)

plt.grid(
    True,
    which='both',
    axis='y',
    color='gray'
)

plt.show()
'''