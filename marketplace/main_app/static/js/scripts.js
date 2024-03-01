$(document).on('click', '#favorite', function() {
    const itemId = $(this).data('item-id');
    const type = $(this).data('vehicle-type');
    $.ajax({
        type: 'GET',
        url: '/ajax/',
        data: { pk: itemId, vehicle: type }, // Send the item ID to the view
        success: function(response) {
            changeImage(`myimage_${response.pk}`, response.image)
            console.log('Function executed successfully:', response.status);
        },
        error: function(error) {
            console.error('Error executing function:', error);
        }
    });
});

function changeImage(id, heart) {
    let image = document.getElementById(id)
    image.src = image.src.endsWith(heart) ? "/static/static_imgs/add-to-favorites-icon.svg" : heart;
    }
