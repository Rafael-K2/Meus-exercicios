let notas = [4, 7, 9, 5, 10, 6, 8]

notas.forEach(function(nota, index){
    if (nota >= 7 ){
        console.log(`Aluno ${index} aprovado com nota: ${nota}!!`)
    }
    else {
        console.log(`Aluno ${index} reprovado com nota: ${nota}!!`)
    }
})