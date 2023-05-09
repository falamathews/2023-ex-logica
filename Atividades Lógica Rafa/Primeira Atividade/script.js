function comprar(){
    let codigo = Number(prompt('Digite o código do produto:'))
    let quantidade = Number(prompt('Digite a quantidade:'))
    
    if(codigo == 1){
        preco = 4
    }else{
        if(codigo == 2){
            preco = 4.5
        }else{
            if(codigo == 3){
                preco = 5.0
            }else
            if(codigo == 4){
                preco = 2.0
            }else
            if(codigo == 5){
                preco = 5
            }
                }
            }
            let total = preco * quantidade
            alert('Valor a pagar: R$' + total.toFixed(2))
        }
