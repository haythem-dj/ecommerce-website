let prices = document.querySelectorAll("[id='price']")
let quantityItems = document.querySelectorAll("[id='quantity']")
let totals = document.querySelectorAll("[id='total']")
let cartTotal = document.getElementById("cart-total")
let cartSubtotal = document.getElementById("cart-subtotal")
let shipping = document.getElementById("shipping")

for(let i = 0; i < quantityItems.length; i++) {
	quantityItems[i].addEventListener("change", e => {
		totals[i].innerText = e.target.value * parseInt(prices[i].innerText.split("$")[1])
		
		let cart_total = 0;
		for(let i = 0; i < totals.length; i++) {
			cart_total += parseInt(totals[i].innerText)
		}

		cartSubtotal.innerText = cart_total
		cartTotal.innerText = parseInt(cartSubtotal.innerText) + parseInt(shipping.innerText)
	})
}