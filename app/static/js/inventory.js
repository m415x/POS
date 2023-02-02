const itemsInventory = document.getElementById('items_inventory')
const templateItemInventory = document.getElementById('template-item_inventory').content
const fragment = document.createDocumentFragment()
const badge = '$'


// Evento cargar el DOM
document.addEventListener('DOMContentLoaded', () => {
    fetchData()
})

// Evento agregar items al inventario
posTab.addEventListener('click', e => {
    closeTab(e)
})

// Evento editar item del inventario
itemsInventory.addEventListener('click', e => {
    btnAction(e)
})


const fetchData = async () => {
    try {
        renderitemsInventory(array_items)
    } catch (error) {
        console.log(error)
    }
}

// Cargar items en INVENTORY
const renderitemsInventory = array_items => {
    array_items.forEach(item => {
        templateItemInventory.querySelector('.filter_item').dataset.item_id = item.id
        templateItemInventory.querySelector('.filter_item').dataset.item_name = item.name
        templateItemInventory.querySelector('.filter_item').dataset.item_info = item.info
        templateItemInventory.querySelector('.card__code').textContent = `${item.category.toUpperCase().slice(0, 3)}-${item.id.toString().padStart(5, 0)}`
        templateItemInventory.querySelector('.card__name').textContent = item.name.toUpperCase()
        templateItemInventory.querySelector('.card__info').textContent = item.info
        templateItemInventory.querySelector('.card__price').textContent = `${badge} ${item.price}`
        templateItemInventory.querySelector('.card__stock').textContent = item.stock
        if(item.stock >= 10) {
            templateItemInventory.querySelector('.card__stock').classList.add('bg-success')
            templateItemInventory.querySelector('.card__stock').classList.remove('bg-warning')
            templateItemInventory.querySelector('.card__stock').classList.remove('bg-danger')
        } else if(item.stock > 0 && item.stock < 10) {
            templateItemInventory.querySelector('.card__stock').classList.add('bg-warning')
            templateItemInventory.querySelector('.card__stock').classList.remove('bg-danger')
        } else {
            templateItemInventory.querySelector('.card__stock').textContent = 'SIN STOCK'
            templateItemInventory.querySelector('.card__stock').classList.add('bg-danger')
        }
        templateItemInventory.querySelector('.card__unit').textContent = item.unit
        templateItemInventory.querySelector('.card__img').setAttribute('src', `../../../media/items/${item.img_name}`)
        templateItemInventory.querySelector('.add__cart').setAttribute('href', `#${item.id}`)
        templateItemInventory.querySelector('.add__cart-mask').dataset.item_id = item.id
        templateItemInventory.querySelector('.add__cart-mask').dataset.item_category_id = item.category_id
        templateItemInventory.querySelector('.add__cart-mask').dataset.item_category = item.category
        templateItemInventory.querySelector('.add__cart-mask').dataset.item_name = item.name
        templateItemInventory.querySelector('.add__cart-mask').dataset.item_info = item.info
        templateItemInventory.querySelector('.add__cart-mask').dataset.item_stock = item.stock
        templateItemInventory.querySelector('.add__cart-mask').dataset.item_unit = item.unit
        templateItemInventory.querySelector('.add__cart-mask').dataset.item_cost = item.cost
        templateItemInventory.querySelector('.add__cart-mask').dataset.item_price = item.price
        const clone = templateItemInventory.cloneNode(true)
        fragment.appendChild(clone)
    })
    itemsInventory.appendChild(fragment)
}

// Busquedar dinámicamente items
document.addEventListener("keyup", e => {
    if (e.target.matches("#input_search")) {
        // "ESC" => Borrar el input
        if (e.key === "Escape") e.target.value = ""
        document.querySelectorAll(".filter_item").forEach(item => {
            item.dataset.item_id.includes(e.target.value.toLowerCase()) 
            || item.dataset.item_name.toLowerCase().includes(e.target.value.toLowerCase()) 
            || item.dataset.item_info.toLowerCase().includes(e.target.value.toLowerCase())
                ? item.classList.remove("visually-hidden")
                : item.classList.add("visually-hidden")
        })
    }
})

// "Ctrl + B" => Hacer foco en buscar 
document.addEventListener("keydown", e => {
    if (e.ctrlKey || e.metaKey) {
        // Analizar las combinaciones permitidas en el proyecto (reemplazar which por key ó code)
        if (String.fromCharCode(e.which).toLowerCase() === 'b') {
            document.querySelector("#input_search").focus()
        }
    }
})

// Agregar items al inventario
const closeTab = e => {
    if(e.target.classList.contains('close_tab')) {
        if(!confirm('¿Desea borrar el carrito?')) {
            e.preventDefault()
        } else {
            cart = {}
            document.querySelector('.tab__clock').textContent = ''
            countClick = 0
            renderItemsCart()
            localStorage.removeItem('cart')
        }
    }
    e.stopPropagation()
}

// Editar-Eliminar item del inventario
const btnAction = e => {
    // Aumenta la cantidad de un item en el carrito
    if(e.target.classList.contains('btn_plus')) {
        const itemCart = cart[e.target.dataset.id]
        itemCart.quantity ++
        cart[e.target.dataset.id] = {...itemCart}
        renderItemsCart()
    }
    // Disminuye la cantidad de un item en el carrito
    if(e.target.classList.contains('btn_minus')) {
        const itemCart = cart[e.target.dataset.id]
        itemCart.quantity --
        if(itemCart.quantity === 0) {
            delete cart[e.target.dataset.id]
        }
        renderItemsCart()
    }
    // Elimina un item del carrito
    if(e.target.classList.contains('del_item-cart')) {
        delete cart[e.target.dataset.id]
        renderItemsCart()
    }
    e.stopPropagation()
}
