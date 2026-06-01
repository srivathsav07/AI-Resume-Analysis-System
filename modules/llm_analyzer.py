import anthropic
import google.generativeai as genai
import openai
import json

class LLMAnalyzer:
    def __init__(self, api_key, provider):
        """
        Initialize LLM Analyzer
        
        Args:
            api_key (str): API key for the chosen provider
            provider (str): "OpenAI GPT-4", "Google Gemini", or "Claude"
        """
        self.api_key = api_key
        self.provider = provider
        self.setup_client()
    
    def setup_client(self):
        """Setup the appropriate API client"""
        if self.provider == "OpenAI GPT-4":
            openai.api_key = self.api_key
            self.client = openai.OpenAI(api_key=self.api_key)
        elif self.provider == "Google Gemini":
            genai.configure(api_key=self.api_key)
            self.model = genai.GenerativeModel('gemini-pro')
        elif self.provider == "Claude":
            self.client = anthropic.Anthropic(api_key=self.api_key)
    
    def build_prompt(self, resume_data, jd_data, ats_score):
        """Build comprehensive prompt for LLM analysis"""
        prompt = f"""
You are an expert ATS (Applicant Tracking System) and recruitment consultant. Analyze the following resume against the job description and provide detailed feedback.

## RESUME DATA:
- Name: {resume_data.get('name', 'N/A')}
- Email: {resume_data.get('email', 'N/A')}
- Phone: {resume_data.get('phone', 'N/A')}
- Skills: {', '.join(resume_data.get('skills', []))}
- Resume Preview: {resume_data.get('raw_text', 'N/A')}

## JOB DESCRIPTION DATA:
- Job Title: {jd_data.get('job_title', 'N/A')}
- Required Skills: {', '.join(jd_data.get('required_skills', []))}
- Experience Level: {jd_data.get('experience_level', 'N/A')}
- Responsibilities: {', '.join(jd_data.get('responsibilities', []))}

## CURRENT ATS SCORE: {ats_score}%

Please provide a comprehensive analysis in the following format:

1. **EXECUTIVE SUMMARY** (2-3 sentences)
   Brief overview of candidate fit

2. **STRENGTHS** (3-5 bullet points)
   What the candidate does well that matches the job

3. **WEAKNESSES** (3-5 bullet points)
   What's missing or needs improvement

4. **SKILL GAP ANALYSIS** (detailed)
   Which skills are missing and how important they are

5. **RECOMMENDATIONS** (5-7 specific, actionable items)
   What the candidate should do to improve their chances

6. **INTERVIEW READINESS** (score 1-10 and explanation)
   Is this candidate ready to interview?

7. **CONFIDENCE SCORE** (percentage)
   Overall likelihood of getting this job with current profile

Please be honest, constructive, and specific in your analysis.
"""
        return prompt
    
    def analyze(self, resume_data, jd_data, ats_score):
        """Get LLM analysis"""
        try:
            prompt = self.build_prompt(resume_data, jd_data, ats_score)
            
            if self.provider == "OpenAI GPT-4":
                return self._analyze_openai(prompt)
            elif self.provider == "Google Gemini":
                return self._analyze_gemini(prompt)
            elif self.provider == "Claude":
                return self._analyze_claude(prompt)
        except Exception as e:
            return f"Error: {str(e)}"
    
    def _analyze_openai(self, prompt):
        """Use OpenAI API for analysis"""
        try:
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert ATS consultant and recruitment specialist with 15+ years of experience."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                temperature=0.7,
                max_tokens=1500
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"OpenAI API Error: {str(e)}"
    
    def _analyze_gemini(self, prompt):
        """Use Google Gemini API for analysis"""
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Gemini API Error: {str(e)}"
    
    def _analyze_claude(self, prompt):
        """Use Claude API for analysis"""
        try:
            message = self.client.messages.create(
                model="claude-3-sonnet-20240229",
                max_tokens=1500,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )
            return message.content[0].text
        except Exception as e:
            return f"Claude API Error: {str(e)}"
