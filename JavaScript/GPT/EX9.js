let produtos = ['Mause','Teclado','Gabinete','Monitor','Headset']

for (let i = 0; i < produtos.length; i++) {
    console.log(i+1,produtos[i])
    if (produtos[i] === produtos[3]) {
        console.log('Monitor encontrado')
    }
}