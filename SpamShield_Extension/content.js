let lastEmailText = "";
let checkTimer = null;
let observer = null;

/* Check extension available */
function extensionReady() {
    return typeof chrome !== "undefined" &&
           chrome.runtime &&
           chrome.runtime.id;
}

/* Show Result Banner */
function showBanner(response) {

    if (!extensionReady()) return;

    let oldBanner = document.querySelector(".spamshield-banner");
    if (oldBanner) oldBanner.remove();

    let banner = document.createElement("div");
    banner.className = "spamshield-banner";

    let message = "";
    let bg = "";

    /* Prediction Type */
    if (response.prediction === "Phishing") {

        message =
            "🎣 Phishing Alert | Score: " +
            response.spam_score + "%";

        bg = "linear-gradient(90deg,#6a00ff,#b000ff)";
    }
    else if (response.prediction === "Spam") {

        message =
            "🚨 Spam Detected | Score: " +
            response.spam_score + "%";

        bg = "linear-gradient(90deg,#ff0000,#ff5f5f)";
    }
    else if (response.prediction === "Suspicious") {

        message =
            "⚠ Suspicious Email | Score: " +
            response.spam_score + "%";

        bg = "linear-gradient(90deg,#ff8c00,#ffcc00)";
    }
    else {

        message =
            "✅ Safe Email | Score: " +
            response.spam_score + "%";

        bg = "linear-gradient(90deg,#00a000,#00d26a)";
    }

    banner.style.background = bg;

    /* Reasons */
    let reasonText = "";

    if (response.reasons &&
        response.reasons.length > 0) {

        reasonText =
            "<div class='spamshield-reasons'>" +
            response.reasons.join(" • ") +
            "</div>";
    }

    banner.innerHTML = `
        <div class="spamshield-left">
            <div class="spamshield-title">${message}</div>
            ${reasonText}
        </div>

        <span class="spamshield-close">✖</span>
    `;

    document.body.prepend(banner);

    let closeBtn =
        banner.querySelector(".spamshield-close");

    if (closeBtn) {
        closeBtn.onclick = () => banner.remove();
    }
}

/* Remove Banner */
function removeBanner() {

    let oldBanner =
        document.querySelector(".spamshield-banner");

    if (oldBanner) oldBanner.remove();
}

/* Detect Opened Email */
function checkEmail() {

    if (!extensionReady()) return;

    let emailBox =
        document.querySelector(".a3s");

    /* If inbox page */
    if (!emailBox) {
        removeBanner();
        lastEmailText = "";
        return;
    }

    let text =
        emailBox.innerText.trim();

    if (text.length < 10) {
        removeBanner();
        return;
    }

    /* Avoid repeated scans */
    if (text === lastEmailText) return;

    lastEmailText = text;

    chrome.runtime.sendMessage(
        {
            action: "checkSpam",
            text: text
        },

        function(response) {

            if (chrome.runtime.lastError) return;
            if (!response) return;

            showBanner(response);
        }
    );
}

/* Delay scans for smooth UI */
function scheduleCheck() {

    clearTimeout(checkTimer);

    checkTimer =
        setTimeout(checkEmail, 1200);
}

/* First Load */
scheduleCheck();

/* Detect Gmail page changes */
observer = new MutationObserver(() => {
    scheduleCheck();
});

observer.observe(document.body, {
    childList: true,
    subtree: true
});