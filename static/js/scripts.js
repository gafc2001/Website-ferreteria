document.addEventListener('DOMContentLoaded', function () {

    //Elementos
    const cartButton = document.getElementById('cart-icon');
    const cart = document.getElementById('cart');
    const listCart = document.getElementById('list-cart');
    const buyButton = document.getElementById('button-cart');
    const addCart = document.getElementsByClassName('add-cart');
    const inputData = document.getElementById('data');
    const closeCart = document.getElementById('close-cart');
    //Abrir carrito
    // let state = false;
    cartButton.addEventListener('click', open)
    closeCart.addEventListener('click', close);
    function open() {
        document.getElementsByTagName('body')[0].classList.add('screen');
        cart.style.display = 'block';
        // state = false
    }
    function close() {
        document.getElementsByTagName('body')[0].classList.remove('screen');
        cart.style.display = 'none';
        // state = true
    }


    //Agregar productos al carrito
    let resumenProducto = []
    let total = 0
    for (let i = 0; i < addCart.length; i++) {
        addCart[i].addEventListener('click', () => {
            buyButton.disabled = false
            let id = addCart[i].getAttribute('data-id');
            let totalElement = document.getElementById('total');
            total++;
            let exist = false;
            //Buscar el id en resumenProducto
            for (producto of resumenProducto) {
                if (producto.id == id) {
                    exist = true
                }
            }
            //Si no existe el producto en (resumenProducto), agregamos un nuevo objeto a 
            //resumenProducto con su id y cantidad
            if (exist == false) {

                resumenProducto.push({
                    'id': id,
                    'cant': 1
                })
                let elements = addCart[i].parentElement.children
                let imgSource = elements[0].children[0].getAttribute('src');
                let productName = elements[1].textContent
                let productPrice = elements[2].textContent

                let productCart = `
                    <div class="product-cart" id=${id}>
                        <p class="quantity">1</p>
                        <div class="cart-image">
                        <img src='${imgSource}' alt="">
                        </div>
                        <p class="product-name" >${productName}</p>
                        <p class="product-price">${productPrice}</p>
                    </div>
                `
                listCart.innerHTML = listCart.innerHTML + productCart

            } else {
                //Si existe el producto en nuestro arreglo resumenProducto, aumentamos su cantidad
                let productElement = document.getElementById(id);
                let quant = productElement.childNodes[1];
                resumenProducto.forEach(e => {
                    if (e.id == id) {
                        e.cant = e.cant + 1
                        quant.innerHTML = e.cant
                    }
                });
            }
            totalElement.style.display = "block";
            totalElement.innerText = total;
            formatResumen = []
            resumenProducto.forEach(e => {
                formatResumen.push(JSON.stringify(e))
            });
            inputData.value = formatResumen.toString();

        })
    }


})