const itemsPos = document.getElementById('items_pos')
const templateItemPos = document.getElementById('template-item_pos').content
const fragment = document.createDocumentFragment()
const badge = '$'

document.addEventListener('DOMContentLoaded', () => {
    fetchData()
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
        templateItemPos.querySelector('.add__cart').dataset.item_id = item.id
        const clone = templateItemPos.cloneNode(true)
        fragment.appendChild(clone)
    })
    itemsPos.appendChild(fragment)
}