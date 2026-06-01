import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from modules.resume_parser import ResumeParser
from modules.jd_analyzer import JobDescriptionAnalyzer
from modules.ats_scorer import ATSScorer
from modules.llm_analyzer import LLMAnalyzer
from modules.recommendation_engine import RecommendationEngine
import json

# Page configuration
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main {background-color: #f8f9fa;}
    .metric-card {background-color: white; padding: 20px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);}
    .score-high {color: #28a745;}
    .score-low {color: #dc3545;}
    .score-medium {color: #ffc107;}
    </style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("🤖 Resume Analyzer")
    st.markdown("---")
    
    mode = st.radio(
        "Select Mode",
        ["📋 Single Resume Analysis", "🏆 Compare Resumes", "💼 Job Matching"],
        index=0
    )
    
    st.markdown("---")
    api_choice = st.selectbox(
        "LLM Provider",
        ["OpenAI GPT-4", "Google Gemini", "Claude"]
    )
    
    if api_choice == "OpenAI GPT-4":
        api_key = st.text_input("Enter OpenAI API Key", type="password")
    elif api_choice == "Google Gemini":
        api_key = st.text_input("Enter Google Gemini API Key", type="password")
    else:
        api_key = st.text_input("Enter Claude API Key", type="password")

# Main content
if mode == "📋 Single Resume Analysis":
    st.title("📄 Single Resume Analysis")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Upload Resume")
        uploaded_resume = st.file_uploader(
            "Choose a resume file",
            type=["pdf", "docx"],
            key="resume_upload"
        )
    
    with col2:
        st.subheader("Job Description")
        jd_input = st.text_area(
            "Paste the job description here",
            height=200,
            placeholder="Looking for a Data Analyst with Python, SQL, and Tableau skills..."
        )
    
    if uploaded_resume and jd_input:
        with st.spinner("📊 Analyzing resume..."):
            try:
                # Step 1: Parse Resume
                parser = ResumeParser()
                resume_data = parser.parse_resume(uploaded_resume)
                
                # Step 2: Analyze Job Description
                jd_analyzer = JobDescriptionAnalyzer()
                jd_data = jd_analyzer.analyze_jd(jd_input)
                
                # Step 3: Calculate ATS Score
                scorer = ATSScorer()
                ats_score = scorer.calculate_score(
                    resume_data['skills'],
                    jd_data['required_skills']
                )
                
                # Step 4: Get LLM Analysis
                if api_key:
                    llm = LLMAnalyzer(api_key, api_choice)
                    llm_analysis = llm.analyze(resume_data, jd_data, ats_score)
                else:
                    llm_analysis = None
                
                # Step 5: Generate Recommendations
                recommender = RecommendationEngine()
                recommendations = recommender.generate_recommendations(
                    resume_data,
                    jd_data,
                    ats_score
                )
                
                # Display Results
                st.success("✅ Analysis Complete!")
                st.markdown("---")
                
                # Tab 1: Overview
                tab1, tab2, tab3, tab4, tab5 = st.tabs([
                    "📊 Overview", 
                    "🎯 Skills Analysis", 
                    "💡 Recommendations", 
                    "🧠 LLM Insights",
                    "📄 Resume Data"
                ])
                
                with tab1:
                    col1, col2, col3 = st.columns(3)
                    
                    with col1:
                        st.metric(
                            "ATS Score",
                            f"{ats_score}%",
                            delta="Match Rate"
                        )
                    
                    with col2:
                        matched = len(set(resume_data['skills']) & set(jd_data['required_skills']))
                        st.metric(
                            "Skills Matched",
                            f"{matched}/{len(jd_data['required_skills'])}",
                            delta="Required Skills"
                        )
                    
                    with col3:
                        missing = len(set(jd_data['required_skills']) - set(resume_data['skills']))
                        st.metric(
                            "Missing Skills",
                            missing,
                            delta="To Learn"
                        )
                    
                    # Score gauge
                    st.markdown("### Score Distribution")
                    fig = go.Figure(go.Indicator(
                        mode="gauge+number",
                        value=ats_score,
                        title={'text': "ATS Match Score"},
                        domain={'x': [0, 1], 'y': [0, 1]},
                        gauge={
                            'axis': {'range': [None, 100]},
                            'bar': {'color': "#1f77b4"},
                            'steps': [
                                {'range': [0, 30], 'color': "#ffcccc"},
                                {'range': [30, 70], 'color': "#ffffcc"},
                                {'range': [70, 100], 'color': "#ccffcc"}
                            ]
                        }
                    ))
                    fig.update_layout(height=400)
                    st.plotly_chart(fig, use_container_width=True)
                
                with tab2:
                    st.subheader("Skill Comparison")
                    
                    col1, col2 = st.columns(2)
                    
                    with col1:
                        st.subheader("✅ Matched Skills")
                        matched_skills = list(set(resume_data['skills']) & set(jd_data['required_skills']))
                        if matched_skills:
                            for skill in matched_skills:
                                st.success(f"✓ {skill}")
                        else:
                            st.info("No matching skills found")
                    
                    with col2:
                        st.subheader("❌ Missing Skills")
                        missing_skills = list(set(jd_data['required_skills']) - set(resume_data['skills']))
                        if missing_skills:
                            for skill in missing_skills:
                                st.error(f"✗ {skill}")
                        else:
                            st.success("All required skills present!")
                    
                    # Skill chart
                    st.markdown("### Skill Match Visualization")
                    all_skills = list(set(resume_data['skills'] + jd_data['required_skills']))
                    skill_match = {
                        'Skill': all_skills,
                        'In Resume': [1 if skill in resume_data['skills'] else 0 for skill in all_skills],
                        'In JD': [1 if skill in jd_data['required_skills'] else 0 for skill in all_skills]
                    }
                    skill_df = pd.DataFrame(skill_match)
                    fig = px.bar(skill_df, x='Skill', y=['In Resume', 'In JD'], barmode='group')
                    st.plotly_chart(fig, use_container_width=True)
                
                with tab3:
                    st.subheader("💡 Personalized Recommendations")
                    for i, rec in enumerate(recommendations, 1):
                        st.info(f"**{i}. {rec}**")
                
                with tab4:
                    if llm_analysis:
                        st.subheader("🧠 AI-Powered Analysis")
                        st.markdown(llm_analysis)
                    else:
                        st.warning("⚠️ Please enter an API key to see LLM insights")
                
                with tab5:
                    st.subheader("Extracted Resume Data")
                    st.json(resume_data)
                    st.subheader("Extracted Job Description Data")
                    st.json(jd_data)
            
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
    else:
        st.info("📌 Please upload a resume and enter a job description to begin analysis")

elif mode == "🏆 Compare Resumes":
    st.title("🏆 Compare Multiple Resumes")
    
    jd_input = st.text_area(
        "Paste the job description",
        height=150,
        placeholder="Job description..."
    )
    
    uploaded_files = st.file_uploader(
        "Upload multiple resumes",
        type=["pdf", "docx"],
        accept_multiple_files=True
    )
    
    if uploaded_files and jd_input:
        with st.spinner("📊 Analyzing resumes..."):
            try:
                parser = ResumeParser()
                jd_analyzer = JobDescriptionAnalyzer()
                scorer = ATSScorer()
                
                jd_data = jd_analyzer.analyze_jd(jd_input)
                
                results = []
                for resume_file in uploaded_files:
                    resume_data = parser.parse_resume(resume_file)
                    ats_score = scorer.calculate_score(
                        resume_data['skills'],
                        jd_data['required_skills']
                    )
                    results.append({
                        'Candidate': resume_file.name.replace('.pdf', '').replace('.docx', ''),
                        'ATS Score': ats_score,
                        'Skills Matched': len(set(resume_data['skills']) & set(jd_data['required_skills'])),
                        'Total Skills': len(jd_data['required_skills'])
                    })
                
                results_df = pd.DataFrame(results).sort_values('ATS Score', ascending=False)
                
                st.subheader("📊 Ranking Results")
                st.dataframe(results_df, use_container_width=True)
                
                # Chart
                fig = px.bar(results_df, x='Candidate', y='ATS Score', 
                            color='ATS Score', color_continuous_scale='Viridis')
                st.plotly_chart(fig, use_container_width=True)
            
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
    else:
        st.info("📌 Upload resumes and provide a job description")

else:  # Job Matching
    st.title("💼 Find Best Matching Jobs")
    
    uploaded_resume = st.file_uploader(
        "Upload your resume",
        type=["pdf", "docx"],
        key="job_match_resume"
    )
    
    if uploaded_resume:
        with st.spinner("📊 Analyzing resume..."):
            try:
                parser = ResumeParser()
                resume_data = parser.parse_resume(uploaded_resume)
                
                st.subheader("Your Skills")
                st.write(", ".join(resume_data['skills']))
                
                # Sample jobs database
                jobs = [
                    {
                        "title": "Data Analyst",
                        "required_skills": ["Python", "SQL", "Tableau", "Statistics"]
                    },
                    {
                        "title": "Business Analyst",
                        "required_skills": ["SQL", "Excel", "Python", "Communication"]
                    },
                    {
                        "title": "Python Developer",
                        "required_skills": ["Python", "JavaScript", "React", "SQL"]
                    },
                    {
                        "title": "Power BI Developer",
                        "required_skills": ["Power BI", "SQL", "DAX", "Excel"]
                    }
                ]
                
                scorer = ATSScorer()
                matches = []
                
                for job in jobs:
                    score = scorer.calculate_score(
                        resume_data['skills'],
                        job['required_skills']
                    )
                    matches.append({
                        'Job Title': job['title'],
                        'Match Score': score,
                        'Skills Match': len(set(resume_data['skills']) & set(job['required_skills']))
                    })
                
                matches_df = pd.DataFrame(matches).sort_values('Match Score', ascending=False)
                
                st.subheader("📋 Best Matching Roles")
                st.dataframe(matches_df, use_container_width=True)
                
                fig = px.bar(matches_df, x='Job Title', y='Match Score',
                            color='Match Score', color_continuous_scale='RdYlGn')
                st.plotly_chart(fig, use_container_width=True)
            
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
    else:
        st.info("📌 Upload your resume to find matching jobs")

st.markdown("---")
st.markdown("<div style='text-align: center'><p>© 2024 AI Resume Analyzer | Powered by Streamlit & LLMs</p></div>", unsafe_allow_html=True)
