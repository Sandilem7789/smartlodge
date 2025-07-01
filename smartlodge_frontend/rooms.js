fetch("http://127.0.0.1:8000/api/rooms/")
  .then(response => response.json())
  .then(data => {
    const container = document.getElementById("room-container");
    data.forEach(room => {
        const card = document.createElement("div");
        card.className = "card";

        const img = document.createElement("img");
        img.src = room.image?.trim() || "https://via.placeholder.com/400x250?text=No+Image"; // Fallback image if no image URL is provided
        img.style.width = "100%"; // Ensure the image fits the card
        img.alt = room.name;

        const title = document.createElement("h2");
        title.textContent = room.name;

        const desc = document.createElement("p");
        desc.textContent = room.description;

        const price = document.createElement("p");
        price.innerHTML = room.rate ? `<strong>R ${room.rate}</strong> per night`: "Price not available"; // Fallback if rate is not provided
        
        //Book Now Button
        const bookBtn = document.createElement("button");
        bookBtn.textContent = "Book Now";
        bookBtn.className = "book-now-btn";

        bookBtn.addEventListener("click", () => {
            document.getElementById("modal-room-name").textContent = `Booking: ${room.name}`;
            document.getElementById("booking-modal").classList.remove("hidden");

            // Optionally pre-fill or pass room info to form logic here
            });

        card.append(img, title, desc, price, bookBtn);
        card.append(img, title, desc, price, bookBtn);
        container.appendChild(card);
    });
})
.catch(error => {
     document.getElementById("room-container").textContent = "Failed to load rooms.";
    console.error(error);
});
// Close modal
document.getElementById("modal-close").addEventListener("click", () => {
    document.getElementById("booking-modal").classList.add("hidden");
});

// Handle form submit
document.getElementById("booking-form").addEventListener("submit", (e) => {
    e.preventDefault();
    const name = document.getElementById("guestName").value;
    const checkIn = document.getElementById("checkIn").value;
    const checkOut = document.getElementById("checkOut").value;
    alert(`Thanks, ${name}! Booking submitted from ${checkIn} to ${checkOut}.`);
    document.getElementById("booking-modal").classList.add("hidden");
});
