document.addEventListener("DOMContentLoaded", () => {
  const fileInput = document.getElementById("pdfFile");
  const fileNameDisplay = document.querySelector(".file-name");
  const pdfIcon = document.querySelector(".pdf-icon");
  const form = document.getElementById("uploadForm");
  const resultDiv = document.getElementById("result");
  const loadingDiv = document.getElementById("loading");

  fileInput.addEventListener("change", function () {
    if (this.files.length > 0) {
      fileNameDisplay.textContent = this.files[0].name;
      pdfIcon.style.display = "inline-block";
    } else {
      fileNameDisplay.textContent = "";
      pdfIcon.style.display = "none";
    }
  });

  form.addEventListener("submit", function (event) {
    event.preventDefault();
    loadingDiv.style.display = "block";
    const formData = new FormData(this);

    fetch("/process", {
      method: "POST",
      body: formData,
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error(`Erro na resposta do servidor: ${response.statusText}`);
        }
        return response.json();
      })
      .then((data) => {
        resultDiv.innerText = data.result; // Exibe o resultado na "box"
        showNotification("Upload realizado com sucesso!", "success");
      })
      .catch((error) => {
        console.error("Erro:", error);
        resultDiv.innerText = "Ocorreu um erro ao processar o exame.";
        showNotification("Ocorreu um erro. Tente novamente.", "error");
      })
      .finally(() => {
        loadingDiv.style.display = "none";
      });
  });

  function showNotification(message, type) {
    const notification = document.createElement("div");
    notification.className = `notification ${type}`;
    notification.innerText = message;
    document.body.appendChild(notification);
    notification.style.display = "block";
    setTimeout(() => {
      notification.remove();
    }, 3000);
  }
});
