var updateBtns = document.getElementsByClassName("update-cart");
for (var i = 0; i < updateBtns.length; i++) {
  updateBtns[i].addEventListener("click", function () {
    var productID = this.dataset.product;
    var action = this.dataset.action;

    console.log("productID:", productID, "Action:", action);
    console.log("USER:", user); // Debugging

    if (user == "AnonymousUser") {
      console.log("User is not logged in.");
    } else {
      updateUserOrder(productID, action);
    }
  });
}

function updateUserOrder(productID, action) {
  console.log("User is logged in , sending data....");

  var url = "/update_item/";
  fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify({
      productID: productID,
      Action: action,
    }),
  })
    .then((response) => {
      console.log("Response status:", response.status);
      return response.json();
    })
    .then((data) => {
      console.log("Data received:", data);
      window.location.reload();
    });
}
