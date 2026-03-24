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
        statusIndicator.classList.add("ofline");
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
        const response = await fetch("http://127.0.0.1:8000/analyze", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ content: content })
        });
        const data = await response.json();

        console.log("RESULT:", data);
        document.getElementById("totalLogs").textContent = data.total_count;
        document.getElementById("errors").textContent = data.total_errors;
        document.getElementById("warnings").textContent = data.total_warnings;
        document.getElementById("suspicious").textContent = data.suspicious_count;
        document.getElementById("peakHour").textContent = data.peak_hour;
    } catch (error) {
        console.error("Error:", error);
        alert("Failed to analyze logs!");
    }
});