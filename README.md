# JE23-FabricForecast-AI
GEN AI

🧵🌍 FabricForecast AI – Sustainable Textile Recommendation & Climate-Adaptive Fashion Agent
🧠 Project Idea
FabricForecast AI is an intelligent assistant that recommends eco-friendly and climate-adaptive fabrics and outfits for users based on weather, occasion, and sustainability preferences. It includes:

RAG-powered document Q&A from sustainability PDFs (e.g., textile reports).

A conversational AI fashion agent that suggests fabric blends (like hemp + cotton) for hot/humid or cold/dry conditions.

A wardrobe analyzer that flags unsustainable choices and suggests alternatives.

🔧 Features
Feature	Description
☀️ Climate-Aware Outfit Suggestion	Suggests breathable or insulating fabrics depending on user location and weather.
🌱 Sustainability Analyzer	Analyzes uploaded outfit/fabric image and suggests eco-friendly alternatives.
🧠 AI Agent for Fashion Advice	Conversational planner powered by Ollama to give climate/style advice.
📄 RAG PDF Insights	Users can upload fashion/climate whitepapers, and ask AI to summarize or answer questions from them.
📦 Wardrobe Health Score	Rates a wardrobe image/text list by sustainability and reusability.

# 🌿 FabricForecast AI – Climate-Aware Sustainable Fashion Advisor

FabricForecast AI is a local AI-powered fashion planner that analyzes your wardrobe, gives weather-adaptive style suggestions, and uses AI + RAG to make eco-conscious decisions.

## 🚀 Features
- Upload outfit/fabric image and get sustainability feedback
- Chat with AI for fashion tips based on current weather
- Upload sustainability reports and ask questions (RAG-based)
- Score your wardrobe and get climate-based suggestions

## 📦 How to Run (VS Code)

```bash
git clone https://github.com/yourname/FabricForecast-AI.git
cd FabricForecast-AI
pip install -r requirements.txt
ollama run tinyllama
streamlit run app.py
