from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.utils import timezone

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True, null=True)
    slug = models.SlugField(unique=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    imagen_url = models.URLField(blank=True, null=True)
    
    class Meta:
        verbose_name_plural = 'Categorías'
        ordering = ['nombre']
    
    def __str__(self):
        return self.nombre

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    telefono = models.CharField(max_length=20)
    direccion = models.TextField()
    fecha_registro = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    precio_oferta = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, validators=[MinValueValidator(0)])
    stock = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, related_name='productos')
    proveedor = models.ForeignKey(Proveedor, on_delete=models.SET_NULL, null=True, related_name='productos')
    imagen_url = models.URLField()
    imagen_adicional_1 = models.URLField(blank=True, null=True)
    imagen_adicional_2 = models.URLField(blank=True, null=True)
    fecha_agregado = models.DateTimeField(auto_now_add=True)
    activo = models.BooleanField(default=True)
    graduacion = models.CharField(max_length=10, blank=True, null=True)
    pais = models.CharField(max_length=50, blank=True, null=True)
    vina = models.CharField(max_length=100, blank=True, null=True)
    cosecha = models.IntegerField(blank=True, null=True)
    
    class Meta:
        ordering = ['-fecha_agregado']
        indexes = [
            models.Index(fields=['categoria', 'activo']),
            models.Index(fields=['nombre']),
        ]
    
    def __str__(self):
        return self.nombre
    
    @property
    def precio_final(self):
        return self.precio_oferta if self.precio_oferta else self.precio

class Perfil(models.Model):
    TIPOS_USUARIO = [
        ('cliente', 'Cliente'),
        ('proveedor', 'Proveedor'),
        ('admin', 'Administrador'),
    ]
    
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    nombre_completo = models.CharField(max_length=200)
    telefono = models.CharField(max_length=20, blank=True)
    direccion = models.TextField(blank=True)
    ciudad = models.CharField(max_length=100, blank=True)
    puntos_recompensa = models.IntegerField(default=0, validators=[MinValueValidator(0)])
    tipo_usuario = models.CharField(max_length=20, choices=TIPOS_USUARIO, default='cliente')
    fecha_registro = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre_completo

class CarritoItem(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carrito_items')
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1, validators=[MinValueValidator(1)])
    fecha_agregado = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('usuario', 'producto')
    
    def __str__(self):
        return f"{self.usuario.username} - {self.producto.nombre}"
    
    @property
    def subtotal(self):
        return self.cantidad * self.producto.precio_final

class Pedido(models.Model):
    ESTADOS_PEDIDO = [
        ('pendiente', 'Pendiente'),
        ('confirmado', 'Confirmado'),
        ('enviado', 'Enviado'),
        ('entregado', 'Entregado'),
        ('cancelado', 'Cancelado'),
    ]
    
    METODOS_PAGO = [
        ('tarjeta', 'Tarjeta de Crédito'),
        ('efectivo', 'Efectivo'),
        ('transferencia', 'Transferencia Bancaria'),
    ]
    
    cliente = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pedidos')
    fecha_pedido = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=20, choices=ESTADOS_PEDIDO, default='pendiente')
    metodo_pago = models.CharField(max_length=20, choices=METODOS_PAGO)
    direccion_envio = models.TextField()
    ciudad_envio = models.CharField(max_length=100)
    telefono_envio = models.CharField(max_length=20)
    observaciones = models.TextField(blank=True)
    
    class Meta:
        ordering = ['-fecha_pedido']
        indexes = [
            models.Index(fields=['cliente', 'estado']),
            models.Index(fields=['-fecha_pedido']),
        ]
    
    def __str__(self):
        return f"Pedido {self.id} - {self.cliente.username}"

class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='detalles')
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)
    cantidad = models.IntegerField(validators=[MinValueValidator(1)])
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    
    def __str__(self):
        return f"Detalle de {self.pedido.id}"
    
    @property
    def subtotal(self):
        return self.cantidad * self.precio_unitario

class Factura(models.Model):
    ESTADOS_PAGO = [
        ('pendiente', 'Pendiente'),
        ('pagado', 'Pagado'),
        ('cancelado', 'Cancelado'),
    ]
    
    pedido = models.OneToOneField(Pedido, on_delete=models.CASCADE, related_name='factura')
    numero_factura = models.CharField(max_length=50, unique=True)
    fecha_emision = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    estado_pago = models.CharField(max_length=20, choices=ESTADOS_PAGO, default='pendiente')
    fecha_pago = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return self.numero_factura

class Inventario(models.Model):
    TIPOS_MOVIMIENTO = [
        ('entrada', 'Entrada'),
        ('salida', 'Salida'),
        ('ajuste', 'Ajuste'),
    ]
    
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, related_name='movimientos')
    cantidad_anterior = models.IntegerField()
    cantidad_nueva = models.IntegerField()
    tipo_movimiento = models.CharField(max_length=20, choices=TIPOS_MOVIMIENTO)
    motivo = models.TextField(blank=True)
    fecha = models.DateTimeField(auto_now_add=True)
    responsable = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    class Meta:
        ordering = ['-fecha']
    
    def __str__(self):
        return f"{self.producto.nombre} - {self.tipo_movimiento}"

class Notificacion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notificaciones')
    titulo = models.CharField(max_length=200)
    mensaje = models.TextField()
    leido = models.BooleanField(default=False)
    fecha = models.DateTimeField(auto_now_add=True)
    tipo = models.CharField(max_length=50, default='info')
    
    class Meta:
        ordering = ['-fecha']
    
    def __str__(self):
        return self.titulo

class Recompensa(models.Model):
    TIPOS_RECOMPENSA = [
        ('ganado', 'Ganado'),
        ('usado', 'Usado'),
    ]
    
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recompensas')
    puntos = models.IntegerField(validators=[MinValueValidator(0)])
    motivo = models.CharField(max_length=200)
    tipo = models.CharField(max_length=20, choices=TIPOS_RECOMPENSA)
    fecha = models.DateTimeField(auto_now_add=True)
    pedido = models.ForeignKey(Pedido, on_delete=models.SET_NULL, null=True, blank=True)
    
    class Meta:
        ordering = ['-fecha']
    
    def __str__(self):
        return f"{self.usuario.username} - {self.puntos} puntos"

class SistemaPago(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    configuracion_json = models.TextField(blank=True)
    activo = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre
