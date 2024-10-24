= Prueba

_Hola_, esto es una *prueba*. Comencemos a trabajar con `typst`.

+ Perro
    - Pastor alemán
    - Labrador
    - Caniche
+ Gato
+ Caballo
+ Oveja

== Figuras

#figure(
    image("glacier.jpg", width: 70%),
    caption: [_Glaciar_]
) <glaciar>

Observemos el glaciar de la figura @glaciar.

== Modos

Si estoy en _code mode_, tras escribir `#figure`, la función `image` se escribe sin el `#`.

Por otro lado, el _caption_ de la figura es texto en formato _markup_, que va dentro de _brackets_: `[...]`.

+ Un _content block_ `[...]` puede contener texto, pero también cualquier tipo de _markup_, llamada a funciones, etc.

+ Un `string` es una secuencia de caracteres entre comillas dobles.

== Referencias

Aquí va una referencia: @manjavacas2024experimental.

== Matemáticas

Esto es una *ecuación* en una línea aparte:

$ Q = rho A v + C $

Y esto es una ecuación _inline_: $F = m dot a$

Y si quiero una variable tipo texto:

$ "Fuerza" = m dot a $

Cosas más complicadas:

$ 7.32 beta + sum_(i=0)^nabla (Q_i (alpha_i - epsilon)) / 2 $

Veamos como introducir un vector (se incluye mediante una función):

$ v := vec(x_1, x_2, x_3, ...) $

Letras caligráficas con `cal`: $cal(P) != cal(R)$.

Y otros símbolos:

$ a arrow.dotted b $
$ c arrow.squiggly d $

#bibliography("bibliography.bib")