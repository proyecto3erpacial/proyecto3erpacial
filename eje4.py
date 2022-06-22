"""
POO
* Elaborar un Programa el cual calcule el costo de produccion, nesecitaras conocer:
- Costo de la materia prima.
- Costo de la mano de obra.
- Cantidad de unidades producidas.
* Mostrar el:
- Costo de produccion total.
- Precio de produccion por unidad.
- El precio del producto al mercado(El doble del precio de produccion).
- Ganancia Generada por unidad.
"""

class produccion():
    def __init__(self, _cmp, _cmo, _cup):
        self.cmp = _cmp
        self.cmo = _cmo
        self.cup = _cup
        self.cpt = (_cmp + _cmo) 
        self.ppu = self.cpt / _cup
        self.ppm = self.ppu * 2
        self.gpu = self.ppu
    
    def mostrar(self):
        print('Costo de la materia prima:', self.cmp)
        print('Costo de la mano de obra:', self.cmo)
        print('Cantidad de unidades producidas:', self.cup)
        print('Costo de produccion total:', self.cpt)
        print('Precio de produccion por unidad:', self.ppu)
        print('El precio del producto al mercado:', self.ppm)
        print('Ganancia Generada por unidad:', self.gpu)
        
cmp = float(input('Escribe el costo de la materia prima: '))
cmo = float(input('Escribe el costo de la mano de obra: '))
cup = float(input('Escribe la cantidad de unidades producidas: '))

pp = produccion(cmp, cmo, cup)
pp.mostrar()