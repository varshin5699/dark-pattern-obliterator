console.log("Content script running");

function removeScriptsAndStyles(htmlString) {

  htmlString = htmlString.replace(/<script\b[^<]*(?:(?!<\/script>)<[^<]*)*<\/script>/gi, '');
  htmlString = htmlString.replace(/<style\b[^<]*(?:(?!<\/style>)<[^<]*)*<\/style>/gi, '');
  htmlString = htmlString.replace(/<img\b[^<]*(?:(?!<\/img>)<[^<]*)*<\/img>/gi, '');
  htmlString = htmlString.replace(/<head\b[^<]*(?:(?!<\/head>)<[^<]*)*<\/head>/gi, '');
  htmlString = htmlString.replace(/(<([^>]+)>)/gi, "");
  htmlString = htmlString.replace(/(\r\n|\n|\r)/gm, " ");
  const htmlArray = htmlString.split(/\s{3,}/g)
  htmlString = htmlString.replace(/\s{3,}/g, '.').trim();

  return htmlString,htmlArray;
}

// Access the HTML of the current webpage
var pageHTML = document.documentElement.outerHTML;
var htmlArray = [];
pageHTML,htmlArray = removeScriptsAndStyles(pageHTML);
console.log(htmlArray);

function highlightText(textArray) {
  const regex = new RegExp(textArray.join('|'), 'gi');
  
  // Function to traverse DOM and highlight only text nodes
  function traverse(node) {
      if (node.nodeType === Node.TEXT_NODE) {
          const html = node.textContent.replace(regex, '<span style="background-color: yellow;">$&</span>');
          const temp = document.createElement('div');
          temp.innerHTML = html;
          while (temp.firstChild) {
              node.parentNode.insertBefore(temp.firstChild, node);
          }
          node.parentNode.removeChild(node);
      } else if (node.nodeType === Node.ELEMENT_NODE) {
          for (let i = 0; i < node.childNodes.length; i++) {
              traverse(node.childNodes[i]);
          }
      }
  }
  traverse(document.body);
}

let higharray = ["flooding inboxes of the users with promotional emails","tricking users into agreeing to certain conditions or clicking a few links.","Dark Pattern by Companies, Harm of Dark Pattern to Users"];

chrome.runtime.onMessage.addListener(function(message, sender, sendResponse) {
  if (message.action === "highlight") {
    console.log("highlighted");
    highlightText(higharray);

    const endpoint = 'https://05ec-35-190-152-232.ngrok-free.app';
    fetch(endpoint, {
    method: 'POST',
    headers: {'Content-Type': 'application/json','Accept':'application/json'},
    body: JSON.stringify({ tokens:['text received'] }),
    mode: 'no-cors',
    crossorigin: true,

    })
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      console.log(response.json());
    })
    .then(jsonResponse => {
      // Handle server response if needed
      console.log('Server response:', jsonResponse);
    })
    .catch(error => {
      // Handle errors
      console.error('Error sending data to server:', error);
    });
  }
});

function extractTextNodes(node) {
  let text = pageHTML;
  return '{\"text\":' + JSON.stringify(htmlArray) + '}';
}


// Extract text from current webpage and send it to background script
chrome.runtime.sendMessage({ action: "extractText", data: extractTextNodes(document.body) });

