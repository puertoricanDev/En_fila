document.addEventListener('DOMContentLoaded', function(){
    get_position();
});

function get_position(){
    const area_id = document.getElementById('area_id').getAttribute('name');
    const En_filaSocket = new WebSocket(
        'ws://'
        + window.location.host
        + '/ws/mi_area/'
        + area_id
        + '/'
    );
    En_filaSocket.onmessage = function(e) {
        const data = JSON.parse(e.data);
        document.querySelector('#area_id').innerHTML = data.position;
    }

    En_filaSocket.onclose = function(e) {
        console.error('Chat socket closed unexpectedly');
    };
}
