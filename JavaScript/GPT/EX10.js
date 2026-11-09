let notas = [3,7,8,10,9,5]
let notas_altas = 0
for (let i = 0; i < notas.length; i++) {
    if (notas[i] >= 7 ) {
        notas_altas++
        console.log(notas[i])
    }
}
console.log('Existem',notas_altas,'notas altas')