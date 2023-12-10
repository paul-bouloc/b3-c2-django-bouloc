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