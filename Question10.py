# =================================
# created by Celeste quinlan 13-Mar-2019
# Course XXXX
# This program displays a plot of the functions x , x 2 and 2 x in the range [0 , 4].
# QUESTION 10 
# =================================

import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

x = np.linspace(0, 1, 2, 4)

plt.plot(x, x , linestyle='solid')
plt.plot(x, x * x, linestyle='dashed')
plt.plot(x, x * x * x, linestyle='dashdot')
#plt.plot(x, x * 3, linestyle='dotted')



#names = ['group_a', 'group_b', 'group_c']
#values = [1, 10, 100]

#plt.figure(1, figsize=(9, 3))

#plt.subplot(131)
#plt.bar(names, values)
#plt.subplot(132)
#plt.scatter(names, values)
#plt.subplot(133)
#plt.plot(names, values)
#plt.suptitle('Categorical Plotting')
plt.show()