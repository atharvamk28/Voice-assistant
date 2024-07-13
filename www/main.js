$(document).ready(function () {
    
    $('.text').textillate({
        loop: true,
        sync: true,
        in:{
            effect: "bounceIn",
        },
        out:{
            effect: "bounceOut",
        }

    });

    // Siri Configuration
    var siriWave = new SiriWave({
        container: document.getElementById("siri-container"),
        width: 800,
        height: 200,
        style: "ios9",
        amplitude: "2",
        speed: "0.30",
        autostart: "true"
      });

    // Siri Message Animation
    $('.siri-message').textillate({
        loop: true,
        sync: true,
        in:{
            effect: "fadeInUp",
            sync: true
        },
        out:{
            effect: "fadeOutUp",
            sync: true
        }

    });

    // mic button event

    $("#MicBtn").click(function () { 
        
        $("#Oval").attr("hidden", true);
        $("#SiriWave").attr("hidden", false);
        eel.playAssistantSound()
        eel.start_interaction()()
    });

});