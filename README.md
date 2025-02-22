<p align="center">
  <a href="https://github.com/XpressAI/xircuits/tree/master/xai_components#xircuits-component-library-list">Component Libraries</a> •
  <a href="https://github.com/XpressAI/xircuits/tree/master/project-templates#xircuits-project-templates-list">Project Templates</a>
  <br>
  <a href="https://xircuits.io/">Docs</a> •
  <a href="https://xircuits.io/docs/Installation">Install</a> •
  <a href="https://xircuits.io/docs/category/tutorials">Tutorials</a> •
  <a href="https://xircuits.io/docs/category/developer-guide">Developer Guides</a> •
  <a href="https://github.com/XpressAI/xircuits/blob/master/CONTRIBUTING.md">Contribute</a> •
  <a href="https://www.xpress.ai/blog/">Blog</a> •
  <a href="https://discord.com/invite/vgEg2ZtxCw">Discord</a>
</p>

<p align="center"><i>Xircuits Component Library for GitHub! Seamlessly integrate GitHub operations into your Xircuits workflows.</i></p>

---

## Xircuits Component Library for GitHub

This library provides Xircuits components to interact with GitHub, enabling seamless automation of repository management, issue tracking, and pull request operations.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Main Xircuits Components](#main-xircuits-components)
- [Installation](#installation)

## Prerequisites

Before you begin, make sure you have the following:

1. Python 3.9+.
2. Xircuits.
3. A GitHub account with a personal access token (PAT) configured.
- A valid GitHub token set as an environment variable or provided directly to the components.


## Main Xircuits Components

### Authorization Component
- **GithubAuthorize Component**: Authorizes a GitHub client using a token or environment variables.

    <img src="https://github.com/user-attachments/assets/a27f52e0-64c8-4f4c-9e0b-d1755e16eb5f" alt="Image" width="200" height="100" />

### Issue Management Components
- **GithubListIssues Component**: Lists issues in a GitHub repository.

    <img src="https://github.com/user-attachments/assets/4981e456-1847-4046-a770-93c421497e9f" alt="Image" width="200" height="125" />

- **GithubGetIssue Component**: Retrieves details of a specific issue.
- **GithubCreateIssue Component**: Creates a new issue in a repository.

### Pull Request Components
- **GithubListPullRequests Component**: Lists pull requests in a GitHub repository.
- **GithubCreatePullRequest Component**: Creates a new pull request.
- **GithubReadPullRequestComments Component**: Reads comments from a pull request.
- **GithubAddPullRequestComment Component**: Adds a comment to a pull request.

## Installation

To use this component library, ensure that you have an existing [Xircuits setup](https://xircuits.io/docs/main/Installation). You can then install the GitHub library using the [component library interface](https://xircuits.io/docs/component-library/installation#installation-using-the-xircuits-library-interface), or through the CLI using:

```
xircuits install github
```

You can also install it manually by cloning the repository:

```
# base Xircuits directory

git clone https://github.com/XpressAI/xai-github xai_components/xai_github
pip install -r xai_components/xai_github/requirements.txt
```

