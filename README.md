plagfinder
==========

Plagiarism detection software.

Synopsis
--------

* Plagiarism detection is the process of locating instances of plagiarism within a work or document. (from Wikipedia)

* This tool uses screen scraping techniques to extract data from Google search results.

Requirements
------------

* Python 3
* PyQt4
* The Natural Language Toolkit (NLTK)

Prerequisites
-------------

1. Download nltk data (punkt) to plagfinder/res/nltk_data
2. Create plagfinder/conf/router: (add your ip, login and password)

		[Router]
		ip = xxx.xxx.xxx.xxx
		user = login
		pwrd = password

Run
---

		python3 plagfinder
