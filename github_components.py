import os
from xai_components.base import InArg, OutArg, Component, xai_component
from github import Github
 

def get_github_client(ctx, client=None, token=None):
    if client is not None:
        return client
    if token is not None:
        return Github(token)
    if ctx.get('github_client', None) is None:
        ctx['github_client'] = Github(os.getenv("GITHUB_TOKEN"))

    return ctx['github_client']

    
@xai_component
class GithubAuthorize(Component):
    """Component to authorize GitHub client using a provided token or environment variables.

    ##### outPorts:
    - client (Github): The authenticated GitHub client.
    """
    token: InArg[str]
    client: OutArg[Github]

    def execute(self, ctx) -> None:
        self.client.value = get_github_client(client=None, token=self.token.value)
        ctx['github_client'] = self.client.value
        

@xai_component
class GithubListIssues(Component):
    """Component to list issues in a GitHub repository.

    ##### inPorts:
    - repo_name (str): The name of the repository in the format 'owner/repo'.
    - client (Github): The authenticated GitHub client.
    
    ##### outPorts:
    - issues (list): A list of issues in the repository.
    """
    repo_name: InArg[str]
    client: InArg[Github]
    issues: OutArg[list]

    def execute(self, ctx) -> None:
        client = ctx['github_client']
        repo = client.get_repo(self.repo_name.value)
        self.issues.value = [issue.title for issue in repo.get_issues()]

@xai_component
class GithubGetIssue(Component):
    """Component to get a specific issue from a GitHub repository.

    ##### inPorts:
    - repo_name (str): The name of the repository in the format 'owner/repo'.
    - issue_number (int): The number of the issue to retrieve.
    - client (Github): The authenticated GitHub client.
    
    ##### outPorts:
    - issue (dict): The details of the issue.
    """
    repo_name: InArg[str]
    issue_number: InArg[int]
    client: InArg[Github]
    issue: OutArg[dict]

    def execute(self, ctx) -> None:
        client = ctx['github_client']
        repo = client.get_repo(self.repo_name.value)
        self.issue.value = repo.get_issue(self.issue_number.value).raw_data

@xai_component
class GithubCreateIssue(Component):
    """Component to create a new issue in a GitHub repository.

    ##### inPorts:
    - repo_name (str): The name of the repository in the format 'owner/repo'.
    - title (str): The title of the new issue.
    - body (str): The body of the new issue.
    - client (Github): The authenticated GitHub client.
    
    ##### outPorts:
    - issue (dict): The details of the created issue.
    """
    repo_name: InArg[str]
    title: InArg[str]
    body: InArg[str]
    client: InArg[Github]
    issue: OutArg[dict]

    def execute(self, ctx) -> None:
        client = ctx['github_client']
        repo = client.get_repo(self.repo_name.value)
        new_issue = repo.create_issue(title=self.title.value, body=self.body.value)
        self.issue.value = new_issue.raw_data

@xai_component
class GithubListPullRequests(Component):
    """Component to list pull requests in a GitHub repository.

    ##### inPorts:
    - repo_name (str): The name of the repository in the format 'owner/repo'.
    - client (Github): The authenticated GitHub client.
    
    ##### outPorts:
    - pull_requests (list): A list of pull requests in the repository.
    """
    repo_name: InArg[str]
    client: InArg[Github]
    pull_requests: OutArg[list]

    def execute(self, ctx) -> None:
        client = ctx['github_client']
        repo = client.get_repo(self.repo_name.value)
        self.pull_requests.value = [pr.title for pr in repo.get_pull_requests()]

@xai_component
class GithubCreatePullRequest(Component):
    """Component to create a new pull request in a GitHub repository.

    ##### inPorts:
    - repo_name (str): The name of the repository in the format 'owner/repo'.
    - title (str): The title of the new pull request.
    - body (str): The body of the new pull request.
    - head (str): The name of the branch where your changes are implemented.
    - base (str): The name of the branch you want to merge your changes into.
    - client (Github): The authenticated GitHub client.
    
    ##### outPorts:
    - pull_request (dict): The details of the created pull request.
    """
    repo_name: InArg[str]
    title: InArg[str]
    body: InArg[str]
    head: InArg[str]
    base: InArg[str]
    client: InArg[Github]
    pull_request: OutArg[dict]

    def execute(self, ctx) -> None:
        client = ctx['github_client']
        repo = client.get_repo(self.repo_name.value)
        new_pr = repo.create_pull(title=self.title.value, body=self.body.value, head=self.head.value, base=self.base.value)
        self.pull_request.value = new_pr.raw_data

@xai_component
class GithubReadPullRequestComments(Component):
    """Component to read comments from a pull request in a GitHub repository.

    ##### inPorts:
    - repo_name (str): The name of the repository in the format 'owner/repo'.
    - pull_request_number (int): The number of the pull request to read comments from.
    - client (Github): The authenticated GitHub client.
    
    ##### outPorts:
    - comments (list): A list of comments on the pull request.
    """
    repo_name: InArg[str]
    pull_request_number: InArg[int]
    client: InArg[Github]
    comments: OutArg[list]

    def execute(self, ctx) -> None:
        client = ctx['github_client']
        repo = client.get_repo(self.repo_name.value)
        pr = repo.get_pull(self.pull_request_number.value)
        self.comments.value = [comment.body for comment in pr.get_review_comments()]

@xai_component
class GithubAddPullRequestComment(Component):
    """Component to add a comment to a pull request in a GitHub repository.

    ##### inPorts:
    - repo_name (str): The name of the repository in the format 'owner/repo'.
    - pull_request_number (int): The number of the pull request to add a comment to.
    - comment (str): The comment to add.
    - client (Github): The authenticated GitHub client.
    
    ##### outPorts:
    - success (bool): Indicates if the comment was added successfully.
    """
    repo_name: InArg[str]
    pull_request_number: InArg[int]
    comment: InArg[str]
    client: InArg[Github]
    success: OutArg[bool]

    def execute(self, ctx) -> None:
        client = ctx['github_client']
        repo = client.get_repo(self.repo_name.value)
        pr = repo.get_pull(self.pull_request_number.value)
        pr.create_issue_comment(self.comment.value)
        self.success.value = True
