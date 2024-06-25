from django.db import models

# Create your models here.

class TipoBicicleta(models.Model):
    t_bici_id = models.IntegerField(primary_key=True)
    nombre_t_bici = models.CharField(max_length=20)
    
    def __str__(self):
        return str(self.nombre_t_bici)

class Bicicleta(models.Model):
    id_bici = models.IntegerField(primary_key=True)
    marca_bici = models.CharField(max_length=20)
    modelo_bici = models.CharField(max_length=20)
    tamano_bici = models.CharField(max_length=20)
    precio_bici = models.IntegerField()
    tipo_bicicleta = models.ForeignKey(TipoBicicleta, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.marca_bici) + ' ' + str(self.modelo_bici)

class Proveedor(models.Model):
    id_proveedor = models.IntegerField(primary_key=True)
    nombre_proveedor = models.CharField(max_length=30)
    correo_proveedor = models.CharField(max_length=100)
    telefono_proveedor = models.CharField(max_length=20)
    direccion_proveedor = models.CharField(max_length=100)
    tipo_proveedor = models.CharField(max_length=20)
    def __str__(self):
        return str(self.nombre_proveedor)

class TipoProducto(models.Model):
    t_prod_id = models.IntegerField(primary_key=True)
    nombre_t_prod = models.CharField(max_length=20)
    def __str__(self):
        return str(self.nombre_t_prod)

class Producto(models.Model):
    id_prod = models.IntegerField(primary_key=True)
    nombre_prod = models.CharField(max_length=30)
    precio_prod = models.IntegerField()
    stock_prod = models.IntegerField()
    pedido = models.ForeignKey('Pedido', on_delete=models.CASCADE)
    tipo_producto = models.ForeignKey(TipoProducto, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.nombre_prod)

class Cliente(models.Model):
    id_cli = models.IntegerField(primary_key=True)
    nombre_cli = models.CharField(max_length=20)
    apellido_cli = models.CharField(max_length=20)
    correo_cli = models.CharField(max_length=100)
    telefono_cli = models.CharField(max_length=20)
    direccion_cli = models.CharField(max_length=100)
    def __str__(self):
        return str(self.nombre_cli) + ' ' + str(self.apellido_cli)

class Pedido(models.Model):
    id_pedido = models.IntegerField(primary_key=True)
    cantidad_pedido = models.IntegerField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    def __str__(self):
        return 'Pedido N°' + str(self.id_pedido)


class Boleta(models.Model):
    id_pago = models.IntegerField(primary_key=True)
    id_boleta = models.IntegerField()
    monto_boleta = models.IntegerField()
    def __str__(self):
        return 'Boleta N°' + str(self.id_boleta)

class Factura(models.Model):
    id_pago = models.IntegerField(primary_key=True)
    id_factura = models.IntegerField()
    monto_factura = models.IntegerField()
    def __str__(self):
        return 'Factura N°' + str(self.id_factura)

class TipoEmpleado(models.Model):
    t_emp_id = models.IntegerField(primary_key=True)
    nombre_t_emp = models.CharField(max_length=20)
    def __str__(self):
        return str(self.nombre_t_emp)

class Empleado(models.Model):
    id_emp = models.IntegerField(primary_key=True)
    nombre_emp = models.CharField(max_length=20)
    apellido_emp = models.CharField(max_length=20)
    correo_emp = models.CharField(max_length=100)
    telefono_emp = models.CharField(max_length=20)
    tipo_empleado = models.ForeignKey(TipoEmpleado, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.nombre_emp) + ' ' + str(self.apellido_emp) + ' - ' + str(self.tipo_empleado.nombre_t_emp)

class Venta(models.Model):
    id_venta = models.IntegerField(primary_key=True)
    fecha_venta = models.DateField()
    monto_venta = models.IntegerField()
    empleado = models.ForeignKey('Empleado', on_delete=models.CASCADE)
    pago = models.ForeignKey('Pago', on_delete=models.CASCADE, related_name='ventas')
    def __str__(self):
        return 'Venta N°' + str(self.id_venta)

class Pago(models.Model):
    id_pago = models.IntegerField(primary_key=True)
    fecha_pago = models.DateField()
    monto_pago = models.IntegerField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name='pagos')
    def __str__(self):
        return 'Pago N°' + str(self.id_pago)

class Arriendo(models.Model):
    id_arriendo = models.IntegerField(primary_key=True)
    fecha_arriendo = models.DateField()
    fecha_entrega = models.DateField()
    cantidad_arriendo = models.IntegerField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    bicicleta = models.ForeignKey(Bicicleta, on_delete=models.CASCADE)
    def __str__(self):
        return 'Arriendo N°' + str(self.id_arriendo) + ' -> ' + str(self.cliente.nombre_cli) + ' ' + str(self.cliente.apellido_cli) + '/' + str(self.bicicleta.modelo_bici)

class Reparacion(models.Model):
    id_rep = models.IntegerField(primary_key=True)
    fecha_ini_rep = models.DateField()
    fecha_fin_rep = models.DateField()
    descripcion_rep = models.CharField(max_length=255)
    estado_rep = models.CharField(max_length=20)
    bicicleta = models.ForeignKey(Bicicleta, on_delete=models.CASCADE)
    def __str__(self):
        return 'Reparacion N°' + str(self.id_rep) + ' -> ' + str(self.bicicleta.marca_bici) + ' - ' + str(self.bicicleta.modelo_bici)