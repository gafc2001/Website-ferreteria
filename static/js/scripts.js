document.addEventListener('DOMContentLoaded',function(){

    //Elementos
    const cartButton = document.getElementById('cart-icon');
    const cart = document.getElementById('cart');
    const listCart = document.getElementById('list-cart');
    const buyButton = document.getElementById('button-cart');
    const addCart = document.getElementsByClassName('add-cart');
    const inputData = document.getElementById('data');

    //Abrir carrito
    let state = false;
    cartButton.addEventListener('click',openCart)
    function openCart(){
        if(state){
            document.getElementsByTagName('body')[0].classList.remove('screen');
            cart.style.display = 'none';
            state = false
        }else{
            document.getElementsByTagName('body')[0].classList.add('screen');
            cart.style.display = 'block';
            state = true
        }
    }
    
    //Agregar productos al carrito
    let idProducts = {}
    let total = 0
    for(let i = 0;i<addCart.length;i++){
        addCart[i].addEventListener('click',()=>{
            let id = addCart[i].getAttribute('data-id');
            let totalElement = document.getElementById('total');
            total++;
            //Si no existe el producto en (idProducts)
            if(!idProducts[id]){
                idProducts[id] = 1;
                let elements = addCart[i].parentElement.children
                let imgSource = elements[0].children[0].getAttribute('src');
                let productName = elements[1].textContent
                let productPrice = elements[2].textContent
                
                let productCart = `
                    <div class="product-cart" id=${id}>
                        <p class="quantity">${idProducts[id]}</p>
                        <div class="cart-image">
                        <img src='${imgSource}' alt="">
                        </div>
                        <p class="product-name" >${productName}</p>
                        <p class="product-price">${productPrice}</p>
                    </div>
                `
                listCart.innerHTML = listCart.innerHTML + productCart
            }else{
                idProducts[id] = idProducts[id]+1;
                let productElement = document.getElementById(id);
                let quant = productElement.childNodes[1]
                quant.innerHTML = idProducts[id]
            }
            totalElement.style.display = "block"
            totalElement.innerText = total
            inputData.value =JSON.stringify(idProducts);
        })
    }
    

})