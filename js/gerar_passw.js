

document.getElementById('gerar_senha').addEventListener('click', function (e) {
    e.preventDefault();
    var senha = generatePassword(10); // Gerar senha de 10 caracteres
    alert('Sua senha temporária é: ' + senha);
});

// Função para gerar senha aleatória
function generatePassword(length) {
    var charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789";
    var password = "";
    for (var i = 0; i < length; ++i) {
        var randomIndex = Math.floor(Math.random() * charset.length);
        password += charset[randomIndex];
    }
    return password;
}
