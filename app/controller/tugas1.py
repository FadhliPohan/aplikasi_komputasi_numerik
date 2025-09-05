from pydantic import BaseModel
from fastapi import APIRouter
from typing import List
import math

router = APIRouter()  # Router khusus untuk tugas1

# Pydantic model untuk input data
class MaclaurinRequest(BaseModel):
    x: float  # nilai x yang ingin dihitung

# Fungsi untuk menghitung Maclaurin Series dari cos^2(x)
def maclaurin_series_cos2(x: float, terms: int = 5) -> float:
    """
    Menghitung Maclaurin Series untuk cos^2(x) sampai n suku.
    :param x: nilai x untuk dihitung.
    :param terms: jumlah suku dalam deret Maclaurin.
    :return: nilai estimasi dari cos^2(x) menggunakan deret Maclaurin.
    """
    result = 1  # suku pertama
    # Deret dimulai dari suku kedua
    for n in range(1, terms):
        if n % 2 == 1:  # hanya untuk suku dengan pangkat genap
            result -= (x**n) / math.factorial(n)
    
    return result

# Endpoint untuk menerima input x dan menghitung Maclaurin Series dari cos^2(x)
@router.post("/tugas1-Maclaurin")
def tugas1_maclaurin(request: MaclaurinRequest):
    # Mengambil nilai x dari input
    x = request.x
    # Menghitung nilai Maclaurin Series untuk cos^2(x)
    result = maclaurin_series_cos2(x)
    return {
        "x": x,
        "cos^2(x) (Maclaurin Approximation)": result
    }
