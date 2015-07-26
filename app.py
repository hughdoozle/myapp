import numpy
import pandas
import Quandl
import datetime
import matplotlib.pyplot as plt

dataset = Quandl.get("EOD/AMGN", trim_start = "2002-01-01", trim_end=datetime.date.today(),authtoken="wrsQXMJSFxsGDDH8-3y8")
dataset.plot()
plt.show()