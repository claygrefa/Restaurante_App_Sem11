# restaurante_app - Semana 11

**Estudiante:** CLAY MEDARDO GREFA TUNAY
**Asignatura:** Programacion Orientada a Objetos
**Semana:** 11 - Taller Practico: Organizacion modular de un sistema
orientado a objetos en Python.

## Descripcion del sistema

`restaurante_app` es una aplicacion de consola escrita en Python que
simula la gestion basica de un restaurante. La aplicacion es una
**evolucion** del proyecto trabajado en la Semana 10: se conservan las
funcionalidades previas y se agregan las mejoras solicitadas para la
Semana 11.

En esta semana se incorporan:

- El atributo **stock** en Producto (nunca negativo).
- La nueva clase **Venta**, que representa la relacion entre un Usuario
  y un Producto vendido.
- La operacion **vender_producto()** en el servicio Restaurante, con
  validacion de usuario, producto, cantidad y stock.
- La **consulta de ventas por usuario**, usando recorrido, comparacion
  y filtrado sobre la coleccion de ventas.
- La **persistencia JSON** ampliada a productos, usuarios y ventas.
- El **manejo especifico de excepciones** de archivo y validacion.

## Estructura del proyecto

```
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
```

## Responsabilidad de cada componente

- **modelos/producto.py:** clase `Producto` con codigo, nombre, precio
  y stock. Incluye validaciones, metodo `vender(cantidad)` y conversion
  a/desde diccionario para JSON.
- **modelos/usuario.py:** clase `Usuario` con identificacion, nombre y
  correo. Incluye validaciones y conversion a/desde JSON.
- **modelos/venta.py:** clase `Venta` que guarda `usuario_id`,
  `producto_codigo` y `cantidad`. Representa la relacion Usuario+Producto.
- **servicios/archivo_servicio.py:** centraliza la lectura y escritura
  de `productos.json`, `usuarios.json` y `ventas.json` con
  `json.dump()`, `json.load()`, `with open()` y `UTF-8`.
- **servicios/restaurante.py:** administra las colecciones y contiene
  toda la logica de negocio: registrar, buscar, listar, vender_producto
  y consultar_ventas_por_usuario.
- **main.py:** interaccion por consola. Solicita datos con `input()`
  y llama a los metodos del servicio Restaurante. **No** modifica
  directamente las colecciones internas.

## Funcionamiento del stock

Cada producto tiene un atributo `stock`. Antes de vender se comprueba:

1. Que el usuario exista.
2. Que el producto exista.
3. Que la cantidad solicitada sea mayor que cero.
4. Que `producto.stock >= cantidad`.

Si alguna validacion falla, la venta se rechaza y el stock no se
modifica. Si todo es correcto, la venta se registra y el stock
disminuye llamando a `producto.vender(cantidad)`.

## Relacion Usuario + Producto -> Venta

La clase `Venta` guarda unicamente las referencias necesarias
(`usuario_id`, `producto_codigo`, `cantidad`). Con esto se puede:

- Registrar una venta en `self._ventas.append(venta)`.
- Consultar las ventas de un usuario recorriendo la coleccion y
  filtrando por `venta.usuario_id`.

## Persistencia

- **productos.json:** guarda los productos y su stock actualizado.
- **usuarios.json:** guarda los usuarios registrados.
- **ventas.json:** guarda las relaciones entre usuarios y productos
  vendidos.

Despues de cada operacion que modifica una coleccion se guarda el
archivo correspondiente. Al iniciar la aplicacion se recuperan las
tres colecciones desde sus archivos JSON.

## Excepciones controladas

- `FileNotFoundError`: si un JSON no existe, se inicia con coleccion
  vacia.
- `json.JSONDecodeError`: controla archivos con contenido invalido.
- `PermissionError`: controla la falta de permisos de lectura o
  escritura.
- `KeyError`: se lanza si a un registro le falta una clave esperada.
- `ValueError`: se usa para validaciones de Producto, Usuario y Venta.

No se utilizan `except: pass` ni capturas genericas para ocultar
errores.

## Forma de ejecucion

Requisitos: Python 3.10 o superior.

```bash
cd restaurante_app
python main.py
```

Al iniciar se muestra un menu por consola con las opciones para
registrar productos, usuarios, vender productos y consultar ventas.

## Pruebas realizadas

1. Ejecutar `main.py`.
2. Registrar un usuario (por ejemplo `1750000001 - LUIS CERDA`).
3. Registrar un producto con stock (por ejemplo `HAM01 - Hamburguesa`,
   precio 3.50, stock 10).
4. Realizar una venta de 2 unidades -> el stock queda en 8.
5. Verificar que `ventas.json` registre la operacion.
6. Consultar las ventas del usuario.
7. Cerrar completamente el programa.
8. Ejecutar nuevamente `main.py`.
9. Confirmar que productos, usuarios y ventas fueron recuperados.
10. Intentar vender una cantidad mayor al stock disponible.
11. Confirmar que la operacion sea rechazada sin alterar el stock ni
    los archivos.


