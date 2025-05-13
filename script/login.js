let btnOpen = document.querySelector('.login')
let btnClose = document.querySelector('.btn-close-logo')
let boxLogin = document.querySelector('.box-login')
btnOpen.addEventListener('click', function(){
    boxLogin.style.top = '0px'
})
btnClose.addEventListener('click', function(){
    boxLogin.style.top = '-350px'
})
let btnOpenSign = document.querySelector('.sign-up')
let boxSign = document.querySelector('.box-sign')
let btnCloseSign = document.querySelector('.box-close-btn')
btnOpenSign.addEventListener('click', function(){
    boxSign.style.top = '0px'
})
btnCloseSign.addEventListener('click', function(){
    boxSign.style.top = '-350px'
})