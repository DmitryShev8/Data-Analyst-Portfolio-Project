# Apa penyebab adanya outlier pada kolom Sales, Quantity, Discount, dan Profit?
# Penyebab adanya outlier pada kolom Sales, Quantity, Discount, dan Profit bisa disebabkan oleh beberapa faktor, seperti:
# 1. Kesalahan input data: Nilai yang sangat tinggi atau rendah mungkin merupakan hasil dari kesalahan saat memasukkan data.
# 2. Transaksi besar: Beberapa transaksi mungkin memiliki nilai penjualan atau keuntungan yang sangat tinggi karena pembelian dalam jumlah besar atau produk dengan harga tinggi.
# 3. Diskon ekstrem: Diskon yang sangat tinggi (mendekati 1) mungkin menunjukkan adanya promosi khusus atau kesalahan dalam pencatatan diskon.
# 4. Produk unik: Beberapa produk mungkin memiliki harga yang sangat tinggi atau rendah, yang dapat menyebabkan nilai outlier pada kolom Sales dan Profit.
# 5. Musiman atau tren pasar: Perubahan musiman atau tren pasar tertentu dapat menyebabkan lonjakan penjualan atau keuntungan yang tidak biasa, yang dapat muncul sebagai outlier dalam data.

# Apakah ada transaksi besar yang menyebabkan outlier pada kolom Sales dan Profit?
large_sales_outliers = df[df["Sales"] > df["Sales"].quantile(0.99)]
large_profit_outliers = df[df["Profit"] > df["Profit"].quantile(0.99)]
print("Transaksi besar yang menyebabkan outlier pada kolom Sales:")
print(large_sales_outliers[["Order ID", "Sales", "Profit"]])
print("Transaksi besar yang menyebabkan outlier pada kolom Profit:")
print(large_profit_outliers[["Order ID", "Sales", "Profit"]])

