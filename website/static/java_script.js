            //name: document.getElementById("name").value,
            //address: document.getElementById("address").value,
            //birthdate: document.getElementById("birthdate").value,
            //telephone: document.getElementById("telephone").value,
            //city: document.getElementById("city").value,
            //state: document.getElementById("state").value,
            //zipcode: document.getElementById("zipcode").value,
            //what_job: document.getElementById("what_job").value,
            //what_do: document.getElementById("what_do").value,
            //previous: document.getElementById("previous").value,
            //explain_why_fired:document.getElementById("explain_why_fired").value,


console.log("JS file loaded")
function form_submit(event){
    console.log("button clicked")
    event.preventDefault()
    fetch("/submit", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({"message": "form submitted"})
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
//debug from line 36 onward
fetch("/submit", {"debug test": "debug second part test"})
.then(res => {
    console.log("STATUS:", res.status);
    return res.text();   // temporarily use text
})
.then(data => {
    console.log("RAW RESPONSE:", data);
})
.catch(err => console.error(err));
}