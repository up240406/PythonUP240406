#Use the countries_data.py file and follow the tasks below
#Sort countries by name, by capital, by population

# ordenados por nombre
from countries_data import countries
paises_ordenados_por_nombre = sorted(countries, key=lambda c: c['name'])
print("Paises ordenados por nombre:")
for country in paises_ordenados_por_nombre:
    print(country['name'])

#ordenados por capital
paises_ordenados_por_capital = sorted(countries, key=lambda c: c['capital'])
print("\nPaises ordenados por capital:")
for country in paises_ordenados_por_capital:
    print(country['capital'])

#ordenados por poblacion
paises_ordenados_por_poblacion = sorted(countries, key=lambda c: c['population'])
print("\nPaises ordenados por poblacion:")
for country in paises_ordenados_por_poblacion:
    print(country['population'])

print("Revisado")