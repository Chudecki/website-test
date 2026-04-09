function form_submit(form_event){
    form_event.preventDefault()
    fetch("/submit", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({

            name: document.getElementById("name").value,
            address: document.getElementById("address").value,
            birthdate: document.getElementById("birthdate").value,
            telephone: document.getElementById("telephone").value,
            city: document.getElementById("city").value,
            state: document.getElementById("state").value,
            zip: document.getElementById("zip").value,
            what_job: document.getElementById("what_job").value,
            what_do: document.getElementById("what_do").value,
            previous: document.getElementById("previous").value,
            explain_why_fired:document.getElementById("explain_why_fired").value,
        })
    })
    .then(res => res.json())
    .then(data => {
        document.getElementById("demo").innerHTML = data.message;
    });
}


