import Image from "next/image";
import FaqCard from "@/componentes_propios/faq/faq-card";
export default function Home() {
  return (
    <div>
      <header>
        <div class="container">
          <a href="#home" class="logo">
            <img src="./images/sharyommto-logo-audi.png" alt="SharyoMTTO Logo">
          </a>
          <button type="button" class="toggle">
            <img src="./images/barra-de-menus.png">
          </button>

          <nav>
            <ul>
              <li><a href="#home">Home</a></li>
              <li><a href="#servicios">Servicios</a></li>
              <li><a href="#preguntas-frecuentes">Preguntas Frecuentes</a></li>
              <li><a href="#nuestros-clientes">Nuestros clientes</a></li>
              <li><a href="#">Sign in</a></li>
              <li><a href="#" class="sign-up">Sign up</a></li>
            </ul>
          </nav>
        </div>
      </header>

      <section id="home" class="hero">
        <div class="container">
          <div class="hero-content">
            <h2>Encuentra el mejor lugar para seguimiento del mantenimiento de tu vehiculo <span>Facilmente</span></h2>


          </div>
          <div class="hero-image">
            <img src="./images/carro-moto-Imagen-.png" alt="Car">
          </div>
        </div>

      </section>

      <section class="how-it-works">
        <div class="container">
          <h2>Agenda tu servicio de mantenimiento en 3 pasos</h2>
          <div class="steps">
            <div class="step">
              <img src="./images/marcador-de-posicion.png" alt="Choose location">
                <h3>Elegi tu Localidad</h3>
                <p>Elegi la localidad donde realizar el servicio</p>
            </div>
            <div class="step">
              <img src="./images/fecha-del-calendario.png" alt="Pick-up date">
                <h3>Elegi una fecha</h3>
                <p>Seleciona la fecha y hora para realizar el mantenimiento de tu vehiculo</p>
            </div>
            <div class="step">
              <img src="./images/mantenimiento-del-automovil.png" alt="Book your car">
                <h3>Busca el taller mas cercano</h3>
                <p>Elegi el taller con las mejores calificaciones </p>
            </div>
          </div>
        </div>
      </section>

      <!-- Why Choose Us Section -->
      <section id="servicios" class="why-choose-us">
        <div class="container">
          <div class="why-choose-us-content">
            <div class="image">
              <img src="./images/Auto -moto-middle.png" alt="Car Image">
            </div>
            <div class="text">
              <h2>Porque Elegirnos</h2>
              <h3>Ofrecemos el mejor servicio de seguimiento del mantenimiento de tu vehiculo</h3>
              <ul>
                <li>
                  <div class="icon"><img src="./images/internet.png" alt="Icon"></div>
                  <div class="info">
                    <h4>Administrar tus vehiculos en la misma app</h4>
                    <p>Podes registrar varios vehiculos y llevar un control personalizado de los mismos</p>
                  </div>
                </li>
                <li>
                  <div class="icon"><img src="./images/agenda.png" alt="Icon"></div>
                  <div class="info">
                    <h4>Mantener el seguro de tu vehiculo siempre vigente</h4>
                    <p>Nosotros te enviaremos un recordatorio antes de la fecha del vencimiento</p>
                  </div>
                </li>
                <li>
                  <div class="icon"><img src="./images/investigacion.png" alt="Icon"></div>
                  <div class="info">
                    <h4>Estado del vehiculo 24 horas</h4>
                    <p>Revisa los datos de tus vehiculos en cualquier momento del dia. Siempre mantenemos los datos actualizados (consumo de combustible, kilometraje, proximos turnos de mantenimiento agendados)</p>
                  </div>
                </li>
                <li>
                  <div class="icon"><img src="./images/apoyo.png" alt="Icon"></div>
                  <div class="info">
                    <h4>Soporte tecnico 24/7</h4>
                    <p>Tenes alguna Pregunta? Contacta SharyoMTTO supporte en cualquier momento que tengas un problema.</p>
                  </div>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </section>

      <section id="nuestros-clientes" class="testimonials">
        <div class="container">
          <h2>Que dicen nuestros usuarios?</h2>
          <div class="testimonial-cards">
            <div class="testimonial-card">
              <img src="./images/testimonio1.png" alt="John Wilson">
                <p>5.0 stars</p>
                <img src="./images/5-estrellas.png" alt="5 estrellas">
                  <p>"Llevo un tiempo utilizando SharyoMTTO. El servicio es estupendo, seguiré utilizándolo."</p>
                  <p><strong>John Wilson</strong></p>
                  <p>From Bogota, Colombia</p>
                </div>
                <div class="testimonial-card">
                  <img src="./images/testimonio2.png" alt="Charlie Johnson">
                    <p>5.0 stars</p>
                    <img src="./images/5-estrellas.png" alt="5 estrellas">
                      <p>"Me siento muy seguro al utilizar los servicios SharyoMTTO. Se que en un solo click tengo toda la informacion de mis vehiculos."</p>
                      <p><strong>Charlie Johnson</strong></p>
                      <p>From Lima, Peru</p>
                    </div>
                    <div class="testimonial-card">
                      <img src="./images/testimonio3.png" alt="Anna Smith">
                        <p>5.0 stars</p>
                        <img class="estrellas" src="./images/5-estrellas.png" alt="5 estrellas">
                          <p>"El mejor servicio de seguimiento de mantenimiento de vehiculos que he utilizado hasta ahora. Excelente servicio, siempre recibo notificaciones y recordatorios para no perder ningun turno."</p>
                          <p><strong>Anna Smith</strong></p>
                          <p>From Buenos Aires, Argentina</p>
                        </div>
                    </div>
                </div>
              </section>
              <section id="preguntas-frecuentes" class="faq">
                <div class="container">
                  <h2>FAQ</h2>
                  <p>Aca tenemos algunas preguntas frecuentes de nuestros usuarios</p>
                  <div class="faq-items">
                    <div class="faq-item">
                      <div class="faq-icon">
                        <img src="./images/preguntas-frecuentes.png" alt="Icon">
                      </div>
                      <div class="faq-content">
                        <h3>¿Qué servicios ofrece SharyoMTTO para el registro y control de mis vehículos?</h3>
                        <p>SharyoMTTO te permite registrar todos tus vehículos, ya sean autos o motos, y llevar un control detallado de todos los documentos relacionados. Puedes almacenar información importante como el seguro del vehículo, la licencia de conducir, y otros documentos esenciales. Además, puedes registrar múltiples vehículos y gestionarlos todos desde una sola cuenta.</p>
                      </div>
                    </div>
                    <div class="faq-item">
                      <div class="faq-icon">
                        <img src="./images/pregunta-y-respuesta.png" alt="Icon">
                      </div>
                      <div class="faq-content">
                        <h3>¿Cómo puedo agendar turnos con mecánicos o talleres a través de SharyoMTTO?</h3>
                        <p>SharyoMTTO facilita la programación de turnos con diferentes mecánicos o talleres. Desde la sección "Agenda" de nuestra página web, puedes seleccionar el vehículo que necesita servicio, elegir el taller o mecánico de tu preferencia, y programar una cita en el calendario. Recibirás recordatorios y notificaciones para asegurarte de que no olvides tu cita.</p>
                      </div>
                    </div>
                    <div class="faq-item">
                      <div class="faq-icon">
                        <img src="./images/preguntas-frecuentes.png" alt="Icon">
                      </div>
                      <div class="faq-content">
                        <h3>¿Puedo llevar un control del kilometraje y el consumo de combustible de mis vehículos en SharyoMTTO?</h3>
                        <p>Sí, SharyoMTTO incluye herramientas para registrar y monitorear el kilometraje y el consumo de combustible de cada uno de tus vehículos. Puedes ingresar los datos cada vez que llenes el tanque y el sistema calculará el rendimiento del combustible, ayudándote a llevar un control eficiente y económico de tu vehículo.</p>
                      </div>
                    </div>
                    <div class="faq-item">
                      <div class="faq-icon">
                        <img src="./images/pregunta-y-respuesta.png" alt="Icon">
                      </div>
                      <div class="faq-content">
                        <h3>¿Qué debo hacer si tengo varios vehículos que quiero gestionar en SharyoMTTO?</h3>
                        <p>SharyoMTTO está diseñado para facilitar la gestión de múltiples vehículos. Puedes registrar cada uno de tus vehículos por separado y llevar un control individualizado de cada uno de ellos. Desde tu cuenta, puedes acceder a la información y los documentos de cada vehículo, programar mantenimientos, y monitorear el kilometraje y el consumo de combustible de forma sencilla. No hay límite en la cantidad de vehículos que puedes agregar.</p>

                      </div>
                    </div>
                  </div>
                </div>
              </section>



              <footer>
                <div class="container">
                  <div class="footer-section">
                    <h3>Contacto</h3>
                    <p>Dirección: Calle 123, Buenos Aires, Argentina</p>
                    <p>Teléfono: +123 456 7890</p>
                    <p>Email: contacto@sharyomtto.com</p>
                  </div>
                  <div class="footer-section">
                    <h3>Nuestros Productos</h3>
                    <ul>
                      <li><a href="#">Registro de Vehículos</a></li>
                      <li><a href="#">Control de Mantenimiento</a></li>
                      <li><a href="#">Seguimiento de Seguros</a></li>
                      <li><a href="#">Calendario</a></li>
                      <li><a href="#">Guía de Talleres</a></li>
                    </ul>
                  </div>
                  <div class="footer-section">
                    <h3>Recursos</h3>
                    <ul>
                      <li><a href="#">Guías de Usuario</a></li>
                      <li><a href="#">FAQs</a></li>
                      <li><a href="#">Centro de Ayuda</a></li>
                      <li><a href="#">Contacto</a></li>
                    </ul>
                  </div>
                  <div class="footer-section">
                    <h3>Seguínos</h3>
                    <ul class="social-media">
                      <li><a href="#"><img src="./images/facebook (1).png" alt="Facebook"></a></li>
                      <li><a href="#"><img src="./images/logotipos.png" alt="Twitter"></a></li>
                      <li><a href="#"><img src="./images/instagram (3).png" alt="Instagram"></a></li>
                    </ul>
                  </div>
                </div>
                <div class="footer-bottom">
                  <p>© 2023 SharyoMTTO. Todos los derechos reservados.</p>
                </div>
              </footer>
              <script src="./scripts.js"></script>
            </div>

            );
}
