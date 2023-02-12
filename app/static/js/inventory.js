const inventoryHeader = document.getElementById('inventory_header')
const itemsInventory = document.getElementById('items_inventory')
const addCategories = document.getElementById('addCategory')
const editCategories = document.getElementById('editCategory')
const templateItemInventory = document.getElementById('template-item_inventory').content
const templateCategories = document.getElementById('template-categories').content
const modalEdit = document.getElementById('modalEdit').content
const fragment = document.createDocumentFragment()
const badge = '$'


// Evento cargar el DOM
document.addEventListener('DOMContentLoaded', () => {
    fetchData()
})

// Evento agregar items al inventario y filtros
inventoryHeader.addEventListener('click', e => {
    btnHeader(e)
})

// Evento editar item del inventario
itemsInventory.addEventListener('click', e => {
    btnEdit(e)
})

// Renderizar JSON
const fetchData = async() => {
    try {
        renderItemsInventory(array_items)
        renderCategories(array_categories)
    } catch(error) {
        console.log(error)
    }
}

// Cargar items en INVENTORY
const renderItemsInventory = array_items => {
    array_items.forEach(item => {
        templateItemInventory.querySelector('.filter_inventory').dataset.item_id = item.id
        templateItemInventory.querySelector('.filter_inventory').dataset.item_name = item.name
        templateItemInventory.querySelector('.filter_inventory').dataset.item_info = item.info
        templateItemInventory.querySelector('.inventory__id').textContent = `${item.category.toUpperCase().slice(0, 3)}-${item.id.toString().padStart(5, 0)}`
        templateItemInventory.querySelector('.inventory__category').textContent = item.category
        templateItemInventory.querySelector('.inventory__name').textContent = item.name.toUpperCase()
        templateItemInventory.querySelector('.inventory__info').textContent = item.info
        templateItemInventory.querySelector('.inventory__stock').textContent = item.stock
        if(item.stock === 1) {
            templateItemInventory.querySelector('.inventory__unit').textContent = item.unit
        } else if(item.unit === 'unidad'){
            templateItemInventory.querySelector('.inventory__unit').textContent = `${item.unit}es`
        } else {
            templateItemInventory.querySelector('.inventory__unit').textContent = `${item.unit}s`
        }
        if(item.stock >= 10) {
            templateItemInventory.querySelector('.inventory__stock').classList.add('text-success')
            templateItemInventory.querySelector('.inventory__stock').classList.remove('text-warning')
            templateItemInventory.querySelector('.inventory__stock').classList.remove('text-danger')
            templateItemInventory.querySelector('.inventory__unit').classList.remove('visually-hidden')
        } else if(item.stock > 0 && item.stock < 10) {
            templateItemInventory.querySelector('.inventory__stock').classList.add('text-warning')
            templateItemInventory.querySelector('.inventory__stock').classList.remove('text-danger')
            templateItemInventory.querySelector('.inventory__unit').classList.remove('visually-hidden')
        } else {
            templateItemInventory.querySelector('.inventory__stock').textContent = 'SIN STOCK'
            templateItemInventory.querySelector('.inventory__stock').classList.add('text-danger')
            templateItemInventory.querySelector('.inventory__unit').classList.add('visually-hidden')
        }
        templateItemInventory.querySelector('.inventory__cost').textContent = `${badge} ${item.cost}`
        templateItemInventory.querySelector('.inventory__price').textContent = `${badge} ${item.price}`
        templateItemInventory.querySelector('.inventory__img').setAttribute('src', `../../../media/items/${item.img_name}`)
        templateItemInventory.querySelector('.inventory__id').dataset.attr = 'sort-id'
        templateItemInventory.querySelector('.inventory__category').dataset.attr = 'sort-category'
        templateItemInventory.querySelector('.inventory__name').dataset.attr = 'sort-name'
        templateItemInventory.querySelector('.inventory__info').dataset.attr = 'sort-info'
        templateItemInventory.querySelector('.inventory__stock').dataset.attr = 'sort-stock'
        templateItemInventory.querySelector('.inventory__cost').dataset.attr = 'sort-cost'
        templateItemInventory.querySelector('.inventory__price').dataset.attr = 'sort-price'
        templateItemInventory.querySelector('.btn__edit').setAttribute('href', `#${item.id}`)
        templateItemInventory.querySelector('.btn__edit').dataset.item_id = item.id
        templateItemInventory.querySelector('.btn__edit').dataset.item_category_id = item.category_id
        templateItemInventory.querySelector('.btn__edit').dataset.item_category = item.category
        templateItemInventory.querySelector('.btn__edit').dataset.item_name = item.name
        templateItemInventory.querySelector('.btn__edit').dataset.item_info = item.info
        templateItemInventory.querySelector('.btn__edit').dataset.item_stock = item.stock
        templateItemInventory.querySelector('.btn__edit').dataset.item_unit = item.unit
        templateItemInventory.querySelector('.btn__edit').dataset.item_cost = item.cost
        templateItemInventory.querySelector('.btn__edit').dataset.item_price = item.price
        templateItemInventory.querySelector('.btn__delete').setAttribute('onclick', `if(!confirm('¿Desea borrar ${item.category.toUpperCase().slice(0, 3)}-${item.id.toString().padStart(5, 0)}?')) event.preventDefault()`)
        templateItemInventory.querySelector('.btn__delete').setAttribute('href', `/delete/${item.id}`)
        const clone = templateItemInventory.cloneNode(true)
        fragment.appendChild(clone)
    })
    itemsInventory.appendChild(fragment)
}

