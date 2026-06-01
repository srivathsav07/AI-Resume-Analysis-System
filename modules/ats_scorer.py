class ATSScorer:
    """
    ATS (Applicant Tracking System) Scorer
    Calculates resume-to-JD compatibility score
    """
    
    def calculate_score(self, resume_skills, required_skills):
        """
        Calculate ATS score based on skill matching
        
        Formula:
        (Matched Skills / Required Skills) × 100
        
        Args:
            resume_skills (list): Skills found in resume
            required_skills (list): Skills required in JD
        
        Returns:
            int: ATS score (0-100)
        """
        if not required_skills:
            return 0
        
        resume_skills_set = set(skill.lower() for skill in resume_skills)
        required_skills_set = set(skill.lower() for skill in required_skills)
        
        # Find matching skills
        matched_skills = resume_skills_set & required_skills_set
        matched_count = len(matched_skills)
        required_count = len(required_skills_set)
        
        # Calculate percentage
        score = (matched_count / required_count) * 100
        
        return round(score, 2)
    
    def get_skill_breakdown(self, resume_skills, required_skills):
        """
        Get detailed breakdown of skill matching
        
        Returns:
            dict: Matched, missing, and extra skills
        """
        resume_skills_set = set(skill.lower() for skill in resume_skills)
        required_skills_set = set(skill.lower() for skill in required_skills)
        
        matched = list(resume_skills_set & required_skills_set)
        missing = list(required_skills_set - resume_skills_set)
        extra = list(resume_skills_set - required_skills_set)
        
        return {
            "matched": matched,
            "missing": missing,
            "extra": extra,
            "match_count": len(matched),
            "required_count": len(required_skills_set)
        }
    
    def get_score_category(self, score):
        """
        Categorize ATS score
        
        Returns:
            str: Category (Poor, Below Average, Average, Good, Excellent)
        """
        if score < 30:
            return "Poor"
        elif score < 50:
            return "Below Average"
        elif score < 70:
            return "Average"
        elif score < 85:
            return "Good"
        else:
            return "Excellent"
    
    def get_score_advice(self, score):
        """
        Get advice based on score
        
        Returns:
            str: Actionable advice
        """
        if score < 30:
            return "This resume doesn't match the job requirements well. Consider learning the core required skills."
        elif score < 50:
            return "Some skills are missing. Focus on acquiring the key technologies mentioned in the job description."
        elif score < 70:
            return "Good foundation, but missing some important skills. Add certifications or projects in the required areas."
        elif score < 85:
            return "Strong match! Consider adding real-world project experience to strengthen your candidacy."
        else:
            return "Excellent match! Your resume aligns well with the job requirements. Ready to apply!"
