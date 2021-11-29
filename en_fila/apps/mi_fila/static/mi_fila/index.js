document.addEventListener('DOMContentLoaded', function(){
    get_position();
});

function get_position(){
    var area_id = document.getElementById('area_id').getAttribute('name');
    area_id = parseInt(area_id)+1
    const En_filaSocket = new WebSocket(
        'ws://'
        + window.location.host
        + '/ws/mi_area/'
        + area_id
        + '/'
    );
    En_filaSocket.onmessage = function(e) {
        const data = JSON.parse(e.data);
        var pteposicion = document.getElementById('pteposicion').getAttribute('name');
        if (parseInt(pteposicion) < parseInt(data.position)) {
          document.querySelector("#area_id").innerHTML =
            "Su turno ah pasado Gracias por utilizar En-Fila.";
        } else if (pteposicion == data.position) {
          document.querySelector("#area_id").innerHTML =
            "Es su turno favor pasar por su area.";
        } else if (pteposicion > data.position) {
            var faltan =  pteposicion - data.position;
          document.querySelector("#area_id").innerHTML =
            `Hay ${faltan} antes que usted.`;
        }
        
        
    }

    En_filaSocket.onclose = function(e) {
        console.error('Chat socket closed unexpectedly');
    };
}
