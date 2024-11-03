/*=============== MOSTRAR MENU ===============*/
const navMenu = document.getElementById("nav-menu"),
  navToggle = document.getElementById("nav-toggle"),
  navClose = document.getElementById("nav-close");

if (navToggle) {
  navToggle.addEventListener("click", () => {
    navMenu.classList.add("show-menu");
  });
}

/*===== CERRAR MENU =====*/
if (navClose) {
  navClose.addEventListener("click", () => {
    navMenu.classList.remove("show-menu");
  });
}

/*=============== OCULTAR MENU MÓVIL ===============*/
const navLink = document.querySelectorAll(".nav__link");

const linkAction = () => {
  const navMenu = document.getElementById("nav-menu");
  navMenu.classList.remove("show-menu");
};
navLink.forEach((n) => n.addEventListener("click", linkAction));

const shadowHeader = () => {
  const header = document.getElementById("header");
  this.scrollY >= 50
    ? header.classList.add("shadow-header")
    : header.classList.remove("shadow-header");
};
window.addEventListener("scroll", shadowHeader);

const scrollUp = () => {
  const scrollUp = document.getElementById("scroll-up");
  this.scrollY >= 350
    ? scrollUp.classList.add("show-scroll")
    : scrollUp.classList.remove("show-scroll");
};
window.addEventListener("scroll", scrollUp);

/*=============== SECCIONES CON ANIMACIONES ===============*/
const sections = document.querySelectorAll("section[id]");

const scrollActive = () => {
  const scrollDown = window.scrollY;

  sections.forEach((current) => {
    const sectionHeight = current.offsetHeight,
      sectionTop = current.offsetTop - 58,
      sectionId = current.getAttribute("id"),
      sectionsClass = document.querySelector(
        ".nav__menu a[href*=" + sectionId + "]"
      );

    if (scrollDown > sectionTop && scrollDown <= sectionTop + sectionHeight) {
      sectionsClass.classList.add("active-link");
    } else {
      sectionsClass.classList.remove("active-link");
    }
  });
};
window.addEventListener("scroll", scrollActive);

/*=============== CONFIGURACIÓN DE ANIMACIONES ===============*/
const sr = ScrollReveal({
  origin: "top",
  distance: "60px",
  duration: 2500,
  delay: 400,
});

sr.reveal(`.home__perfil, .about__image, .contact__mail`, { origin: "right" });
sr.reveal(
  `.home__name, .home__info, 
            .about__container .section__title-1, .about__info, 
            .contact__social, .contact__data`,
  { origin: "left" }
);
sr.reveal(`.services__card, .projects__card`, { interval: 100 });

/*=============== VALIDACIONES DE FORMULARIO ===============*/
/* NÚMERO DE TELÉFONO */
function onlyNumbers(event) {
  const key = event.key;
  const input = event.target;

  if (key === "Backspace" || key === "Delete" || key === "Tab") return true;

  if (key >= "0" && key <= "9") {
    if (input.value.length < 8) {
      return true;
    } else {
      event.preventDefault();
      return false;
    }
  }

  event.preventDefault();
  document.getElementById("phone-error-message").style.display = "block";
  setTimeout(() => {
    document.getElementById("phone-error-message").style.display = "none";
  }, 2000);
  return false;
}

/* CORREO ELECTRÓNICO */
function validateEmail() {
  const emailInput = document.getElementById("email");
  const errorMessage = document.getElementById("email-error-message");

  const emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;

  if (!emailPattern.test(emailInput.value)) {
    errorMessage.style.display = "block";
    emailInput.setCustomValidity("");
  } else {
    errorMessage.style.display = "none";
    emailInput.setCustomValidity("");
  }
}

/* FECHA DE ENTREGA */
const dateTimeInput = document.getElementById("date_time");
const errorMessage = document.getElementById("date-time-error-message");

dateTimeInput.addEventListener("change", function () {
  const selectedDateTime = new Date(this.value);
  const now = new Date();

  now.setSeconds(0);
  now.setMilliseconds(0);
  now.setHours(now.getHours() + 1);

  if (selectedDateTime < now) {
    errorMessage.style.display = "block";
    this.value = "";
  } else {
    errorMessage.style.display = "none";
  }
});

