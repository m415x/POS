// $(document).ready(function () {
$(function () {
    // MOSTRAR EDIT
    $(".btn__edit").on('click', function (event) {
        let item = $(this)
        event.preventDefault()
        const item_id = item.data('item_id')
        const item_category = item.data('item_category')
        const item_name = item.data('item_name')
        const item_info = item.data('item_info')
        const item_stock = item.data('item_stock')
        const item_cost = item.data('item_cost')
        const item_price = item.data('item_price')
        const item_img = item.data('item_img')
        console.log(item_id)
        console.log(item_category)
        console.log(item_name)
        console.log(item_info)
        console.log(item_stock)
        console.log(item_cost)
        console.log(item_price)
        console.log(item_img)
        // var value1 = $(this).attr('href')
        // const value2 = value1.replaceAll("'", "")
        // const value3 = value2.replace("(", "")
        // const values = value3.replace(")", "")
        // const listVal = values.split(", ")
        // console.log(listVal)
        $('#modalEdit').modal('show')
        $('#editCode').val(parseInt(item_id))
        // var slice = item.slice(0, 3).toLocaleUpperCase()////////////////////////////////
        // $('#editLetter').html(slice)
        $('#editcategory').val(item_category).change()
        // $('#editName').val(item_name)
        $('#editName').attr('value', item_name)
        $('#editInfo').val(item_info)
        $('#editStock').val(parseFloat(item_stock))
        $('#editCost').val(parseFloat(item_cost))
        $('#editPrice').val(parseFloat(item_price))
        const src = `../../../media/items/${item_img}`
        $('#pic_file').attr("src", src)
        console.log(src)
    })
    // MOSTRAR ADD
    $("#btn__add").click(function (event) {
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
$("#editFile").change(function () { //Cuando el input cambie (se cargue un nuevo archivo) se va a ejecutar de nuevo el cambio de imagen y se verá reflejado.
    readURL(this);
    $('#pic_up').attr('hidden', false)
    $('#pic_label').attr('hidden', false)

});
