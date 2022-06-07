"""Debes utilizar todo lo que sabes sobre los strings, las listas y
sus métodos o funciones para transformar el siguiente texto:

    thor lanzó su martillo#flash ha fallado por un pie! -gritó Loki Laufeyson#dos pies
-le corrigió Hulk#flash menea la cabeza como disgustado... -agrega el comentarista

En:

    Thor lanzó su martillo...

    - ¡Flash ha fallado por un pie! -gritó Loki Laufeyson.
    - Dos pies le corrigió Hulk.
    - Flash menea la cabeza como disgustado... -agrega el comentarista.

Es prohibido modificar directamente el texto.
"""

TEXT_1 = ('thor lanzó su martillo#flash ha fallado por un pie! -gritó Loki Laufeyson'
         '#dos pies -le corrigió Hulk#flash menea la cabeza como disgustado... -agrega el comentarista')

# Divide the text into 4 lines:
text_2 = TEXT_1.split('#')

text_2[0] = (text_2[0] + '...\n').capitalize()

text_2[1] = text_2[1].capitalize()
text_2[1] = '- ' + text_2[1] + '.'
text_2[1] = text_2[1].replace('- ', '- ¡').replace(' l', ' L')

text_2[2] = text_2[2].capitalize()
text_2[2] = '- ' + text_2[2] + '.'
text_2[2] = text_2[2].replace(' -', ' ').replace('h', 'H')

text_2[3] = text_2[3].capitalize()
text_2[3] = '- ' + text_2[3] + '.'

# Join the 4 corrected lines:
FINAL_TEXT = '\n'.join(text_2)

print(FINAL_TEXT)
