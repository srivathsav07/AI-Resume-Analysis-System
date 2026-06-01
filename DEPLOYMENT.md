# Setup & Deployment Guide

## Local Development Setup

### Step 1: Environment Setup
```bash
# Extract the zip file
unzip resume-analyzer.zip
cd resume-analyzer

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Configure API Keys
```bash
# Copy the example configuration
cp .env.example .env

# Edit .env file and add your API keys
# Option 1: Add keys directly in the app via Streamlit sidebar
# Option 2: Set environment variables
export OPENAI_API_KEY="your_key_here"
export GEMINI_API_KEY="your_key_here"
export CLAUDE_API_KEY="your_key_here"
```

### Step 4: Run the Application
```bash
streamlit run app.py
```

The application will open at `http://localhost:8501`

---

## Docker Deployment

### Create Dockerfile
```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8501

CMD ["streamlit", "run", "app.py"]
```

### Build and Run with Docker
```bash
# Build the image
docker build -t resume-analyzer .

# Run the container
docker run -p 8501:8501 resume-analyzer
```

---

## Streamlit Cloud Deployment

### Prerequisites
- GitHub account with the repository
- Streamlit account (https://share.streamlit.io)

### Steps:
1. Push your code to GitHub
2. Go to https://share.streamlit.io
3. Connect your GitHub repository
4. Select the branch and app.py file
5. Add secrets in "Advanced Settings":
   - OPENAI_API_KEY
   - GEMINI_API_KEY
   - CLAUDE_API_KEY

---

## Heroku Deployment

### Create Files

**Procfile:**
```
web: streamlit run app.py --logger.level=error
```

**runtime.txt:**
```
python-3.11.7
```

### Deploy
```bash
# Install Heroku CLI
# https://devcenter.heroku.com/articles/heroku-cli

# Login to Heroku
heroku login

# Create Heroku app
heroku create your-app-name

# Set environment variables
heroku config:set OPENAI_API_KEY=your_key_here
heroku config:set GEMINI_API_KEY=your_key_here
heroku config:set CLAUDE_API_KEY=your_key_here

# Deploy
git push heroku main
```

---

## AWS Deployment (EC2)

### Setup EC2 Instance
```bash
# SSH into your EC2 instance
ssh -i your-key.pem ec2-user@your-instance-ip

# Update system
sudo yum update -y
sudo yum install python3-pip git -y

# Clone repository
git clone your-repo-url
cd resume-analyzer

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run with nohup (background process)
nohup streamlit run app.py --server.port 80 > app.log 2>&1 &
```

---

## Google Cloud Run Deployment

### Create app.yaml
```yaml
runtime: python39

env: standard

handlers:
  - url: /.*
    script: auto

entrypoint: streamlit run app.py --logger.level=error --server.port 8080
```

### Deploy
```bash
# Install Google Cloud SDK
# https://cloud.google.com/sdk/docs/install

# Initialize and authenticate
gcloud init
gcloud auth application-default login

# Deploy
gcloud run deploy resume-analyzer \
  --source . \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --set-env-vars OPENAI_API_KEY=your_key
```

---

## Environment Variables

### Required for Full Functionality
- `OPENAI_API_KEY` - OpenAI API access
- `GEMINI_API_KEY` - Google Gemini API access
- `CLAUDE_API_KEY` - Anthropic Claude API access

### Optional Configuration
- `DEFAULT_LLM` - Default LLM provider
- `MAX_FILE_SIZE` - Maximum upload size in MB
- `ENABLE_ADVANCED_FEATURES` - Enable/disable advanced features

---

## Production Checklist

- [ ] Add proper error handling and logging
- [ ] Set up SSL/TLS certificates
- [ ] Configure CORS if needed
- [ ] Set up rate limiting
- [ ] Add authentication/authorization
- [ ] Configure backup and recovery
- [ ] Set up monitoring and alerting
- [ ] Load test the application
- [ ] Document API endpoints
- [ ] Create maintenance plan

---

## Troubleshooting Deployment

### Issue: ModuleNotFoundError
```bash
# Make sure all dependencies are installed
pip install -r requirements.txt
```

### Issue: API Key Not Found
```bash
# Verify environment variables are set correctly
echo $OPENAI_API_KEY
```

### Issue: Port Already in Use
```bash
# Run on different port
streamlit run app.py --server.port 8502
```

### Issue: High Memory Usage
```bash
# Optimize Streamlit configuration
# Create .streamlit/config.toml
[logger]
level = "error"

[client]
maxMessageSize = 50
```

---

## Performance Optimization

### Caching
- Use `@st.cache_data` for expensive computations
- Implement Redis for distributed caching

### Database
- Use SQLite for local storage
- Migrate to PostgreSQL for production

### API Calls
- Implement request batching
- Add retry logic with exponential backoff
- Cache API responses

### Frontend
- Lazy load components
- Optimize image sizes
- Minify CSS/JS

---

## Security Best Practices

1. **Never commit API keys** - Use environment variables
2. **Validate file uploads** - Check file types and sizes
3. **Sanitize user input** - Prevent injection attacks
4. **Use HTTPS** - Encrypt data in transit
5. **Implement rate limiting** - Prevent abuse
6. **Regular updates** - Keep dependencies current
7. **Audit logs** - Monitor suspicious activity
8. **Access control** - Implement proper authentication

---

## Monitoring & Logging

### Set up Application Monitoring
```python
import logging

logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
```

### Monitor Key Metrics
- API response times
- Error rates
- File upload success rate
- LLM API costs
- User engagement

---

## Maintenance

### Regular Tasks
- Update dependencies: `pip install --upgrade -r requirements.txt`
- Monitor API costs and usage
- Clean up old logs and temporary files
- Review and update documentation
- Test backup and recovery procedures

### Monthly
- Review error logs
- Update skill database
- Security audit
- Performance analysis

### Quarterly
- Major version updates
- Infrastructure review
- User feedback analysis
- Feature planning

---

For more help, refer to the main README.md file.
