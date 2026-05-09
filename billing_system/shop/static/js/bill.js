/* ===============================
   PRODUCT SEARCH FUNCTION
================================*/

function searchProduct() {

let input = document.getElementById("searchInput");
let filter = input.value.toUpperCase();
let table = document.getElementById("productTable");
let tr = table.getElementsByTagName("tr");

for (let i = 1; i < tr.length; i++) {

let td = tr[i].getElementsByTagName("td")[0];

if (td) {

let txtValue = td.textContent || td.innerText;

if (txtValue.toUpperCase().indexOf(filter) > -1) {

tr[i].style.display = "";

} else {

tr[i].style.display = "none";

}

}

}

}



/* ===============================
   BILL TOTAL CALCULATION
================================*/

function calculateTotal() {

let prices = document.querySelectorAll(".price");
let qtys = document.querySelectorAll(".qty");

let subtotal = 0;

for(let i=0;i<prices.length;i++){

let price = parseFloat(prices[i].innerText);

let qty = parseInt(qtys[i].value);

if(!isNaN(qty)){

subtotal += price * qty;

}

}

document.getElementById("subtotal").innerText = subtotal.toFixed(2);

calculateGST();

}



/* ===============================
   GST CALCULATION
================================*/

function calculateGST(){

let subtotal = parseFloat(document.getElementById("subtotal").innerText);

let gst = parseFloat(document.getElementById("gst").value);

if(isNaN(gst)) gst = 0;

let gstAmount = subtotal * gst / 100;

let total = subtotal + gstAmount;

document.getElementById("gstAmount").innerText = gstAmount.toFixed(2);

document.getElementById("total").innerText = total.toFixed(2);

}



/* ===============================
   PRINT BILL
================================*/

function printBill(){

window.print();

}



/* ===============================
   DASHBOARD COUNTER ANIMATION
================================*/

function animateCounter(id, target){

let element = document.getElementById(id);

let count = 0;

let interval = setInterval(function(){

count++;

element.innerText = count;

if(count >= target){

clearInterval(interval);

}

},20);

}