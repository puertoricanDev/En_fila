document.addEventListener('DOMContentLoaded', function(){
    get_position();
});

function get_position(){
    const area_id = document.getElementById('area_id').getAttribute('name');
    console.log(area_id)
    // const chatSocket = new WebSocket(
    //     'ws://'
    //     + window.location.host
    //     + '/ws/mi_fila/'
    //     + area_id
    //     + '/'
    // );
    // chatSocket.onmessage = function(e) {
    //     const data = JSON.parse(e.data);
    //     console.log(data)
    //     document.getElementById('area_id').value = data.position;
    // }

    // chatSocket.onclose = function(e) {
    //     console.error('Chat socket closed unexpectedly');
    // };
}
