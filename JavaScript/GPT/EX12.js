let precos = [15, 30, 45, 10, 20, 100]

let total = 0
let m_vinte = 0
for (let i = 0; i < precos.length; i++) {
    if (precos[i] > 20) {
        total = total + precos[i]
        m_vinte++
    }
}

console.log('Os preços maiores que vinte somam',total,'contendo',m_vinte,'números maiores que vinte')