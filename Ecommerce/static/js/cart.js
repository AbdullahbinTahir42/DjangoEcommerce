for (var i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener("click", function () {
        var productID = this.dataset.product;
        var action = this.dataset.action;

        console.log("productID:", productID, "Action:", action);
        console.log("USER:", user); // Debugging

        if (user == "AnonymousUser") {
            console.log("User is not logged in.");
        } else {
            console.log("User is logged in:", user);
        }
    });
}


function updateUserOrder(productID,action)
{
    console.log("User is logged in , sending data....")

    var url = '/update_item/'
    fetch(url, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body:JSON.stringify({
            'productID ' : productID,
            'action ' : action 
        })
})
 .then((response)=>{
    return response.json()
 })
    
 .then((data)=>{
    console.log('Data : ', data)
 })
    }
