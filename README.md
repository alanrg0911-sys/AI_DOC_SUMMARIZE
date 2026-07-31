Pretty basic program that uses Ollama AI locally to summarize PDFs.

The speed of the summarize heavily depends on your system specs and the amount of text of the PDF. 

As this is mean to run locally you need to install Ollama and you can change the model in the code if you wish to (default model is llama3.2:3b).

The program has a history function where you can see the date when you summarize a document and the name of that document and the main function summarize PDF which opens a file selector so you can select the file that you want to summarize(ONLY PDF FILES) and you just have to wait for it to finish to summarize.
As I stated before the time on getting the summary depends on your system specs and the amount of text of the PDF.

For the moment this program does not have a proper user interface, everything is through CLI and also does not have a function were you can export the summarized text to a new PDF file(yet).

To run the program you just to run the main.py. 

You can use the command python main.py in the terminal of the project.
