document.addEventListener("DOMContentLoaded", function() {
    var imageInput = document.getElementById("image");
    var imageError = document.getElementById("image_error");
    var form = document.getElementById("feedbackForm");

    form.addEventListener('submit', function(event) {
        var hasError = false;

        // **Check if an image is uploaded first**
        if (imageInput.files.length === 0) {
            showImageError();
            event.preventDefault(); // Stop submission immediately
            return;
        }

        // **Validate other fields only if the image is valid**
        if (document.getElementById("author_name").value.trim() === "") {
            alert("Author name is required!");
            hasError = true;
        }
        else if (document.getElementById("text").value.trim() === "") {
            alert("Title is required!");
            hasError = true;
        }
        else if (document.getElementById("desc").value.trim() === "") {
            alert("Description is required!");
            hasError = true;
        }
        else if (document.getElementById("desc").value.trim().length > 250) {
            alert("Description should not exceed 250 characters!");
            hasError = true;
        }

        if (hasError) {
            event.preventDefault(); // Stop form submission if errors exist
        }
    });

    function showImageError() {
        imageError.innerText = "Please Upload an Image";
        imageError.style.color = "red";
        imageError.style.fontWeight = "bold";
        imageError.style.display = "block";
    }

    imageInput.addEventListener('change', function() {
        if (this.files.length > 0) {
            imageError.innerText = ""; // Remove error message
            imageError.style.display = "none";
        }
    });
});
