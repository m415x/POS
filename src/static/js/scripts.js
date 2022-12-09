
// function readonlyOff() {
//     document.querySelectorAll('.edit__input').readOnly = false;
// }

// document.querySelector('.btn__edit').addEventListener('click', function(e) {
//     e.preventDefault()
//     document.querySelectorAll('.edit__input').readOnly = false;
// })

document.getElementById('btn__edit').addEventListener('click', function(e) {
    // Evitar comportamiento normal del evento (¿submit?)
    e.preventDefault();
    // Desactivar todos los campos de la tabla
    document.querySelector('#table input').readOnly = true
    // Buscar solo los campos en esta fila y activar
    document.querySelector(this).closest('tr').getElementsByTagName('input').readonly="false"
});