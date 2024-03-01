#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px


# In[4]:


df = pd.read_csv('ISPU.csv')
print(df)


# In[5]:


df.head()


# In[6]:


#Data Cleansing
df.info()


# In[7]:


df.isnull()


# In[8]:


df.isnull().sum()


# In[9]:


#Total Number of Missing NA
df.isnull().sum().sum()


# In[10]:


df.fillna('0')


# In[11]:


df.duplicated().sum()


# In[12]:


import pandas as pd

df[['a_o3', 'a_no2', 'a_hc']] = df[['a_o3', 'a_no2', 'a_hc']].fillna(0)

# Menampilkan DataFrame setelah pengisian nilai null
print(df)


# In[13]:


import pandas as pd
#EDA
# Data awal
data = df['index_ISPU']

# Membuat DataFrame
df1 = pd.DataFrame(data)

# Fungsi untuk mengonversi index_ISPU menjadi kategori
def categorize_ISPU(index):
    if index <= 50:
        return 'Baik'
    elif index <= 100:
        return 'Sedang'
    elif index <= 200:
        return 'Tidak Sehat'
    elif index <= 300:
        return 'Sanagat Tidak Sehat'
    else:
        return 'Bahaya'

# Menambahkan kolom category
df['category'] = df['index_ISPU'].apply(categorize_ISPU)

print(df)


# In[14]:


df.head(10)


# In[15]:


import matplotlib.pyplot as plt

# Menghitung total nilai polutan untuk setiap polutan
total_pollutants = df[['a_pm10', 'a_pm25', 'a_so2', 'a_co', 'a_o3', 'a_no2']].sum()

# Menggambar pie chart
plt.figure(figsize=(8, 8))
plt.pie(total_pollutants, labels=total_pollutants.index, autopct='%1.1f%%', startangle=140)
plt.title('Persentase Polutan di Indonesia')
plt.axis('equal')  # Agar pie chart berbentuk lingkaran
plt.show()


# In[16]:


# Memilih 10 teratas berdasarkan nilai index_ISPU
top_10_highest = df.nlargest(10, 'index_ISPU')
top_10_lowest = df.nsmallest(10, 'index_ISPU')

# Membalik urutan data agar nilai tertinggi menjadi bar paling atas untuk 10 tertinggi
top_10_highest = top_10_highest[::-1]

# Membuat subplot untuk stasiun dengan index ISPU tertinggi
plt.figure(figsize=(20, 8))
plt.subplot(1, 2, 1)
bars1 = plt.barh(top_10_highest['id_stasiun'], top_10_highest['index_ISPU'], color='skyblue')
plt.xlabel('Index ISPU')
plt.title('Top 10 Stasiun dengan Nilai Index ISPU Tertinggi')

# Menampilkan nilai index ISPU disamping bar
for bar, value in zip(bars1, top_10_highest['index_ISPU']):
    plt.text(bar.get_width(), bar.get_y() + bar.get_height() / 2, f'{value}', ha='left', va='center')

# Membalik urutan data agar nilai tertinggi menjadi bar paling bawah untuk 10 terendah
top_10_lowest = top_10_lowest[::-1]

# Membuat subplot untuk stasiun dengan index ISPU terendah
plt.subplot(1, 2, 2)
bars2 = plt.barh(top_10_lowest['id_stasiun'], top_10_lowest['index_ISPU'], color='lightgreen')
plt.xlabel('Index ISPU')
plt.title('Top 10 Stasiun dengan Nilai Index ISPU Terendah')

# Menampilkan nilai index ISPU disamping bar
for bar, value in zip(bars2, top_10_lowest['index_ISPU']):
    plt.text(bar.get_width(), bar.get_y() + bar.get_height() / 2, f'{value}', ha='left', va='center')

plt.tight_layout()  # Mengatur layout agar tidak tumpang tindih
plt.show()


# In[17]:


import matplotlib.pyplot as plt

# Menghitung rata-rata nilai index ISPU untuk setiap provinsi dan pulau
mean_ISPU_provinsi = df.groupby('provinsi')['index_ISPU'].mean().sort_values(ascending=False)
mean_ISPU_pulau = df.groupby('p3e')['index_ISPU'].mean().sort_values(ascending=False)

# Membuat subplot untuk tingkat ISPU berdasarkan provinsi
plt.figure(figsize=(20, 6))
plt.subplot(1, 2, 1)
plt.bar(mean_ISPU_provinsi.index, mean_ISPU_provinsi.values, color='skyblue')
plt.xlabel('Provinsi')
plt.ylabel('Rata-rata Index ISPU')
plt.title('Rata-rata Index ISPU Berdasarkan Provinsi')
plt.xticks(rotation=45, ha='right')  # Memutar label sumbu x agar mudah dibaca

# Membuat subplot untuk tingkat ISPU berdasarkan pulau
plt.subplot(1, 2, 2)
plt.bar(mean_ISPU_pulau.index, mean_ISPU_pulau.values, color='lightgreen')
plt.xlabel('Pulau')
plt.ylabel('Rata-rata Index ISPU')
plt.title('Rata-rata Index ISPU Berdasarkan Pulau')
plt.xticks(rotation=45, ha='right')  # Memutar label sumbu x agar mudah dibaca

plt.tight_layout()
plt.show()


# In[18]:


import plotly.graph_objects as go

fig = go.Figure()

for pollutant in ["a_pm10", "a_pm25", "a_so2", "a_co", "a_o3", "a_hc"]:
    fig.add_trace(go.Scatter(x=df['tanggal'], y=df[pollutant], mode='lines',
                             name=pollutant))

fig.update_layout(title='Time Series Analysis of Air Pollutants in Indonesia',
                  xaxis_title='tanggal', yaxis_title='Concentration (µg/m³)')
fig.show()


# In[19]:


import seaborn as sns
import matplotlib.pyplot as plt

# Memilih kolom polutan
pollutants = df[['a_pm10', 'a_pm25', 'a_so2', 'a_co', 'a_o3', 'a_no2']]

# Menghitung korelasi antar polutan
correlation_matrix = pollutants.corr()

# Membuat heatmap korelasi
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", square=True)
plt.title('Correlation Between Pollutant')
plt.show()


# In[20]:


import plotly.graph_objects as go

fig = go.Figure()

for pollutant in ["a_pm10", "a_pm25", "a_so2", "a_co", "a_o3", "a_hc"]:
    fig.add_trace(go.Scatter(x=df['tanggal'], y=df[pollutant], mode='lines',
                             name=pollutant))

fig.update_layout(title='Time Series Analysis of Air Pollutants in Indonesia',
                  xaxis_title='tanggal', yaxis_title='Concentration (µg/m³)')
fig.show()


# In[ ]:




