// Загрузка списка стран при загрузке страницы
$(document).ready(function() {
    $.ajax({
        url: 'http://localhost:8000/sync/country_currency', // URL на сервере для получения списка стран
        method: 'GET',
        success: function(response) {
            response.forEach(function(country) {
                $('#countries').append(new Option(country.name, country.code));
            });
        },
        error: function(error) {
            alert('Произошла ошибка при загрузке списка стран.');
        }
    });
});

// Обработка формы синхронизации данных
$('#syncForm').on('submit', function(event) {
    event.preventDefault();
    const startDate = $('#startDate').val();
    const endDate = $('#endDate').val();
    
    $.ajax({
        url: 'http://localhost:8000/sync/relative_change', // URL на сервере для обработки синхронизации данных
        method: 'POST',
        data: { startDate, endDate },
        success: function(response) {
            alert('Данные успешно синхронизированы!');
        },
        error: function(error) {
            alert('Произошла ошибка при синхронизации данных.');
        }
    });
});

// Обработка формы и отображение графика
$('#relativeChangesForm').on('submit', function(event) {
    event.preventDefault();
    const countries = $('#countries').val();
    const startDate = $('#relativeStartDate').val();
    const endDate = $('#relativeEndDate').val();
    
    $.ajax({
        url: 'http://localhost:8000/sync/relative-changes', // URL на сервере для получения относительных изменений курсов
        method: 'POST',
        data: { countries, startDate, endDate },
        success: function(response) {
            // Отображение графика с использованием Chart.js
            const ctx = document.getElementById('relativeChangesChart').getContext('2d');
            const chart = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: response.dates,
                    datasets: response.data
                },
                options: {
                    responsive: true,
                    title: {
                        display: true,
                        text: 'Относительные изменения курсов валют'
                    }
                }
            });
        },
        error: function(error) {
            alert('Произошла ошибка при загрузке данных.');
        }
    });
});
