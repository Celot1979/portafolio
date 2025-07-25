
# styles.py

# Paleta de Colores
colors = {
    'background': '#121212',
    'secondary_bg': '#1E1E1E',
    'text': '#E0E0E0',
    'accent': '#00BFFF',
    'accent_secondary': '#00FFB8',
    'error': '#FF6B6B',
}

# Tipografía
fonts = {
    'heading': 'Poppins, sans-serif',
    'body': 'Inter, sans-serif',
}

# Estilos base para la aplicación
base_style = {
    'font_family': fonts['body'],
    'color': colors['text'],
    'background_color': colors['background'],
    'line_height': '1.6',
}

# Estilos para los títulos
heading_style = {
    'font_family': fonts['heading'],
    'font_weight': '700',
    'color': '#FFFFFF', # Títulos en blanco puro para más contraste
    'line_height': '1.2',
    'margin_bottom': '0.5em',
}

# Estilos para los enlaces
link_style = {
    'color': colors['accent'],
    'text_decoration': 'none',
    'transition': 'color 0.3s ease',
    '_hover': {
        'color': colors['accent_secondary'],
        'text_decoration': 'underline',
    },
}

# Estilos para los botones
button_style = {
    'background_color': colors['accent'],
    'color': '#FFFFFF',
    'border': 'none',
    'padding': '1em 2em',
    'border_radius': '8px',
    'font_weight': '600',
    'cursor': 'pointer',
    '_hover': {
        'opacity': '0.9',
    },
}

# Animaciones
animations = {
    'fade_in': {
        'animation': 'fadeIn 1s ease-out forwards',
        '@keyframes fadeIn': {
            'from': {'opacity': '0'},
            'to': {'opacity': '1'},
        },
    },
    'gradient_background': {
        'background_size': '400% 400%',
        'animation': 'gradientAnimation 15s ease infinite',
        '@keyframes gradientAnimation': {
            '0%': {'background_position': '0% 50%'},
            '50%': {'background_position': '100% 50%'},
            '100%': {'background_position': '0% 50%'},
        },
    },
}
