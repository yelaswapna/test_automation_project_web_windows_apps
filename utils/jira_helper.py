from jira import JIRA
from utils.config import JIRA_SERVER, JIRA_USER, JIRA_API_TOKEN, JIRA_PROJECT_KEY

def create_jira_issue(summary, description):
    jira = JIRA(server=JIRA_SERVER, basic_auth=(JIRA_USER, JIRA_API_TOKEN))
    issue_dict = {
        'project': {'key': JIRA_PROJECT_KEY},
        'summary': summary,
        'description': description,
        'issuetype': {'name': 'Bug'},
    }
    new_issue = jira.create_issue(fields=issue_dict)
    return new_issue