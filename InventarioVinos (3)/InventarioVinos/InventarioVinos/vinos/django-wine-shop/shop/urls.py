from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('carrito/', views.carrito, name='carrito'),
    path('producto/<int:producto_id>/', views.detalle_producto, name='detalle_producto'),
    path('registro/', views.registro_view, name='registro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('agregar_al_carrito/<int:producto_id>/', views.agregar_carrito, name='agregar_al_carrito'),
    # Alias names expected by templates (keeps backward compatibility)
    path('agregar/<int:producto_id>/', views.agregar_carrito, name='agregar_carrito'),
    path('api/agregar_carrito/', views.agregar_carrito_api, name='agregar_carrito_api'),
    path('eliminar_del_carrito/<int:item_id>/', views.eliminar_carrito, name='eliminar_del_carrito'),
    path('eliminar/<int:item_id>/', views.eliminar_carrito, name='eliminar_carrito'),
    path('actualizar_cantidad/<int:item_id>/', views.actualizar_carrito, name='actualizar_cantidad'),
    path('actualizar/<int:item_id>/', views.actualizar_carrito, name='actualizar_carrito'),
    path('checkout/', views.checkout, name='checkout'),
    # Endpoint para crear pedido (usado por el frontend mediante fetch)
    path('crear_pedido/', views.crear_pedido, name='crear_pedido'),
    path('perfil/', views.perfil_usuario, name='perfil_usuario'),
    path('mis_pedidos/', views.mis_pedidos, name='mis_pedidos'),
    path('detalle_pedido/<int:pedido_id>/', views.detalle_pedido, name='detalle_pedido'),
    path('admin_panel/', views.admin_panel, name='admin_panel'),
    path('generar_reporte_excel/', views.generar_reporte_excel, name='generar_reporte_excel'),
    path('api/carrito/', views.api_carrito, name='api_carrito'),
    path('api/agregar_carrito/', views.agregar_carrito_api, name='agregar_carrito_api'),
    
    # CRUD Productos
    path('productos/', views.productos_list, name='productos_list'),
    path('productos/crear/', views.producto_create, name='producto_create'),
    path('productos/editar/<int:id>/', views.producto_edit, name='producto_edit'),
    path('productos/eliminar/<int:id>/', views.producto_delete, name='producto_delete'),
    
    # CRUD Proveedores
    path('proveedores/', views.proveedores_list, name='proveedores_list'),
    path('proveedores/crear/', views.proveedor_create, name='proveedor_create'),
    path('proveedores/editar/<int:id>/', views.proveedor_edit, name='proveedor_edit'),
    path('proveedores/eliminar/<int:id>/', views.proveedor_delete, name='proveedor_delete'),
    
    # CRUD Pedidos
    path('pedidos/', views.pedidos_list, name='pedidos_list'),
    path('pedidos/editar/<int:id>/', views.pedido_edit, name='pedido_edit'),
    path('pedidos/eliminar/<int:id>/', views.pedido_delete, name='pedido_delete'),
    
    # CRUD Clientes
    path('clientes/', views.clientes_list, name='clientes_list'),
    path('clientes/crear/', views.cliente_create, name='cliente_create'),
    path('clientes/editar/<int:id>/', views.cliente_edit, name='cliente_edit'),
    path('clientes/eliminar/<int:id>/', views.cliente_delete, name='cliente_delete'),
    
    # CRUD Usuarios
    path('usuarios/', views.usuarios_list, name='usuarios_list'),
    path('usuarios/crear/', views.usuario_create, name='usuario_create'),
    path('usuarios/editar/<int:id>/', views.usuario_edit, name='usuario_edit'),
    path('usuarios/eliminar/<int:id>/', views.usuario_delete, name='usuario_delete'),
    
    # Roles
    path('roles/', views.roles_list, name='roles_list'),
]
