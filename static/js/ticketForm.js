function addCustomer() {
    const customerList = document.getElementById('customerList');

    const customerEntry = document.createElement('div');
    customerEntry.classList.add('customer-entry');

    customerEntry.innerHTML = `
        <label>Customer Name:</label>
        <input type="text" name="customer_name[]" placeholder="Enter Full Name" required>
        <label>Age Category:</label>
        <select name="age_category[]" required>
            <option value="Adult">Adult</option>
            <option value="Child">Child</option>
        </select>
        <button type="button" class="remove-customer" onclick="removeCustomer(this)">Remove</button>
    `;
    customerList.appendChild(customerEntry);
}

function removeCustomer(button) {
    const customerEntry = button.parentElement;
    customerEntry.remove();
}
