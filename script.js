function updateDashboard() {
    fetch('soc_data.json')
        .then(response => response.json())
        .then(data => {

            // SOC values
            document.getElementById('soc_emg').style.width = data.SOC_EMG + "%";
            document.getElementById('soc_ev1').style.width = data.SOC_EV1 + "%";
            document.getElementById('soc_ev2').style.width = data.SOC_EV2 + "%";

            document.getElementById('emg_val').innerText = data.SOC_EMG.toFixed(1);
            document.getElementById('ev1_val').innerText = data.SOC_EV1.toFixed(1);
            document.getElementById('ev2_val').innerText = data.SOC_EV2.toFixed(1);

            // Mode logic (basic – ML output can replace this)
            let modeText = "Normal Charging";
            if (data.SOC_EMG < 40) {
                modeText = "🚑 Emergency Priority Mode";
            }

            document.getElementById('mode').innerText = modeText;
            document.getElementById('time').innerText = "Last Update: " + data.time;
        })
        .catch(err => console.log("Waiting for data..."));
}

// Update every 1 second
setInterval(updateDashboard, 1000);
