let validar_formulario = () => {

    // let usuario = $("#nombre").val;
    // let correo = $("#correo").val;
    // let contrasena = $("#contrasena").val;
    let usuario = document.getElementById("nombre").value;
    let correo = document.getElementById("email").value;
    let contrasena = document.getElementById("contrasena").value;
    let expresionRegulraCorreo = "/^\w+([\.-]?\w+)@\w+([\.-]?\w+)(\.\w{2,3})+$/";

    if (!correo.match(expresionRegulraCorreo)) {
        alert("el correo esta mal");
    }

    if (usuario.length > 8) {
        alert("ingresar el nombre dle usuario");
    }

    if (contrasena.length > 8) {
        alert("contraseña esta mal");
    }
}

let mostrarPassword = () => {
    let campoTipo = document.getElementById("contrasena");
    campoTipo.type = "text";
    //campoTipo.type == "password" ? campoTipo.type = "text" : campoTipo.type = "password";
    // if(tipo.type == "password"){
    //     tipo.type = "text";
    // }
}

let ocultarPassword = () => {
    let campoTipo = document.getElementById("contrasena");
    campoTipo.type = "password";
    //campoTipo.type == "text" ? campoTipo.type = "password" : campoTipo.type = "text";
    // if(tipo.type == "text"){
    //     tipo.type = "password";
    // }
}