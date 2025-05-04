async function sendMessage() {
    const message = document.getElementById("userInput").value;

    const response = await fetch("http://localhost:5000/chat", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ message })
    });

    const data = await response.json();
    document.getElementById("chatLog").innerHTML += `<p><strong>Você:</strong> ${message}</p>`;
    document.getElementById("chatLog").innerHTML += `<p><strong>Bot:</strong> ${data.response}</p>`;
  }