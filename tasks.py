from crewai import Task

class VideoEditingTasks:

    def business_analysis_task(self, agent,inputs):
        return Task(
        agent=agent,
 description="Analyze the provided needs video editing workflow from inputs and time expenditure in order to better understand the customer's needs. Here are the customer needs: {inputs} ",
        expected_output="""A report defining the problem in business terms and potential solutions after thorourghly analyzing the solutions for the customer's needs based on their reported
        problem. Customer Conversation: {inputs}.
        Here's a template of the report that will be used by the BSA when communicating with the business:
        Sample Report Template
Executive Summary
Purpose: (Briefly describe the goal of this report and what it aims to achieve.)
Key Findings: (Summarize the main insights gathered from the analysis.)
Introduction
Background: (Provide context or background information that explains why this report was necessary.)
Scope: (Define the boundaries of the report, including what was and was not analyzed.)
Current Workflow Analysis
Step-by-Step Breakdown:
(Step Name): (Description of the step, tools used, and common issues.)
(Repeat for each relevant step)
Time Expenditure
Data Collection: (Describe how data about time usage was collected.)
Analysis: (Present the analysis of the data, possibly using graphs or charts.)
Comparison: (Compare this data against industry standards or historical data.)
Challenges Identified
Bottlenecks: (Detail any specific stages where delays are most frequent.)
Technical Limitations: (Describe any hardware or software limitations affecting performance.)
Skill Gaps: (Identify areas where additional training or skills are needed.)
Recommendations
Process Improvements:
(Suggest specific improvements to streamline processes.)
(Additional suggestions.)
Training and Development: (Propose training or educational sessions to address skill gaps.)
Technology Upgrades: (Recommend upgrades to software or hardware if applicable.)
Conclusion
Summary of Findings: (Reiterate the key points discovered during the analysis.)
Expected Outcomes: (Describe what improvements or benefits are expected from implementing the recommendations.)
Next Steps: (Outline the actions to be taken following the report.)
        """,

        )

    def video_editor_task(self, agent,context):
        return Task(
            agent=agent,
            context=context,
                    description="Outline the qualifications, skills, and software requirements for a video editor given the provided context",
        expected_output="""A detailed description of the video editing need after analysis from the BSA report is provided, here is a sample report:
        Video Editor’s Custom Report Template
1. Introduction
Overview of Project Requirements: Describe the project's scope including the type and quantity of videos, target audience, and delivery platforms which impact the editing requirements.
Objectives of the Video Editing Task: Define specific goals such as increasing viewer engagement, clarifying message delivery, or enhancing visual storytelling.
2. Technical Specifications
Required Software and Tools:
Video Editing Software: List essential software like Adobe Premiere Pro, Final Cut Pro, or DaVinci Resolve and specify version requirements if applicable.
Supportive Tools: Include auxiliary software like Adobe After Effects for motion graphics and color correction tools.
Detailed Skills Needed:
Basic Editing: Cutting, trimming, and sequencing skills (Beginner to Intermediate level).
Advanced Post-Production: Color grading, sound mixing, and visual effects (Intermediate to Advanced level).
3. Creative Requirements
Style Guidelines: Outline the aesthetic and thematic guidelines based on the brand or creative direction, including any color schemes, font styles, and overall tone.
Types of Effects and Animations Needed:
Transitional Effects: Usage of wipes, fades, and dissolves.
Animations: Details about character and infographic animations that enhance storytelling or informational delivery.
4. Operational Details
Time Estimates Per Video:
Short Form Content: Time required for editing videos up to 10 minutes.
Long Form Content: Detailed breakdown for videos longer than 10 minutes, including stages of editing.
Workflow and Process Outline:
Pre-Production: Planning phase interactions with other team members.
Production Workflow: Step-by-step workflow from raw footage to final output.
Review Cycles: Expected number of iterations before final approval.
5. Budget and Resource Allocation
Cost Estimates Per Video or Project:
By Video Length: Cost analysis based on the video length and complexity.
By Project: Overall budget required for entire projects considering bulk work or long-term engagements.
Equipment and Software Licenses Needed:
Hardware: Specifications for computers, external storage, etc.
Software Subscriptions: Costs associated with necessary software licenses and updates.
6. Conclusion
Summary of Key Points: Recap the critical technical and creative requirements along with operational guidelines.
Recommendations for Implementation:
Immediate Actions: Steps that need to be taken to start the project effectively.
Long-Term Recommendations: Strategic suggestions for future projects or ongoing content production.""",

        )

    def recruitment_task(self, agent,context):
        return Task(
            agent=agent,
            context=context,
                    description="Create a job description and define the hiring process for a video editor.",
        expected_output="""A clear detailed guide that includes the next steps for searching for a candidate and return the following report:
        Talent Recruiter’s Job Posting and Screening Template
1. Job Postings
Create three distinct job postings designed to attract candidates with varying levels of expertise and specialization:

Entry-Level Video Editor:

Description: Outline the basic requirements and duties for newcomers or those with limited professional experience.
Requirements: List proficiency in basic video editing software, a good sense of timing and pacing, and a portfolio of school projects or personal work.
Mid-Level Video Editor:

Description: Target professionals with solid experience in video production, looking for career growth.
Requirements: Detailed knowledge of advanced video editing software, experience with client-driven projects, and ability to handle multiple projects simultaneously.
Senior Video Editor:

Description: Aimed at highly experienced individuals capable of managing entire projects and mentoring junior staff.
Requirements: Expert-level proficiency with a suite of video editing tools, proven track record of successful projects, and strong leadership skills.
2. Candidate Testing with Short Projects
Project Outline: Design a short project relevant to your current video needs. For instance, edit a 2-minute promotional video using provided raw footage.
Evaluation Criteria: Clarity of the edited video, creative use of transitions and effects, and adherence to the brief.
3. Interview Questions
Develop a set of questions that explore technical skills, creativity, and fit within your company’s culture. Here are some examples:

Technical Proficiency: What software tools are you most proficient in, and what is your workflow like?
Creative Questions: Can you describe a project where you had to think outside the box?
Cultural Fit: How do you handle feedback from superiors or clients?
Each category should have at least 10 questions to thoroughly assess the candidate.

4. Green Flags and Red Flags
Green Flags:
Shows a keen eye for detail.
Exhibits a proactive approach to learning new skills.
Has a collaborative attitude.
Red Flags:
Unclear or generic answers to technical questions.
Lack of specific examples in their portfolio.
Shows reluctance to adapt to new technologies or workflows.
5. Additional Recommendations
Reference Checks: Always conduct reference checks to validate the candidate’s previous employment and character.
Continuous Feedback: Implement a system to gather feedback from candidates about the recruitment process to improve and refine your approach.
        """,

        )

    def project_management_task(self, agent,context):
        return Task(
            agent=agent,
            context=context,
            description="Devise a 14-day action plan to hire a video editor.",
        expected_output="""A step-by-step hiring plan with milestones and deadlines formatted in the following way:
Comprehensive Project Execution Plan
Executive Summary
Purpose: Deliver a detailed, actionable plan based on inputs from all preceding stages to seamlessly recruit a suitable video editor.
Overview: This plan includes timelines, milestones, decision points, and resource allocations, designed to ensure clarity and ease of execution for the customer.
Introduction
Project Scope: Outline of the project’s goals, emphasizing the importance of each role in contributing to this comprehensive plan.
Stakeholders: List of all involved parties including the BSA, Video Editor Consultant, Talent Recruiter, and any other key personnel.
Compilation of Inputs
From the BSA: Summary of the customer needs as identified and the business implications discussed.
From the Video Editor Consultant: Insights into the technical and creative requirements essential for the role.
From the Talent Recruiter: Overview of the job market analysis, candidate profiles, and screening strategies that have been developed.
Detailed Action Plan
Phase 1: Pre-Recruitment Preparation (Days 1-3)

Activities: Finalize job description, set up recruitment tools, and prepare initial communication materials.
Deliverables: Job description document, recruitment platform setup confirmation.
Phase 2: Recruitment Launch (Days 4-6)

Activities: Job posting across multiple platforms, initiation of targeted headhunting.
Deliverables: Links to live job postings, schedule of headhunting activities.
Phase 3: Screening and Interviews (Days 7-10)

Activities: Screening of applications, scheduling and conducting interviews.
Deliverables: Shortlist of candidates, interview notes, and assessments.
Phase 4: Final Selection and Offer (Days 11-12)

Activities: Final review meeting, decision on the selected candidate, job offer preparation and dispatch.
Deliverables: Final candidate report, copy of the job offer sent.
Phase 5: Onboarding and Feedback (Days 13-14)

Activities: Onboarding schedule preparation, initial feedback collection on the recruitment process.
Deliverables: Onboarding itinerary, feedback report.
Strategy for Ongoing Support
Training and Integration: Plans for integrating the new hire into the current team, including specific training sessions tailored to fill any identified skills gaps.
Monitoring and Adjustment: Mechanisms for monitoring the effectiveness of the new hire and adjustments based on early results and feedback.
Conclusion
Summary of the Plan: Recap of the comprehensive strategy laid out in the action plan.
Commitment to Success: Reinforcement of the project manager’s commitment to guiding the customer through the execution phase and beyond
        """,

        )


