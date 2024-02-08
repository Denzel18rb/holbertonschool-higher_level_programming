const ulElement = document.appendChild
document.addEventListener("DOMContentLoaded", function () {
        const Additem = document.querySelector("#add_item");
        Additem.addEventListener("click", function (){
        const ulElement = document.querySelector('.my_list')
        const li = document.createElement('li')
        li.textContent = 'Item'
        ulElement.appendChild(li);
        });
});