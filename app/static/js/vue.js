// * POS ---------------------------------------
var app = Vue.createApp({
    data() {
        return {
            items: array_items,
            cart_items: cart_items,
        }
    },
    delimiters: ['[[', ']]']
}).mount('#app_pos')


// * INVENTORY ----------------------------------
// var app = Vue.createApp({
//     data() {
//         return {
//             items: array_items
//         }
//     },
//     delimiters: ['[[', ']]']
// }).mount('#app_inv')