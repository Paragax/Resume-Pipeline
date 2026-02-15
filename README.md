# Overview

This repository provides a simple automation pipeline for managing and publishing a LaTeX-based resume.

Its primary purpose is to keep resume editing and portfolio hosting **cleanly separated**. Instead of storing LaTeX sources inside your portfolio website, you can maintain your resume independently while automatically syncing the generated PDF.

The workflow solves a common problem:

- Updating a resume but forgetting to update the website
- Avoiding hosting raw LaTeX artifacts publicly
- Eliminating the need for Overleaf-based editing

With this setup, you can:

- Edit your resume locally in VS Code
- Preview changes in real time while editing
- Build PDFs using a custom script
- Automatically publish the final resume PDF to your portfolio repository

This repository generates **two resume variants**:

- A full resume intended for direct job applications
- A public-facing resume with hidden or redacted information

The public resume is designed to prevent exposing personally identifiable information (PII) that should not appear on a portfolio website. For example, it is generally not advisable to publish your phone number on a public-facing site.

What information is shown or hidden is controlled directly within the `.tex` file, allowing you to fully customize what gets exposed.

By default, the PDF committed to the portfolio repository is the **public/hidden-info resume**. This behavior can be adjusted in the GitHub workflow if needed.

Additionally, whenever you make edits and push changes to GitHub, the automation pipeline will rebuild the PDFs and update the resume hosted on your portfolio website.

This setup was originally built around [Jake’s Resume template](https://github.com/sb2nov/resume), but the workflow is completely generic and works with **any `.tex` file**.

This keeps your portfolio lightweight while preserving a flexible, developer-friendly resume workflow.

# VS Code Requirement

This project expects you to use VS Code with the following extension installed:

Search for:

`LaTeX Workshop` by James Yu

This extension is required for:

- Building the PDF resume
- Using the custom build recipe
- Proper PDF preview inside VS Code

# Configuration

Before running the script, you **must update the configuration values** in:

`scripts/constants.py`

The script relies on these constants to control file names, output paths, and Git commit identity.

The API_TOKEN_GITHUB needs to be set in the Secrets section of your repository options. You can retrieve the API_TOKEN_GITHUB [here](https://github.com/settings/tokens) (set the `repo` permissions).

## PDF Configuration

- **`PDF`**  
  Defines the **path and filename** of the PDF containing the full/public version of your resume.

- **`HIDDEN_PDF`**  
  Defines the **path and filename** of the PDF containing the version with hidden or private information.

Update these values if you rename your files or change your folder structure.

## Git Configuration

- **`GIT_USER_NAME`**  
  Your Git username used for automated commits.

- **`GIT_USER_EMAIL`**  
  Your Git email used for commits.

- **`GIT_DEST_REPO`**  
  The destination repository where the PDF will be committed.

You may also commit to a specific folder instead of the repository root by:

1. Opening the workflow file
2. Uncommenting `destination_folder`
3. Defining your desired path

## Important

Failure to update these values may result in:

- Incorrect file names
- Failed CI/CD runs
- Commits pushed to the wrong repository

Remember to set your API_TOKEN_GITHUB.

## Example

```python
PUBLIC_PDF = Path("resume.pdf")
HIDDEN_PDF = Path("resume_hidden_info.pdf")

GIT_USER_NAME  = "Paragax"
GIT_USER_EMAIL = "paragax@users.noreply.github.com"
GIT_DEST_REPO = "Paragax/portfolio"
```
