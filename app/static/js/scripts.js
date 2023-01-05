//* READY
$(document).ready(function () {
    // MOSTRAR EDIT
    $(".btn__edit").click(function(event){
        event.preventDefault()
        var value1 = $(this).attr('href')
        const value2 = value1.replaceAll("'", "")
        const value3 = value2.replace("(", "")
        const values = value3.replace(")", "")
        const listVal = values.split(", ")
        console.log(listVal)
        $('#modalEdit').modal('show')
        $('#formCode').val(parseFloat(listVal[0]))
        var slice = listVal[1].slice(0, 2).toLocaleUpperCase()
        $('#formLetter').html(slice)
        $('#formType').val(listVal[1]).change()
        $('#formName').val(listVal[2])
        $('#formInfo').val(listVal[3])
        $('#formStock').val(parseFloat(listVal[4]))
        $('#formCost').val(parseFloat(listVal[5]))
        $('#formPrice').val(parseFloat(listVal[6]))
        const src = `userpic/${listVal[7]}`
        $('#pic_file').attr("src", src)
        console.log(src)
    })
    // MOSTRAR ADD
    $("#btn__add").click(function(event){
        event.preventDefault()
        $('#modalAdd').modal('show')
    })
    // OCULTAR IMG SIN SRC
    var src = $('#pic_up').attr('src')
    if (src == '') {
        $('#pic_up').attr('hidden', true)
        $('#pic_label').attr('hidden', true)
    // } else {
    //     $('#pic_up').attr('hidden', false)
    }
    // MOSTRAR HORA DE CARGA POS
    var date = new Date()
    var hour = `${date.getHours().toString().padStart(2, '0')}:${date.getMinutes().toString().padStart(2, '0')}`
    $('.tab__clock').html(hour)
})


//* FUNCIÓN PREVISUALIZAR IMAGEN AL CARGAR MODAL EDIT
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
    $('#pic_up').attr('hidden', false)
    $('#pic_label').attr('hidden', false)

});




// $(document).ready(function(){
//     $("#btn__edit").click(function(){
//         $(".edit__input")
//         .removeAttr('readonly')
//         .removeAttr('disabled')

//         .addClass('border-bottom');
//         $("#btn__edit").hide();
//         $(".btn__confirm").removeClass('visually-hidden');

//         $(".btn__file").removeClass('visually-hidden');
//     })
// })

// $(document).ready(function(){
//     $("#btn__cancel").click(function(){
//         $(".edit__input")
//         .attr('readonly', true)
//         .attr('disabled', true)

//         .removeClass('border-bottom');
//         $("#btn__edit").show();
//         $(".btn__confirm").addClass('visually-hidden');
//         $(".btn__delete").removeClass('visually-hidden');
//         $(".btn__file").addClass('visually-hidden');
//     })
// })