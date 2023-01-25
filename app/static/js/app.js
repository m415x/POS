const itemsPos = document.getElementById('items_pos')
const templateItemPos = document.getElementById('template-item_pos').content
const fragment = document.createDocumentFragment()
const badge = '$'
let cart = {}

document.addEventListener('DOMContentLoaded', () => {
    fetchData()
})

itemsPos.addEventListener('click', e => {
    addCart(e)
})

const fetchData = async () => {
    try {
        pintarItems_pos(array_items)
    } catch (error) {
        console.log(error)
    }
}

const pintarItems_pos = array_items => {
    array_items.forEach(item => {
        templateItemPos.querySelector('.card__code').textContent = `${item.category.toUpperCase().slice(0, 3)} - ${item.id.toString().padStart(5, 0)}`
        templateItemPos.querySelector('.card__name').textContent = item.name.toUpperCase()
        templateItemPos.querySelector('.card__info').textContent = item.info
        templateItemPos.querySelector('.card__price').textContent = `${badge} ${item.price}`
        templateItemPos.querySelector('.card__stock').textContent = item.stock //Agregar if-else con colores y sin stock
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
    console.log(object)
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
    console.log(cart)
}