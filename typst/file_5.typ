
= Funciones

Las plantillas son *funciones* que permiten reutilizar formatos previamente definidos.

#let amazed(term) = box[#emoji.sparkle #term #emoji.sparkle]

Por ejemplo, `amazed(term)` es una función que añade chispas al término que le pasemos como #amazed[argumento]. En la previsualización en local con `Tinymist` no se ve bien y hace falta renderizarlo por completo.

Ahora hago una función algo más compleja, con valores de argumentos (`color`) predefinidos.

  ```
  #let coloured(term, color: purple) = {
    text(color, term)
  }
  ```

#let coloured(term, color: purple) = {
  text(color, term)
}

Ahora si utilizo `coloured` se #coloured[colorea de morado por defecto, y si no del color que] #coloured(color:blue)[le indique].

Los _curly braces_ (`{}`) permiten entrar en modo código.

= Plantillas

Las plantillas funcionan de forma similar, pero envolviendo todo el documento en una función personalizada.

Como esto es algo enrevesado, utilizamos una regla `show` que se aplica a todo el documento.

Algo así: `show: mifuncion`

Vamos a probarlo.

#show: coloured

Esto ahora debería ser morado. A partir de aquí todo el texto es morado. La función se aplica a todo el documento a partir de aquí.

#let blacky(term, color: black) = {
  text(color, term)
}

Paso todo a negro de nuevo aplicando globalmente otra función.

  ```
  #let blacky(term, color: black) = {
    text(color, term)
  }
  ```

`#show: blacky`

#show: blacky

Ahora volvemos al negro.

= Definimos nuestra plantilla

Declaro mi variable `template` que toma como argumento el `doc` y lo modifica.

Cambio la fuente y defino una regla `show`.

#let template(doc) = [
  #set text(font: "Ubuntu Mono")
  #show "a": [A]
  #doc
]

#show: template

En esta plantilla cada vez que escribo la letra A aparece en mayúscula. Y la letra es `Ubuntu mono`.

En el siguiente archivo (`file_6.typ`) definiré una plantilla de documento.