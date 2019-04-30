
function submit() {
    alert("Test");
}

document.addEventListener('readystatechange', addSubmit);

function addSubmit() {
    document.getElementById('idForm').addEventListener('submit', submit);
}
