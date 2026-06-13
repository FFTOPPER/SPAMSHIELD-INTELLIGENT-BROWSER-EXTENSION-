chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {

    if (request.action === "checkSpam") {

        fetch("https://spamshield-intelligent-browser-extension.onrender.com/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ text: request.text })
        })
        .then(response => response.json())
        .then(data => sendResponse(data))
        .catch(error => sendResponse({ error: "Failed" }));

        return true;
    }

});