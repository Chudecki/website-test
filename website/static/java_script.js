console.log("JS file loaded")

function form_submit(event){
    console.log("button clicked")
    event.preventDefault()

    const formData = {

        name: document.getElementById("name").value,
        address: document.getElementById("address").value,
        birthdate: document.getElementById("birthdate").value,
        telephone: document.getElementById("telephone").value,
        city: document.getElementById("city").value,
        state: document.getElementById("state").value,
        zipcode: document.getElementById("zipcode").value,
        what_job: document.getElementById("what_job").value,
        what_do: document.getElementById("what_do").value,
        previous: document.getElementById("previous").value,
        explain_why_fired: document.getElementById("explain_why_fired").value

    }

    fetch("/submit", {
    method: "POST",
    headers: { "Content-Type": "application/json" },

    //dont delete this it keeps the whole code intact spent like 20 mins on this its anoying... BALRIGHT
    body: JSON.stringify(formData)
})


.then(res => {
    if (!res.ok) {
        throw new Error("Server error");
    }
    return res.json();
})

.then(data => {
    document.getElementById("demo").innerHTML = data.message;
})

.catch(err => {
    console.error(err);
});
}