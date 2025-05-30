from google.adk.agents import LoopAgent,SequentialAgent

from .subagents.analysis_process_agent import analysis_process_agent
from .subagents.style_guide_generator_agent import style_guide_generator_agent

thumbnail_analysis_loop_agent = LoopAgent(
    name = "Thumbnail_Analysis_Loop",
    max_iterations = 20,
    sub_agents = [analysis_process_agent],
    description =   """
                        Iteratively analyzes thumbnails one by one until all are processed
                    """, 
)


thumbnail_analyzer_agent = SequentialAgent(
    name = "Thumbnail_Analyzer_Root",
    sub_agents = [thumbnail_analysis_loop_agent,style_guide_generator_agent],
    description =   """
                        Analyzes multiple thumbnails from a YouTube channel,
                        then creates a comprehensive style guide based on all analyses 
                    """,
)