import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df = pd.read_csv("Superstore.csv")
df

# Data Info
df.info()

data_dictionary = pd.DataFrame({
    "Column": [
        "ID", "Order ID", "Order Date", "Ship Date", "Ship Mode",
        "Customer ID", "Customer Name", "Segment", "Country", "City",
        "State", "Postal Code", "Region", "Product ID", "Category",
        "Sub-Category", "Product Name", "Sales", "Quantity", "Discount", "Profit"
    ],
    "Type": [
        "int64", "object", "object", "object", "object",
        "object", "object", "object", "object", "object",
        "object", "int64", "object", "object", "object",
        "object", "object", "float64", "int64", "float64", "float64"
    ],
    "Definition": [
        "Identifier (unique)",
        "Pesanan unik untuk setiap transaksi",
        "Tanggal ketika pesanan dibuat",
        "Tanggal ketika pesanan dikirim",
        "Jenis mode pengiriman (First Class, Second Class, Standard Class, Same Day)",
        "Identifier pelanggan unik",
        "Nama lengkap pelanggan",
        "Segment pelanggan (Consumer, Corporate, Home Office)",
        "Negara tempat pelanggan berada",
        "Kota tempat pelanggan berada",
        "Provinsi tempat pelanggan berada",
        "Kode pos tempat pelanggan berada",
        "Wilayah penjualan (East, West, Central, South)",
        "Produk unik yang dijual",
        "Kategori produk",
        "Sub-kategori produk",
        "Nama produk",
        "Total pendapatan penjualan",
        "Jumlah item yang dibeli",
        "Diskon yang diberikan pada transaksi (antara 0 dan 1)",
        "Keuntungan yang diperoleh dari penjualan"
    ]
})

data_dictionary

# Check Unique Values
for column in df.columns:
    unique_values = df[column].unique()
    print(f"Unique values in '{column}': {unique_values}\n")

# Cek banyak baris dan kolom
print(f"Jumlah baris: {df.shape[0]}")
print(f"Jumlah kolom: {df.shape[1]}")

# Order Id punya kode unik, contoh: CA-2017-152156
# Ambil 2 huruf pertama untuk cek apakah ada pola tertentu
df["Order ID Prefix"] = df["Order ID"].str[:2]
print("Unique values in 'Order ID Prefix':")
print(df["Order ID Prefix"].unique())

# Product ID punya kode unik, contoh: FUR-BO-10001798
# Ambil 3 huruf pertama untuk cek apakah ada pola tertentu
df["Product ID Prefix"] = df["Product ID"].str[:3]
print("Unique values in 'Product ID Prefix':")
print(df["Product ID Prefix"].unique())

# Ambil 2 huruf setelah tanda '-' pada Product ID untuk cek apakah ada pola tertentu
df["Product ID Middle"] = df["Product ID"].str.split("-").str[1]
print("Unique values in 'Product ID Middle':")
print(df["Product ID Middle"].unique())

# Apakah 2 huruf pertama pada Customer ID sama dengan inisial nama pelanggan
# Initial CG dengan nama Claiere Gute (CG)
# Cek jumlah yang true dan false
df["Customer ID Initial"] = df["Customer ID"].str[:2]
df["Customer Name Initial"] = df["Customer Name"].str.split().str[0].str[0] + df["Customer Name"].str.split().str[1].str[0]
df["Customer ID Matches Name Initial"] = df["Customer ID Initial"] == df["Customer Name Initial"]
matches_count = df["Customer ID Matches Name Initial"].value_counts()
print("Jumlah Customer ID yang cocok dengan inisial nama pelanggan:")
print(matches_count)

# Cek yang false
false_matches = df[df["Customer ID Matches Name Initial"] == False][["Customer ID", "Customer Name", "Customer ID Initial", "Customer Name Initial"]]
print("Contoh Customer ID yang tidak cocok dengan inisial nama pelanggan:")
print(false_matches)

# Cek apakah ada Product ID yang kode kategori atau sub-kategori yang tidak sesuai dengan nama kolom kategori dan sub-kategori
# Contoh: FUR-BO-10001798, kode kategori FUR (Furniture), kode sub-kategori BO (Bookcases)
df["Product ID Category"] = df["Product ID"].str.split("-").str[0]
df["Product ID Sub-Category"] = df["Product ID"].str.split("-").str[1]
df["Category Matches Product ID"] = df["Category"].str[:3].str.upper() == df["Product ID Category"]
df["Sub-Category Matches Product ID"] = df["Sub-Category"].str[:2].str.upper() == df["Product ID Sub-Category"]
category_matches_count = df["Category Matches Product ID"].value_counts()
sub_category_matches_count = df["Sub-Category Matches Product ID"].value_counts()
print("Jumlah kategori yang cocok dengan kode kategori pada Product ID:")
print(category_matches_count)
print("Jumlah sub-kategori yang cocok dengan kode sub-kategori pada Product ID:")
print(sub_category_matches_count)

# Apakah ada inkonsistensi dalam data?
# Inkonsistensi dapat berupa nilai yang tidak sesuai dengan definisi kolom, seperti nilai negatif pada kolom 'Sales' atau 'Profit', atau diskon yang lebih besar dari 1.
# Cek nilai negatif pada kolom 'Sales' dan 'Profit'
negative_sales = df[df['Sales'] < 0]
negative_profit = df[df['Profit'] < 0]
print("Baris dengan nilai negatif pada 'Sales':")
print(negative_sales)

# Cek diskon yang lebih besar dari 1
invalid_discount = df[df['Discount'] > 1]
print("Baris dengan diskon lebih besar dari 1:")
print(invalid_discount)

# Cek Missing Values
missing_values = df.isnull().sum()
print("Missing values in each column:")
print(missing_values)

# Check duplicated values
duplicated_values = df.duplicated().sum()
print(f"Jumlah nilai duplikat: {duplicated_values}")
