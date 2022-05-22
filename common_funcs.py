def select_image(name):
    return f"ressources\\{name}"


def set_color(color):
    colors = {
        'bg': "#9A9A9A",
        'darkbg': "#242424",
        'text2': 'white',
        'text': 'white',
        'buttonactive': '#001242',
        'onactivebutton': '#050B1C',
        'fourthbg': '#050B1C',
        'entrytext': 'white',
        'error': 'red',
        'tertiarybg': '#D9D9D9',
        'copyright': '#C6CACB'
    }
    return colors[color]