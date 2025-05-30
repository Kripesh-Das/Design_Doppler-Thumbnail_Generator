from google.adk.agents import SequentialAgent

from .save_analysis_agent import save_analysis_agent
from .single_thumbnail_analyzer_agent import single_thumbnail_analyzer_agent
from .thumbnail_selector_agent import thumbnail_selector_agent

analysis_process_agent = SequentialAgent(
    name = "Thumbnail_Anlysis_Process",
    sub_agents = [thumbnail_selector_agent,single_thumbnail_analyzer_agent,save_analysis_agent],
    description =   """
                    Processes thumbnails one at a time by:
                        1. Selecting the next thumbnail that needs analysis
                        2. Performing detailed visual analysis of the selected thumbnail
                        3. Saving the analysis for future reference and style guide creat
                    """,
)