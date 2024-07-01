import os
import requests
from dotenv import load_dotenv

# load variables from .env
load_dotenv()

# Access the environment variables
proxycurl_api_key = os.getenv('PROXYCURL_API_KEY')


def scrape_linkedin_profile(linkedin_profile_url: str, mock: bool=True):
    """
    scrape information from LinkedIn profiles, 
    Manually scrape the information from the LinkedIn profile
    """

    if mock:
        linkedin_profile_url = "https://gist.githubusercontent.com/felixyh/bdcbced7c2b5f5cd881492194ed19b76/raw/aa20ea45812d4064a38a107a95b4fc9c36da92e7/sojson.com.json"
        response = requests.get(
            linkedin_profile_url,
            timeout=10,
        )

    else:
        proxycurl_api_key = os.getenv('PROXYCURL_API_KEY')
        headers = {'Authorization': 'Bearer ' + proxycurl_api_key}
        api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'
        params = {
            'url': linkedin_profile_url,
            }
        response = requests.get(
            api_endpoint,
            params=params,
            headers=headers,
            timeout=10,
            )
    data = response.json()
    return data

if __name__ == "__main__":
    print(
        scrape_linkedin_profile(
            linkedin_profile_url="https://www.linkedin.com/in/felix-yang-a61abb135/"
        )
    )