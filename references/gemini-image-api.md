# Gemini Credential Notes

This skill uses Nano Banana only.

This file exists because some Nano Banana environments rely on Gemini credentials for authentication.
Treat the Gemini key as a credential requirement, not as permission to switch image models.

## Credential check order

Before generation:

1. Check `GEMINI_API_KEY`.
2. If it is missing, check `GOOGLE_API_KEY`.
3. If both are missing, ask the user for the Gemini API key and stop generation until it is available.

## Hard rules

- keep the image-generation path labeled as `Nano Banana`
- do not switch to another image model because credentials are missing
- do not silently fall back to Flash or a lower-quality path
- record the credential source in the prompt log or notes

## Prompt-log notation

- `Nano Banana`
- `Nano Banana credential source: GEMINI_API_KEY`
- or `Nano Banana credential source: GOOGLE_API_KEY`
- or `Nano Banana credential source: user-provided key`
