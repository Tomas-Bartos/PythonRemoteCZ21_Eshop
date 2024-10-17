// ** Autocomplete search bar **
$(document).ready(function () {
    // Add class inactive
    $('#search-input').closest('#search-form').addClass('inactive');

    // Remove class inactive when focused
    $('#search-input').on('focus', function () {
        $(this).closest('#search-form').removeClass('inactive');
        $('#suggestions').addClass('active');
    });

    // Add class inactive when out of focus
    $('#search-input').on('blur', function () {
        $(this).closest('#search-form').addClass('inactive');
        $('#suggestions').removeClass('active');
    });

    // Define currentIndex outside of the event functions to ensure global scope within this document ready function
    let currentIndex = -1;

    // When the user types in the search input field
    $('#search-input').on('input', function () {
        let query = $(this).val(); // Get the current input value
        currentIndex = -1;  // Reset the index when a new search is performed
        if (query.length > 1) {
            $.ajax({
                url: '/Eshop_app/product-autocomplete/',
                // Send the input as 'term' parameter
                data: {term: query},
                success: function (data) {
                    // Clear any previous suggestions
                    $('#suggestions').empty();
                    // Iterate over the returned data and add each item to the suggestions list
                    data.forEach(function (item) {
                        // Append each item as a new list element
                        $('#suggestions').append(`<li>${item}</li>`);
                    });
                }
            });
        } else {
            $('#suggestions').empty();
        }
    });

    // handle click on search suggestions
    $('#suggestions').on('click', 'li', function () {
        // remove (Kategorie) from url
        let selectedQuery = $(this).text().replace(' (Kategorie)', '');
        $('#search-input').val(selectedQuery);
        $('#search-form').submit();
    });

    // Handle keydown for arrow keys and Enter
    $('#search-input').on('keydown', function (e) {
        let items = $('#suggestions li');
        if (items.length === 0) return;

        if (e.key === 'ArrowDown') {
            currentIndex = (currentIndex + 1) % items.length;
            updateActiveItem(items);
        } else if (e.key === 'ArrowUp') {
            currentIndex = (currentIndex - 1 + items.length) % items.length;
            updateActiveItem(items);
        } else if (e.key === 'Enter') {
            e.preventDefault();
            if (currentIndex >= 0) {
                $(items[currentIndex]).click();
            }
        }
    });

    // add and remove .active
    function updateActiveItem(items) {
        items.removeClass('active');
        $(items[currentIndex]).addClass('active');
    }
});
// ** Autocomplete search bar END **


// ** Weather widget **
document.addEventListener("DOMContentLoaded", function () {
    // register at https://openweathermap.org/ get API key
    const apiKey = 'f4b0e35b03f1251b52af784a652c6435';

    // get and display weather
    function fetchWeather(lat, lon) {
        const url = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&units=metric&lang=cs&appid=${apiKey}`;
        fetch(url)
            .then(response => response.json())
            .then(data => {
                const temp = data.main.temp;
                const feelsLike = data.main.feels_like;
                const humidity = data.main.humidity;
                const windSpeed = data.wind.speed;
                const city = data.name;
                const country = data.sys.country;
                const pressure = data.main.pressure;

                // insert data into the widget
                const weatherDiv = document.getElementById('weather-widget');
                weatherDiv.innerHTML = `
                    <h6>Počasí pro ${city}, ${country}</h6><span></span>
                    <div>Teplota: <span>${temp} °C</span></div>
                    <div>Pocitová teplota: <span>${feelsLike} °C</span></div>
                    <div>Vlhkost: <span>${humidity} %</span></div>
                    <div>Tlak: <span>${pressure} hPa</span></div>
                    <div>Rychlost větru: <span>${windSpeed} m/s</span></div>
                `;
            })
            .catch(error => {
                console.error('Chyba při načítání počasí:', error);
                document.getElementById('weather-widget').innerText = 'Nepodařilo se načíst počasí.';
            });
    }

    // get user geolocation
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
            function (position) {
                const lat = position.coords.latitude;
                const lon = position.coords.longitude;
                fetchWeather(lat, lon);
            },
            function (error) {
                console.error('Chyba při získávání polohy:', error);
                document.getElementById('weather-widget').innerText = 'Nepodařilo se získat polohu.';
            }
        );
    } else {
        document.getElementById('weather-widget').innerText = 'Geolokace není podporována.';
    }
});
// ** Weather widget END **


// product added to the cart
$(document).ready(function () {
    $('.add_to_cart_form').submit(function (event) {
        event.preventDefault(); // prevent default form behavior

        const $form = $(this); // Ulož odkaz na aktuální formulář
        const productId = $form.find('input[name="product_id"]').val(); // Získá ID produktu z formuláře

        $.ajax({
            url: '/Eshop_app/add_to_cart/', // url for add to the cart
            type: 'POST',
            data: $(this).serialize(), // send all data from form
            headers: {
                'X-CSRFToken': '{{ csrf_token }}' // add CSRF token for django
            },
            success: function (response) {
                // remove div with message if already exists
                $form.find('.cart_message').remove();

                // create div with mesage
                const messageDiv = $('<div class="cart_message">' + response.message + '</div>');
                $form.append(messageDiv);

                // display message
                messageDiv.slideDown().delay(1000).slideUp(function () {
                    $(this).remove(); // remove after hiding the div
                });
            },
            error: function (xhr, status, error) {
                // alert("Nastala chyba: " + error); // error handler
                console.log('chyba je:', error);
            }
        });
    });
});
// ** product added to the cart END **
