window.onload = function() {
    const elements = document.querySelectorAll('[id^="expandButton_"]');
    createFunctions(elements.length)
    console.log("Page is fully loaded!");
};

function createFunctions(n) {
    for (let i = 1; i <= n; i++) {
        window['changeText_' + i] = function() {
            const button = document.getElementById('expandButton_' + i);
            if (button.textContent === 'Свернуть') {
                button.textContent = 'Развернуть';
            } else {
                button.textContent = 'Свернуть';
            }
        };
    }
}