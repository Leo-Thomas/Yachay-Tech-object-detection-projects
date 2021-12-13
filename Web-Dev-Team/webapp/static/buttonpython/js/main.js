function DownloadImage() {
    var img_down = document.getElementById('inference_img').src;
    const downloadInstance = document.createElement('a');
    downloadInstance.href = img_down
    downloadInstance.target = '_blank';
    downloadInstance.download = 'img_bounding_boxes';

    document.body.appendChild(downloadInstance);
    downloadInstance.click();
    document.body.removeChild(downloadInstance);
}

(function() {
    // The width and height of the captured photo. We will set the
    // width to the value defined here, but the height will be
    // calculated based on the aspect ratio of the input stream.

    var width = 400; // We will scale the photo width to this
    var height = 300; // This will be computed based on the input stream

    // |streaming| indicates whether or not we're currently streaming
    // video from the camera. Obviously, we start at false.

    var streaming = false;

    // The various HTML elements we need to configure or control. These
    // will be set by the startup() function.

    var video = null;
    var canvas = null;
    var photo = null;
    var startbutton = null;

    function startup() {
        document.getElementById('contenedor-img').innerHTML = `<span>
                          <video id='video' height=300 width=400 class='me-3'></video>
                          <canvas id='canvas' height=300 width=400 class='ms-3'></canvas>
                      </span> `


        video = document.getElementById('video');
        canvas = document.getElementById('canvas');
        photo = document.getElementById('photo');
        startbutton = document.getElementById('startbutton');

        navigator.mediaDevices.getUserMedia({ video: true, audio: false })
            .then(function(stream) {
                video.srcObject = stream;
                video.play();
            })
            .catch(function(err) {
                console.log("An error occurred: " + err);
            });

        video.addEventListener('canplay', function(ev) {
            if (!streaming) {
                height = video.videoHeight / (video.videoWidth / width);

                // Firefox currently has a bug where the height can't be read from
                // the video, so we will make assumptions if this happens.

                if (isNaN(height)) {
                    height = width / (4 / 3);
                }

                video.setAttribute('width', width);
                video.setAttribute('height', height);
                canvas.setAttribute('width', width);
                canvas.setAttribute('height', height);
                streaming = true;
            }
        }, false);

        startbutton.addEventListener('click', function(ev) {
            takepicture();
            ev.preventDefault();
        }, false);

        clearphoto();
    }

    // Fill the photo with an indication that none has been
    // captured.

    function clearphoto() {
        var context = canvas.getContext('2d');
        context.fillStyle = "#AAA";
        context.fillRect(0, 0, canvas.width, canvas.height);

        var data = canvas.toDataURL('image/png');
        photo.setAttribute('value', data);
    }

    // Capture a photo by fetching the current contents of the video
    // and drawing it into a canvas, then converting that to a PNG
    // format data URL. By drawing it on an offscreen canvas and then
    // drawing that to the screen, we can change its size and/or apply
    // other changes before drawing it.

    function takepicture() {
        var context = canvas.getContext('2d');
        if (width && height) {
            canvas.width = width;
            canvas.height = height;
            context.drawImage(video, 0, 0, width, height);

            var data = canvas.toDataURL('image/png');
            photo.setAttribute('value', data);
        } else {
            clearphoto();
        }
    }

    // Set up our event listener to run the startup process
    // once loading is complete.
    var camerabutton = document.getElementById('startcamera');
    camerabutton.addEventListener('click', startup, false);
})();

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function DisplayBtnPhoto() {
    document.getElementById("startbutton").classList.remove("d-none");
    document.getElementById("send_photo").classList.remove("d-none");
    document.getElementById("startcamera").classList.add("d-none");
    document.getElementById("submitform").classList.add("d-none");
    document.getElementById("btn-home").classList.remove("d-none");
    document.getElementById("btn-download").classList.add("d-none");
    document.getElementById("form-generar").classList.add("d-none");
    document.getElementById("text-results").classList.add("d-none")
    document.getElementById("startinference").classList.add("d-none");
    document.getElementById("btn-cancelar").innerHTML = `Cancel`;
}

function ResetBtnPhoto() {
    document.getElementById("send_photo").classList.add("d-none");
    document.getElementById("startbutton").classList.add("d-none");
    document.getElementById("startcamera").classList.remove("d-none");
    document.getElementById("submitform").classList.remove("d-none");
    document.getElementById("form-generar").classList.remove("d-none");
    document.getElementById("btn-download").classList.remove("d-none");
    document.getElementById("btn-home").classList.remove("d-none");
    document.getElementById("btn-cancelar").innerHTML = `Home`;

}

function DisableWhenCount() {
    document.getElementById("startcamera").classList.remove("d-none");
    document.getElementById("submitform").classList.remove("d-none");
}

function ShowWait() {
    document.getElementById('contenedor-img').innerHTML = `<div class="mx-auto my-auto d-flex align-items-center justify-content-center" id="contenedor-img">
  <p class="text-capitalize fs-1 text-center my-auto">Patience is a virtue</p> 
</div>`

    document.getElementById("wait").classList.remove("d-none")
    Waiting()
}





function Waiting() {
    window.dotsGoingUp = true;
    var dots = window.setInterval(function() {
        var wait = document.getElementById("wait");
        if (window.dotsGoingUp)
            wait.innerHTML += "o";
        else {
            wait.innerHTML = wait.innerHTML.substring(1, wait.innerHTML.length);
            if (wait.innerHTML === "o")
                window.dotsGoingUp = true;
        }
        if (wait.innerHTML.length > 9)
            window.dotsGoingUp = false;
        return
    }, 100);
}


