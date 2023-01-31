// $(document).ready(function () {
let cart_items_id = []
let cart_items = []
const myLocalStorage = window.localStorage

const badge = '$'


$(function () {

    /*// AGREGAR ITEM AL CARRITO
    $(".add__cart").on('click', function () {
        let item = $(this)
        const item_id = item.data('item_id')

        // Agregamos al array el id del item seleccionado
        cart_items_id.push(item_id)
        console.log(cart_items_id)

        // Renderizamos el carrito
        cartRender()

        // Guardamos el carrito en Local Storage
        saveCartLocalStorage()
    })
    
    // BORRAR ITEM DEL CARRITO
    $(".btn__del_cart_item").on('click', function () {

        //Borramos item del carrito
        delCartItem()
    })*/


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
    $("#btn__add--item").click(function (event) {
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

})


//* FUNCIÓN PREVISUALIZAR IMAGEN AL CARGAR MODAL EDIT
function readURL(input) {
    if (input.files && input.files[0]) { //Revisamos que el input tenga contenido
        var reader = new FileReader() //Leemos el contenido
        reader.onload = function (e) { //Al cargar el contenido lo pasamos como atributo de la imagen de arriba
            $('#pic_up').attr('src', e.target.result)
        }
        reader.readAsDataURL(input.files[0])
    }
}

$("#editFile").change(function () { //Cuando el input cambie (se cargue un nuevo archivo) se va a ejecutar de nuevo el cambio de imagen y se verá reflejado.
    readURL(this)
    $('#pic_up').attr('hidden', false)
    $('#pic_label').attr('hidden', false)
})


/*//* FUNCIÓN RENDERIZAR CARRITO 
function cartRender() { //!FUNCIONA MAL

    // Quitamos los duplicados
    const cartWithoutDuplicate = [...new Set(cart_items_id)]
    
    // Generamos los Nodos a partir de carrito
    cartWithoutDuplicate.forEach((item) => {
        
        // Obtenemos el item que necesitamos de la variable base de datos
        const myItem = array_items.filter((itemDB) => {
            
            // ¿Coincide las id? Solo puede existir un caso
            return itemDB.id === parseInt(item)
        });
        
        // Cuenta el número de veces que se repite el producto
        const numberItemUnits = cart_items_id.reduce((total, itemId) => {
            
            // ¿Coincide las id? Incremento el contador, en caso contrario no mantengo
            return itemId === item ? total += 1 : total;
        }, 0)
        
        // Creamos el objeto item del carrito 
        cart_items.push(
            {
                id: `${myItem[0].id}`,
                category_id: `${myItem[0].category_id}`,
                category: `${myItem[0].category}`,
                name: `${myItem[0].name}`,
                info: `${myItem[0].info}`,
                quantity: `${numberItemUnits}`,
                price: `${myItem[0].price}`,
            }
        )
    })
    console.log(cart_items)
    // Calculamos el precio total de la venta
    // const totalSale = totalSale() //!REVISAR
}


//* FUNCIÓN ELIMINAR ITEM DEL CARRITO
function delCartItem(event) {

    // Obtenemos el producto ID que hay en el boton pulsado
    const id = event.target.dataset.item_id

    // Borramos todos los productos
    cart_items_id = cart_items_id.filter((carritoId) => {
        return carritoId !== id
    })

    // volvemos a renderizar
    cartRender()

    // Actualizamos el Local Storage
    saveCartLocalStorage()
}


//* FUNCIÓN CALCULAR EL PRECIO TOTAL TENIENDO EN CUENTA PRODUCTOS REPETIDOS
function totalSale() {

    // Recorremos el array del carrito 
    return cart_items_id.reduce((total, item) => {

        // De cada elemento obtenemos su precio
        const myItem = array_items.filter((itemDB) => {
            return itemDB.id === parseInt(item)
        });
        // Los sumamos al total
        return total + myItem[0].price
    }, 0).toFixed(2)
}


//* FUNCION VACIAR EL CARRITO
function emptyCart() {

    // Limpiamos los productos guardados
    cart_items_id = []

    // Renderizamos los cambios
    cartRender()

    // Borramos Local Storage
    localStorage.clear();
}


//* FUNCIÓN GUARDAR EN LOCAL STORAGE
function saveCartLocalStorage () {
    myLocalStorage.setItem('cart', JSON.stringify(cart_items_id))
}


//* FUNCIÓN CARGAR CARRITO DESDE LOCAL STORAGE
function getCartLocalStorage () {

    // ¿Existe un carrito previo guardado en Local Storage?
    if (myLocalStorage.getItem('cart') !== null) {

        // Carga la información
        carrito = JSON.parse(myLocalStorage.getItem('cart'))
    }
}
*/

/*// MOSTRAR HORA DE CARGA POS
var date = new Date()
var hour = `${date.getHours().toString().padStart(2, '0')}:${date.getMinutes().toString().padStart(2, '0')}`
$('.tab__clock').html(hour)

getCartLocalStorage()
cartRender()*/