#let conf(
  title: none,
  authors: (),
  abstract: [],
  doc
) = {

  // Sets globales

  set heading(numbering: "1.")

  show heading: it => [
    #it
    #v(.2cm)
  ]

  set page(
    paper: "us-letter",
    footer: context [
      #align(center)[
        #counter(page).display()
      ]
    ],
    columns: 2
  )

  set par(justify: true)

  set text(
    font: "Libertinus Serif",
    size: 11pt
  )

  // Cabecera (titulo, autores, abstract)

  place(
    top + center,
    float: true,
    scope: "parent",
    clearance: 1cm
  )[
    // Titulo
    #text(17pt, weight: "bold", title)
    
    #v(1cm)

    // Autores
    #let n_authors = authors.len()
    #let n_cols = calc.min(n_authors, 3)

    #grid(
      columns: (1fr,) * n_cols,
      row-gutter: 25pt,
      ..authors.map(author => [
        #author.name \
        #author.affiliation \
        #link("mailto:" + author.email)
      ])  
    )

    #v(1cm)

    // Abstract
    #par(justify: false)[
      #smallcaps[Abstract]\
      #abstract
    ]
  ]

  // Resto del documento

  set align(left)

  doc
}

// Aquí indicamos la regla show que se aplica al documento. Closure.

#show: doc => conf(
  title: [Plantilla de ejemplo],
  authors: (
      (
        name: "Theresa Tungsten",
        affiliation: "Artos Institute",
        email: "tung@artos.edu",
      ),
      (
        name: "Eugene Deklan",
        affiliation: "Honduras State",
        email: "e.deklan@hstate.hn",
      ),
            (
        name: "Theresa Tungsten",
        affiliation: "Artos Institute",
        email: "tung@artos.edu",
      ),
      (
        name: "Eugene Deklan",
        affiliation: "Honduras State",
        email: "e.deklan@hstate.hn",
      ),
            (
        name: "Eugene Deklan",
        affiliation: "Honduras State",
        email: "e.deklan@hstate.hn",
      ),
            (
        name: "Theresa Tungsten",
        affiliation: "Artos Institute",
        email: "tung@artos.edu",
      )
    ),
  abstract: [
    La instrucción `..authors.map(author => ...)` se utiliza para dividir la informaicón de cada autor en tres líneas diferentes.  El número de columnas es el mínimo entre 3 y el número de autores. Si hay más de 3 autores, se añade una nueva fila.
  ],
  doc
)

= Introducción

Algunos apuntes sobre cómo he hecho la plantilla:

- Defino la cabecera con *título*, *autores* y *abstract* y luego hago que vaya seguida del documento (`doc`). El formato de esta cabecera ya lo vimos antes.

- La regla `show: doc` la utilizo para indicar la configuración del documento.

- Los autores son un `array` de diccionarios que puede ser variable. Se determina dinámicamente el número y se ajusta el `grid` donde los ubico. Utilzo `.len()`.

= Syntax <syntag>

- Code: #(1+2) ----> `#(1+2)`

- Math: $-x$

#let name = [*Typst!*]
- Markup: #name

- Línea en blanco con `parbreak`: #parbreak()

- #link("https://www.estoesunlink.es")

- Mira la sección con etiqueta llamada @syntag[Sección].

/ Término: descripción

#set text(lang: "es")

- 'quote' "quote" ----> comillas inglesas y españolas, fijando previamente el `lang: "es"`.

- Puedo escribir diferentes símbolos gracias a `#sym.` Por ejemplo: #sym.dot.circle.big, #sym.gt.triple.nested, #sym.prec.tilde.

- Un rectángulo: #rect(width: 1cm)

- Maths: $x^2$, $1 / (x + 3)$, $d arrow.r.long e$, $x y$, $a <- b, c != h$, $cal(R) "means real"$, $floor(x)$, $dots$

#let suma(x,y) = x + y

- Code blocks: #{ let x = 1; x + 2 } --> `#{ let x = 1; x + 2}`. Array #(1,2,3), Dict #(a:"hi", b:"bye"), function call: #suma(1,2).


#lorem(500)