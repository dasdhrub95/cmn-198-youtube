#Indico political analysis
import indicoio
indicoio.config.api_key = 'YOUR_API_KEY'

# single example
indicoio.political("I have a constitutional right to bear arms!")

# batch example
indicoio.political([
    "I have a constitutional right to bear arms!",
    "I wish more candidates cared about the environment."
])
