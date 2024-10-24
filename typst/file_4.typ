#set par(justify: true)

#set text(
  font: "Liberation Serif",
  size: 11pt
)

#let title = [
  Este título está en una variable
]

#set page(
  paper: "presentation-16-9",
  numbering: "1",
  footer: align(center + horizon, title),
  columns: 2
)

#place(
  top + center,
  float: true,
  scope: "parent",
  clearance: 1cm
)[
  #text(17pt)[
    *#title*
  ]
  #par(justify: false)[
    *Abstract*
    #lorem(50)
  ]
]

= ¿Qué he hecho?

Este texto está en dos columnas porque indiqué `columns:2` en la regla de `page`.

Puedo usar el valor de la variable `title` escribiendo `#title`.

Escribo comentarios con `//`.

// #lorem(40)

He utilizado `place` para colocar el títuo y el _abstract_. El argumento `clearance` permite añadir cierto espacio. El `center` se hereda, sustituyendo al `align`.

Voy a escribir un cuadrado con `place`. Lo coloco a la derecha y lo coloreo de rojo con `rect(fill:red)`. Su posición es con respecto a la columna.

#place(
  horizon + right,
  rect(fill:red)
)

Si quiero que esté en mitad del texto, indico `float: true`. Este es el cuadrado azul.

= Personalizar headings

Creo una regla `show` para personalizar mis _headings_. Su efecto tiene lugar a partir de este punto.

#show smallcaps: set text(font: "Latin Modern Roman Caps")

#show heading: it => [
  #set align(center)
  #set text(13pt, weight: "regular", font: "Liberation Sans")
  #block(
    smallcaps(it.body)
  )
]

= Otra sección

Usé `smallcaps` para cambiar el tipo de letra.

= Y aquí otra

Ahora voy a personalizar los headings dependiendo de su nivel.

Los de nivel 1 será de una forma, y los de nivel 2 de otra. Accedo al nivel empleando `heading.where(level: 1)`.

Con `where`permite filtrar. Por otro lado, puedo acceder al `body` de un `content` empleando `.body`, que es el texto que me interesa de la variable que contiene el *título*.

#show heading.where(
  level: 1
): x => block(width: 100%)[
  #set align(center)
  #set text(
    13pt,
    weight: "regular",
    font: "Liberation Sans"    
  )
  #smallcaps[#x.body]
]

#show heading.where(
  level: 2
): x => text(
    size: 11pt,
    weight: "bold",
    style: "italic",
    x.body + [.]
)

= Nuevo título

#lorem(10)

== Y aquí va otro
#smallcaps[Hola, ¿funcionan las _smallcaps_?]. ¡Cuidado! Porque dependen de la fuente.

#box(
  stroke: 1pt,
  inset: 1pt,
  outset: 1pt
)[
 Esto es un `box` con `stroke`, `inset` y `outset` editados.
]