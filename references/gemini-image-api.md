# Gemini Image API

Use this when the user wants Gemini instead of Nano Banana.

## Model preference

For final campaign generation:
- prefer the Pro Image Preview model path
- do not default to Flash for the main campaign

In this workflow, the critical rule is:
- use a Pro Image Preview model for anchor and final slides
- only use Flash if the user explicitly permits a lower-quality fallback

If your environment exposes a versioned Pro Image Preview model identifier, use that exact Pro variant. Do not silently substitute a Flash model.

## Python calling pattern

```python
from google import genai
from google.genai import types

client = genai.Client(api_key=GEMINI_API_KEY)

response = client.models.generate_content(
    model="gemini-3-pro-image-preview",
    contents=[prompt, *opened_images],
    config=types.GenerateContentConfig(
        response_modalities=["IMAGE"],
    ),
)
```

## Workflow guidance

- use the Pro Image Preview model for slide 1
- use the normalized export of slide 1 as the style reference for slides 2 to N
- keep a prompt log that records the model used
- normalize outputs after generation
- run a crop-verification pass on normalized exports

## Quality rule

If a Pro Image Preview model is available, do not let the workflow quietly degrade to Flash for the main set.
