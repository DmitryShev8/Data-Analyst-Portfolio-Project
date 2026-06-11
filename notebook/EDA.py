# Check distribusi semua data numerik
numerical_columns = df.select_dtypes(include=[np.number]).columns
for column in numerical_columns:
    plt.figure(figsize=(10, 6))
    sns.histplot(df[column], kde=True)
    plt.title(f"Distribusi {column}")
    plt.xlabel(column)
    plt.ylabel("Frekuensi")
    plt.show()

# Average Discount
average_discount = df["Discount"].mean()
print(f"Rata-rata diskon: {average_discount:.2f}")

# Data dari tahun berapa ke tahun berapa dilihat dari kolom Order Date
df["Order Date"] = pd.to_datetime(df["Order Date"])
min_year = df["Order Date"].dt.year.min()
max_year = df["Order Date"].dt.year.max()
print(f"Data mencakup tahun: {min_year} hingga {max_year}")

# Outlier analysis untuk kolom Sales, Quantity, Discount, dan Profit
outlier_columns = ["Sales", "Quantity", "Discount", "Profit"]
for column in outlier_columns:
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=df[column])
    plt.title(f"Boxplot {column} untuk Analisis Outlier")
    plt.xlabel(column)
    plt.show()


# Cek korelasi antara Sales, Quantity, Discount, dan Profit
correlation_matrix = df[["Sales", "Quantity", "Discount", "Profit"]].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", vmin=-
1, vmax=1)
plt.title("Matriks Korelasi antara Sales, Quantity, Discount, dan Profit")
plt.show()

# Analisis nilai outlier pada kolom Sales, Quantity, Discount, dan Profit
for column in outlier_columns:
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]
    print(f"Outliers in '{column}':")
    print(outliers[[column]])
