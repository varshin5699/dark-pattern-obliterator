function downloadData() {
    chrome.runtime.sendMessage({ action: "downloadData" });
}
  
// Attach downloadData function to download button click event
document.getElementById("downloadButton").addEventListener("click", downloadData);
