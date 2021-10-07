function validarExtension() {
    var archivo = document.getElementById('idArchivo');
    var nombreArchivo = archivo.value;
    var extensiones = ["jpg", "gif", "png", "jpeg"];
    var separar = nombreArchivo.split(".")[1];//cadena.split("signo por el cual se divide")[posición]
    var extension = false;
    for (i in extensiones) {
        if (extensiones[i] === separar) {
            extension = true;
        }
    }if(extension){//si es verdadera :)
        alert("Archivo permitido");
    }else//si es falsa :(
    alert("Archivo no permitido");

}