function send_image() {

    document.getElementById("btn-download").classList.add("d-none");
    document.getElementById("form-generar").classList.add("d-none");
    document.getElementById("startbutton").classList.add("d-none");
    document.getElementById("send_photo").classList.add("d-none");
    document.getElementById("submitform").classList.add("d-none");
    document.getElementById('contenedor-img').innerHTML = ' ';
    document.getElementById('results_inference').innerHTML = ' ';
    document.getElementById("btn-cancelar").innerHTML = `Cancel`;
    ShowWait()
    var form = new FormData(document.getElementById('form_photo'));
    fetch("/", {
        method: "POST",
        body: form,
        headers: {
            "X-CSRFToken": getCookie('csrftoken'),
            "X-Requested-With": "XMLHttpRequest"
        }
    }).then(
        function(response) {
            return response.json()

        }
    ).then(
        function(data) {
            fetch(data.edit_url, {
                method: "GET",
                headers: {
                    "X-CSRFToken": getCookie('csrftoken'),
                    "X-Requested-With": "XMLHttpRequest"
                }
            }).then(
                function() {
                    fetch(data.raw_url, {
                        method: "GET",
                        headers: {
                            "X-CSRFToken": getCookie('csrftoken'),
                            "X-Requested-With": "XMLHttpRequest"
                        }
                    }).then(
                        function() {
                            var datos = data;
                            console.log(datos);
                            console.log(typeof(datos.accuracy));
                            console.log(typeof(datos.roses));
                            console.log(datos);
                            document.getElementById("text-results").classList.remove("d-none")
                            document.getElementById('contenedor-img').innerHTML = `<img class="me-2" src=` + datos.raw_url + ` id="input_img" height=300 width=400>
                                                                                   <img class="ms-2" src=` + datos.edit_url + ` id="inference_img" height=300 width=400>`;

                            document.getElementById('results_inference').innerHTML = `
                                                          <p class="text-center mt-4 fs-3">Roses found: <span
                                                                  class="fs-2" >` + datos.roses + `</span></p> 
                                                                  <p class="text-center mt-4 fs-3">Accuracy (avg): <span
                                                                  class="fs-2" >` + datos.accuracy + `</span></p>`;
                            ResetBtnPhoto()
                            document.getElementById("startinference").classList.remove("d-none");
                            document.getElementById("wait").classList.add("d-none")

                        }
                    )
                }
            )
        }
    )
};

function submit_image() {
    document.getElementById("btn-download").classList.add("d-none");
    document.getElementById("form-generar").classList.add("d-none");
    document.getElementById("startbutton").classList.add("d-none");
    document.getElementById("send_photo").classList.add("d-none");
    document.getElementById("submitform").classList.add("d-none");
    document.getElementById("startinference").classList.add("d-none");
    document.getElementById("startcamera").classList.add("d-none");
    document.getElementById("btn-home").classList.remove("d-none");
    document.getElementById('contenedor-img').innerHTML = ' ';
    document.getElementById('results_inference').innerHTML = ' ';
    document.getElementById("btn-cancelar").innerHTML = `Cancel`;

    ShowWait()
    var form = new FormData(document.getElementById('submitform'));
    fetch("/", {
        method: "POST",
        body: form,
        headers: {
            "X-CSRFToken": getCookie('csrftoken'),
            "X-Requested-With": "XMLHttpRequest"
        }
    }).then(
        function(response) {
            return response.json()

        }
    ).then(
        function(data) {
            fetch(data.edit_url, {
                method: "GET",
                headers: {
                    "X-CSRFToken": getCookie('csrftoken'),
                    "X-Requested-With": "XMLHttpRequest"
                }
            }).then(
                function() {
                    fetch(data.raw_url, {
                        method: "GET",
                        headers: {
                            "X-CSRFToken": getCookie('csrftoken'),
                            "X-Requested-With": "XMLHttpRequest"
                        }
                    }).then(
                        function() {
                            var datos = data;
                            console.log(datos);
                            console.log(typeof(datos.accuracy));
                            console.log(typeof(datos.roses));
                            console.log(datos);
                            document.getElementById("text-results").classList.remove("d-none")
                            document.getElementById('contenedor-img').innerHTML = `<img class="me-2" src=` + datos.raw_url + ` id="input_img" height=300 width=400>
                                                                                   <img class="ms-2" src=` + datos.edit_url + ` id="inference_img" height=300 width=400>`;

                            document.getElementById('results_inference').innerHTML = `
                                                          <p class="text-center mt-4 fs-3">Roses found: <span
                                                                  class="fs-2" >` + datos.roses + `</span></p> 
                                                                  <p class="text-center mt-4 fs-3">Accuracy (avg): <span
                                                                  class="fs-2" >` + datos.accuracy + `</span></p>`;
                            ResetBtnPhoto()
                            document.getElementById("wait").classList.add("d-none")

                            document.getElementById("startinference").classList.remove("d-none");
                        }
                    )
                }
            )
        }
    )
};

document.getElementById("startbutton").onclick = function() {
    document.getElementById("send_photo").classList.remove("disabled")
};

function DisplayBtnPhoto() {
    document.getElementById("startbutton").classList.remove("d-none");
    document.getElementById("send_photo").classList.remove("d-none");
    document.getElementById("startcamera").classList.add("d-none");
    document.getElementById("submitform").classList.add("d-none");
    document.getElementById("btn-home").classList.remove("d-none");
    document.getElementById("btn-download").classList.add("d-none");
    document.getElementById("form-generar").classList.add("d-none");
    document.getElementById("text-results").classList.add("d-none")
    document.getElementById("startinference").classList.add("d-none");
    document.getElementById("btn-cancelar").innerHTML = `Cancel`;
}



document.getElementById("startcamera").onclick = DisplayBtnPhoto;

document.getElementById("contar").onclick = DisableWhenCount;