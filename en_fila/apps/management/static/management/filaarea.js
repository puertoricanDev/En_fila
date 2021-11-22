document.addEventListener("DOMContentLoaded", function () {
  change_position();
});
function change_position(){
  area_id = document.querySelector("#area_id").getAttribute("name");
  next_position = document.querySelector("#turno_actual").getAttribute("name");
  alert(area_id);
  const En_filaSocket = new WebSocket(
    "ws://" + window.location.host + "/ws/mi_area/" + `${area_id}` + "/"
  );
  
    En_filaSocket.send(
      JSON.stringify({
        next_position: next_position,
      })
    );
  
  };
