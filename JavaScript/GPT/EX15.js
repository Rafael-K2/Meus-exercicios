let precos = [100, 250, 80, 300, 150]

precos.forEach(function(preco){
    console.log(`Preço normal ${preco} Preço com desconto ${(preco - 10/100*preco).toFixed(2)}`)
})