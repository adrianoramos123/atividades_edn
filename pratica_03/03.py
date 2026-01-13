"""
3- Conversor de Temperatura
Crie um programa que converta temperaturas entre Celsius, Fahrenheit e Kelvin.
O usuário deve informar a temperatura, a unidade de origem e a unidade para qual deseja converter.
"""

temperatura = float(input("Informe o valor númerico da temperatura: "))
print("Unidades de temperatura")
print("1. Celsius (°C)")
print("2. Fahrenheit (°F)")
print("3. Kelvin (K)")
unidade_origem = int(input("Informe o número da unidade de origem: "))
unidade_destino = int(input("Informe o número da unidade de destino: "))

if unidade_origem == 1 and unidade_destino == 2:
    celsius_fahrenheit = (temperatura*(9/5))+32
    print(f"{temperatura: .2f} (°C) = {celsius_fahrenheit: .2f} (°F)")

elif unidade_origem == 1 and unidade_destino == 3:
    celsius_kelvin = temperatura + 273.15
    print(f"{temperatura: .2f} (°C) = {celsius_kelvin: .2f} (K)")

elif unidade_origem == 2 and unidade_destino == 1:
    fahrenheit_celsius = (temperatura-32)*(5/9)
    print(f"{temperatura: .2f} (°F) = {fahrenheit_celsius: .2f} (°C)")

elif unidade_origem == 2 and unidade_destino == 3:
    fahrenheit_kelvin = (temperatura-32)*(5/9)+273.15
    print(f"{temperatura: .2f} (°F) = {fahrenheit_kelvin: .2f} (K)")

elif unidade_origem == 3 and unidade_destino == 1:
    kelvin_celsius = temperatura - 273.15
    print(f"{temperatura: .2f} (K) = {kelvin_celsius: .2f} (°C)")

else:
    kelvin_fahrenheit = (temperatura - 273.15)*(9/5)+32
    print(f"{temperatura: .2f} (K) = {kelvin_fahrenheit: .2f} (°F)")