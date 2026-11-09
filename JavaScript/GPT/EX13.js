let estoque = ['mouse', 'teclado', 'monitor', 'headset', 'webcam']

let produto = prompt('Qual produto vc deseja: ').toLowerCase()

if (estoque.includes(produto) === true) {
    console.log('Item existe no estoque')
}
else {
    console.log('Item invalido')
}