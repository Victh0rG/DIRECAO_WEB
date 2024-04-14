
document.getElementById('login').addEventListener('submit', function(event){
    event.preventDefault(); // Previne o envio do formulário antes da validação
    
    var user = document.getElementById('user').value;
    var password = document.getElementById('password').value;
    
    // Verifica se tanto o email quanto a senha foram fornecidos
    if (user === "" || password === "") {
        alert('Por favor, preencha tanto o usuário quanto a senha.');
    } else {
        // Se ambos os campos estão preenchidos, redireciona para a próxima página
        window.location.href = "main.html";
    }
});