// Sustainable Smartcity Assistant - main.js
// Handles all form submissions via fetch to backend API

const API_BASE = 'http://localhost:8000';

function showToast(message) {
  let toast = document.getElementById('toast');
  if (!toast) {
    toast = document.createElement('div');
    toast.id = 'toast';
    toast.className = 'toast';
    document.body.appendChild(toast);
  }
  toast.textContent = message;
  toast.style.display = 'block';
  setTimeout(() => { toast.style.display = 'none'; }, 2500);
}

// Chat form
const chatForm = document.getElementById('chat-form');
if (chatForm) {
  chatForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const prompt = chatForm.prompt.value;
    const respDiv = document.getElementById('chat-response');
    respDiv.textContent = 'Thinking...';
    try {
      console.log(API_BASE);
      
      const res = await fetch(`${API_BASE}/chat/ask`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ prompt })
      });
      const data = await res.json();
      respDiv.textContent = data.response || 'No response.';
      showToast('Message sent!');
    } catch (err) {
      respDiv.textContent = 'Error contacting assistant.';
      showToast('Error!');
    }
  });
}

// Upload form
const uploadForm = document.getElementById('upload-form');
if (uploadForm) {
  uploadForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const fileInput = uploadForm.file;
    const summaryDiv = document.querySelector('.summary-content');
    const anomalyAlert = document.getElementById('anomaly-alert');
    summaryDiv.textContent = 'Uploading...';
    anomalyAlert.style.display = 'none';
    const formData = new FormData();
    formData.append('file', fileInput.files[0]);
    try {
      const res = await fetch(`${API_BASE}/upload`, {
        method: 'POST',
        body: formData
      });
      const data = await res.json();
      summaryDiv.textContent = data.summary || 'No summary.';
      if (data.anomalies && data.anomalies.length > 0) {
        anomalyAlert.style.display = 'block';
        anomalyAlert.querySelector('.anomaly-message').textContent = 'Anomalies found in uploaded data.';
      } else {
        anomalyAlert.style.display = 'none';
      }
      showToast('File uploaded!');
    } catch (err) {
      summaryDiv.textContent = 'Error uploading file.';
      showToast('Error!');
    }
  });
}

// KPI form
const kpiForm = document.getElementById('city-form');
if (kpiForm) {
  kpiForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const city = kpiForm.city.value;
    const waterDiv = document.getElementById('water-usage');
    const airDiv = document.getElementById('air-quality');
    const energyDiv = document.getElementById('energy-usage');
    waterDiv.textContent = airDiv.textContent = energyDiv.textContent = 'Loading...';
    try {
      // For demo, use /vector-search as a mock (replace with real /kpi endpoint if available)
      const res = await fetch(`${API_BASE}/vector-search`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ query: city })
      });
      const data = await res.json();
      // Mock: just show the city name in all fields
      waterDiv.textContent = `${city} Water: 123`;
      airDiv.textContent = `${city} Air: Good`;
      energyDiv.textContent = `${city} Energy: 456 kWh`;
      showToast('KPI data loaded!');
    } catch (err) {
      waterDiv.textContent = airDiv.textContent = energyDiv.textContent = 'Error.';
      showToast('Error!');
    }
  });
}

// Tips form
const tipsForm = document.getElementById('tips-form');
if (tipsForm) {
  tipsForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const keyword = tipsForm.keyword.value;
    const resultsDiv = document.getElementById('tips-results');
    resultsDiv.textContent = 'Searching...';
    try {
      const res = await fetch(`${API_BASE}/search-tips`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ keyword })
      });
      const data = await res.json();
      if (data.tips && data.tips.length > 0) {
        resultsDiv.innerHTML = '<ul>' + data.tips.map(tip => `<li>${tip}</li>`).join('') + '</ul>';
      } else {
        resultsDiv.textContent = 'No tips found.';
      }
      showToast('Search complete!');
    } catch (err) {
      resultsDiv.textContent = 'Error searching tips.';
      showToast('Error!');
    }
  });
}

// Feedback form
const feedbackForm = document.getElementById('feedback-form');
if (feedbackForm) {
  feedbackForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const formData = new FormData(feedbackForm);
    try {
      const res = await fetch(`${API_BASE}/feedback`, {
        method: 'POST',
        body: formData
      });
      const data = await res.json();
      showToast(data.message || 'Feedback submitted!');
      feedbackForm.reset();
    } catch (err) {
      showToast('Error!');
    }
  });
} 