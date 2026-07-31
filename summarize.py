import ollama

def summarize(text):

    response = ollama.chat(
        model = "llama3.2:3b",
        messages=[
            { 
            "role":"user",
            "content":f"""

            Summarize the following document.

            -Keep the main idea
            -Make it as concise as possible

            {text}
            """
            }

        ]
    )
    return response["message"]["content"]