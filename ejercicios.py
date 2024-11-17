import math

# 1. Monto capitalizado con 6 rentas anuales vencidas
TNA = 0.36
TET = TNA / 4
TEA = (1 + TET) ** 4 - 1
R = 1000
n = 6
F1 = R * ((1 + TEA) ** n - 1) / TEA
print(f"1. Monto capitalizado: S/. {F1:.2f}")

# 2. Monto acumulado con depósitos quincenales
R = 500
n = 12
TEM = 0.03
TEQ = (1 + TEM) ** 0.5 - 1
F2 = R * ((1 + TEQ) ** n - 1) / TEQ
print(f"2. Monto acumulado: S/. {F2:.2f}")

# 3. Monto capitalizado con depósitos mensuales
R = 400
TNA = 0.24
TNS = TNA / 2
TEA = (1 + TNS) ** 2 - 1
TNM = math.pow(1 + TEA, 1 / 12) - 1
n = 8
F3 = R * ((1 + TNM) ** n - 1) / TNM
print(f"3. Monto capitalizado: S/. {F3:.2f}")

# 4. Importe para cancelar préstamo hoy
R = 10
t = 35
TNA = 0.48
TEA = (1 + TNA / 4) ** 4 - 1
TND = math.pow(1 + TEA, 1 / 365) - 1
P = R * ((1 - (1 + TND) ** -t) / TND)
print(f"4. Importe para cancelar préstamo: S/. {P:.2f}")

# 5. Valor presente de una anualidad
R = 2000
TNA = 0.24
TEB = (1 + TNA / 4) ** (60 / 90) - 1
n = 12
VP = R * (1 - (1 + TEB) ** -n) / TEB
print(f"5. Valor presente: S/. {VP:.2f}")

# 6. Cuota mensual para saldo de auto
P = 5000
TEA = 0.18
TEM = math.pow(1 + TEA, 30 / 360) - 1
n = 24
R = P * TEM / (1 - (1 + TEM) ** -n)
print(f"6. Cuota mensual: S/. {R:.2f}")

# 7. Cuota trimestral para amortización de deuda
P = 5000
TNS = 0.045 * 2
TET = math.pow(1 + TNS, 0.5) - 1
n = 6
R = P * TET * (1 + TET) ** n / ((1 + TET) ** n - 1)
print(f"7. Cuota trimestral: S/. {R:.2f}")

# 8. Tasa anual efectiva de un depósito
R = 2000
P = 32000
n = 24
# Usamos interpolación para encontrar la tasa
i0, R0 = 0.035, 32116.735
i1, R1 = 0.036, 31782.042
i = i0 + (P - R0) * (i1 - i0) / (R1 - R0)
TEA = (1 + i) ** 4 - 1
print(f"8. Tasa anual efectiva: {TEA * 100:.2f}%")

# 9. TNA del préstamo en cuotas quincenales
R = 50
P = 1000
n = 24
# Usamos interpolación para encontrar la tasa
i0, R0 = 0.01, 1062.169
i1, R1 = 0.02, 945.696
i = i0 + (P - R0) * (i1 - i0) / (R1 - R0)
TNA = i * 24
print(f"9. TNA: {TNA * 100:.2f}%")

# 10. TET de una renta cuatrimestral
R = 700
S = 7000
n = 9
# Usamos interpolación para encontrar la tasa
i0, R0 = 0.02, 6828.239902
i1, R1 = 0.03, 7111.374
i = i0 + (S - R0) * (i1 - i0) / (R1 - R0)
TEA = (1 + i) ** 3 - 1
TET = math.pow(1 + TEA, 1 / 6) - 1
print(f"10. TET: {TET * 100:.2f}%")

# 11. Número de pagos para préstamo
P = 125000
VP = 1875000
TEA = 0.25
TEM = math.pow(1 + TEA, 1 / 12) - 1
n = math.log(1 + VP * TEM / P) / math.log(1 + TEM)
print(f"11. Número de pagos: {math.ceil(n)}")

