let fileInput = document.getElementById("file");
let fileList = document.getElementById("files-list");
let numOfFiles = document.getElementById("num-of-files");

fileInput.addEventListener("change", () => {
  fileList.innerHTML = "";
  numOfFiles.textContent = `${fileInput.files.length} File Selected`;

  for (i of fileInput.files) {
    let reader = new FileReader();
    let listItem = document.createElement("li");
    let fileName = i.name;
    let fileSize = (i.size / 1024).toFixed(1);
    listItem.innerHTML = `<p>${fileName}</p><p>${fileSize}KB</p>`;
    if (fileSize >= 1024) {
      fileSize = (fileSize / 1024).toFixed(1);
      listItem.innerHTML = `<p>${fileName}</p><p>${fileSize}MB</p>`;
    }
    fileList.appendChild(listItem);
  }
})
const form = document.getElementById("myForm");
form.addEventListener("submit", function(event) {
  const allowedExtensions = /(\.jpg|\.jpeg|\.png)$/i;
  if (!allowedExtensions.exec(fileInput.value)) {
    alert("Invalid file type. Please upload a JPG, JPEG, or PNG file.");
    event.preventDefault();
    return false;
  }
  // Form is valid, proceed with submission
});

function init() {
    var inputFile = document.getElementById('file');
    inputFile.addEventListener('change', mostrarImagen, false);
}
function mostrarImagen(event) {
    var file = event.target.files[0];
    var reader = new FileReader();
    reader.onload = function (event) {
        var img = document.getElementById('imagen');
        img.src = event.target.result;
        img.width = 150;
        img.height = 150;
    }
    reader.readAsDataURL(file);
}

window.addEventListener('load', init, false);