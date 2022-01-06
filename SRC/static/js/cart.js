updateBtns = document.getElementsByClassName("update-cart")

for (let i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener("click", function () {
        let menuId = this.dataset.m
        let action = this.dataset.action

        if (user === "AnonymousUser"){
            console.log("Not authenticated!")
            updateAnonymousUserOrder(menuId, action)
            console.log("_______________________________________!")
        } else {
            updateUserOrder(menuId, action)
        }
    })
}

function updateUserOrder(menuId, action){
    console.log("authenticated! sending data ...")

    const url = "/update-item/";

    fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken":csrftoken,
        },
        body: JSON.stringify({"menuId":menuId, "action":action})
    })
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            console.log("Data: ", data)
            location.reload()
        });
}

function updateAnonymousUserOrder(menuId, action){
    console.log("not authenticated! sending data ...")

    const url = "/update-item/";

    fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken":csrftoken,
        },
        body: JSON.stringify({"menuId":menuId, "action":action})
    })
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            console.log("Data: ", data)
            location.reload()
        });
}
