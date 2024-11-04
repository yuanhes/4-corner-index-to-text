document.getElementById('translate_button').addEventListener('click', function() {
    const inputField = document.getElementById('number_input');
    const number = inputField.value.trim();

    if (!number) {
        alert("Please enter a valid number before clicking translate.");
        return;
    }

    // Proceed with the request to the backend if the input is valid
    // Add your existing fetch or AJAX logic here
});

