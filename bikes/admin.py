from django.contrib import admin
from .models import TipoBicicleta, Bicicleta, Proveedor, TipoProducto, Producto, Cliente, Pedido, Boleta, Factura, TipoEmpleado, Empleado, Venta, Pago, Arriendo, Reparacion

# Register your models here.

admin.site.register(TipoBicicleta)
admin.site.register(Bicicleta)
admin.site.register(Proveedor)
admin.site.register(TipoProducto)
admin.site.register(Producto)
admin.site.register(Cliente)
admin.site.register(Pedido)
admin.site.register(Boleta)
admin.site.register(Factura)
admin.site.register(TipoEmpleado)
admin.site.register(Empleado)
admin.site.register(Venta)
admin.site.register(Pago)
admin.site.register(Arriendo)
admin.site.register(Reparacion)