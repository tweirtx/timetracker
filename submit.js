
function submit() {
    const userID = document.getElementById("user_id").value;
    $.post('execute', {'user_id': userID}, function (data) {
        alert(data);
    });
}

document.addEventListener('readystatechange', addSubmit);

function addSubmit() {
    document.getElementById('idForm').addEventListener('submit', submit);
}
