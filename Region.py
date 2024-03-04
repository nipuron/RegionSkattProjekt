import numpy as np
import scipy.stats as stats
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
import statsmodels.formula.api as smf
import os 
Skatt_delta= pd.read_excel("RegionData.xlsx")

#Förändring i skatt
sns.scatterplot(Skatt_delta, x='År', y='Skatteförändring', hue='Styre')
plt.show()
reg_lin=smf.ols(formula='Skatteförändring~Styre',data=Skatt_delta).fit()
print(reg_lin.summary())
#Förändring i skatt tillsammans med konjukturläge

#Mandatperioder av Resp styre som predikator för hur skatten är
#Tillsammans med inkomst och befolkningstäthet
Skatt=pd.read_excel('RegionData.xlsx',sheet_name='Skattenivå')

sns.scatterplot(Skatt,x='Snittinkomst',y='Skatt')
plt.show()
sns.scatterplot(Skatt,x='Befolkningstäthet',y='Skatt')
plt.show()

reg_lin=smf.ols(formula='Skatt~Befolkningstäthet+Snittinkomst+PolitikIndex+PolitikIndex:Snittinkomst',data=Skatt).fit()
print(reg_lin.summary())

#Mandatperioder av Resp styre som predikator för hur skatten är
#Tillsammans med inkomst och befolkningstäthet Utan Stockholm
Skatt_UtanSthlm =pd.read_excel('RegionData.xlsx',sheet_name='Skattenivå(UtanStockholm)')
reg_lin=smf.ols(formula='Skatt~Befolkningstäthet+Snittinkomst+PolitikIndex+PolitikIndex:Snittinkomst',data=Skatt_UtanSthlm).fit()
print(reg_lin.summary())