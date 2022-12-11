//* FUNCIÓN MOSTRAR MODAL EDIT
$(document).ready(function () {
    $('#modalEdit').modal('show')
})


//* FUNCIÓN PREVISUALIZAR IMAGEN A CARGAR
function readURL(input) {
    if (input.files && input.files[0]) { //Revisamos que el input tenga contenido
        var reader = new FileReader(); //Leemos el contenido
        reader.onload = function (e) { //Al cargar el contenido lo pasamos como atributo de la imagen de arriba
            $('#pic_up').attr('src', e.target.result);
        }
        reader.readAsDataURL(input.files[0]);
    }
}
$("#formFile").change(function () { //Cuando el input cambie (se cargue un nuevo archivo) se va a ejecutar de nuevo el cambio de imagen y se verá reflejado.
    readURL(this);
});
