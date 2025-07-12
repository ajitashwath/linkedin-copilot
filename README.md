# LinkedIn Copilot
An AI-powered LinkedIn automation tool built with CrewAI and Streamlit that helps professionals create engaging content, generate leads, and stay informed with daily news summaries.

## 🚀 Features

- **AI-Powered Content Creation**: Generate engaging LinkedIn posts using AI agents
- **Daily News Summaries**: Get concise business news summaries to stay informed
- **Lead Generation**: Identify potential leads from LinkedIn engagement
- **LinkedIn Integration**: Seamlessly post content directly to LinkedIn
- **Multi-Agent System**: Powered by CrewAI with specialized agents for different tasks

## 🏗️ Architecture

The project uses a multi-agent architecture with CrewAI:

- **Researcher Agent**: Researches trending topics and gathers relevant information
- **Content Creator Agent**: Creates engaging, professional LinkedIn posts
- **Lead Generator Agent**: Identifies potential leads from engagement patterns
- **News Summarizer Agent**: Provides daily business news summaries

## 📋 Prerequisites

- Python 3.9+
- LinkedIn Developer Account
- API Keys for:
  - LinkedIn API
  - OpenAI API
  - Serper API (for web searches)

## 🛠️ Installation

1. **Clone the repository**
```bash
git clone https://github.com/Kartavya-AI/LinkedIn-Post.git
cd Linked-Post
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

4. **Set up these API Keys**
```
# LinkedIn API Configuration
LINKEDIN_CLIENT_ID=your_linkedin_client_id
LINKEDIN_CLIENT_SECRET=your_linkedin_client_secret
LINKEDIN_FALLBACK_ACCESS_TOKEN=your_fallback_token  # Optional for testing

# OpenAI API
OPENAI_API_KEY=your_openai_api_key

# Serper API (for web searches)
SERPER_API_KEY=your_serper_api_key
```

## 🔧 LinkedIn API Setup

1. **Create a LinkedIn Developer Account**
   - Go to [LinkedIn Developer Portal](https://developer.linkedin.com/)
   - Create a new app

2. **Configure OAuth Settings**
   - Redirect URI: `https://linkedin-copilot.streamlit.app/signin-linkedin/`
   - Scopes required:
     - `openid`
     - `profile`
     - `email`
     - `w_member_social`
     - `r_liteprofile`

3. **Get API Credentials**
   - Copy your Client ID and Client Secret
   - Add them to your `.env` file

## 🚀 Usage

### Running the Streamlit App

```bash
streamlit run app.py
```

### Using the CLI

```bash
# Get daily summary
python -m src.linkedin_copilot.main run

# Generate content for a topic
python -c "from src.linkedin_copilot.main import LinkedInCopilot; copilot = LinkedInCopilot(); print(copilot.generate_content('AI trends'))"
```

### Authentication Methods

The app supports two authentication methods:
1. **Manual Access Token**
   - Paste a valid LinkedIn access token directly
   - Useful for testing and development

## 📱 Web Interface

The Streamlit web interface provides:

- **Authentication Status**: Shows current login state
- **API Configuration**: Manage API keys directly in the sidebar
- **Content Generation**: Enter topics and generate LinkedIn posts
- **Daily Summary**: Get today's business news
- **Lead Generation**: Find potential leads from engagement
- **Post Management**: Edit and publish content directly to LinkedIn

## 🎯 Core Functionality

### Content Generation
```python
from src.linkedin_copilot.main import LinkedInCopilot

copilot = LinkedInCopilot()
content = copilot.generate_content("AI in the workplace")
print(content)
```

### Daily News Summary
```python
summary = copilot.get_daily_summary()
print(summary)
```

### Posting to LinkedIn
```python
# Requires valid access token
success = copilot.post_to_linkedin(content, access_token)
```

### Lead Generation
```python
leads = copilot.find_leads(access_token)
for lead in leads:
    print(lead)
```

## 🤖 Agent Configuration

Agents are configured in YAML files:

### `src/linkedin_copilot/config/agents.yaml`
Defines the roles, goals, and backstories for each agent.

### `src/linkedin_copilot/config/tasks.yaml`
Specifies the tasks each agent can perform.

## 📁 Project Structure

```
linkedin-copilot/
├── app.py                          # Main Streamlit application
├── src/
│   └── linkedin_copilot/
│       ├── __init__.py
│       ├── main.py                 # Core LinkedIn Copilot logic
│       ├── crew.py                 # CrewAI configuration
│       ├── config/
│       │   ├── agents.yaml         # Agent configurations
│       │   └── tasks.yaml          # Task definitions
│       └── tools/
│           ├── __init__.py
│           └── custom_tool.py      # LinkedIn authentication tools
└── README.md                       # This file
```

## 🚀 Deployment

### Streamlit Cloud
The app is configured for Streamlit Cloud deployment:
- Set environment variables in Streamlit Cloud settings
- Ensure the redirect URI matches your deployment URL

### Local Development
```bash
streamlit run app.py --server.port 8501
```

## 🤝 Contributing
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 🙏 Acknowledgments

- [CrewAI](https://github.com/joaomdmoura/crewAI) for the multi-agent framework
- [Streamlit](https://streamlit.io/) for the web interface
- [LinkedIn API](https://developer.linkedin.com/) for social media integration
- [OpenAI](https://openai.com/) for AI-powered content generation
