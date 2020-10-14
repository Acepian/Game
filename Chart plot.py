import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

appl_price = [93.95, 112.15, 104.05, 144.85, 169.49]
ms_price = [39.01, 50.29, 57.05, 69.98, 94.39]
year = [2014, 2015, 2016, 2017,2018]
plt.plot(year, appl_price, 'ok',year, ms_price, 'g')

plt.xlabel('Year')
plt.ylabel('Stock Price')

#plt.axis([2013, 2019, 20, 180])

plt.show()

fig_1 = plt.figure(1, figsize=(20, 4.8))
apple_price = fig_1.add_subplot(121)
microsoft_price = fig_1.add_subplot(122)

apple_price.plot(year, appl_price)
apple_price.xaxis.set_major_locator(MaxNLocator(integer=True))

microsoft_price.scatter(year, ms_price)
microsoft_price.xaxis.set_major_locator(MaxNLocator(integer=True))

plt.show()
