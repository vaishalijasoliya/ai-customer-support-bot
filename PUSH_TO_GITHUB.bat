@echo off
echo ========================================
echo Push to GitHub - Quick Script
echo ========================================
echo.

echo Step 1: Make sure you've created a GitHub repository first!
echo Go to: https://github.com/new
echo.
pause

echo.
echo Step 2: Enter your GitHub username:
set /p GITHUB_USERNAME="GitHub Username: "

echo.
echo Step 3: Enter your repository name (default: ai-customer-support-bot):
set /p REPO_NAME="Repository Name: "
if "%REPO_NAME%"=="" set REPO_NAME=ai-customer-support-bot

echo.
echo Step 4: Adding remote and pushing...
echo.

git remote add origin https://github.com/%GITHUB_USERNAME%/%REPO_NAME%.git
git branch -M main
git push -u origin main

echo.
echo ========================================
echo Done! Check your GitHub repository!
echo ========================================
pause

