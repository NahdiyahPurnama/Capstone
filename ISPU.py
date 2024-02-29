import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import seaborn as sns

def main():
    st.title("Analisis Kualitas Udara di Indonesia dengan Standar ISPU")
    st.header("Pendahuluan")
    st.text("Kualitas udara sangat mempengaruhi kualitas kehidupan mahluk hidup dan lingkungan.")  
    st.text("Salah satu upaya pengendalian pencemaran udara yaitu memberi informasi tentang ") 
    st.text("kualitas udara. ISPU (Indeks Standar Pencemaran Udara) merupakan standar penggambaran ")
    st.text("kualitas udara. Dengan informasi yang diberikan kepada masyarakat dapat mengetahui")
    st.text("kualitas udara di daerah tersebut dan dapat melakukan tindakan untuk mencegah")
    st.text("dari dampak polusi udara.")

  
    
    # Membaca file CSV menggunakan path relatif
    df = pd.read_csv('ISPU.csv')
    
    #DATA
    st.header("Data")
    st.text("Data yang digunakan bersumber dari kementrian lingkungan hidup dan kehutanan yaitu")  
    st.text("data monitoring ISPU (Indeks standar pencemaran udara). Stasiun ISPU berada di  ") 
    st.text("54 daerah di Indonesia. Data yang diambil dari tanggal 26 februari 2024 sampai")
    st.text("27 februari 2024.")
    # Data untuk pie chart
    labels = 'pm10', 'pm25', 'so2', 'co', 'o3', 'no2'
    sizes = [1.7, 1.3, 2.7, 87.8, 3.6, 2.9]
    
    st.header("Analisis")
    
    # Membuat pie chart
    st.subheader("Presentase Polutan di Indonesia")
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=130)
    ax.set_title('Persentase Polutan di Indonesia')
    ax.axis('equal')  # Memastikan pie chart digambar sebagai lingkaran
    # Menampilkan pie chart
    st.pyplot(fig)
    #Insight pie chart
    st.subheader("Insight")
    st.text("Polutan udara terbanyak di Indonesia yaitu gas karbon monoksida (CO), umumnya") 
    st.text("berasal dari bahan bakar dan polutan udara terkecil yaitu PM2.5 yang merupakan")  
    st.text("Partikel udara yang berukuran lebih kecil dari 2.5 mikron (mikrometer).") 
   
   
    # Data untuk analisis ke-2 TOP 10 ISPU tertinggi dan terendah
  
    st.subheader("10 Stasiun dengan Index ISPU Tertinggi dan Terendah")
    
    top_10_highest = df.nlargest(10, 'index_ISPU')
    top_10_lowest = df.nsmallest(10, 'index_ISPU')

    # Membalik urutan data agar nilai tertinggi menjadi bar paling atas untuk 10 tertinggi
    top_10_highest = top_10_highest[::-1]

    # Membuat subplot untuk stasiun dengan index ISPU tertinggi
    fig, ax = plt.subplots(1, 2, figsize=(20, 10))

    bars1 = ax[0].barh(top_10_highest['id_stasiun'], top_10_highest['index_ISPU'], color='skyblue')
    ax[0].set_xlabel('Index ISPU')
    ax[0].set_title('Top 10 Stasiun dengan Nilai Index ISPU Tertinggi')

    # Menampilkan nilai index ISPU disamping bar
    for bar, value in zip(bars1, top_10_highest['index_ISPU']):
        ax[0].text(bar.get_width(), bar.get_y() + bar.get_height() / 2, f'{value}', ha='left', va='center')

    # Membalik urutan data agar nilai tertinggi menjadi bar paling bawah untuk 10 terendah
    top_10_lowest = top_10_lowest[::-1]

    # Membuat subplot untuk stasiun dengan index ISPU terendah
    bars2 = ax[1].barh(top_10_lowest['id_stasiun'], top_10_lowest['index_ISPU'], color='lightgreen')
    ax[1].set_xlabel('Index ISPU')
    ax[1].set_title('Top 10 Stasiun dengan Nilai Index ISPU Terendah')

    # Menampilkan nilai index ISPU disamping bar
    for bar, value in zip(bars2, top_10_lowest['index_ISPU']):
        ax[1].text(bar.get_width(), bar.get_y() + bar.get_height() / 2, f'{value}', ha='left', va='center')

    plt.tight_layout()  # Mengatur layout agar tidak tumpang tindih
    # Menampilkan plot menggunakan st.pyplot()
    st.pyplot(fig)
    
   

   #data3

    
    mean_ISPU_provinsi = df.groupby('provinsi')['index_ISPU'].mean().sort_values(ascending=False)
    mean_ISPU_pulau = df.groupby('p3e')['index_ISPU'].mean().sort_values(ascending=False)

    # Streamlit App
    st.subheader('Tingkat ISPU Berdasarkan Provinsi dan Pulau')

    # Tampilkan plot untuk tingkat ISPU berdasarkan provinsi
    st.subheader('Rata-rata ISPU Berdasarkan Provinsi')
    fig1, ax1 = plt.subplots()
    ax1.bar(mean_ISPU_provinsi.index, mean_ISPU_provinsi.values, color='skyblue')
    ax1.set_xlabel('Provinsi')
    ax1.set_ylabel('Rata-rata Index ISPU')
    ax1.set_title('Rata-rata Index ISPU Berdasarkan Provinsi')
    plt.xticks(rotation=60, ha='right')  # Memutar label sumbu x agar mudah dibaca
    st.pyplot(fig1)

    # Tampilkan plot untuk tingkat ISPU berdasarkan pulau
    st.subheader('Rata-rata ISPU Berdasarkan Pulau')
    fig2, ax2 = plt.subplots()
    ax2.bar(mean_ISPU_pulau.index, mean_ISPU_pulau.values, color='lightgreen')
    ax2.set_xlabel('Pulau')
    ax2.set_ylabel('Rata-rata Index ISPU')
    ax2.set_title('Rata-rata Index ISPU Berdasarkan Pulau')
    plt.xticks(rotation=45, ha='right')  # Memutar label sumbu x agar mudah dibaca
    st.pyplot(fig2)
    
    
    
    #Data 4
    pollutants = df[['a_pm10', 'a_pm25', 'a_so2', 'a_co', 'a_o3', 'a_no2']]

    # Menghitung korelasi antar polutan
    correlation_matrix = pollutants.corr()

    # Streamlit App
    st.subheader('Heatmap Korelasi Antara Polutan')

    # Membuat heatmap korelasi menggunakan Seaborn
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", square=True)
   
    st.pyplot(plt)
    st.subheader("Insight")
    st.text("Koefisien korelasi mengukur kekuatan dan arah hubungan linier antara dua variabel.")
    st.text("Polutan pm2.5 dan pm10 menunjukkan korelasi positif yang nilainya mendekati 1,")
    st.text("sedangkan polutan lainnya yaitu NO2, SO2, CO, O3 menunjukkan korelasi yang nilainya mendekati 0.")
    st.text("nilainya mendekati 0.")
if __name__ == "__main__":
    main()