/* DIRECCION DE ENTREGA */
const data = {
  "Alta Verapaz": ["Cobán", "San Pedro Carcha", "Santa Cruz Verapaz"],
  "Baja Verapaz": ["Salamá", "Rabinal", "Granados"],
  Chimaltenango: ["Chimaltenango", "San Martín Jilotepeque", "Sumpango"],
  Chiquimula: ["Chiquimula", "San José La Arada", "Esquipulas"],
  "El Progreso": [
    "Guastatoya",
    "San Agustín Acasaguastlán",
    "San Antonio La Paz",
  ],
  Escuintla: ["Escuintla", "Santa Lucía Cotzumalguapa", "La Democracia"],
  Guatemala: ["Guatemala", "Mixco", "Villa Nueva", "San Miguel Petapa"],
  Huehuetenango: ["Huehuetenango", "La Libertad", "Cuilco"],
  Izabal: ["Puerto Barrios", "Morales", "Los Amates"],
  Jalapa: ["Jalapa", "San Pedro Jocopilas", "Mataquescuintla"],
  Jiménez: ["San José", "San Sebastián", "Santa Ana"],
  Petén: ["Flores", "Santa Elena", "San Benito"],
  Quetzaltenango: ["Quetzaltenango", "Salcajá", "San Carlos Sija"],
  Quiché: ["Santa Cruz del Quiché", "Chichicastenango", "Patzité"],
  Retalhuleu: ["Retalhuleu", "San Sebastián", "San Martín Zapotitlán"],
  Sacatepéquez: ["Antigua Guatemala", "San Lucas Sacatepéquez", "Pastores"],
  "San Marcos": ["San Marcos", "Tejutla", "San Pedro Sacatepéquez"],
  "Santa Rosa": ["Santa Rosa de Lima", "Cuilapa", "San Juan Tecuaco"],
  Solalá: ["Solalá", "San José Chacaya", "Santa Clara La Laguna"],
  Suchitepéquez: ["Mazatenango", "San Francisco Zapotitlán", "Zunilito"],
  Totonicapán: ["Totonicapán", "San Cristóbal Totonicapán", "Santa Lucía"],
  Zacapa: ["Zacapa", "La Unión", "Estanzuela"],
};

const departmentSelect = document.getElementById("department");
const municipalitySelect = document.getElementById("municipality");

function loadDepartments() {
  Object.keys(data).forEach((department) => {
    const option = document.createElement("option");
    option.value = department;
    option.textContent = department;
    departmentSelect.appendChild(option);
  });
}

function loadMunicipalities(department) {
  municipalitySelect.innerHTML =
    '<option value="" disabled selected>Municipio</option>';

  data[department].forEach((municipality) => {
    const option = document.createElement("option");
    option.value = municipality;
    option.textContent = municipality;
    municipalitySelect.appendChild(option);
  });
}

departmentSelect.addEventListener("change", function () {
  loadMunicipalities(this.value);
});

loadDepartments();

/* AGREGAR PRODUCTOS */
const productsToBuy = JSON.parse(localStorage.getItem("localProducts")) || [];
const products = [
  {
    id: 1,
    producto: "Pintura aceite",
    precio: 44.5,
  },
  {
    id: 2,
    producto: "Martillo mango de madera",
    precio: 55.5,
  },
  {
    id: 3,
    producto: "Taladro Lion",
    precio: 250.0,
  },
  {
    id: 4,
    producto: "Ventana de PVC 1.50 x 1.00 m",
    precio: 665.0,
  },
  {
    id: 5,
    producto: "Escalera de aluminio 19.4",
    precio: 1525.0,
  },
];

const onAddProduct = (id) => {
  const product = products.find((p) => p.id == id);
  if (!product) return;

  productsToBuy.push(product);
  localStorage.setItem("localProducts", JSON.stringify(productsToBuy));
  alert("Se agregó un producto al carrito.");
  renderProducts();
};

const renderProducts = () => {
  const purchaseDetails = document.getElementById("purchase-details");
  purchaseDetails.innerHTML = "";

  const list = document.createElement("ul");

  productsToBuy.forEach((product) => {
    const productElement = document.createElement("li");
    productElement.textContent = `${
      product.producto
    } - Q ${product.precio.toFixed(2)}`;
    list.appendChild(productElement);
  });

  purchaseDetails.appendChild(list);
};

renderProducts();

/* REMOVER PRODUCTOS */
const onCleanProducts = () => {
  const existsInStorage = localStorage.getItem("localProducts");
  if (!existsInStorage) return;

  localStorage.removeItem("localProducts");
  renderProducts();

  alert("Se removieron los productos del carrito.");
  window.location.reload();
};

/* CONFIRMAR ORDEN */
const form = document.getElementById("contact-form");
form.addEventListener("submit", (event) => {
  if (!productsToBuy || !productsToBuy?.length) {
    alert("Debe agregar productos al carrito.");
    return;
  }

  const value = Object.values(form).reduce((obj, field) => {
    obj[field.name] = field.value;
    return obj;
  }, {});

  event.preventDefault();
  localStorage.removeItem("localProducts");
  window.location.reload();
});
