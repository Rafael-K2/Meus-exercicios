let notas = [7, 4, 9, 5, 10];

notas.push(8)
let selecionado = notas.indexOf(4)
notas.splice(selecionado,1)

let selecionado_2 = notas.indexOf(5)
notas.splice(selecionado_2,1,6)

console.log(notas)

let quantia = notas.length
console.log(quantia)