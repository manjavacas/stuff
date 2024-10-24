#set page(
  paper: "presentation-16-9",
  numbering: "1",
  header: [The _header_],
  footer: context [
      #box[
      Utilizo `#h(1fr)` para separar texto de número de página.
      #h(1fr)
      #counter(page).display(
        "1 / 1",
        both: true
      )
      ]
  ]
)

#set par(justify: true)

#set text(
  font: "Liberation Serif",
  size: 11pt
)

#align(center, text(17pt)[
  *Advanced stiling*
])

#v(.75cm)

#grid(
  columns: (1fr, 1fr),
  align(center)[
    *Pepe*\
    #link("mailto:pepe@pepe.edu")
  ],
  align(center)[
    *Pepa*\
    #link("mailto:pepa@pepa.edu")
  ]
)

#v(.75cm)

#align(center)[
  #box(
    width: 12cm,
  )[
    #set par(
      justify: true,
    )
    #set text(10pt)
    *Abstract* \
    #align(left)[
      #lorem(90)
    ]

    #v(.5cm)
  ] 
]

He ajustado las dimensiones de la página a tamaño de presentación en 16/9. He añadido un `header` y un `footer` con número de página incluido. También he añadido un título manualmente, así como los autores haciendo uso de `grid`. Los he separado del título y _abstract_ empleando `v`. El `grid` emplea dimensiones fraccionadas (aunque se pueden usar `lenghts`. El _abstract_ de ejemplo contiene `sets` propios para ajustar el texto al formato correspondiente.

#lorem(1000)