let energia = 25;

if (energia < 0 ) {
    console.log('Energia Inválida');
} else if (energia === 0) {
    console.log('Energia zerada');
} else if (energia >= 1 && energia <= 30) {
    console.log('Energia baixa');
} else if (energia >= 31 && energia <= 70) {
    console.log('Energia média');
} else {
    console.log('Energia alta');
}