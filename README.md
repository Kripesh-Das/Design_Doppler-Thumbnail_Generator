# 🎨 ADK Thumbnail Generator

Welcome to **ADK Thumbnail Generator** — an intelligent, modular tool for analyzing and generating high-impact YouTube thumbnails using state-of-the-art AI and automation.

---

## ✨ Features

- **AI-Powered Thumbnail Analysis**  
  Evaluate and score thumbnails for engagement, clarity, and relevance.

- **Automated Thumbnail Generation**  
  Instantly create new, visually appealing thumbnails tailored to your content.

- **Multi-Agent Architecture**  
  Easily extend and customize with modular agents for different tasks.

- **Seamless API Integrations**  
  Works with Google GenAI, OpenAI, and YouTube Data APIs.

- **Secure & Configurable**  
  All sensitive settings are managed via environment variables.

---

## 🗂️ Project Structure

```
ADK-Thumbnail_Generater/
│
├── youtube_thumbnail_agent/
│   ├── subagents/
│   │   └── thumbnail_analyzer_agent/
│   │       ├── agent.py
│   │       └── __init__.py
│   ├── constants.py
│   └── .env
│
├── requirements.txt
└── README.md
```

---

## ⚡ Quickstart

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/ADK-Thumbnail_Generater.git
   cd ADK-Thumbnail_Generater
   ```

2. **Set up your environment**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Configure your API keys**  
   Edit `youtube_thumbnail_agent/.env` with your credentials:
   ```properties
   GOOGLE_GENAI_USE_VERTEXAI=FALSE
   GOOGLE_API_KEY=your-google-api-key
   OPENAI_API_KEY=your-openai-api-key
   YOUTUBE_API_KEY=your-youtube-api-key
   ```
   > **Never share your API keys publicly!**

4. **Run the agent**
   ```bash
   python -m youtube_thumbnail_agent
   ```
   *(Replace with your actual entry point if different)*

---

## 🛠️ Customization

- **Add new agents:**  
  Place new agent modules in `subagents/` and register them in your workflow.

- **Change constants:**  
  Edit `constants.py` for directory paths and other settings.

- **Integrate new APIs:**  
  Add keys to `.env` and update your agent logic.

---

## 🤝 Contributing

Pull requests and issues are welcome!  
Please follow best practices and respect the privacy of API credentials.

---

## 📄 License

Licensed under the [MIT License](LICENSE).

---

## 📢 Disclaimer

- **Keep your API keys secret!**
- This project is for educational and research purposes only.
- Use responsibly and comply with all relevant API terms of service.

---

## 💬 Contact

For questions or suggestions, open an issue or contact the maintainer.

---
