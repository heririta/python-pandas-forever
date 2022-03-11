# Belajar Python Pandas

# import pandas
from pydoc import describe
import pandas as pd

# *Dataframe
# mengenal dataframe (sebuah table yang terdiri dari kolom dan baris)
# membuat dataframe sederhana
# parameter mengunankan type data dictionary
# key adalah minuman dan harga, values : type data list Object
# key dan values, dipisahkan dengan tanda :
# key dari type dictionary menjadi nama kolom dan value dari list akan menjadi data record
# perhatikan! jumlah data pada setiap value -> listnya harus sama misal data pertama 2 data data selanjutnya juga 2 data
contoh_df1 = pd.DataFrame(data={
    'Minuman': ['Bandrek', 'Kopi Hitam'],
    'Harga': [4500, 3200]
})
print(contoh_df1)

# by default index yang ada di dataframe index adalah integer
contoh_df2 = pd.DataFrame(data={
    'Budi': ['suka', 'suka'],
    'Wati': ['tidak suka', 'suka']
}, index=['mangga', 'jambu'])
print(contoh_df2)

# *Series
# Series = data untuk 1 coloumn
contoh_df3 = pd.Series(data=[100, 200, 300, 400, 500])
print(contoh_df3)

# Series juga bisa diberikan index dan juga nama Seriesnya
contoh_df4 = pd.Series(data=[100, 200, 300], index=[
                       'Mangga', 'Pisang', 'Jambu'], name='Harga Buah')
print(contoh_df4)

# memuat file csv ke dalam dataframe
# wine_df = pd.read_csv('./dataset/winemag-data-130k-v2.csv'
wine_df = pd.read_csv('./dataset/winemag-data-130k-v2.csv', index_col=0)
# .head() by default menampilkan hanya 5 data pertama, head(10) menampilkan 10 data pertama
print(wine_df.head())

# melihat dimensi dataframe dengan attibure .shape : (65499, 14) , 65499 jumlah baris , 14 jumlah columns
print(wine_df.shape)

# mengunakan salah satu kolom sebagai index, sebelumnya resultnya overlapping
# wine_df = pd.read_csv('./dataset/winemag-data-130k-v2.csv', index_col=0)
# [5 rows x 13 columns]
# (65499, 13)

# *menyimpan dataframe ke dalam file csv
minuman_df = pd.DataFrame(data={
    'Minuman': ['Bandrek', 'Kopi Hitam'],
    'Harga': [4500, 3200]
})
print(minuman_df)

# minuman_df.to_csv('./output/minuman.csv')
# menyimpan dataframe ke dalam file csv tanpa menyertakan index
minuman_df.to_csv('./output/minuman.csv', index=False)

# *Melakukan akses pada kolom dataframe

# akses pada columns
# cara 1 : sebagai atribute base, nama column tidak ada karakter spasi
print(wine_df.country)
print(wine_df.province)

# cara 2 : sebagai dictionary index, index = data string , ketika column mengandung spasi jadi tidak bermasalah
print(wine_df['country'])
print(wine_df['price'])

# mengakses data dengan mengunakan namadataframe[index_namacolumn (data string)][indexrecord_ke]
print(wine_df['country'][0])

# *akses data pada dataframe dengan mengunakan index-base selection dan label-base selection
# kedua mekanime ini mendahulukan baris index kemudian column index, row lalu columns

# *index-base selection
# method .iloc[row index, column index]
print(wine_df.iloc[0])  # mengakses data pada baris index ke 0
print(wine_df.head())
# mengakses data pada baris index ke 2 dan column index ke 0
print(wine_df.iloc[2, 1])

# mengunakan slicing pada iloc[]
print(wine_df.iloc[:, 0])  # mengakses semua baris dan column index ke 0

# mengakses baris index 0 dan 7 column index pertama
print(wine_df.iloc[0, :7])

# mengakses dari baris index ke 1 sampai index ke 3, column index 0
print(wine_df.iloc[1:3, 0])

# melewatkan list untuk melakuakan akses data pada baris dan kolom tertentu dari dataframe
print(wine_df.iloc[[0, 3, 8], 0])

# mengunakan negative index untuk mengakses data pada baris dan kolom tertentu dari dataframe
print(wine_df.iloc[-5, 0])

# *label-based selection
# method .loc[row index, column index]

# mengakses row index ke 0 , nama kolom 'country'
print(wine_df.loc[0, 'country'])
print(wine_df.loc[0:5, 'country'])
# semua row, untuk column2 tertentu
print(
    wine_df.loc[:, ['taster_name', 'taster_twitter_handle', 'points']].head())

# *alternatif lain
# namadf[[list string nama columns]][row index]
# menampilkan column tertentu
print(wine_df[['country', 'province']][:].head())
print(wine_df[['country', 'province']][:5])  # menampilkan 5 baris awal

# menganti index
# .set_index('nama columns')
# cara ini kurang tepat karena termasuk modifikasi, dan modifikasi itu tidak mengunakan dataframe asal
print(wine_df.set_index('title').head())

# jika ada modifikasi pada dataframe pandas akan menghasilkan dataframe baru, seperti ini
# df = wine_df.set_index('title')
print(wine_df)
print(df)

# inplace=False, jika inplace adalah True, modifikasi terjadi pada dataframe yang sedang diakses tidak menghasilkan dataframe baru
# wine_df.set_index('title', inplace=True)
print(wine_df)

# mengembalikan index kekondisi semula
# wine_df.reset_index()
print(wine_df)

# *Seleksi data pada dataframe
# (Conditional Selection)
print(wine_df['country'] == 'Italy')

# menampilkan baric yang true saja sesuai dengan conditional
print(wine_df.loc[wine_df['country'] == 'Italy'].head())

print(wine_df.loc[(wine_df['country'] == 'Italy') & (
    wine_df['points'] >= 90)].head())  # where di query sql


# *Mengenal beberapa built in method (logic yang lebih kompleks)
# mengenal method .isin([list])
# where or -> isin , seperti in (,) di query sql
print(wine_df.loc[wine_df['country'].isin(['Italy', 'France'])].head())

# mengenal .isna() dan .notna() kalau di sql query -> is null, not is null
print(wine_df[wine_df['price'].isna()].head())
# select country, price form wine_df where price is null
print(wine_df.loc[wine_df['price'].isna(), ['country', 'price']].head())

# *Menambah kolom baru pada dataframe
# mendata seluruh kolom yang tersedia dengan attribute .columns
print(wine_df.columns)

# menambahkan kolom baru dengan nama critic dan diberi nilai everyone untuk setiap baris
# wine_df['critic']='everyone'
print(wine_df.columns)
print(wine_df['critic'].head(10))

# menambah kolom baru dengan nama index_backward dan diberi nilai bilangan bulat dari besar ke kecil sesuai dengan banyaknya jumlah baris
# wine_df['index_backwards'] = range(len(wine_df),0,-1)
print(wine_df['index_backwards'].head())

# *Menghasilkan ringkasan (summary) data pada Dataframe
# .describe() data statistic dari setiap kolom type numeric
print(wine_df.describe())
print(wine_df['points'].describe())  # untuk columns points
print(wine_df['points'].mean())
print(wine_df['taster_name'].describe())  # untuk columns points type string
# untuk columns points type string, select distinct di sql query
print(wine_df['taster_name'].unique())
# select column , count(*) from df group by column
print(wine_df['taster_name'].value_counts().head())
