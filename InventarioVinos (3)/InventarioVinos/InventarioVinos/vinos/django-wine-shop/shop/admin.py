from django.contrib import admin
from .models import (
    Categoria, Proveedor, Producto, Perfil, CarritoItem,
    Pedido, DetallePedido, Factura, Inventario, Notificacion,
    Recompensa, SistemaPago
)

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'slug', 'parent')
    prepopulated_fields = {'slug': ('nombre',)}
    search_fields = ('nombre',)

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'correo', 'telefono')
    search_fields = ('nombre', 'correo')

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'precio_oferta', 'stock', 'categoria', 'activo')
    list_filter = ('categoria', 'activo', 'fecha_agregado')
    search_fields = ('nombre', 'descripcion')
    readonly_fields = ('fecha_agregado',)
    fieldsets = (
        ('Información Básica', {
            'fields': ('nombre', 'descripcion', 'categoria', 'proveedor', 'activo')
        }),
        ('Precios y Stock', {
            'fields': ('precio', 'precio_oferta', 'stock')
        }),
        ('Imágenes', {
            'fields': ('imagen_url', 'imagen_adicional_1', 'imagen_adicional_2')
        }),
        ('Detalles del Vino', {
            'fields': ('graduacion', 'pais', 'vina', 'cosecha')
        }),
        ('Fechas', {
            'fields': ('fecha_agregado',),
            'classes': ('collapse',)
        }),
    )

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('nombre_completo', 'usuario', 'tipo_usuario', 'puntos_recompensa')
    list_filter = ('tipo_usuario', 'fecha_registro')
    search_fields = ('nombre_completo', 'usuario__username')
    readonly_fields = ('fecha_registro',)



@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente', 'estado', 'total', 'fecha_pedido')
    list_filter = ('estado', 'metodo_pago', 'fecha_pedido')
    search_fields = ('cliente__username', 'id')
    readonly_fields = ('fecha_pedido',)
    fieldsets = (
        ('Información del Pedido', {
            'fields': ('cliente', 'fecha_pedido', 'estado', 'total')
        }),
        ('Pago', {
            'fields': ('metodo_pago',)
        }),
        ('Envío', {
            'fields': ('direccion_envio', 'ciudad_envio', 'telefono_envio')
        }),
        ('Observaciones', {
            'fields': ('observaciones',)
        }),
    )

@admin.register(DetallePedido)
class DetallePedidoAdmin(admin.ModelAdmin):
    list_display = ('pedido', 'producto', 'cantidad', 'precio_unitario')
    search_fields = ('pedido__id', 'producto__nombre')

@admin.register(Factura)
class FacturaAdmin(admin.ModelAdmin):
    list_display = ('numero_factura', 'pedido', 'total', 'estado_pago', 'fecha_emision')
    list_filter = ('estado_pago', 'fecha_emision')
    search_fields = ('numero_factura', 'pedido__id')
    readonly_fields = ('fecha_emision',)

@admin.register(Inventario)
class InventarioAdmin(admin.ModelAdmin):
    list_display = ('producto', 'tipo_movimiento', 'cantidad_anterior', 'cantidad_nueva', 'fecha')
    list_filter = ('tipo_movimiento', 'fecha')
    search_fields = ('producto__nombre',)
    readonly_fields = ('fecha',)

@admin.register(Notificacion)
class NotificacionAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'usuario', 'tipo', 'leido', 'fecha')
    list_filter = ('leido', 'tipo', 'fecha')
    search_fields = ('titulo', 'usuario__username')
    readonly_fields = ('fecha',)

@admin.register(Recompensa)
class RecompensaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'puntos', 'tipo', 'motivo', 'fecha')
    list_filter = ('tipo', 'fecha')
    search_fields = ('usuario__username', 'motivo')
    readonly_fields = ('fecha',)

@admin.register(SistemaPago)
class SistemaPagoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'activo', 'fecha_creacion')
    list_filter = ('activo', 'fecha_creacion')
    search_fields = ('nombre',)
    readonly_fields = ('fecha_creacion',)
