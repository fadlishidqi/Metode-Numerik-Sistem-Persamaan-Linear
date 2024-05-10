# Metode Dekomposisi LU Gauss

Metode Dekomposisi LU Gauss adalah sebuah algoritma yang digunakan untuk menyelesaikan sistem persamaan linear \( Ax = b \), di mana \( A \) adalah matriks koefisien, \( x \) adalah vektor solusi yang ingin dicari, dan \( b \) adalah vektor konstanta.

## Algoritma

Algoritma Metode Dekomposisi LU Gauss terdiri dari langkah-langkah berikut:

1. Dekomposisi matriks koefisien \( A \) menjadi matriks segitiga bawah \( L \) dan matriks segitiga atas \( U \) menggunakan eliminasi Gauss.
2. Menyelesaikan sistem persamaan linear \( Ly = b \) untuk mendapatkan vektor \( y \) menggunakan substitusi maju.
3. Menyelesaikan sistem persamaan linear \( Ux = y \) untuk mendapatkan vektor solusi \( x \) menggunakan substitusi mundur.

## Penggunaan

### Fungsi: `luGauss(A, b)`

Fungsi `luGauss` menerima dua parameter: matriks koefisien \( A \) dan vektor konstanta \( b \), dan mengembalikan vektor solusi \( x \) dari sistem persamaan linear \( Ax = b \).

```python
Cntoh penggunaan
J = np.array([[4, 5, 6],
              [1, 3, 8],
              [3, 1, 2]])
K = np.array([1, 2, 2])

print("Solusi x:")
print(metode_lu_gauss(J, K))

