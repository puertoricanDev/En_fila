document.addEventListener("DOMContentLoaded", function () {
  change_position();
});
function change_position(){
  const En_filaSocket = new WebSocket(
    "ws://" + window.location.host + "/ws/mi_area/" + 1 + "/"
  );
  document.querySelector("#next").onclick = function (e) {
    //const messageInputDom = document.querySelector('#chat-message-input');
    //const message = messageInputDom.value;
    En_filaSocket.send(
      JSON.stringify({
        next_position: 13,
      })
    );
  };
}