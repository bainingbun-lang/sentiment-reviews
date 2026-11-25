# sentiment-reviews

Clasifica reseñas de productos como **positivo**, **negativo** o **neutro**. Sin dependencias, solo Python 3.

## Uso

```bash
python3 sentiment.py reviews.txt
cat reseñas.txt | python3 sentiment.py
```

Cada línea del archivo es una reseña. Al final muestra el porcentaje por categoría.

```
positivo    4  Excelente producto, llegó rápido y la calidad es buena.
negativo   -1  Muy malo, se rompió al segundo día.
neutro      0  Está bien, nada especial.
```

## Cómo funciona

Suma puntos por palabras de un léxico pequeño (español e inglés). Si hay una negación ("no", "nunca", "not") dentro de las dos palabras anteriores, invierte el signo.

## Limitaciones

- No entiende ironía ni contexto.
- El léxico es pequeño; amplíalo en `POSITIVE` y `NEGATIVE`.

## Tests

```bash
python3 test_sentiment.py
```
