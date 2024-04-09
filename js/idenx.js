
document.getElementById('login').addEventListener('submit', function(event){
    event.preventDefault;

var user = document.getElementById('user').value;
var password = document.getElementById9('password').value;

if (user === user && password === password){
    window.location.href = "main.html";
} else{
    alert('usuário ou senha incorretos');
}
});