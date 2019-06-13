import matplotlib.pyplot as plt

kwh = [9274.0, 9280.5, 9286.5, 9289.5, 9293.0, 9297.0, 9300.0, 9302.5, 9306.5,
       9307.0, 9310.5, 9314.5]

days = [0, 61, 91, 106, 126, 142, 149, 162, 176, 184, 217, 235]

plt.plot(days, kwh)
plt.ylabel('Kw/h')
plt.show()
