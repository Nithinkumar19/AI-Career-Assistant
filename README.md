# GenAI Career Assistant: A Multi-Agent Approach

<img src="multiagent.png" alt="GenAI Career Assistant Architecture" width="500">

**Author**: [Nithin Kumar K]
**Linkedin**: [NithinKumar](https://www.linkedin.com/in/nithin-kumar-k-935514258/)

Welcome to the GenAI Career Assistant, a powerful tool designed to revolutionize the job search process using cutting-edge AI technology. This project leverages a multi-agent architecture to provide personalized career guidance, making job hunting more efficient and tailored to individual needs.

## Table of Contents

- [Demo](#demo)
- [Why It's Needed](#why-its-needed)
- [Features](#features)
- [Architecture Overview](#architecture-overview)
- [Key Components](#key-components)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Future Improvements](#future-improvements)
- [Contributing](#contributing)
- [License](#license)




## Why It's Needed

In today's rapidly evolving job market, finding the right job and standing out from the competition can be challenging. The GenAI Career Assistant addresses this by leveraging AI to:

- Tailor job searches to your industry, experience, and location.
- Generate standout cover letters that highlight your strengths.
- Provide detailed insights into potential employers.
- Streamline the job application process through an intelligent, multi-agent system.

## Features

- **Personalized Job Search:** Automatically find job listings that match your criteria.
- **Custom Cover Letters:** Generate cover letters tailored to specific job applications.
- **Company Research:** Gather and present key information about potential employers.
- **Resume Analysis:** Extract and analyze key information from your resume to optimize job matches.
- **Interactive UI:** Easy-to-use interface built with Streamlit for a seamless user experience.

## Architecture Overview

The GenAI Career Assistant is built on a Supervisor Multi-Agent Architecture. Here's how it works:

- **Supervisor:** Manages the overall workflow, deciding which agent to invoke next.
- **JobSearcher:** Handles job search queries and retrieves relevant listings.
- **ResumeAnalyzer:** Extracts and analyzes information from uploaded resumes.
- **CoverLetterGenerator:** Crafts customized cover letters based on resume and job details.
- **WebResearcher:** Performs web searches to gather relevant company information.
- **ChatBot:** Manages general queries and provides conversational responses.

## Key Components

- **Agent Creation and Configuration:** A common function is used to set up agents with specific tools and prompts.
- **Specialized Tools:** Custom tools enhance the agents' capabilities, such as job search tools, resume extractors, and web search tools.
- **Streamlit UI:** The user interface is designed to be intuitive and responsive, facilitating interaction with the assistant.

## Technologies Used

- **LangGraph:** For creating and managing multi-agent workflows.
- **Streamlit:** For building the user interface.
- **OpenAI API:** For leveraging large language models (LLMs).
- **SerperClient and FireCrawlClient:** For web search and scraping capabilities.