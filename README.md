# Metode Dekomposisi LU Gauss

Metode Dekomposisi LU Gauss adalah sebuah algoritma yang digunakan untuk menyelesaikan sistem persamaan linear \( Ax = b \), di mana \( A \) adalah matriks koefisien, \( x \) adalah vektor solusi yang ingin dicari, dan \( b \) adalah vektor konstanta.

## Algoritma

Algoritma Metode Dekomposisi LU Gauss terdiri dari langkah-langkah berikut:

1. Dekomposisi matriks koefisien \( A \) menjadi matriks segitiga bawah \( L \) dan matriks segitiga atas \( U \) menggunakan eliminasi Gauss.
2. Menyelesaikan sistem persamaan linear \( Ly = b \) untuk mendapatkan vektor \( y \) menggunakan substitusi maju.
3. Menyelesaikan sistem persamaan linear \( Ux = y \) untuk mendapatkan vektor solusi \( x \) menggunakan substitusi mundur.

## Penggunaan

### Fungsi: `metode_lu_gauss(A, b)`

Fungsi `metode_lu_gauss` menerima dua parameter: matriks koefisien \( A \) dan vektor konstanta \( b \), dan mengembalikan vektor solusi \( x \) dari sistem persamaan linear \( Ax = b \).

```python
import numpy as np

def metode_lu_gauss(A, b):
    # Implementasi algoritma dekomposisi LU Gauss
    pass

# Contoh penggunaan
A = np.array([[3, 2, -2],
              [-1, -2, 3],
              [2, 1, 2]])
b = np.array([6, -5, 4])

print("Solusi x:")
print(metode_lu_gauss(A, b))

