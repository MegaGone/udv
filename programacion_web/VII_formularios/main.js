/* SESIÓN */
const validateSession = () => {
  // "True"
  const isAuthenticated = localStorage.getItem("AUTHENTICATED");

  if (!isAuthenticated) {
    return (location.href = "/");
  }
};

const closeSession = () => {
  location.href = "/";
  localStorage.removeItem("AUTHENTICATED");
};

/* INICIO DE SESIÓN */
if (location.pathname === "/" || location.pathname === "/index.html") {
  const baseUsername = "202302745";
  const basePassword = "P@sswo0rd,2024!";

  document.getElementById("username").value = baseUsername;
  document.getElementById("password").value = basePassword;

  const spinner = document.getElementById("spinner");
  spinner.style.display = "none";

  const loginForm = document.getElementById("loginForm");
  loginForm.addEventListener("submit", (event) => {
    event.preventDefault();

    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    if (username !== baseUsername || password !== basePassword)
      return alert("Usuario/Contraseña no válido.");

    const button = document.getElementById("button");
    button.style.display = "none";
    spinner.style.display = "block";

    setTimeout(() => {
      button.style.display = "block";
      spinner.style.display = "none";

      // SESIÓN
      localStorage.setItem("AUTHENTICATED", "True");

      location.href = "usuarios.html";
    }, 2000);
  });
}

/* CREAR USUARIO */
if (location.href.includes("usuarios.html")) {
  validateSession();

  const usersSpinner = document.getElementById("users-spinner");
  usersSpinner.style.display = "none";

  const usersForm = document.getElementById("usersForm");
  usersForm.addEventListener("submit", (event) => {
    event.preventDefault();

    let name = document.getElementById("name").value;
    let username = document.getElementById("username").value;
    let password = document.getElementById("password").value;

    if (!name || !username || !password) return alert("Campos requeridos.");

    const usersButton = document.getElementById("users-button");
    usersButton.style.display = "none";
    usersSpinner.style.display = "block";

    setTimeout(() => {
      usersButton.style.display = "block";
      usersSpinner.style.display = "none";
      usersForm.reset();

      alert("Usuario registrado exitósamente.");
    }, 2000);
  });
}

/* CREAR PRODUCTO */
if (location.href.includes("productos.html")) {
  validateSession();

  const productsSpinner = document.getElementById("products-spinner");
  productsSpinner.style.display = "none";

  const productsForm = document.getElementById("productsForm");
  productsForm.addEventListener("submit", (event) => {
    event.preventDefault();

    let code = document.getElementById("code").value;
    let description = document.getElementById("description").value;

    if (!code || !description) return alert("Campos requeridos.");

    const productsButton = document.getElementById("products-button");
    productsButton.style.display = "none";
    productsSpinner.style.display = "block";

    setTimeout(() => {
      productsButton.style.display = "block";
      productsSpinner.style.display = "none";
      productsForm.reset();

      alert("Producto registrado exitósamente.");
    }, 2000);
  });
}
