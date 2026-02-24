from locust import HttpUser, task, between
import random

PRODUCT_IDS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

class WineShopUser(HttpUser):
    wait_time = between(1, 3)

    def on_start(self):
        self.client.post(
            "/login/",
            data={"username": "admin", "password": "admin"},
            allow_redirects=True
        )

    @task(3)
    def home(self):
        self.client.get("/")

    @task(3)
    def catalogo(self):
        self.client.get("/catalogo/")

    @task(2)
    def ver_producto(self):
        producto_id = random.choice(PRODUCT_IDS)
        self.client.get(f"/producto/{producto_id}/")

    @task(2)
    def agregar_al_carrito(self):
        producto_id = random.choice(PRODUCT_IDS)
        self.client.post(
            "/api/agregar_carrito/",
            json={"producto_id": producto_id, "cantidad": 1}
        )

    @task(1)
    def ver_carrito(self):
        self.client.get("/carrito/")

    @task(1)
    def crud_productos(self):
        self.client.get("/productos/")

    @task(1)
    def crud_clientes(self):
        self.client.get("/clientes/")
