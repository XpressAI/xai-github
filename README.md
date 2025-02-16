# xai_github

xai_github is a custom component library for Xircuits, designed to facilitate interactions with GitHub. It provides a set of components that allow users to perform various GitHub operations such as listing issues, creating issues, managing pull requests, and more.

## Features

- **GithubAuthorize**: Authorize a GitHub client using a token or environment variable.
- **GithubListIssues**: List issues in a specified GitHub repository.
- **GithubGetIssue**: Retrieve details of a specific issue from a repository.
- **GithubCreateIssue**: Create a new issue in a GitHub repository.
- **GithubListPullRequests**: List pull requests in a specified repository.
- **GithubCreatePullRequest**: Create a new pull request in a repository.
- **GithubReadPullRequestComments**: Read comments from a pull request.
- **GithubAddPullRequestComment**: Add a comment to a pull request.

## Installation

To install the required dependencies, run:

```bash
pip install -r requirements.txt
```

## Usage

Import the components into your Xircuits workflow to interact with GitHub repositories. Ensure you have a valid GitHub token set as an environment variable or provided directly to the components.

## License

This project is licensed under the MIT License.

## Author

Eduardo Gonzalez - [egonzalez@xpress.ai](mailto:egonzalez@xpress.ai)

## Repository

[GitHub Repository](https://github.com/xpressai/xai-github)
