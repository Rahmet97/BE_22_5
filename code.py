import pandas
import matplotlib.pyplot as plt
from datetime import datetime

mydataset = {
  'first_name': ['Quvonchbek', 'Sardor', 'Shoxrux', 'Asilbek', 'Uldaulet', 'Xumoyun', 'Uyg`unbek', 'Saidaminxuja', 'Ozod', 'Shahzod'],
  'last_name': ['Ibragimov', 'Safaraliyev', 'Abdullayev', 'Turdaliyev', 'Sabirova', "O'xtamov", 'Karimjonov', 'Muminov', 'Imomov', 'Ilhomov'],
  'birthday': ['2004-01-01', '2005-02-02', '2006-03-03', '2007-04-04', '2000-05-05', '1994-02-01', '2001-01-18', '2002-05-12', '2007-04-16', '2003-12-09'],
  'age': []
}

mydataset['age'] = [datetime.now().year - int(i[:4]) for i in mydataset['birthday']]

myvar = pandas.DataFrame(mydataset)

data = pandas.read_excel('financials_sample_data.xlsx')

data.head(10).plot()

plt.style.use(style='fast')
plt.show()
