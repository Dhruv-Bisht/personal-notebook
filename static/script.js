// Auto-resize textarea
const textarea = document.querySelector('textarea');
if (textarea) {
    textarea.addEventListener('input', () => {
        textarea.style.height = 'auto'; // Reset height
        textarea.style.height = textarea.scrollHeight + 'px'; // Set new height
    });
}

// Confirm before adding a note
const form = document.querySelector('form');
if (form) {
    form.addEventListener('submit', (e) => {
        const noteContent = textarea.value.trim();
        if (!noteContent) {
            e.preventDefault();
            alert("Please write something before saving!");
            return;
        }
        // Optional: confirm action
        const confirmSave = confirm("Do you want to save this note?");
        if (!confirmSave) {
            e.preventDefault();
        }
    });
}
