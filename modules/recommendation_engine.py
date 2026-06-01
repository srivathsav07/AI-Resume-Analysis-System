class RecommendationEngine:
    """
    Generates personalized recommendations to improve resume-to-job match
    """
    
    def __init__(self):
        self.recommendations_template = {
            "skill_learning": "Learn and add {skill} to your skill set - it's crucial for this role",
            "project_building": "Build a project using {skill} and showcase it in your portfolio",
            "certification": "Get certified in {skill} to demonstrate expertise",
            "experience": "Gain hands-on experience in {skill} through internships or freelance work",
            "formatting": "Improve resume formatting and ATS optimization for better parsing",
            "quantification": "Quantify achievements with metrics (e.g., 'improved efficiency by 40%')",
            "keywords": "Add relevant keywords from the job description to your resume",
            "cover_letter": "Write a targeted cover letter highlighting how your skills match the role",
            "networking": "Network with professionals in the {skill} space to learn latest trends",
            "course": "Complete an online course in {skill} on platforms like Coursera, Udemy, or LinkedIn Learning"
        }
    
    def generate_recommendations(self, resume_data, jd_data, ats_score):
        """
        Generate personalized recommendations based on analysis
        
        Returns:
            list: List of recommendation strings
        """
        recommendations = []
        
        resume_skills_set = set(skill.lower() for skill in resume_data.get('skills', []))
        required_skills_set = set(skill.lower() for skill in jd_data.get('required_skills', []))
        
        missing_skills = list(required_skills_set - resume_skills_set)
        
        # Recommendation 1: Focus on missing critical skills
        if missing_skills:
            top_missing = missing_skills[0]
            recommendations.append(
                f"🎯 Learn {top_missing} - This is a key requirement for the {jd_data.get('job_title', 'role')} position"
            )
        
        # Recommendation 2: Build projects with missing skills
        if len(missing_skills) > 1:
            skill_pair = " and ".join(missing_skills[:2])
            recommendations.append(
                f"📁 Create a project combining {skill_pair} - Demonstrate practical experience"
            )
        
        # Recommendation 3: Optimize resume formatting
        recommendations.append(
            "📝 Optimize your resume with relevant keywords from the job description for better ATS parsing"
        )
        
        # Recommendation 4: Quantify achievements
        recommendations.append(
            "📊 Add quantifiable metrics to your achievements (e.g., 'Increased performance by X%')"
        )
        
        # Recommendation 5: Get certifications
        if missing_skills:
            cert_skill = missing_skills[0]
            recommendations.append(
                f"🏆 Earn a certification in {cert_skill} from recognized platforms like Coursera or AWS"
            )
        
        # Recommendation 6: Tailor cover letter
        recommendations.append(
            "💼 Write a personalized cover letter highlighting how your existing skills transfer to this role"
        )
        
        # Recommendation 7: Based on ATS Score
        if ats_score < 50:
            recommendations.append(
                "⚠️ Consider acquiring more foundational skills before applying - Focus on core requirements first"
            )
        elif ats_score < 70:
            recommendations.append(
                "✅ You have a solid foundation - Add specialized skills to stand out from other candidates"
            )
        else:
            recommendations.append(
                "🚀 Excellent match! Prepare for interviews by brushing up on technical and behavioral questions"
            )
        
        return recommendations
    
    def generate_improvement_plan(self, resume_data, jd_data):
        """
        Generate a structured improvement plan
        
        Returns:
            dict: Detailed improvement plan with timeline
        """
        resume_skills_set = set(skill.lower() for skill in resume_data.get('skills', []))
        required_skills_set = set(skill.lower() for skill in jd_data.get('required_skills', []))
        missing_skills = list(required_skills_set - resume_skills_set)
        
        plan = {
            "month_1": {
                "focus": "Foundation",
                "actions": [
                    "Review the job description thoroughly",
                    "Identify top 3 missing skills",
                    f"Start learning: {missing_skills[0] if missing_skills else 'core technologies'}"
                ]
            },
            "month_2": {
                "focus": "Skill Development",
                "actions": [
                    f"Complete online course in {missing_skills[0] if missing_skills else 'first skill'}",
                    "Start building a portfolio project",
                    "Practice coding/technical challenges"
                ]
            },
            "month_3": {
                "focus": "Project Showcase",
                "actions": [
                    "Complete a significant project using new skills",
                    "Update resume with new skills and projects",
                    "Get GitHub/portfolio reviewed by peers"
                ]
            },
            "month_4": {
                "focus": "Application Ready",
                "actions": [
                    "Polish resume and cover letter",
                    "Apply to target positions",
                    "Prepare for technical interviews"
                ]
            }
        }
        
        return plan
    
    def get_learning_resources(self, skill):
        """
        Suggest learning resources for a specific skill
        
        Returns:
            dict: Resources and learning paths
        """
        resources = {
            "Python": {
                "courses": ["Python for Data Science (Coursera)", "Complete Python Bootcamp (Udemy)"],
                "platforms": ["Codecademy", "DataCamp", "Real Python"],
                "projects": ["Build a Python CLI tool", "Create a web scraper", "Develop a data analysis script"]
            },
            "SQL": {
                "courses": ["SQL for Data Analysis (Coursera)", "The Complete SQL Bootcamp (Udemy)"],
                "platforms": ["LeetCode SQL", "HackerRank", "Mode Analytics SQL Tutorial"],
                "projects": ["Design a database schema", "Query optimization exercises", "Data aggregation challenges"]
            },
            "JavaScript": {
                "courses": ["JavaScript Algorithms and Data Structures (FreeCodeCamp)", "Complete JavaScript Course (Udemy)"],
                "platforms": ["JavaScript.info", "Eloquent JavaScript", "You Don't Know JS"],
                "projects": ["Build a todo app", "Create a weather app", "Develop a calculator"]
            },
            "React": {
                "courses": ["React for Beginners (Wes Bos)", "React Complete Guide (Udemy)"],
                "platforms": ["React official docs", "Scrimba React course", "egghead.io"],
                "projects": ["Build a portfolio website", "Create a note-taking app", "Develop a e-commerce site"]
            }
        }
        
        return resources.get(skill, {
            "courses": ["General online courses available"],
            "platforms": ["Coursera", "Udemy", "edX"],
            "projects": ["Build real-world projects to practice"]
        })
