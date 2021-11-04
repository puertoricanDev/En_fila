document.addEventListener('DOMContentLoaded', function(){
    get_position();
});

function get_position(){
    const area_id = document.getElementById('area_id').getAttribute('name');
    console.log(area_id)
    const En_filaSocket = new WebSocket(
        'ws://'
        + window.location.host
        + '/ws/mi_area/'
        + 1
        + '/'
    );
    En_filaSocket.onmessage = function(e) {
        const data = JSON.parse(e.data);
        console.log(data)
        // document.getElementById('area_id').value = data.position;
    }

    En_filaSocket.onclose = function(e) {
        console.error('Chat socket closed unexpectedly');
    };
}
