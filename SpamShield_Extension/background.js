chrome.runtime.onMessage.addListener((request, sender, sendResponse) => {

    if (request.action === "checkSpam") {

        fetch("http://localhost:5000/predict", {
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