// Buscar dinámicamente items
document.addEventListener("keyup", e => {
    if (e.target.matches("#input_search")) {
        // "ESC" => Borrar contenido del input
        if(e.key === "Escape") e.target.value = ""
        document.querySelectorAll(".filter_inventory").forEach(item => {
            item.dataset.item_id.includes(e.target.value.toLowerCase()) 
            || item.dataset.item_name.toLowerCase().includes(e.target.value.toLowerCase()) 
            || item.dataset.item_info.toLowerCase().includes(e.target.value.toLowerCase())
                ? item.classList.remove("visually-hidden")
                : item.classList.add("visually-hidden")
        })
    }
})

// "Ctrl + B" => Hacer foco en input buscar 
document.addEventListener("keydown", e => {
    if((e.ctrlKey || e.metaKey) && e.code == 'KeyB') {
        document.querySelector("#input_search").focus()
    }
})

/*// Ordenar items
// const tableContent = document.getElementById("table-content")
const tableButtons = document.querySelectorAll(".sorted_button")
const sortItems = (data, param, direction = "asc") => {
    // tableContent.innerHTML = ''
    const sortedItems =
        direction == "asc"
            ? [...data].sort(function (a, b) {
                if (a[param] < b[param]) {
                    return -1
                }
                if (a[param] > b[param]) {
                    return 1
                }
                return 0
            })
            : [...data].sort(function (a, b) {
                if (b[param] < a[param]) {
                    return -1
                }
                if (b[param] > a[param]) {
                    return 1
                }
                return 0
            })
    // getTableContent(sortedItems)
    renderItemsInventory(sortedItems)
}

const resetButtons = (event) => {
    [...tableButtons].map((button) => {
        if (button !== event.target) {
            button.removeAttribute("data-sort")
        }
    })
}

window.addEventListener("load", () => {
    renderItemsInventory(array_items);

    [...tableButtons].map((button) => {
        button.addEventListener("click", (e) => {
            resetButtons(e)
            if (e.target.getAttribute("data-sort") == "desc") {
                sortItems(array_items, e.target.id, "desc")
                e.target.setAttribute("data-sort", "asc")
            } else {
                sortItems(array_items, e.target.id, "asc")
                e.target.setAttribute("data-sort", "desc")
            }
        })
    })
})*/


/*
// Agregar items al inventario
const btnHeader = e => {
    if(e.target.classList.contains('btn_add_item')) {
        e.preventDefault()
        const modalAdd = document.getElementById('modalAdd')
        modalAdd.classList.remove('visually-hidden')
        const selectCategory = document.querySelector("#addUnit")
        const addItem = () => {
            const option = document.createElement('option')
            const valor = 'algo'
            option.value = valor;
            option.text = valor;
            $select.appendChild(option);
        };
    }
    e.stopPropagation()
}

// Editar item del inventario
const btnEdit = e => {
    if(e.target.classList.contains('btn__edit')) {
        const itemInventory = array_items[e.target.dataset.item_id]
        modalEdit.querySelector('#formLetters').textContent = itemInventory.category.toUpperCase().slice(0, 3)
        
        renderItemsCart()
    }
    e.stopPropagation()
}
*/

// Cargar categorías en MODALS
const renderCategories = array_categories => {
    array_categories.forEach(category => {
        templateCategories.querySelector('.option-category').setAttribute('value', category.id)
        templateCategories.querySelector('.option-category').textContent = category.category
        const clone = templateCategories.cloneNode(true)
        fragment.appendChild(clone)
    })
    addCategories.appendChild(fragment)
    editCategories.appendChild(fragment)
}