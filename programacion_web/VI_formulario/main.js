const loginForm = document.getElementById("loginForm");

loginForm.addEventListener("submit", (event) => {
  event.preventDefault();

  const username = document.getElementById("username").value;
  const dpi = document.getElementById("dpi").value;
  const gender = document.getElementById("gender").value;

  const data = {
    "Nombre completo": username,
    DPI: dpi,
    Género: gender,
  };

  alert(JSON.stringify(data));
});
