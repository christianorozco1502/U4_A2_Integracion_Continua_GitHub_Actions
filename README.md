Cobertura de pruebas
Modelos (test_models.py):
Se realizaron 2 pruebas para comprobar la creación de videojuegos y usuarios, así como la verificación de contraseñas.

Rutas (test_routes.py):
Se realizaron 3 pruebas para comprobar el acceso a la página de inicio de sesión y verificar que las rutas protegidas no permitan el acceso sin iniciar sesión.

API (test_api.py):
Se realizaron 5 pruebas para comprobar las funciones de consultar, agregar, modificar y eliminar videojuegos mediante la API.

Resultados:
Se ejecutaron un total de 10 pruebas unitarias y todas finalizaron correctamente, sin presentar errores.
Para ejecutar las pruebas se utilizó el siguiente comando: python -m unittest discover -s tests -v
Los resultados completos se guardaron en el archivo results.txt.