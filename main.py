
import os
from decouple import config
from crewai import Crew, Process
from textwrap import dedent
from agents import VideoEditingAgents
from tasks import VideoEditingTasks

# Set up environment variables
os.environ["OPENAI_API_KEY"] = config('OPENAI_API_KEY')
os.environ["SERPER_API_KEY"] = config('SERPER_API_KEY')

class VideoEditingCrew:
    def __init__(self, inputs):
        self.inputs = inputs
        self.agents = VideoEditingAgents()
        self.tasks = VideoEditingTasks()

    def run(self):
        # Initialize agents
        business_analyst = self.agents.business_analyst()
        video_editor = self.agents.video_editor()
        talent_recruiter = self.agents.talent_recruiter()
        project_manager = self.agents.project_manager()

        # Initialize tasks with respective agents
        bsa_task = self.tasks.business_analysis_task(business_analyst,self.inputs)
        editor_task = self.tasks.video_editor_task(video_editor, [bsa_task])
        recruiter_task = self.tasks.recruitment_task(talent_recruiter,[editor_task])
        pm_task = self.tasks.project_management_task(project_manager,[bsa_task,editor_task,recruiter_task])

        # Form the crew with defined agents and tasks
        crew = Crew(
            agents=[business_analyst, video_editor, talent_recruiter, project_manager],
            tasks=[bsa_task, editor_task, recruiter_task, pm_task],
            process=Process.sequential
        )

        # Execute the crew to carry out the video editing project
        return crew.kickoff()

if __name__ == "__main__":
    print("Welcome to the Video Editing Crew Setup")
    print("---------------------------------------")
    inputs = dedent("""\
                    I edit 6 videos a week, monday through Saturday, usually i spend 4 to 6 hours making a video depending on 
                    how much time i need to research the topic, and actually implement and record what im gonna teach. My editing usually 
                    consists mostly of cropping out silences, or bad takes as well as cleaning up the audio using CapCut.  I also make the thumbnail 
                    using Canva, use vidiq to try and get a good title and retrieve the description from my Loom application transcript which i use to record. 
                    Also I would want to have accurate time stamps of each of the sections of my video.""")
    video_crew = VideoEditingCrew(inputs)
    result = video_crew.run()

    print("\n\n##############################")
    print("## Here are the results of your video editing project:")
    print("##############################\n")
    print(result)





