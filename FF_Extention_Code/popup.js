console.log("Inside2");

    document.addEventListener("DOMContentLoaded", function () {
        const button = document.getElementById("autoFillButton"); // Replace "myButton" with your element's ID
        if (button) {
            button.addEventListener("click", function() {
                // Your event handling code
				console.log("Inside");
				browser.tabs.executeScript({ file: "content.js" });
            });
        }
    });
