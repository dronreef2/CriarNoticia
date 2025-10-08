# Copilot Instructions for CriarNoticia

## Project Overview
CriarNoticia is an automated content pipeline using Google Gemini API. It:
- Searches for news using Google Search integration
- Structures data with Pydantic models
- Generates AI-powered analysis
- Creates images with Imagen 3.0

The project is primarily in **Portuguese** with English prompts for image generation.

## General Guidelines
- Write clear, maintainable, and well-documented code
- Follow best practices for the technology stack being used
- Ensure all code changes include appropriate error handling
- Keep functions small and focused on a single responsibility
- All user-facing text, comments, and documentation should be in **Portuguese**

## Code Style

### Python Conventions
- Use **snake_case** for function and variable names (e.g., `criar_briefing_avancado`, `topico_central`)
- Use **PascalCase** for class names (e.g., `BriefingDeNoticias`, `ArtigoEncontrado`)
- Use type hints for function parameters and return values
- Use docstrings in Portuguese for all functions and classes
- Maintain consistent 4-space indentation
- Add comments for complex logic or non-obvious implementations

### Naming Conventions
- Portuguese names for variables, functions, and classes (e.g., `topico`, `artigos`, `analise_sintetizada`)
- Descriptive names that clearly indicate purpose
- Use emojis in print statements for better UX (e.g., "🚀", "✅", "🔎")

## Project Structure

### Main Files
- `criar_briefing_noticias.py`: Core pipeline implementation
- `exemplos_uso.py`: Advanced usage examples and patterns
- `requirements.txt`: Python dependencies (google-generativeai, pydantic)
- `config.env.example`: Template for environment configuration
- `README.md`: Main documentation in Portuguese
- `QUICKSTART.md`: 5-minute quick start guide
- `IMPLEMENTATION_SUMMARY.md`: Technical implementation details

### Key Dependencies
- `google-generativeai`: Google Gemini API client
- `pydantic`: Data validation and schema definition

## Google Gemini API Guidelines

### Client Initialization
- Use the new `genai.Client()` pattern, not deprecated methods
- Configure API key via `genai.configure(api_key=...)` before creating client
- Prefer environment variables for API keys: `os.getenv('GOOGLE_API_KEY')`

### API Usage
- Use `GoogleSearch` tool for web search integration
- Use `response_schema` parameter with Pydantic models for structured output
- Use Gemini 1.5 Pro for text generation (model: `gemini-1.5-pro`)
- Use Imagen 3.0 for image generation (model: `imagen-3.0-generate-001`)
- Set appropriate temperature (e.g., 0.5 for balanced creativity)
- Use 16:9 aspect ratio for social media images

### Error Handling
- Always wrap API calls in try-except blocks
- Implement retry logic for transient failures
- Provide helpful error messages in Portuguese
- Log errors but never expose API keys in logs

## Pydantic Best Practices

### Model Definition
- Use `Field(description=...)` to guide the AI model on what to generate
- Provide clear, detailed descriptions in Portuguese for each field
- Use appropriate Python types: `str`, `List[...]`, `int`, etc.
- Make descriptions specific about format and content expectations

### Example Structure
```python
class ArtigoEncontrado(BaseModel):
    titulo: str = Field(description="O título exato da matéria.")
    fonte: str = Field(description="O nome do veículo de comunicação.")
    resumo_curto: str = Field(description="Um resumo de uma a duas frases.")
```

## Documentation
- Update README.md when adding new features or making significant changes
- Document all public APIs and functions with Portuguese docstrings
- Include examples in documentation where appropriate
- Maintain the emoji-rich, friendly documentation style
- Keep QUICKSTART.md updated for new users
- Update IMPLEMENTATION_SUMMARY.md for technical changes

## Testing and Examples

### Testing Approach
- Test API integration carefully to avoid unnecessary API costs
- Validate Pydantic models with mock data when possible
- Test error handling paths without making actual API calls
- Use example topics from `exemplos_uso.py` for consistency

### Usage Examples
- Add new examples to `exemplos_uso.py` when introducing features
- Keep examples commented out to prevent accidental API usage
- Document each example with clear purpose and expected behavior
- Include error handling patterns in examples

## Version Control
- Write clear, descriptive commit messages in Portuguese or English
- Keep commits focused on a single logical change
- Reference issue numbers in commit messages when applicable
- Don't commit: API keys, `.env` files, generated images, cache files

## Security - CRITICAL

### API Key Protection
- **NEVER** commit actual API keys to the repository
- Always use placeholders like `"SUA_API_KEY_AQUI"` in code
- Document environment variable usage: `os.getenv('GOOGLE_API_KEY')`
- Ensure `.gitignore` includes: `.env`, `*.env`, API key files
- Remind users to obtain keys from: https://aistudio.google.com/app/apikey

### Input Validation
- Validate and sanitize all user inputs, especially topic strings
- Be cautious with user-provided file paths
- Validate API responses before using them

### Cost Monitoring
- Remind users to monitor API usage to avoid unexpected costs
- Implement reasonable limits on API calls in examples
- Document API costs implications in README

## Special Considerations

### Multimodal Pipeline
- Understand the 4-stage pipeline: Search → Structure → Analyze → Visualize
- Keep stages modular and testable independently
- Handle failures gracefully at each stage
- Allow continuation even if image generation fails

### Brazilian Portuguese Context
- Use Brazilian Portuguese conventions in text
- Consider Brazilian news sources and context
- Keep prompts culturally appropriate

### Performance
- Batch operations when possible to reduce API calls
- Cache results when appropriate
- Use appropriate timeouts for network operations
- Monitor rate limits and implement backoff strategies