# bandingkan dengan outlier keseluruhan pada kolom Sales dan Profit lebih dari 1.5 IQR
Q1_sales = df["Sales"].quantile(0.25)
Q3_sales = df["Sales"].quantile(0.75)
IQR_sales = Q3_sales - Q1_sales
lower_bound_sales = Q1_sales - 1.5 * IQR_sales
upper_bound_sales = Q3_sales + 1.5 * IQR_sales
overall_sales_outliers = df[(df["Sales"] < lower_bound_sales) | (df["Sales"] > upper_bound_sales)]
Q1_profit = df["Profit"].quantile(0.25)
Q3_profit = df["Profit"].quantile(0.75)
IQR_profit = Q3_profit - Q1_profit
lower_bound_profit = Q1_profit - 1.5 * IQR_profit
upper_bound_profit = Q3_profit + 1.5 * IQR_profit
overall_profit_outliers = df[(df["Profit"] < lower_bound_profit) | (df["Profit"] > upper_bound_profit)]
print("Outlier keseluruhan pada kolom Sales:")
print(overall_sales_outliers[["Order ID", "Sales", "Profit"]])
print("Outlier keseluruhan pada kolom Profit:")
print(overall_profit_outliers[["Order ID", "Sales", "Profit"]])
# Kesimpulan: Transaksi besar untuk sales ternyata sedikit (100 baris dari 1167 (outlier keseluruhan) dan untuk profit juga sedikit (100 baris dari 1881 (outlier keseluruhan))
# Cek faktor lain yang mungkin menyebabkan outlier pada kolom Sales dan Profit, seperti kategori produk atau wilayah penjualan
# Cek kategori produk untuk transaksi dengan outlier pada Sales
large_sales_outliers_category = large_sales_outliers[["Order ID", "Sales", "Profit", "Category"]]
print("Kategori produk untuk transaksi dengan outlier pada Sales:")
print(large_sales_outliers_category)
# Cek wilayah penjualan untuk transaksi dengan outlier pada Sales
large_sales_outliers_region = large_sales_outliers[["Order ID", "Sales", "Profit", "Region"]]
print("Wilayah penjualan untuk transaksi dengan outlier pada Sales:")
print(large_sales_outliers_region)
# Cek frekuensi kategori produk untuk transaksi dengan outlier pada Sales
outlier_category_counts = overall_sales_outliers["Category"].value_counts()
print("Frekuensi kategori produk untuk transaksi dengan outlier pada Sales:")
print(outlier_category_counts)
outlier_category_counts = overall_sales_outliers["Category"].value_counts()
print("Frekuensi kategori produk untuk transaksi dengan outlier pada Sales:")
print(outlier_category_counts)
# Cek frekuensi kategori produk untuk transaksi dengan outlier pada Profit
outlier_category_counts = overall_profit_outliers["Category"].value_counts()
print("Frekuensi kategori produk untuk transaksi dengan outlier pada Profit:")
print(outlier_category_counts)
# Cek frekuensi region untuk transaksi dengan outlier pada Sales
outlier_region_counts = overall_sales_outliers["Region"].value_counts()
print("Frekuensi region untuk transaksi dengan outlier pada Sales:")
print(outlier_region_counts)
# Cek frekuensi wilayah penjualan untuk transaksi dengan outlier pada Profit
outlier_region_counts = overall_profit_outliers["Region"].value_counts()
print("Frekuensi wilayah penjualan untuk transaksi dengan outlier pada Profit:")
print(outlier_region_counts)
# Kesimpulan: Tidak ada pola yang jelas dalam kategori dan region
# Next steps: Analisis lebih lanjut untuk mencari faktor lain yang mungkin menyebabkan outlier, seperti waktu transaksi (musiman atau tren)
# Analisis waktu transaksi untuk melihat apakah ada pola musiman atau tren yang mungkin menyebabkan outlier pada Sales dan Profit
df["Order Month"] = df["Order Date"].dt.to_period("M")
monthly_sales = df.groupby("Order Month")["Sales"].sum()
monthly_profit = df.groupby("Order Month")["Profit"].sum()
plt.figure(figsize=(12, 6))
monthly_sales.plot(label="Total Sales", marker="o")
monthly_profit.plot(label="Total Profit", marker="o")
plt.title("Tren Bulanan Total Sales dan Total Profit")
plt.xlabel("Order Month")
plt.ylabel("Total")
plt.legend()
plt.show()
# Kesimpulan: Tidak ditemukan pola musiman atau tren yang jelas dalam data, sehingga faktor lain mungkin perlu dianalisis untuk menjelaskan adanya outlier pada Sales dan Profit.
# Next steps: Analisis berdasarkan segmen pelanggan sales dan profit untuk melihat apakah ada segmen pelanggan tertentu yang lebih sering mengalami outlier pada Sales dan Profit.
segment_sales_outliers = overall_sales_outliers["Segment"].value_counts()
print("Frekuensi segmen pelanggan untuk transaksi dengan outlier pada Sales:")
print(segment_sales_outliers)
segment_profit_outliers = overall_profit_outliers["Segment"].value_counts()
print("Frekuensi segmen pelanggan untuk transaksi dengan outlier pada Profit:")
print(segment_profit_outliers)
# Segmen consumer memiliki frekuensi outlier tertinggi untuk sales dan profit, yang mungkin menunjukkan bahwa segmen ini lebih rentan terhadap transaksi besar atau kerugian besar. 
# Analisis lebih lanjut dapat dilakukan untuk memahami karakteristik pelanggan dalam segmen ini dan faktor-faktor yang mungkin menyebabkan outlier pada Sales dan Profit.

segmen_consumer_sales_outliers = overall_sales_outliers[overall_sales_outliers["Segment"] == "Consumer"]
print("Transaksi dengan outlier pada Sales untuk segmen Consumer:")
print(segmen_consumer_sales_outliers[["Order ID", "Sales", "Profit", "Segment"]])

segmen_consumer_profit_outliers = overall_profit_outliers[overall_profit_outliers["Segment"] == "Consumer"]
print("Transaksi dengan outlier pada Profit untuk segmen Consumer:")
print(segmen_consumer_profit_outliers[["Order ID", "Sales", "Profit", "Segment"]])
