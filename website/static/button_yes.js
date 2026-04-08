function yes() {
    fetch("/submit", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ answer:'yes'})
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("demo").innerHTML = data.message;
    });
}