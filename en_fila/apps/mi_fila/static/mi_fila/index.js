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
        document.querySelector('#area_id').innerHTML = data.position;
        console.log(data)
    }

    En_filaSocket.onclose = function(e) {
        console.error('Chat socket closed unexpectedly');
    };
}
