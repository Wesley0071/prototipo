function interacao() {
    // Obter o elemento select
    const select = document.getElementById("destination");
    
    // Obter o ID da opção selecionada
    const selectedOptionId = select.options[select.selectedIndex].id;
    
    // Atribuir o ID à variável (por exemplo, mostrar no console)
    console.log("ID da opção selecionada:", selectedOptionId);
    
    // Exemplo de uso: alterar o href do link
    document.getElementById("meu_link").href = `#${selectedOptionId}`;
}
