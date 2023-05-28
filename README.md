# Course Compass

Course Compass is a Python-based project that allows users to upload a PDF of their course outline. The program will then extract important course information and display it to the users. It aims to simplify the process of extracting key details from course outlines such as prerequisites, antirequisites, textbooks needed, important dates, test information, and grade distribution/methods of evaluation.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Known Issues](#known-issues)
- [Future Plans](#future-plans)
- [Contributing](#contributing)

## Installation

To run Course Compass, you need to ensure that the following dependencies are installed:

- openai: Install using `pip install openai`
- tkinter: Install using `pip install tkinter`
- textwrap: Install using `pip install textwrap`

## Usage

1. Download the main.py and analyzePDF.py files and place them in a folder.
2. Open the folder with your preferred Python environment.
3. Open the main.py file and replace the API key on the 8th line (`openai.api_key = "REPLACE(SEE INSTRUCTIONS)"`) with your ChatGPT API key. Instructions for obtaining the API key can be found here.
4. Run the main.py file. A GUI window will appear, allowing you to upload your PDF course outline.

## Example

Suppose you have a course syllabus for "CS 2034B Data Analytics" from Western University. After uploading the PDF, Course Compass will extract the following information:


Course: CS 2034b Data Analytics<br>
Prerequisites: NONE<br><br>
Antirequisites: NONE<br><br>
Instructor: Stephen Watt<br><br>
Methods of Evaluation: Assignments(4) - 15%, Weekly Labs(20%), Midterm(20%), Final Exam (45%)<br><br>
Assignment Information: Assignment 1 - Due Feb 2nd (3%), Assignment 2 - Due Feb 23 (4%), Assignment 3 - Due Mar 9 (4%), Assignment 4 - Due Mar 10 (4%)<br><br>
Additional Information: You may contact the course instructor via e-mail with brief questions regarding course material or clarification of assignments. However, please first check the course website for answers to frequently asked questions, or to see if the information is already there, before e-mailing the instructor. You must include CS2034 in the subject line (otherwise it might get filtered as spam). Please send E-mail from your UWO account and send E-mail in plain text format.<br>

## Known Issues
Processing larger syllabus files may take longer (approximately 15-30 seconds). Please be patient during the extraction process.

## Future Plans
Currently, the focus of Course Compass is on the functional aspects of extracting course information. Visually, there is room for improvement and enhancements. If you have ideas or suggestions to make the project visually appealing or want to contribute to its overall design, your contributions are most welcome.

## Contributing
Contributions are welcome to Course Compass. If you have any ideas, suggestions, or bug fixes, please submit them as issues or pull requests on the project repository. Your contributions will be greatly appreciated.

Please note that the emphasis of the project has been on the functionality part, and there is significant scope for visual improvements. If you are interested in enhancing the project's visual aesthetics, feel free to contribute and make it visually appealing.

