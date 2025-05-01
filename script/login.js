let btnOpen = document.querySelector('.login')
let btnClose = document.querySelector('.btn-close-logo')
let boxLogin = document.querySelector('.box-login')
btnOpen.addEventListener('click', function(){
    boxLogin.style.top = '0px'
})
btnClose.addEventListener('click', function(){
    boxLogin.style.top = '-350px'
})
