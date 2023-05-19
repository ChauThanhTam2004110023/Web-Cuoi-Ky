// ---------------------Menu_item-----------
const toP=document.querySelector(", top")
window.addEventListener("scroll", function(){
    const X= this.pageXOffset;
    if(X>1){toP.classList.add("active")}
    else{
        toP.classList.remove("active")
    }
})
//  ---------------------Menu_Slidebar-Cartegory-----------
const itemsliderbar = document.querySelectorAll(".cartegory-left")
itemsliderbar.forEach(function(menu, index){
    menu.addEventListener("click",function(){
        menu.classList.toggle("block")
    })
})

// --------------------PRODUCT-----------------
const bigImg = document.querySelector(".product-content-left-big-img img")
const smalImg = document.querySelectorAll(".product-content-left-small-img img")
smalImg.forEach(function(imgItem,x){
    imgItem.addEventListener("click",function(){
        bigImg.src=imgItem.src
    })
})





const thongbao =document.querySelector(".thongbao")
const thongtinbosung =document.querySelector(".thongtinbosung")
if(thongbao){
    thongbao.addEventListener("click", function(){
        document.querySelector(".product-content-right-bottom-content-thongbao").style.display ="none"
        document.querySelector(".product-content-right-bottom-content-thongtinbosung").style.display ="block"
    })
}
if(thongtinbosung){
    thongthongtinbosungbao.addEventListener("click", function(){
        document.querySelector(".product-content-right-bottom-content-thongbao").style.display ="block"
        document.querySelector(".product-content-right-bottom-content-thongtinbosung").style.display ="none"
    })
}
const butTon = document.querySelector(".product-content-right-bottom-top")
if(butTon){
    butTon.addEventListener("click", function(){
        document.querySelector(".product-content-right-bottom-content-big").classList.toggle("activeB")
    })
}