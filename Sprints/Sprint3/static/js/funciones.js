function guardar(){
    document.getElementById("IdFormulario").action="/reservas/guardar/";
}
function visualizar(){
    document.getElementById("IdFormulario").action="/reservas/visualizar/";
}
function eliminar(){
    document.getElementById("IdFormulario").action="/reservas/eliminar/";
}
function actualizar(){
    document.getElementById("IdFormulario").action="/reservas/actualizar/";
}
//FUNCIONES VUELOS
function guardarV(){
    document.getElementById("IdFormularioV").action="/vuelos/guardar/";
}
function visualizarV(){
    document.getElementById("IdFormularioV").action="/vuelos/visualizar/";
}
function eliminarV(){
    document.getElementById("IdFormularioV").action="/vuelos/eliminar/";
}
function actualizarV(){
    document.getElementById("IdFormularioV").action="/vuelos/actualizar/";
}

