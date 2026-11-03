let saldo = 100;
let saque = 10;

if (saque <= 0) {
    console.log('Valor de saque inválido!');
} else if (saque > saldo) {
    console.log('Saque acima do saldo!');
} else if (saque < saldo) {
    saldo = saldo - saque 
    console.log('Saque feito, você tem',saldo,'Restante!');
} else if (saque === saldo) {
    saldo = saque - saldo
    console.log('Você usou todo o saldo!')
}