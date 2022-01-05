updateBtns = document.getElementsByClassName("update-food")
let numbers = document.getElementsByClassName("number")

for (let i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener("click", function () {
        let foodId = updateBtns[i].value
        console.log("food ID: ", foodId)
        let mo_number = numbers[i]
        if (user === "AnonymousUser"){
            console.log("Not authenticated!")
        } else {
            updateUserOrder(foodId, mo_number.value)
            console.log("UPDATED!!!")
            console.log(numbers[i].value)
        }
    })
}

function updateUserOrder(foodId, number){
    console.log("authenticated! sending data ...")

    const url = "/cart-update/";

    fetch(url, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken":csrftoken,
        },
        body: JSON.stringify({"foodId":foodId, "number":number})
    })
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            console.log("Data: ", data)
            window.location.reload();
        });
}
