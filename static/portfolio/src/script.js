

const tabs = document.querySelectorAll('.projects__tab');
const tabsContent = document.querySelectorAll('.projects__content');
const tabsParrent = document.querySelector('.projects__tabs');


const activeClass = "active";


function removeClass(array) {
    array.forEach(element => {
        element.classList.remove(activeClass)
    });
}

function addClass(activeItem, targetId) {
    activeItem[targetId - 1].classList.add(activeClass);
}


tabsParrent.addEventListener('click', (event)=>{
    const targetId = event.target.dataset.id;
    
    removeClass(tabs);
    removeClass(tabsContent);
    addClass(tabs, targetId);
    addClass(tabsContent, targetId);
})



