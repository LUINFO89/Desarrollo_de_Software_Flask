function validar_formulario() {
   
    var username= document.formRegistro.nombre;
    var email = document.formRegistro.email;
    var password = document.formRegistro.contrasena;
  
    var username_len = username.value.length;
    if (username_len == 0 || username_len < 8) {
      alert("Debes ingresar un username con min. 8 caracteres");
      passid.focus();
      return false; //Para la parte dos, que los datos se conserven
    }
  
    var formato_email = /^\w+([\.-]?\w+)@\w+([\.-]?\w+)(\.\w{2,3})+$/;
    if (!email.value.match(formato_email)) {
      alert("Debes ingresar un email electronico valido!");
      email.focus();
      return false; //Para la parte dos, que los datos se conserven
    }
  
    var passid_len = password.value.length;
    if (passid_len == 0 || passid_len < 8) {
      alert("Debes ingresar una password con mas de 8 caracteres");
      passid.focus();
    }

    else{
        alert("bienvenido al sistema")
        
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
  
  function showForm() {
    document.getElementById("formRegistro").style.display = "block";
  }
  
  function hideForm() {
    document.getElementById("formRegistro").style.display = "none";
  }