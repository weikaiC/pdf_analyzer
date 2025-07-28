# pdf_analyzer

You will need an Google API key to run this.

How to run this:
```
pip install -r requirements.txt

# Load the example documents into Chroma
python load_data.py

# Run the analyzer
python main.py
```

Output Demo:
```
Query: what is this pdf about?

Thinking...

Based on the context provided, this document is a newsletter from a company called Drylab, published in May 2017 for its investors and friends. The newsletter serves as a comprehensive business update, detailing the company's progress and future plans.

The main focus of the newsletter is the company's expansion into the American market and the upcoming launch of its new product, "Drylab 3.0". The text describes a recent, successful tour of the US where company representatives met with major industry players such as Netflix, Apple, the Academy of Motion Picture Arts and Sciences, and the International Cinematographers Guild. The official launch of Drylab 3.0 is scheduled for the International Broadcasters Convention in Amsterdam in September, although the development is noted to be about a month behind schedule.

The document also provides updates on several other key areas of the business. It reports on a successful investment round that raised new capital, strong sales performance with an 80% return customer rate, and the acquisition of new customers in Canada and France. Furthermore, it details the growth of the team, including the hiring of new developers, interns, and accomplished mentors from the film industry.

Finally, the newsletter covers Drylab's engagement with the broader film and technology industries. It discusses their attendance at the National Association of Broadcasters (NAB) convention and Apple's World Wide Developers Conference (WWDC), as well as a strategic decision to skip the Cine Gear expo. It also mentions collaborations with major tech companies like Amazon, Google, and IBM for cloud computing, and with partners like Apple and Paralinx. An announcement for the company's Annual General Meeting is also included.
```
You can replace the example pdf in the documents folder with your own pdfs, and the chatbot will use those instead