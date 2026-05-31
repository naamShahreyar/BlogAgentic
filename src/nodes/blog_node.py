from src.states.blog_state import BlogState

class BlogNode:
    
    def __init__(self, llm):
        self.llm = llm
    
    def title_creation(self, state: BlogState):
        
        if 'topic' in state and state['topic']:
            
            prompt = """
                        You are an expert blog content writer. Use Markdown Formatting. Generate a blog title for the topic {topic}.
                        The title should be creative and SEO friendly.
                    """
                    
            system_message = prompt.format(topic=state['topic'])
            response = self.llm.invoke(system_message)
            return {'blog': {'title': response.content}}
        
    def content_generation(self, state: BlogState):
        
        if 'topic' in state and state['topic']:
            system_prompt = """
                            Youb are an expert blog writer. Use Markdown formatting.
                            Generate a detailed blog content with detailed breakdown for the topic {topic}
                            """
            system_message = system_prompt.format(topic=state['topic'])
            response = self.llm.invoke(system_message)
            
            return {'blog': {'title': state['blog']['title'], "content": response.content}}
            
            