let currentThreadId =
    localStorage.getItem("travel_thread_id") || null;

let latestAnswerMarkdown = "";

let thinkingInterval = null;


/* ================================
   QUICK PROMPT
================================ */

function setPrompt(text) {

    const input =
        document.getElementById("userInput");

    input.value = text;

    input.focus();
}


/* ================================
   LOADING
================================ */

function setLoading(isLoading) {

    const sendBtn =
        document.getElementById("sendBtn");

    const btnText =
        document.getElementById("btnText");

    const btnLoader =
        document.getElementById("btnLoader");

    const thinkingStatus =
        document.getElementById("thinkingStatus");


    sendBtn.disabled = isLoading;


    if (isLoading) {

        btnText.classList.add("hidden");

        btnLoader.classList.remove("hidden");

        thinkingStatus.classList.remove("hidden");

        startThinkingAnimation();

    } else {

        btnText.classList.remove("hidden");

        btnLoader.classList.add("hidden");

        thinkingStatus.classList.add("hidden");

        stopThinkingAnimation();

    }
}


/* ================================
   THINKING ANIMATION
================================ */

function startThinkingAnimation() {

    const thinkingText =
        document.getElementById("thinkingText");


    const messages = [

        "Analyzing your travel request...",

        "Searching for the best travel options...",

        "Checking flights and destinations...",

        "Researching hotels and accommodation...",

        "Building your personalized itinerary...",

        "Optimizing your travel plan...",

        "Preparing your Travexa AI experience..."

    ];


    let index = 0;


    thinkingText.textContent =
        messages[index];


    thinkingInterval =
        setInterval(() => {

            index =
                (index + 1) %
                messages.length;


            thinkingText.textContent =
                messages[index];

        }, 2200);
}


function stopThinkingAnimation() {

    if (thinkingInterval) {

        clearInterval(
            thinkingInterval
        );

        thinkingInterval = null;

    }
}


/* ================================
   ERROR
================================ */

function showError(message) {

    const errorBox =
        document.getElementById("errorBox");

    errorBox.textContent =
        message;

    errorBox.classList.remove(
        "hidden"
    );
}


function hideError() {

    const errorBox =
        document.getElementById("errorBox");

    errorBox.classList.add(
        "hidden"
    );

    errorBox.textContent = "";
}


/* ================================
   RESULT
================================ */

function showResult(
    answer,
    threadId
) {

    latestAnswerMarkdown =
        answer;


    const resultSection =
        document.getElementById(
            "resultSection"
        );

    const resultBox =
        document.getElementById(
            "resultBox"
        );

    const threadInfo =
        document.getElementById(
            "threadInfo"
        );


    if (
        typeof marked !==
        "undefined"
    ) {

        resultBox.innerHTML =
            marked.parse(answer);

    } else {

        resultBox.innerText =
            answer;

    }


    threadInfo.textContent =
        `Thread ID: ${threadId}`;


    resultSection.classList.remove(
        "hidden"
    );


    setTimeout(() => {

        resultSection.scrollIntoView({
            behavior: "smooth",
            block: "start"
        });

    }, 150);
}


/* ================================
   SEND REQUEST
================================ */

async function sendMessage() {

    hideError();


    const input =
        document.getElementById(
            "userInput"
        );


    const message =
        input.value.trim();


    if (!message) {

        showError(
            "Please enter your travel request first."
        );

        input.focus();

        return;
    }


    setLoading(true);


    try {

        const response =
            await fetch(
                "/api/travel",
                {

                    method: "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body:
                        JSON.stringify({
                            message:
                                message,

                            thread_id:
                                currentThreadId
                        })

                }
            );


        let data;


        try {

            data =
                await response.json();

        } catch {

            throw new Error(
                "The server returned an invalid response."
            );

        }


        if (
            !response.ok ||
            !data.success
        ) {

            throw new Error(
                data.error ||
                "Something went wrong while generating your travel plan."
            );

        }


        currentThreadId =
            data.thread_id;


        localStorage.setItem(
            "travel_thread_id",
            currentThreadId
        );


        showResult(
            data.answer,
            data.thread_id
        );


    } catch (error) {

        showError(
            error.message
        );

    } finally {

        setLoading(false);

    }
}


/* ================================
   COPY RESULT
================================ */

