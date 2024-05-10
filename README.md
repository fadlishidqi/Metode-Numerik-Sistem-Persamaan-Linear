# Metode Dekomposisi LU Gauss

Metode Dekomposisi LU Gauss adalah sebuah algoritma yang digunakan untuk menyelesaikan sistem persamaan linear \( Ax = b \), di mana \( A \) adalah matriks koefisien, \( x \) adalah vektor solusi yang ingin dicari, dan \( b \) adalah vektor konstanta.

## Algoritma

Algoritma Metode Dekomposisi LU Gauss terdiri dari langkah-langkah berikut:

1. Dekomposisi matriks koefisien \( A \) menjadi matriks segitiga bawah \( L \) dan matriks segitiga atas \( U \) menggunakan eliminasi Gauss.
2. Menyelesaikan sistem persamaan linear \( Ly = b \) untuk mendapatkan vektor \( y \) menggunakan substitusi maju.
3. Menyelesaikan sistem persamaan linear \( Ux = y \) untuk mendapatkan vektor solusi \( x \) menggunakan substitusi mundur.

# Metode Dekomposisi Crout

Metode Dekomposisi Crout adalah algoritma yang digunakan untuk menyelesaikan sistem persamaan linear dengan memecah matriks koefisien menjadi matriks segitiga bawah \( L \) dan matriks segitiga atas \( U \). Setelah matriks segitiga \( L \) dan \( U \) terbentuk, sistem persamaan linear diselesaikan dengan substitusi maju dan mundur.

## Algoritma

Langkah-langkah untuk Metode Dekomposisi Crout adalah sebagai berikut:

1. Menginisialisasi matriks segitiga bawah \( L \) dengan elemen diagonal utama \( L_ii = 1 \) dan menginisialisasi matriks segitiga atas \( U \) dengan nol.
2. Menghitung elemen matriks segitiga atas \( U \) menggunakan rumus iteratif yang mengurangi produk antara elemen-elemen matriks segitiga bawah \( L \) dan matriks segitiga atas \( U \) dari elemen matriks asli \( A \).
3. Menghitung elemen matriks segitiga bawah \( L \) menggunakan rumus iteratif yang melibatkan elemen-elemen dari matriks segitiga bawah \( L \) dan matriks segitiga atas \( U \) dari matriks asli \( A \).
4. Setelah mendapatkan matriks segitiga atas \( U \) dan matriks segitiga bawah \( L \), sistem persamaan linear \(Ly = b\) dan \(Ux = y\) diselesaikan untuk mendapatkan solusi \( x \).

# Metode Matriks Balikan

Metode Matriks Balikan adalah salah satu pendekatan dalam aljabar linear untuk menyelesaikan sistem persamaan linear. Dalam metode ini, solusi sistem persamaan linear \(Ax = b\) ditemukan dengan menghitung invers dari matriks koefisien \(A\) dan kemudian mengalikan matriks invers tersebut dengan vektor hasil \(b\).

## Algoritma

Langkah-langkah untuk Metode Matriks Balikan adalah sebagai berikut:

1. **Menghitung Invers Matriks**: Pertama-tama, metode ini menghitung invers dari matriks koefisien \(A\) menggunakan fungsi `np.linalg.inv(A)`.
2. **Mengalikan Matriks Invers dengan Vektor Hasil**: Selanjutnya, matriks invers \(A\) dikalikan dengan vektor hasil \(b\) menggunakan operasi perkalian matriks (`np.dot(A_inv, b)`).
3. **Solusi Sistem Persamaan Linear**: Hasil perkalian tersebut akan menjadi solusi dari sistem persamaan linear.
