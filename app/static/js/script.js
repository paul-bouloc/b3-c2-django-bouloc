function hideFormPassword() {
    var x = document.getElementById("password");
    if (x.type === "password") {
        x.type = "text";
        document.getElementById("hidePassword").innerHTML = "Hide password";
    } else {
        x.type = "password";
        document.getElementById("hidePassword").innerHTML = "Show password";
    }
}

function generateStrongPassword(){
    var length = 15,
        charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+{}:<>?|[];',./",
        retVal = "";
    for (var i = 0, n = charset.length; i < length; ++i) {
        retVal += charset.charAt(Math.floor(Math.random() * n));
        }
    document.getElementById("password").value = retVal;

    var x = document.getElementById("password");
    if(x.type === "password"){
        hideFormPassword()
    }
}