var noteId;

function openModal(button) {
  var modal = document.getElementById("noteModal");
  var title = button.getAttribute("data-title");
  var description = button.getAttribute("data-description");
  var date = button.getAttribute("data-date");

  document.getElementById("modal-title").innerText = title;
  // Set the description as HTML content using innerHTML
  document.getElementById("modal-description").innerHTML = description;
  document.getElementById("modal-date").innerText = date;

  modal.style.display = "block";
}

function closeModal() {
  document.getElementById("noteModal").style.display = "none";
}

function editNote() {
  // Add functionality to edit note here
}
function deleteNote(button) {
  noteId = button.getAttribute("data-id");
  // Store the note ID in a global variable for later use
  window.currentNoteId = noteId;
  openDeleteModal();
}

function openDeleteModal() {
  document.getElementById("deleteNoteModal").style.display = "block";
}
function closeDeleteModal() {
  document.getElementById("deleteNoteModal").style.display = "none";
}

function closeModal() {
  const modal = document.getElementById('noteModal');
  modal.style.display = 'none';

  // Exit fullscreen mode if currently in fullscreen
  if (document.fullscreenElement) {
      document.exitFullscreen();
  }
}
function confirmDelete() {
  // Get the note ID from the global variable
  var noteId = window.currentNoteId;

  fetch(`/notes/${noteId}/delete`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRF-TOKEN": getCsrfToken(),
    },
  })
    .then((response) => {
      if (response.ok) {
        // Reload the page or update the UI as needed
        location.reload();
      } else {
        console.error("Error deleting note:", response.statusText);
        // Handle error (e.g., display an error message to the user)
      }
    })
    .catch((error) => {
      console.error("Error deleting note:", error);
      // Handle error (e.g., display an error message to the user)
    });

  // Close the modal after confirming deletion
  closeDeleteModal();
}

function getCsrfToken() {
  var csrfTokenElement = document.querySelector("meta[name='_csrf']");
  return csrfTokenElement ? csrfTokenElement.getAttribute("content") : null;
}
function toggleFullScreen(button) {
  const modalContent = button.parentElement;
  if (!document.fullscreenElement) {
      modalContent.requestFullscreen().catch(err => {
          alert(`Error attempting to enable full-screen mode: ${err.message} (${err.name})`);
      });
  } else {
      document.exitFullscreen();
  }
}
