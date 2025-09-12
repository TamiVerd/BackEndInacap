from django.shortcuts import render

def bienvenida(request):
    return render(request, 'productos/bienvenida.html')

def index(request):
    # Diccionario de datos de productos
    productos = [
        {
            'id': 1,
            'nombre': 'Camara Nikon Reflex D7200 + Lente 18-140',
            'precio': '$1.290.000',
            'descripcion': 'Cámara réflex digital de alta calidad con lente versátil. Ideal para fotografía profesional y amateur.',
            'imagen': 'nikon.jpg'
        },
        {
            'id': 2,
            'nombre': 'Portátil Asus X507UA Intel Core I3 4GB RAM',
            'precio': '$900.000',
            'descripcion': 'Portátil ligero y eficiente para uso diario, con procesador Intel Core i3 y 4GB de RAM.',
            'imagen': 'asus.jpg'
        },
        {
            'id': 3,
            'nombre': 'Mando dualshock para playstation 4',
            'precio': 'Agotado',
            'descripcion': 'Controlador de juego original para PlayStation 4 con vibración y botones de alta respuesta.',
            'imagen': 'ps4.jpg'
        },
        {
            'id': 4,
            'nombre': 'Tableta Asus Transformer Pad',
            'precio': '$200.000',
            'descripcion': 'Tableta convertible con teclado desmontable. Perfecta para trabajo y entretenimiento.',
            'imagen': 'asus-pad.jpg'
        }
    ]
    
    contexto = {'productos': productos}
    return render(request, 'productos/index.html', contexto)

# Nueva vista para el detalle del producto
from django.shortcuts import render, get_object_or_404
# Importa get_object_or_404 para manejar errores si el producto no existe

def detalle_producto(request, producto_id):
    productos = [
        # ... (la misma lista de diccionarios de arriba)
    ]
    # Busca el producto por su 'id' en la lista
    producto_encontrado = None
    for producto in productos:
        if producto['id'] == producto_id:
            producto_encontrado = producto
            break
            
    # Si no se encuentra el producto, renderiza una página de error o redirige
    if producto_encontrado is None:
        return render(request, 'productos/producto_no_encontrado.html', {'producto_id': producto_id})

    contexto = {'producto': producto_encontrado}
    return render(request, 'productos/detalle_producto.html', contexto)