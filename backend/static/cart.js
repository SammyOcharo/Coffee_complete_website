var updateBtns = document.getElementsByClassName('update-cart')


for (var i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function() {
        var menuId = this.dataset.product
        var action = this.dataset.action
        console.log('menuId:', menuId, 'action:', action)

        console.log('USER:', user)

        if (user === 'AnonymousUser') {
            console.log('Not logged in')
        } else {
            updateUserOrder(menuId, action)
        }
    })
}

function updateUserOrder(menuId, action) {
    console.log('user is logged in sending data')

    var url = '/update_item/'

    fetch(url, {
        method: 'post',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken,

        },
        body: JSON.stringify({ 'menuId': menuId, 'action': action })
    })

    .then((response) => {
        return response.json()
    })

    .then((data) => {
        console.log('data:', data)
        location.reload()
    })
}