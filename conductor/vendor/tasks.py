from bs4 import BeautifulSoup
import requests

from conductor import celeryapp
from conductor.vendor.models import PromptSchool


@celeryapp.task
def scan_prompt() -> None:
    """Scan the Prompt website for new schools with essays."""
    prompt_school_url = "http://pages.prompt.com/2018-2019prompts"
    response = requests.get(prompt_school_url, timeout=5)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    anchors = soup.find_all("a")
    for anchor in anchors:
        if "id" not in anchor.attrs:
            continue

        slug = anchor.attrs["id"]
        name = anchor.next_sibling
        if not PromptSchool.objects.filter(slug=slug).exists():
            PromptSchool.objects.create(slug=slug, name=name)
