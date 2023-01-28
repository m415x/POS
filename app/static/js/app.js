const itemsPos = document.getElementById('items_pos')
const headerCart = document.getElementById('header_cart')
const itemsCart = document.getElementById('items_cart')
const footerCart = document.getElementById('footer_cart')
// const inputQuantity = document.getElementById('input_quantity')
const templateItemPos = document.getElementById('template-item_pos').content
const templateHeaderCart = document.getElementById('template-header_cart').content
const templateItemCart = document.getElementById('template-item_cart').content
const templateFooterCart = document.getElementById('template-footer_cart').content
const fragment = document.createDocumentFragment()
const badge = '$'
let cart = {}

document.addEventListener('DOMContentLoaded', () => {
    fetchData()
    if(localStorage.getItem('cart')) {
        cart = JSON.parse(localStorage.getItem('cart'))
        renderItemsCart()
    }
})

itemsPos.addEventListener('click', e => {
    addCart(e)
})

itemsCart.addEventListener('click', e => {
    btnAction(e)
})

const fetchData = async () => {
    try {
        renderItemsPos(array_items)
    } catch (error) {
        console.log(error)
    }
}

const renderItemsPos = array_items => {
    array_items.forEach(item => {
        templateItemPos.querySelector('.card__code').textContent = `${item.category.toUpperCase().slice(0, 3)}-${item.id.toString().padStart(5, 0)}`
        templateItemPos.querySelector('.card__name').textContent = item.name.toUpperCase()
        templateItemPos.querySelector('.card__info').textContent = item.info
        templateItemPos.querySelector('.card__price').textContent = `${badge} ${item.price}`
        templateItemPos.querySelector('.card__stock').textContent = item.stock //Agregar if-else con colores y sin stock
        /*if(item.stock >= 10) {
            templateItemPos.querySelector('.card__stock').classList.add('bg-success')
            console.log('VERDE')
        } else if(item.stock > 0) {
            templateItemPos.querySelector('.card__stock').classList.add('bg-warning')
            console.log('AMARILLO')
        } else {
            templateItemPos.querySelector('.card__stock').textContent = 'SIN STOCK'
            templateItemPos.querySelector('.card__stock').classList.add('bg-danger')
            console.log('ROJO')
        }*/
        templateItemPos.querySelector('.card__img').setAttribute('src', `../../../media/items/${item.img_name}`)
        templateItemPos.querySelector('.add__cart').setAttribute('href', `#${item.id}`)
        templateItemPos.querySelector('.add__cart-mask').dataset.item_id = item.id
        templateItemPos.querySelector('.add__cart-mask').dataset.item_category_id = item.category_id
        templateItemPos.querySelector('.add__cart-mask').dataset.item_category = item.category
        templateItemPos.querySelector('.add__cart-mask').dataset.item_name = item.name
        templateItemPos.querySelector('.add__cart-mask').dataset.item_info = item.info
        templateItemPos.querySelector('.add__cart-mask').dataset.item_stock = item.stock
        templateItemPos.querySelector('.add__cart-mask').dataset.item_cost = item.cost
        templateItemPos.querySelector('.add__cart-mask').dataset.item_price = item.price

        const clone = templateItemPos.cloneNode(true)
        fragment.appendChild(clone)
    })
    itemsPos.appendChild(fragment)
}

const addCart = e => {
    if(e.target.classList.contains('add__cart-mask')) {
        setCart(e.target.parentElement)
    }
    e.stopPropagation()
}

const setCart = object => {
    // console.log(object)
    const item = {
        id: object.querySelector('.add__cart-mask').dataset.item_id,
        category_id: object.querySelector('.add__cart-mask').dataset.item_category_id,
        category: object.querySelector('.add__cart-mask').dataset.item_category,
        name: object.querySelector('.add__cart-mask').dataset.item_name,
        info: object.querySelector('.add__cart-mask').dataset.item_info,
        stock: object.querySelector('.add__cart-mask').dataset.item_stock,
        cost: object.querySelector('.add__cart-mask').dataset.item_cost,
        price: object.querySelector('.add__cart-mask').dataset.item_price,
        quantity: 1
    }
    if(cart.hasOwnProperty(item.id)) {
        item.quantity = cart[item.id].quantity + 1
    }
    cart[item.id] = {...item}
    renderItemsCart()
}

