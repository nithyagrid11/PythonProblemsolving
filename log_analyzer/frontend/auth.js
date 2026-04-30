async function registerUser() {
    const username = document.getElementById("username").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;

    const response = await fetch(
        "http://127.0.0.1:8001/register",
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                username,
                email,
                password
            })
        }
    );

    const data = await response.json();

    alert(data.message || data.detail);

    if (response.ok) {
        window.location.href = "login.html";
    }
}


async function loginUser() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    const formData = new URLSearchParams();
    formData.append("username", username);
    formData.append("password", password);

    const response = await fetch(
        "http://127.0.0.1:8001/login",
        {
            method: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded"
            },
            body: formData
        }
    );

    const data = await response.json();

    if (response.ok) {
        localStorage.setItem(
            "token",
            data.access_token
        );

        alert("Login successful");

        window.location.href = "index.html";
    } else {
        alert(data.detail);
    }
}