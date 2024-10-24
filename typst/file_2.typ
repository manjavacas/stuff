= Estilo

== Párrafos

Además de funciones que _insertan_ contenido como `image`, tenemos otras que _manipulan_ contenido.

Definimos un párrafo con `par` e indicamos indentación de 1cm + `justify`:

#par(first-line-indent: 1cm, hanging-indent: 1cm, justify: true)[
  Esto es un texto con sangría para probar las capacidades de la función `par`: justificación, espaciado, etc.Aprovecho para probar los saltos de línea manuales mediante `\`, así comola introducción de texto con la función `lorem`.\
  Esta es la segunda línea, también con sangría.\
  Tercera línea. Veamos si funciona la justificación...\
  #lorem(40)
]

Según la documentación, el `content` que se pasa a una función en `typst` va entre _brackets_ tras llamar a la función. Es lo mismo:

`#par([hola])` que `#par()[hola]`

Por ejemplo:

+ #par(lorem(40))

+ #par([#lorem(40)])

== Reglas

Podemos definir reglas para que apliquen a todas las ocurrencias de un contenido a lo largo del texto. Para ello empleamos `set`.

*Texto sin justificar:* 

#lorem(40)

*A partir de aquí, defino una regla y el texto siempre se justifica:*

#set par(justify: true)

#lorem(40)

Escribo `#set` seguido de la función con parámetros estáticos/_default_ (ej. `par(justify:true)`).

= Reglas _show_

Vamos ahora con `show`. Nos permite redefinir cómo `typst` muestra ciertos elementos.

Definimos una funcion personalizada que siempre muestra la palabra "Robot" junto a un logo.

#show "Robot": name => box[
  #box(image("bot.svg", height: 0.7em))
  #name
]

Lo probamos escribiendo Robot y viendo qué pasa.

#show "Glaciar": name => box[
  #box(image("glacier.jpg", height: 0.7em))
  #name
]

Otro `show` personalizado para Glaciar. Aunque este se ve peor.

+ Indicamos después de `show` la cadena de texto que se verá afectada.

+ Después, se indica el argumento `name`. Es una variable que tiene efecto a lo largo de `show`.

+ Se utiliza un `box` para evitar salto de línea entre logo y nombre.


Voy a añadir un salto de página con `pagebreak` y fijar una serie de reglas a continuación.

#pagebreak()

#set text(
  18pt,
  font: "new computer modern", 
  style: "oblique",
  weight: "semibold"
)

#set page(
  paper: "a5",
  margin: (x: 10pt, y: 15pt)
)

#set par(
  justify: true,
  leading: 1cm
)

Esto es un nuevo comienzo. Soy un Robot.

Cambié la configuración por defecto de:\ `text`, `page` y `par`.

Incluyo ahora la numeración de _headings_ (función `heading`).

#set heading(numbering: "1.")

= Y ahora

= Tengo números

== En los _headings_

Y con letras...

#set heading(numbering: "1.a")

= Esto es

== Otra prueba

== Para verlo

`typst` internamente llama a `heading` y `text` cada vez que escribimos `= Heading` o _markup_. Es _syntax sugar_ para estas funciones.