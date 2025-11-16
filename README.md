<div align="center">
  <img src="plugin/stop-the-slop/icons/stop-the-slop.png" alt="Stop the Slop" width="128">
</div>

# What is this project

Build a defensive application (maybe a browser plugin?) that helps users course correct when engaging with AI content or other content that could be harmful.

# Why this project?

AI Slop has become a major problem online. A 2025 study estimates that 40% of new content on Medium and Quora and 2.5% on Reddit is made with GenAI [1]. Unlike typical low-quality posts, this content hides who is speaking. The EU AI Act, effective August 2, 2026, will require AI content disclosure but exempts law enforcement. This creates asymmetric power dynamics between citizens and law enforcement. If we extrapolate from this policy,  AI generated content could act against the interest of users across many situations ranging as foreign influence campaigns, phishing, fraud to more benign but equally harmful like a missed opportunity for social interaction. The AI slop trend could make people dumber, less informed, worsen attention spans, increase political divides, and encourage neglect of real human interaction. 

We need tools that defend against harmful GenAI content. We need to Stop the Slop.

# Goal: 

Detect and reduce harm from AI-generated content by suggesting protective actions for users.

# Timeboxing: 

November 21–23 (D/acc hackathon)

# Scope:

- Ideate on harmful content and user course-correction
- Build browser extension and backend for evals/data storageTest and document
Stretch goal: telemetry backend

# Team needs:

- Generalists with software, UX, ML/eval, writing, or software distribution experience
- Anyone with other relevant skills who thinks they can contribute


[1] https://sites.google.com/view/sources-aislop 

# For candidates:

We will make a short assessment on fit for people who want to contribute. This repo contains boilerplate code for a python backend and a browser plugin. Make a PR that detects if the user is on Reddit or ChatGPT, log the current url to console and change the border color to a specific color depending on the current web page. Feel free to vibe the PR.

