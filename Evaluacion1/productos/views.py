from django.shortcuts import render, redirect

# Diccionario de datos de productos. Es mejor definirlo aquí para que ambas funciones lo usen.
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

def bienvenida(request):
    """
    Vista para la página de bienvenida.
    """
    return render(request, 'productos/bienvenida.html')

def catalogo(request):
    """
    Vista para el catálogo de productos.
    """
    contexto = {'productos': productos}
    return render(request, 'productos/catalogo.html', contexto)

from django.shortcuts import render, redirect

def detalle_producto(request, producto_id):
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

    producto_encontrado = None
    for producto in productos:
        if producto['id'] == producto_id:
            producto_encontrado = producto
            break
            
    if producto_encontrado:
        contexto = {'producto': producto_encontrado}
        return render(request, 'productos/detalle_producto.html', contexto)
    else:
        # Redirige al catálogo si el producto no se encuentra
        return redirect('productos:catalogo')