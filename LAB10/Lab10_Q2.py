#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 13:34:54 2021

@author: alphantulukcu
"""

import matplotlib.pyplot as pl
import numpy as np

student = np.loadtxt('students.txt',skiprows= 1)

half = student[student[0:,0] == 2]
hmath = half[0:,1]
hread = half[0:,2]
hwrt = half[0:,3]
x = np.arange(0,len(half))

pl.clf()
pl.subplot(2,2,1)
pl.hist(hwrt, 4)
pl.title('Frequency of Writing Gr.\nof Half Sc. Students')

pl.subplot(2,2,2)
pl.plot(x, hmath, 'mo:', x, hread,'cx-')
pl.ylabel('Grades')
pl.title('Math vs Reading Gr.\nof Half Sc. Students')
pl.legend(['Math', 'Reading'])

pl.subplot(2,2,3)
sizes = [len(student[student[0:,0] == 1]),len(student[student[0:,0] == 2]),len(student[student[0:,0] == 3])]
names = 'Full', 'Half', 'Non'
pl.pie(sizes, explode = (0.,0.,0.1),labels = names, autopct='%1.1f%%')
pl.title('Scholarship Percentages')

pl.subplot(2,2,4)
allravg = np.mean(student[0:,2])
halfravg = np.mean(hread)
names = ['Half-sc.','All']
ind = np.arange(len(names))
pl.bar(0,halfravg,0.6,align = 'center')
pl.bar(1,allravg,0.6,align = 'center')
# pl.xlabel('Half-sc. All')
pl.ylabel('Average of Grades')
pl.title('Reading Grades: Half sc. vs All Students')
pl.xticks(ind, names)


pl.tight_layout()

pl.show()
