# Restaurante App - Semana 11

## Estudiante
Cesar Ayala

## Descripción del Sistema
Evolución del proyecto `restaurante_app` orientada a la Programación Orientada a Objetos. Esta versión incorpora la persistencia JSON completa para productos, usuarios y ventas, implementando la relación principal entre un `Usuario` y un `Producto` a través de la entidad `Venta`, controlando rigurosamente el stock disponible.

## Estructura del Proyecto
restaurante_app/
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante.py
├── main.py
└── README.md

## Responsabilidad de los Componentes
- **modelos/producto.py:** Administra la clase Producto, validaciones de stock positivo y serialización JSON.
- **modelos/usuario.py:** Administra la clase Usuario y sus propiedades.
- **modelos/venta.py:** Modela la relación asociando usuario, producto y cantidad.
- **servicios/restaurante.py:** Contiene toda la lógica de negocio, búsquedas, control de stock y coordinación de colecciones.
- **servicios/archivo_servicio.py:** Centraliza la lectura y escritura segura mediante `json.load()` y `json.dump()`.
- **main.py:** Gestiona la interfaz por consola y la interacción mediante `input()`.

## Pruebas Realizadas
1. Registro exitoso de usuarios y productos con stock inicial.
2. Ejecución de ventas válidas reduciendo de forma automática el stock y actualizando `ventas.json` y `productos.json`.
3. Intento de venta con stock insuficiente o cantidades inválidas (rechazado correctamente sin alterar datos).
4. Consulta filtrada de ventas por usuario.
5. Cierre completo de la aplicación y reinicio comprobando la persistencia y recuperación de los tres archivos JSON.