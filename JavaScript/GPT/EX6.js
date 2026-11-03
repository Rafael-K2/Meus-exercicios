let inventario = ['Espada', 'Escudo', 'Poção'];

inventario.push('Arco')
inventario.unshift('Capacete')
inventario.pop()
let selecionado = inventario.indexOf('Escudo')
inventario.splice(selecionado, 1)
let selecionado_2 = inventario.indexOf('Poção')
inventario.splice(selecionado_2,1 ,'Poção de cura')

console.log(inventario)