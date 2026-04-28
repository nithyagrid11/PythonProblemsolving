console.log("JS loaded");

let statusChartInstance = null;
let trafficChartInstance = null;

/* for the status - online or offline  */
window.addEventListener("load",updateStatus);
window.addEventListener("online",updateStatus);
window.addEventListener("offline",updateStatus);

function updateStatus(){
    console.log("Function called")
    const statusIndicator = document.getElementById('status-indicator');
    const statusText = document.getElementById("status-text");
    if(navigator.onLine){
        statusIndicator.classList.remove('offline');
        statusIndicator.classList.add("online");
        statusText.textContent="Online";
    }
    else{
        statusIndicator.classList.remove('online');
        statusIndicator.classList.add("offline");
        statusText.textContent="Offline";
    }
}

/* To trigger the input */
const customButton = document.getElementById("customButton");
const fileInput = document.getElementById("fileInput");
const fileNameDisplay = document.getElementById("fileNameDisplay");
const logContent = document.getElementById("logContent");

customButton.addEventListener('click',()=>{
    fileInput.click();
});
/* To handle the file selection */
fileInput.addEventListener('change',(event)=>{
    const selectedFile = event.target.files[0];
    if (!selectedFile){
        fileNameDisplay.textContent = "No file choosen";
        logContent.textContent="";
        return;
    }
    if(!selectedFile.name.endsWith(".log") && !selectedFile.name.endsWith(".txt")){
        alert("Please upload a '.log' or '.txt' file");
        fileInput.value="";
        return;
    }
    fileNameDisplay.textContent = selectedFile.name;
    const reader = new FileReader(); /* reads file content and converts to text */
    reader.onload = function(e){ /* callback */
        console.log("CONTENT:", e.target.result);
        logContent.textContent = e.target.result;
    };
    reader.onerror = function () {
    console.log("Error reading file");
    };
    reader.readAsText(selectedFile); /* starts reading the lines */
});

/* anaylse button process */
const analyzeButton = document.getElementById("commentbutton");
const textarea = document.getElementById("comment");
analyzeButton.addEventListener("click",async(e)=>{
    e.preventDefault();
    let content = textarea.value;
    const fileText = document.getElementById("logContent").textContent;
    if (fileText.trim() !== ""){
        content = fileText;
    }
    if (!content.trim()) {
        alert("No log data provided");
        return;
    }
    try {
        const response = await fetch("http://127.0.0.1:8001/analyze", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ content: content }) /* js object -> json */
        });

        if (!response.ok) {
           throw new Error("Server error");
        }
        const data = await response.json();

        document.querySelector(".chart-container").style.display = "flex";
        document.getElementById("analysis-placeholder").style.display = "none";
        
        /* writing into cards */
        console.log("RESULT:", data);
        document.getElementById("totalLogs").textContent = data.total_count;
        document.getElementById("errors").textContent = data.total_errors;
        document.getElementById("warnings").textContent = data.total_warnings;
        document.getElementById("suspicious").textContent = data.suspicious_count;
        document.getElementById("peakHour").textContent = data.peak_hour;

        const spike_detection = document.getElementById("spike-detection");
        if (!data.spike_hours || Object.keys(data.spike_hours).length == 0){
           spike_detection.textContent = "No spikes";
        }else{
        let hours = Object.keys(data.spike_hours);
        spike_detection.textContent = `${hours.join(", ")}`;
        }

        /* status chart */
        const total = data.total_count;
        const errors = data.total_errors;
        const warnings = data.total_warnings;
        const success = total - errors - warnings;
        const statuschart = document.getElementById("statusChart").getContext('2d');
        if (statusChartInstance){
            statusChartInstance.destroy();
        }
        statusChartInstance = new Chart(statuschart, {
            type: "pie",
            data: {
                labels: ["Errors", "Warnings", "Success"],
                datasets: [{
                    data: [errors,warnings,success],
                    backgroundColor: ["#ff4d4d", "#e6e028", "#4caf50"]
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false
            }
        });

        /* Line chart */
        const usage = data.details["usage slots"] || {};
        const sortedhours = Object.keys(usage).sort((a, b) => a - b);
        const sortedcount = sortedhours.map(hour => usage[hour]);
        const trficChart = document.getElementById("trafficChart").getContext("2d");
        if (trafficChartInstance){
            trafficChartInstance.destroy();
        } 
        trafficChartInstance = new Chart(trficChart,{
            type: "line",
            data:{
                labels: sortedhours,
                datasets: [{
                    label: "Traffic",
                    data: sortedcount,
                    fill: false,
                    tension: 0.3
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false
            }
        });
    } catch (error) {
        console.error("Error:", error);
        alert("Failed to analyze logs!");
        document.querySelector(".chart-container").style.display = "none";
        document.getElementById("analysis-placeholder").style.display = "block";
    }
});
/* history */
async function loadHistory(){
    const container = document.getElementById("history-container")
    if (container.style.display == "block"){
        container.style.display = "none";
        return;
    }
    container.style.display = "block";
    container.style.overflow = "scroll";

    const res = await fetch("http://127.0.0.1:8001/history")
    const data = await res.json();
    container.innerHTML = "";
    data.history.reverse().forEach(item => {
        const card = document.createElement("div");
        card.className = "history-card";
        card.innerHTML = `
            <p><b>Logs:</b> ${item.logs}</p>
            <p><b>Result:</b> ${JSON.stringify(item.result)}</p>
            <p><b>Time:</b> ${item.timestamp}</p>
        `;
        container.appendChild(card);
    });
    console.log("History function")
};