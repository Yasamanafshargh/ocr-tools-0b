// Add a loading spinner when the user clicks "Extract & Translate"
const form = document.querySelector('form');
form.addEventListener('submit', function() {
    // Show a loading indicator (e.g., "loading..." text, spinner)
    const submitButton = form.querySelector('button');
    submitButton.innerText = 'Loading...';
    submitButton.disabled = true; // Disable the button during processing
});
