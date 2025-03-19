from django.shortcuts import render

import google.generativeai as genai
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.conf import settings

# Configure the Gemini API
genai.configure(api_key=settings.GEMINI_API_KEY)

@csrf_exempt
def chat_with_ai(request):
    if request.method == "POST":
        data = json.loads(request.body)
        user_query = data.get("query", "")

        if not user_query:
            return JsonResponse({"error": "Query cannot be empty"}, status=400)

        # Use the correct model from your list
        model = genai.GenerativeModel("gemini-1.5-pro-latest")  # or "gemini-1.5-flash-latest"
        response = model.generate_content(user_query)

        return JsonResponse({"response": response.text})

    return JsonResponse({"error": "Invalid request method"}, status=405)


def chat_page(request):
    return render(request, "talk_with_ai/chat.html")