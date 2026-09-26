import os
import json
import requests
import gradio as gr
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")


def get_weather(location):
    """Get the current weather information for a given location."""

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": location,
        "appid": OPENWEATHER_API_KEY,
        "units": "metric"
    }

    response = requests.get(url, params=params)
    data = response.json()

    if response.status_code != 200:
        return {"error": "City not found"}

    return {
        "location": data["name"],
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"]
    }


tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get the current weather information for a location.",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "Name of the city or location"
                    }
                },
                "required": ["location"]
            }
        }
    }
]


def weather_assistant(location):

    if not location.strip():
        return "Please enter a city or location."

    messages = [
        {
            "role": "system",
            "content": (
                "You are a helpful weather assistant. "
                "Use the get_weather tool whenever the user asks "
                "about the weather of a location."
            )
        },
        {
            "role": "user",
            "content": f"What's the weather in {location}?"
        }
    ]

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=messages,
        tools=tools,
        tool_choice="auto"
    )

    assistant_message = response.choices[0].message

    if assistant_message.tool_calls:

        messages.append({
            "role": "assistant",
            "content": assistant_message.content,
            "tool_calls": [
                {
                    "id": tool_call.id,
                    "type": "function",
                    "function": {
                        "name": tool_call.function.name,
                        "arguments": tool_call.function.arguments
                    }
                }
                for tool_call in assistant_message.tool_calls
            ]
        })

        for tool_call in assistant_message.tool_calls:

            arguments = json.loads(
                tool_call.function.arguments
            )

            weather_result = get_weather(
                arguments["location"]
            )

            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": json.dumps(weather_result)
            })

        final_response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=messages
        )

        return final_response.choices[0].message.content

    return assistant_message.content


# -------------------------
# Gradio UI
# -------------------------

with gr.Blocks(title="Weather Assistant") as demo:

    gr.Markdown(
        """
        # 🌤️ Weather Assistant

        Ask about the current weather of any city using
        **Groq Tool Calling + OpenWeather API**.
        """
    )

    location = gr.Textbox(
        label="Enter City",
        placeholder="Example: Hyderabad",
        lines=1
    )

    get_weather_button = gr.Button(
        "🌦️ Get Weather"
    )

    output = gr.Textbox(
        label="Weather Information",
        lines=5
    )

    get_weather_button.click(
        fn=weather_assistant,
        inputs=location,
        outputs=output
    )

    location.submit(
        fn=weather_assistant,
        inputs=location,
        outputs=output
    )


demo.launch(
    server_name="0.0.0.0"
)