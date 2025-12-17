async function getRecommendation() {
  const summary = document.getElementById("summary").value;

  const response = await fetch("http://127.0.0.1:5000/recommend", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ summary })
  });

  const data = await response.json();
  document.getElementById("result").innerText = data.recommendation;
}
