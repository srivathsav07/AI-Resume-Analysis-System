# 🚀 Quick Start Guide

## 5-Minute Setup

### 1. Install & Run (Linux/macOS)
```bash
unzip resume-analyzer.zip
cd resume-analyzer
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

### 2. Install & Run (Windows)
```bash
unzip resume-analyzer.zip
cd resume-analyzer
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

### 3. Open Browser
Visit `http://localhost:8501`

---

## Using the App (2 minutes)

### Option 1: Single Resume Analysis
1. **Upload Resume** - Click "Upload Resume" and select PDF or DOCX
2. **Add Job Description** - Paste the job posting you're interested in
3. **View Results**:
   - ATS Score (match percentage)
   - Matched skills (✓)
   - Missing skills (✗)
   - AI recommendations
   - Interview tips

### Option 2: Compare Multiple Resumes
1. Upload 2+ resumes
2. Paste one job description
3. See candidates ranked by match score

### Option 3: Find Matching Jobs
1. Upload your resume
2. System shows best matching roles from database

---

## To Use AI Features (Optional)

1. Get a free API key:
   - **OpenAI**: https://platform.openai.com (free $5 credits)
   - **Gemini**: https://makersuite.google.com (free tier)
   - **Claude**: https://console.anthropic.com (free credits)

2. Paste your API key in the sidebar

3. You'll get:
   - Deep resume analysis
   - Detailed strengths & weaknesses
   - Specific improvement recommendations
   - Interview readiness score
   - Success probability

---

## File Guide

| File | Purpose |
|------|---------|
| `app.py` | Main application |
| `modules/resume_parser.py` | Parse PDFs & DOCXs |
| `modules/jd_analyzer.py` | Analyze job descriptions |
| `modules/ats_scorer.py` | Calculate match score |
| `modules/llm_analyzer.py` | AI analysis |
| `modules/recommendation_engine.py` | Generate tips |
| `requirements.txt` | Dependencies to install |
| `README.md` | Full documentation |

---

## Troubleshooting

### "ModuleNotFoundError: No module named 'streamlit'"
```bash
pip install -r requirements.txt
```

### "Port 8501 is in use"
```bash
streamlit run app.py --server.port 8502
```

### PDF not extracting text
- Use DOCX format instead
- Ensure PDF is not scanned image
- Check if PDF is password protected

### Skills not detected
- Ensure exact spelling matches skill database
- Check capitalization (Python vs python)
- Add skill to database in `resume_parser.py`

### API errors
- Verify API key is correct
- Check you have API credits
- Ensure internet connection

---

## What's Included

✅ Resume parsing (PDF & DOCX)  
✅ Job description analysis  
✅ ATS score calculation  
✅ Skill gap identification  
✅ AI-powered insights  
✅ Personalized recommendations  
✅ Interactive visualizations  
✅ Resume comparison  
✅ Job matching  
✅ Interview readiness scoring  

---

## Next Steps

1. **Test it** - Upload your resume and a job posting
2. **Review recommendations** - See what skills to learn
3. **Learn missing skills** - Use suggested resources
4. **Improve resume** - Apply feedback
5. **Apply with confidence** - You're ready!

---

## Free Resources for Learning

**Python**
- https://www.python.org/about/gettingstarted/
- https://realpython.com/

**SQL**
- https://www.w3schools.com/sql/
- https://sqlzoo.net/

**Tableau/Power BI**
- https://www.tableau.com/en-us/learn
- https://learn.microsoft.com/en-us/power-bi/

**Statistics**
- https://www.khanacademy.org/math/statistics-probability
- https://www.coursera.org/courses

---

## Tips for Best Results

1. **Use recent resume** - Update with latest skills
2. **Paste full job description** - More details = better analysis
3. **Check exact skill names** - "Python" not "python"
4. **Add projects** - Show skills in action
5. **Get certifications** - Prove expertise
6. **Use AI features** - Get deeper insights
7. **Act on recommendations** - Actually learn the skills!

---

## Have Questions?

- Check **README.md** for detailed docs
- Read **DEPLOYMENT.md** for advanced setup
- See **SAMPLE_DATA.md** for test data
- Check troubleshooting section above

---

**Ready to improve your resume? Let's go! 🚀**

Enjoy using AI Resume Analyzer!
