def pregunta_01():
    """
    Calcule la suma de los valores de la segunda columna (`value`) del
    archivo `data/data.csv.gz` y retorne el resultado como un número entero.

    Ejemplo del formato de la respuesta:

        214
    """

    raise NotImplementedError



import gzip
from pathlib import Path

data = Path(__file__).parents[1] / "data" / "data.csv.gz"
print(next(f).strip())