function copyResult() {

    const resultBox =
        document.getElementById(
            "resultBox"
        );


    const text =
        resultBox.innerText;


    if (!text) {
        return;
    }


    navigator.clipboard
        .writeText(text)

        .then(() => {

            const copyBtn =
                document.querySelector(
                    ".copy-btn"
                );


            const oldText =
                copyBtn.textContent;


            copyBtn.textContent =
                "Copied ✓";


            setTimeout(() => {

                copyBtn.textContent =
                    oldText;

            }, 1500);

        })

        .catch(() => {

            showError(
                "Could not copy the travel plan."
            );

        });
}


/* ================================
   PDF DOWNLOAD
================================ */

function downloadPDF() {

    const pdfContent =
        document.getElementById(
            "pdfContent"
        );


    if (
        !latestAnswerMarkdown ||
        !pdfContent
    ) {

        showError(
            "No travel plan available to download."
        );

        return;
    }


    const downloadBtn =
        document.querySelector(
            ".download-btn"
        );


    const oldText =
        downloadBtn.textContent;


    downloadBtn.textContent =
        "Preparing PDF...";


    downloadBtn.disabled =
        true;


    const options = {

        margin: 0.5,

        filename:
            "Travexa-AI-Travel-Plan.pdf",

        image: {

            type: "jpeg",

            quality: 0.98

        },

        html2canvas: {

            scale: 2,

            useCORS: true,

            backgroundColor:
                "#ffffff"

        },

        jsPDF: {

            unit: "in",

            format: "a4",

            orientation:
                "portrait"

        },

        pagebreak: {

            mode: [
                "avoid-all",
                "css",
                "legacy"
            ]

        }

    };


    html2pdf()

        .set(options)

        .from(pdfContent)

        .save()

        .then(() => {

            downloadBtn.textContent =
                oldText;

            downloadBtn.disabled =
                false;

        })

        .catch(() => {

            downloadBtn.textContent =
                oldText;

            downloadBtn.disabled =
                false;


            showError(
                "Could not download PDF."
            );

        });
}


/* ================================
   CTRL + ENTER
================================ */

document.addEventListener(
    "keydown",
    function (event) {

        if (
            event.ctrlKey &&
            event.key === "Enter"
        ) {

            sendMessage();

        }

    }
);


/* ================================
   3D HERO MOUSE EFFECT
================================ */

const orbScene =
    document.getElementById(
        "orbScene"
    );


if (orbScene) {

    const heroVisual =
        orbScene.parentElement;


    heroVisual.addEventListener(
        "mousemove",
        function (event) {

            const rect =
                heroVisual
                    .getBoundingClientRect();


            const x =
                event.clientX -
                rect.left;


            const y =
                event.clientY -
                rect.top;


            const centerX =
                rect.width / 2;


            const centerY =
                rect.height / 2;


            const rotateY =
                (
                    (x - centerX) /
                    centerX
                ) * 8;


            const rotateX =
                -(
                    (y - centerY) /
                    centerY
                ) * 8;


            orbScene.style.transform =
                `
                rotateX(${rotateX}deg)
                rotateY(${rotateY}deg)
                `;

        }
    );


    heroVisual.addEventListener(
        "mouseleave",
        function () {

            orbScene.style.transform =
                "rotateX(0deg) rotateY(0deg)";

        }
    );

}


/* ================================
   PLANNER 3D TILT
================================ */

const plannerCard =
    document.getElementById(
        "plannerCard"
    );


if (
    plannerCard &&
    window.innerWidth > 900
) {

    plannerCard.addEventListener(
        "mousemove",
        function (event) {

            const rect =
                plannerCard
                    .getBoundingClientRect();


            const x =
                event.clientX -
                rect.left;


            const y =
                event.clientY -
                rect.top;


            const centerX =
                rect.width / 2;


            const centerY =
                rect.height / 2;


            const rotateY =
                (
                    (x - centerX) /
                    centerX
                ) * 1.2;


            const rotateX =
                -(
                    (y - centerY) /
                    centerY
                ) * 1.2;


            plannerCard.style.transform =
                `
                perspective(1200px)
                rotateX(${rotateX}deg)
                rotateY(${rotateY}deg)
                `;

        }
    );


    plannerCard.addEventListener(
        "mouseleave",
        function () {

            plannerCard.style.transform =
                `
                perspective(1200px)
                rotateX(0deg)
                rotateY(0deg)
                `;

        }
    );

}


/* ================================
   INPUT AUTO HEIGHT
================================ */

const userInput =
    document.getElementById(
        "userInput"
    );


if (userInput) {

    userInput.addEventListener(
        "input",
        function () {

            this.style.height =
                "auto";


            const newHeight =
                Math.min(
                    Math.max(
                        this.scrollHeight,
                        175
                    ),
                    350
                );


            this.style.height =
                `${newHeight}px`;

        }
    );

}