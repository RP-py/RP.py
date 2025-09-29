from abc import ABC, abstractmethod
import math

class FormaGeometrica(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

class CalculadoraArea:
    def obtener_area(self, forma: FormaGeometrica):
        return forma.calcular_area()

class Rectangulo(FormaGeometrica):
    def __init__(self, alto: float, ancho: float):
        self.alto = alto
        self.ancho = ancho
        
    def calcular_area(self):
        return self.alto * self.ancho

class Circulo(FormaGeometrica):
    def __init__(self, radio: float):
        self.radio = radio
        
    def calcular_area(self):
        return math.pi * self.radio**2

class Triangulo(FormaGeometrica):
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura
        
    def calcular_area(self):
        return (self.base * self.altura) / 2

calculadora = CalculadoraArea()
rectangulo = Rectangulo(alto=10, ancho=5)
circulo = Circulo(radio=3)
triangulo = Triangulo(base=4, altura=6)

print(f"Área del Rectángulo: {calculadora.obtener_area(rectangulo)}")
print(f"Área del Círculo: {calculadora.obtener_area(circulo):.2f}")
print(f"Área del Triángulo: {calculadora.obtener_area(triangulo)}")