document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('load-data-btn').addEventListener('click', function() {
        const email = document.getElementById('email-input').value;
        if (email) {
            fetch(`/generar_informe/${email}`)
                .then(response => {
                    if (!response.ok) {
                        if (response.status === 404) {
                            throw new Error('Persona no encontrada');
                        } else {
                            throw new Error('Error en la solicitud: ' + response.status);
                        }
                    }
                    return response.json();
                })
                .then(data => {
                    const tableBody = document.getElementById('informe-table-body');
                    tableBody.innerHTML = ''; // Limpiar tabla antes de cargar nuevos datos

                    if (data.length === 0) {
                        alert('No hay infracciones listadas para este correo electrónico.');
                    } else {
                        data.forEach(infraccion => {
                            const tr = document.createElement('tr');
                            tr.innerHTML = `
                                <td>${infraccion.placa_patente}</td>
                                <td>${infraccion.timestamp}</td>
                                <td>${infraccion.comentarios}</td>
                            `;
                            tableBody.appendChild(tr);
                        });
                    }
                })
                .catch(error => {
                    console.error('Error:', error);
                    alert(error.message);
                });
        } else {
            alert("Por favor, ingrese un correo electrónico.");
        }
    });
});
