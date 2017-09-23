# -*- coding: utf-8 -*-

import sys
import os
import urllib

import nltk
from PyQt4 import QtCore

import model.file
import core.router

class MainProcess(QtCore.QThread):
    def __init__(self, window, loaded_files):
        QtCore.QThread.__init__(self)

        # Qt4 window
        self.window = window

        # Router
        self.router = core.router.Router(window)

        # Loaded files list
        self.loaded_files = loaded_files

    def run(self):
        try:
            # Emit process started signal
            self.window.start_proc_sign.emit()

            # Get text files
            content = {}
            for file_name in self.loaded_files.loaded_files_list:
                if os.path.isfile(file_name):
                    content[file_name] = model.file.File(file_name).read_utf8_file().replace('\n', ' ').strip()

            # Text to sentences
            sents = {}
            for current_file in content:
                sents[current_file] = (nltk.tokenize.sent_tokenize(content[current_file]))

            # Calculate the total number of sentences (for the progress bar)
            sents_count = 0
            for part in sents:
                sents_count += len(sents[part])

            # Loop files
            # step_all = step for all files progress bar
            step_all = 100 / sents_count

            # done_all = all files progress bar value
            done_all = 0

            # Loop all files
            for part in sents:
                # step = step for this file's progress bar
                step = 100 / len(sents[part])

                # done = value of this file's progress bar
                done = 0

                # Search on Google
                for sent_part in sents[part]:
                    # Data
                    # Remove white space and carriage returns
                    sent_part = ' '.join(sent_part.strip().split())

                    # Replace special characters
                    sent = urllib.request.quote(sent_part)

                    # Prepare url
                    url = 'https://www.google.com/search?q="' + sent + '"'

                    # Possible strings for result not found on Google
                    not_found_1 = "did not match any documents"
                    not_found_2 = "No results found for"
                    not_found_3 = "Showing results for"

                    # Repeat if any exception occurs
                    while True:
                        try:
                            # Connection
                            req = urllib.request.Request(url)

                            # Add headers
                            req.add_header('User-Agent', 'Mozilla/5.0')
                            req.add_header('Accept-Language', 'en-US')

                            # Open url
                            con = urllib.request.urlopen(req)

                            # Save page
                            req_str = con.read().decode('UTF-8')

                            # None of the possible not found strings are found
                            if req_str.find(not_found_1) == -1 and req_str.find(not_found_2) == -1 and req_str.find(not_found_3) == -1:
                                self.window.write_colored_sign.emit(sent_part, 'red')
                            else:
                                self.window.write_colored_sign.emit(sent_part, 'green')

                            # Break the loop if no exception occurs
                            break

                        except urllib.error.HTTPError as e:
                            # Google antibot protection sends error 503
                            if str(e).find("HTTP Error 503") != -1:
                                # Show error message in status bar
                                self.window.update_status_sign.emit(str(e))

                                # Request restarting the rooter
                                self.router.restart_router()
                            else: # Bad url format
                                # Write sentence in blue
                                self.window.write_colored_sign.emit(sent_part, 'blue')

                                # Break the loop because this sentence can't be searched on Google
                                break

                        except urllib.error.URLError as e:
                            # Emit error message to status bar
                            self.window.update_status_sign.emit(str(e))

                            # Restart router and try again
                            self.router.restart_router()

                    # Update file's progress bar
                    done += step
                    self.window.update_progress_sign.emit(int(done))

                    # Update all files' progress bar
                    done_all += step_all
                    self.window.update_progress_all_sign.emit(int(done_all))

        except KeyboardInterrupt:
            raise SystemExit

        finally:
            self.window.end_proc_sign.emit()