const renderItemsCart = () => {
    itemsCart.innerHTML = ''
    Object.values(cart).forEach(item => {
        templateItemCart.querySelector('.cart_id').setAttribute('title', `${item.category.toUpperCase().slice(0, 3)} - ${item.id.toString().padStart(5, 0)}`)
        templateItemCart.querySelector('.cart_name').textContent = item.name.toUpperCase()
        templateItemCart.querySelector('.cart_info').textContent = item.info
        templateItemCart.querySelector('.cart_price-unit').textContent = `${badge} ${item.price} / ${item.unit}`
        templateItemCart.querySelector('.btn_minus').dataset.id = item.id
        templateItemCart.querySelector('.cart_quantity').dataset.id = item.id
        templateItemCart.querySelector('.cart_quantity').textContent = item.quantity
        templateItemCart.querySelector('.btn_plus').dataset.id = item.id
        templateItemCart.querySelector('.cart_ppq').textContent = `${badge} ${item.price*item.quantity}`
        templateItemCart.querySelector('.del_item-cart').dataset.id = item.id

        const clone = templateItemCart.cloneNode(true)
        fragment.appendChild(clone)
    })
    itemsCart.appendChild(fragment)

    renderHeaderCart()
    renderFooterCart()

    /*Object.values(cart).forEach(item => {
    selectText(item.id)
    })*/
    
    localStorage.setItem('cart', JSON.stringify(cart))
}

/*function selectText(id) {
    const input = document.querySelectorAll('.cart_quantity')[id]
    input.focus()
    input.select()
}*/

const renderHeaderCart = () => {
    headerCart.innerHTML = ''
    if(Object.keys(cart).length === 0) {
        headerCart.innerHTML = ''
        return
    }
    const cartQuantity = Object.values(cart).reduce((acc, {quantity}) => acc + quantity, 0)

    templateHeaderCart.querySelector('.cart_quantity').textContent = cartQuantity

    const clone = templateHeaderCart.cloneNode(true)
    fragment.appendChild(clone)
    headerCart.appendChild(fragment)
}

const renderFooterCart = () => {
    footerCart.innerHTML = ''
    if(Object.keys(cart).length === 0) {
        footerCart.innerHTML = ''
        return
    }
    const cartTotal = Object.values(cart).reduce((acc, {quantity, price}) => acc + quantity * price, 0)

    templateFooterCart.querySelector('.cart_total').textContent = `${badge} ${Math.round(cartTotal * 100) / 100}`

    const clone = templateFooterCart.cloneNode(true)
    fragment.appendChild(clone)
    footerCart.appendChild(fragment)
}

const btnAction = e => {
    // Acción de aumentar
    if(e.target.classList.contains('btn_plus')) {
        const itemCart = cart[e.target.dataset.id]
        itemCart.quantity ++
        cart[e.target.dataset.id] = {...itemCart}
        renderItemsCart()
    }
    // Acción de disminuir
    if(e.target.classList.contains('btn_minus')) {
        const itemCart = cart[e.target.dataset.id]
        itemCart.quantity --
        if(itemCart.quantity === 0) {
            delete cart[e.target.dataset.id]
        }
        renderItemsCart()
    }
    // Acción de eliminar
    if(e.target.classList.contains('del_item-cart')) {
        delete cart[e.target.dataset.id]
        renderItemsCart()
    }
    e.stopPropagation()
}


// const colour = document.querySelectorAll('.card__stock').innerHTML
// console.log(colour)
/*colour.textContent.forEach(item => {
    if(item >= 10) {
        document.querySelector('.card__stock').classList.add('bg-success')
        console.log('VERDE')
    } else if(item > 0) {
        document.querySelector('.card__stock').classList.add('bg-warning')
        console.log('AMARILLO')
    } else {
        document.querySelector('.card__stock').textContent = 'SIN STOCK'
        document.querySelector('.card__stock').classList.add('bg-danger')
        console.log('ROJO')
    }
})*/


/*inputQuantity.addEventListener("input", (e) => {
    inputChange(e)
})

const inputChange = e => {
    if(e.target.classList.contains('cart_quantity')) {
        let quantity = inputQuantity.textContent
        const itemCart = cart[e.target.dataset.id]
        itemCart.quantity = quantity
        cart[e.target.dataset.id] = {...itemCart}
        renderItemsCart()
    }
    e.stopPropagation()
}*/
