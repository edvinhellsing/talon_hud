from .typing import HudContentEvent

# Class for managing a part of the HUD content
class HudPartialContent:

    topic_types = None
	
    def __init__(self):
        self.topic_types = {}
    
    # Get a specific topic from the known topic types
    def get_topic(self, topic_type: str, topic = None) -> list:
        topic_contents = []
        if topic_type in self.topic_types:
            for known_topic in self.topic_types[topic_type]:
                if topic == None or topic == known_topic:
                    if isinstance(self.topic_types[topic_type][known_topic], list):
                        topic_contents.extend(self.topic_types[topic_type][known_topic])
                    else:
                        topic_contents.append(self.topic_types[topic_type][known_topic])
                        
        return topic_contents
        
    # Override a specific topic from the known topic types
    def set_topic(self, topic_type, topic, content):
        if topic_type not in self.topic_types:
            self.topic_types[topic_type] = {}
        self.topic_types[topic_type][topic] = content
    
    # Remove a specific topic
    def remove_topic(self, topic_type, topic):
        if topic_type not in self.topic_types:
            self.topic_types[topic_type] = {}
        
        if topic in self.topic_types[topic_type]:
            del self.topic_types[topic_type][topic]

    # Process an event
    def process_event(self, event: HudContentEvent):
        if event.operation == 'replace':
            self.set_topic(event.topic_type, event.topic, event.content)
        elif event.operation == 'remove':
            self.remove_topic(event.topic_type, event.topic)
        # Other types of content events need manual changing ( patch and append for example )