// Cuando el usuario hace clic en el botón "mostrar-relato"
// se insertará en la página el microrelato definido más abajo.
document.getElementById('mostrar-relato').addEventListener('click', function() {
    // Texto que se mostrará al activar el botón. Utilizamos las comillas
    // invertidas para permitir saltos de línea en la cadena sin complicaciones.
    const microrelato = `
Abrió lentamente el viejo libro, cuyas páginas guardaban silencio desde hace décadas.
Allí, escrita con una caligrafía temblorosa, encontró la última frase de su vida:
“Siempre supiste cómo termina esto”.
`;

    // Se reemplaza el contenido del párrafo con id "texto-relato"
    // por el microrelato almacenado anteriormente.
    document.getElementById('texto-relato').innerText = microrelato;
});
