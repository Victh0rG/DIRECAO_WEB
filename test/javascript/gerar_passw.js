
const passInput = document.querySelector('#gerar_senha');

const numbers = [0,1,2,3,4,5,6,7,8,9]
const caracters = Array.from(Array(26).map((_, i) => i + 97));
const lowerCaracters = caracters.map((item) => String.fromCharCode(item))
const upperCaracters = lowerCaracters.map((item) => item.toUpperCase())

linkgerar.addEvent("click", () => {
    gerarPassowrd(
        chkNumber.checked,
        chkLower.checked,
        chkUpper.checked,
        lenInput.value,
    );
});

const genrarPassword = (
    hasnumbers,
    hasLower,
    hasUpper,
    length
 ) => {
    const newArray = [ 
        ...(hasnumbers ? numbers : []),
        ...(hasLower ? lowerCaracters : []),
        ...(hasUpper ? upperCaracters : []),
    ];

    if(newArray.length === 0 ) return;

    let password = "";

    for (let i = 0; i < length; i++){
        const randomIndex = Math.floor(Math.random() * newArray.length);
        password += newArray[randomIndex];
    }

    passInput.value = password;
};