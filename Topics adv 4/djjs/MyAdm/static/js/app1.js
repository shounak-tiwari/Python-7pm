document.addEventListener('DOMContentLoaded', function () {
    function run() {
        let name_inp = document.getElementById('name_inp').value;
        let regex = /^[a-zA-Z ]{0,30}$/;

        if (regex.test(name_inp)) {
            // alert('Error: Please enter a valid name (2-30 characters, letters and spaces only).');
            console.log("ge")
        } else {
            alert('not  Valid name entered!');
            document.getElementById("name_inp").value = ""
        }
    }

    console.log("hello");
    document.getElementById('name_inp').addEventListener("input", run);
});


run()