document.addEventListener("DOMContentLoaded", function () {
  change_position();
});
function change_position(){
  area_id = document.querySelector("#area_id").getAttribute("name");
  area_id = parseInt(area_id);
  next_position = document.querySelector("#turno_actual").getAttribute("name");
  const En_filaSocket = new WebSocket(
    "ws://" + window.location.host + "/ws/mi_area/" + `${area_id}` + "/"
  );
  
  document.querySelector("#next").onclick = function (e) {
    //const messageInputDom = document.querySelector('#chat-message-input');
    //const message = messageInputDom.value;
    En_filaSocket.send(
      JSON.stringify({
        next_position: parseInt(next_position)+1,
      })
    );}
    document.querySelector("#back").onclick = function (e) {
      //const messageInputDom = document.querySelector('#chat-message-input');
      //const message = messageInputDom.value;
      En_filaSocket.send(
        JSON.stringify({
          next_position: parseInt(next_position)-1,
        })
      );}
  
  };
