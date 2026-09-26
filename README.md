# 🌤️ Weather Assistant

An AI-powered **Weather Assistant** built using **Python, Groq LLM, OpenWeather API, and Gradio**.

The application uses **LLM tool calling** to understand a user's weather request, automatically call the `get_weather()` function, retrieve real-time weather information from OpenWeather, and generate a natural-language response.

## 🚀 Live Demo

🔗 **[Weather Assistant – Live Application](https://weatherassisstant.onrender.com/)**

## 📌 Features

* 🌍 Get current weather information for a city
* 🤖 AI-powered weather assistant using Groq
* 🔧 Function/tool calling with the Groq API
* 🌡️ Displays current temperature
* ☁️ Provides current weather description
* 📍 Identifies the requested location
* 🖥️ Simple and interactive Gradio interface
* 🔐 API keys securely stored using environment variables
* ☁️ Deployed on Render

## 🛠️ Technologies Used

* **Python**
* **Gradio**
* **Groq API**
* **OpenWeather API**
* **Requests**
* **python-dotenv**
* **Render**

## 🧠 How It Works

The application follows this workflow:

```text
User
  ↓
Gradio Interface
  ↓
Groq LLM
  ↓
Detects Weather Request
  ↓
get_weather() Tool
  ↓
OpenWeather API
  ↓
Weather Data
  ↓
Groq LLM
  ↓
Natural Language Response
  ↓
User
```

## 🔧 Tool Calling

The application exposes the following function to the LLM:

```python
get_weather(location)
```

The function retrieves weather information from the OpenWeather API.

The tool returns:

```json
{
    "location": "Hyderabad",
    "temperature": 28.5,
    "description": "clear sky"
}
```

The Groq model then uses this information to generate a user-friendly response.

## 💬 Example

### User Input

```text
What's the weather in Hyderabad?
```

### Assistant

```text
The current weather in Hyderabad is 28.5°C with clear sky.
```

## 📂 Project Structure

```text
WeatherAssisstant/
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

## 🔑 Environment Variables

Create a `.env` file locally:

```env
GROQ_API_KEY=your_groq_api_key
OPENWEATHER_API_KEY=your_openweather_api_key
```

⚠️ **Never upload your `.env` file to GitHub.**

The `.gitignore` file should contain:

```gitignore
.env
__pycache__/
```

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/jaswanthramadasappa-lab/WeatherAssisstant.git
```

Navigate into the project:

```bash
cd WeatherAssisstant
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Create your `.env` file and add your API keys.

Run the application:

```bash
python app.py
```

The Gradio application will start locally.

## ☁️ Deployment

This project is deployed using **Render**.

### Render Configuration

**Build Command:**

```bash
pip install -r requirements.txt
```

**Start Command:**

```bash
python app.py
```

The application uses Render's assigned port:

```python
demo.launch(
    server_name="0.0.0.0",
    server_port=int(os.environ.get("PORT", 7860))
)
```

## 🔐 Security

API keys are loaded using environment variables:

```python
from dotenv import load_dotenv
import os

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
```

API keys should **never be hardcoded or committed to GitHub**.

## 🎯 Project Objective

The main objective of this project is to understand how **Generative AI models can interact with external tools and APIs**.

This project demonstrates:

* LLM integration
* Function/tool calling
* API integration
* Environment variable management
* Gradio UI development
* Cloud deployment using Render

## 👨‍💻 Author

**R. Jaswanth**

B.Tech – Computer Science and Engineering
Madanapalle Institute of Technology and Science

### 🔗 Connect

* GitHub: [jaswanthramadasappa-lab](https://github.com/jaswanthramadasappa-lab)

## ⭐ Support

If you found this project useful, consider giving the repository a ⭐ on GitHub.
